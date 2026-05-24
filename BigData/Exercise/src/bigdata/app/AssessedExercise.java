package bigdata.app;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.time.Instant;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;

import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.broadcast.Broadcast;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Encoders;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;

import bigdata.objects.Asset;
import bigdata.objects.AssetFeatures;
import bigdata.objects.AssetMetadata;
import bigdata.objects.AssetRanking;
import bigdata.objects.StockPrice;
import bigdata.objects.TickerStats;
import bigdata.transformations.filters.NullPriceFilter;
import bigdata.transformations.maps.PriceReaderMap;
import bigdata.transformations.pairing.AssetMetadataPairing;

import scala.Tuple2;

public class AssessedExercise {

public static void main(String[] args) throws InterruptedException {

		//--------------------------------------------------------
	    // Static Configuration
	    //--------------------------------------------------------
		String datasetEndDate = "2020-04-01";
		double volatilityCeiling = 4;
		double peRatioThreshold = 25;

		long startTime = System.currentTimeMillis();

		// The code submitted for the assessed exerise may be run in either local or remote modes
		// Configuration of this will be performed based on an environment variable
		String sparkMasterDef = System.getenv("SPARK_MASTER");
		if (sparkMasterDef==null) {
			File hadoopDIR = new File("resources/hadoop/"); // represent the hadoop directory as a Java file so we can get an absolute path for it
			System.setProperty("hadoop.home.dir", hadoopDIR.getAbsolutePath()); // set the JVM system property so that Spark finds it
			sparkMasterDef = "local[4]"; // default is local mode with two executors
		}

		String sparkSessionName = "BigDataAE"; // give the session a name

		// Create the Spark Configuration
		SparkConf conf = new SparkConf()
				.setMaster(sparkMasterDef)
				.setAppName(sparkSessionName)
				.set("spark.sql.shuffle.partitions", "8")
				.set("spark.default.parallelism", "8")
				.set("spark.driver.memory", "4g")
				.set("spark.executor.memory", "4g");

		// Create the spark session
		SparkSession spark = SparkSession
				  .builder()
				  .config(conf)
				  .getOrCreate();


		// Get the location of the asset pricing data
		String pricesFile = System.getenv("BIGDATA_PRICES");
		if (pricesFile==null) pricesFile = "resources/all_prices-noHead.csv"; // default is a sample with 3 queries

		// Get the asset metadata
		String assetsFile = System.getenv("BIGDATA_ASSETS");
		if (assetsFile==null) assetsFile = "resources/stock_data.json"; // default is a sample with 3 queries


    	//----------------------------------------
    	// Pre-provided code for loading the data
    	//----------------------------------------

    	// Create Datasets based on the input files

		// Load in the assets, this is a relatively small file
		Dataset<Row> assetRows = spark.read().option("multiLine", true).json(assetsFile);
		//assetRows.printSchema();
		System.err.println(assetRows.first().toString());
		JavaPairRDD<String, AssetMetadata> assetMetadata = assetRows.toJavaRDD().mapToPair(new AssetMetadataPairing());

		// Load in the prices, this is a large file (not so much in data size, but in number of records)
    	Dataset<Row> priceRows = spark.read().csv(pricesFile); // read CSV file
    	Dataset<Row> priceRowsNoNull = priceRows.filter(new NullPriceFilter()); // filter out rows with null prices
    	Dataset<StockPrice> prices = priceRowsNoNull.map(new PriceReaderMap(), Encoders.bean(StockPrice.class)); // Convert to Stock Price Objects


		AssetRanking finalRanking = rankInvestments(spark, assetMetadata, prices, datasetEndDate, volatilityCeiling, peRatioThreshold);

		long endTime = System.currentTimeMillis();

		System.out.println(finalRanking.toString());

		// Export results to JSON for visualization dashboard
		String out = System.getenv("BIGDATA_RESULTS");
		String resultsDIR = "results/";
		if (out!=null) resultsDIR = out;

		long executionTimeSeconds = (endTime - startTime) / 1000;
		bigdata.util.ResultsExporter.exportToJSON(finalRanking, executionTimeSeconds, resultsDIR);

		System.out.println("Holding Spark UI open for 10 minutes: http://localhost:4040");

		Thread.sleep(600000); // 10 minutes = 600000 milliseconds

		// Close the spark session
		spark.close();

		try {
			BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(new File(resultsDIR).getAbsolutePath()+"/SPARK.DONE")));

			Instant sinstant = Instant.ofEpochSecond( startTime/1000 );
			Date sdate = Date.from( sinstant );

			Instant einstant = Instant.ofEpochSecond( endTime/1000 );
			Date edate = Date.from( einstant );

			writer.write("StartTime:"+sdate.toGMTString()+'\n');
			writer.write("EndTime:"+edate.toGMTString()+'\n');
			writer.write("Seconds: "+((endTime-startTime)/1000)+'\n');
			writer.write('\n');
			writer.write(finalRanking.toString());
			writer.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}

	}


    public static AssetRanking rankInvestments(SparkSession spark, JavaPairRDD<String, AssetMetadata> assetMetadata, Dataset<StockPrice> prices, String datasetEndDate, double volatilityCeiling, double peRatioThreshold) {

    	// only keep prices on or before the cutoff date
    	Dataset<StockPrice> filteredPrices = prices.filter(new bigdata.transformations.filters.DateFilter(datasetEndDate));

    	// pair each price with its ticker so we can group them
    	JavaPairRDD<String, StockPrice> pricePairs = filteredPrices.toJavaRDD()
    			.mapToPair(new bigdata.transformations.pairing.StockPricePairing());

    	// instead of doing groupByKey (which shuffles all the raw price records),
    	// we process each partition locally and build a compact TickerStats per ticker.
    	// this way only the small summary objects get shuffled, not millions of price rows.
    	JavaPairRDD<String, TickerStats> partialStats = pricePairs.mapPartitionsToPair(iter -> {
    		// bucket prices by ticker within this partition
    		HashMap<String, ArrayList<StockPrice>> localGroups = new HashMap<>();
    		while (iter.hasNext()) {
    			Tuple2<String, StockPrice> pair = iter.next();
    			localGroups.computeIfAbsent(pair._1(), k -> new ArrayList<>()).add(pair._2());
    		}

    		ArrayList<Tuple2<String, TickerStats>> results = new ArrayList<>();
    		for (Map.Entry<String, ArrayList<StockPrice>> entry : localGroups.entrySet()) {
    			ArrayList<StockPrice> priceList = entry.getValue();

    			// need them in chronological order
    			priceList.sort((p1, p2) -> {
    				if (p1.getYear() != p2.getYear()) return Short.compare(p1.getYear(), p2.getYear());
    				if (p1.getMonth() != p2.getMonth()) return Short.compare(p1.getMonth(), p2.getMonth());
    				return Short.compare(p1.getDay(), p2.getDay());
    			});

    			TickerStats stats = new TickerStats();
    			stats.setTotalPrices(priceList.size());

    			// grab the last 252 close prices for volatility (roughly 1 year of trading days)
    			int volStart = Math.max(0, priceList.size() - 252);
    			for (int i = volStart; i < priceList.size(); i++) {
    				StockPrice sp = priceList.get(i);
    				long date = TickerStats.encodeDate(sp.getYear(), sp.getMonth(), sp.getDay());
    				stats.addClosePrice(date, sp.getClosePrice());
    			}

    			// also keep the last 6 for computing 5-day returns
    			int retStart = Math.max(0, priceList.size() - 6);
    			for (int i = retStart; i < priceList.size(); i++) {
    				StockPrice sp = priceList.get(i);
    				long date = TickerStats.encodeDate(sp.getYear(), sp.getMonth(), sp.getDay());
    				stats.addRecentPrice(date, sp.getClosePrice());
    			}

    			results.add(new Tuple2<>(entry.getKey(), stats));
    		}
    		return results.iterator();
    	});

    	// now merge the partial stats across partitions - this is the only shuffle
    	JavaPairRDD<String, TickerStats> mergedStats = partialStats.reduceByKey(TickerStats::merge);

    	// convert to features and drop anything with volatility >= threshold
    	JavaPairRDD<String, AssetFeatures> lowVolatilityAssets = mergedStats
    			.mapToPair(t -> new Tuple2<>(t._1(), t._2().toAssetFeatures()))
    			.filter(new bigdata.transformations.filters.VolatilityFilter(volatilityCeiling));

    	// broadcast the metadata to all executors so we can do a map-side lookup
    	// instead of a shuffle join (the metadata table is small enough for this)
    	Map<String, AssetMetadata> metadataMap = assetMetadata.collectAsMap();
    	Broadcast<Map<String, AssetMetadata>> broadcastMetadata = spark.sparkContext().broadcast(
    			metadataMap,
    			scala.reflect.ClassTag$.MODULE$.apply(Map.class)
    	);

    	// look up metadata, filter by P/E ratio, and build the final Asset objects
    	JavaRDD<Asset> assets = lowVolatilityAssets.map(tuple -> {
    				String ticker = tuple._1;
    				AssetFeatures features = tuple._2;
    				AssetMetadata metadata = broadcastMetadata.value().get(ticker);

    				if (metadata == null) return null;

    				double peRatio = metadata.getPriceEarningRatio();
    				if (peRatio <= 0 || peRatio >= peRatioThreshold) return null;

    				features.setPeRatio(peRatio);
    				return new Asset(ticker, features,
    						metadata.getName(), metadata.getIndustry(), metadata.getSector());
    			}).filter(Objects::nonNull);

    	// pick the top 5 by returns
    	List<Asset> topAssets = assets.top(5);

    	AssetRanking finalRanking = new AssetRanking();
    	Asset[] assetArray = new Asset[5];
    	for (int i = 0; i < topAssets.size() && i < 5; i++) {
    		assetArray[i] = topAssets.get(i);
    	}
    	finalRanking.setAssetRanking(assetArray);

    	return finalRanking;

    }

}
