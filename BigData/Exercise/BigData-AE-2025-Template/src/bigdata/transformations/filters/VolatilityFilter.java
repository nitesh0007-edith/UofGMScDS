package bigdata.transformations.filters;

import org.apache.spark.api.java.function.Function;
import bigdata.objects.AssetFeatures;
import scala.Tuple2;

/**
 * Drops assets that are too volatile (at or above the threshold).
 */
public class VolatilityFilter implements Function<Tuple2<String, AssetFeatures>, Boolean> {

    private static final long serialVersionUID = 1L;

    private double volatilityThreshold;

    public VolatilityFilter(double volatilityThreshold) {
        this.volatilityThreshold = volatilityThreshold;
    }

    @Override
    public Boolean call(Tuple2<String, AssetFeatures> assetWithFeatures) throws Exception {
        return assetWithFeatures._2.getAssetVolitility() < volatilityThreshold;
    }
}
