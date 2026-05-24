package bigdata.transformations.pairing;

import org.apache.spark.api.java.function.PairFunction;
import bigdata.objects.StockPrice;
import scala.Tuple2;

/**
 * Keys each StockPrice by its ticker symbol for grouping.
 */
public class StockPricePairing implements PairFunction<StockPrice, String, StockPrice> {

    private static final long serialVersionUID = 1L;

    @Override
    public Tuple2<String, StockPrice> call(StockPrice price) throws Exception {
        return new Tuple2<>(price.getStockTicker(), price);
    }
}
