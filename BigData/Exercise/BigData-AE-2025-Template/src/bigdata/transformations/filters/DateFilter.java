package bigdata.transformations.filters;

import org.apache.spark.api.java.function.FilterFunction;
import bigdata.objects.StockPrice;
import bigdata.util.TimeUtil;
import java.time.Instant;

/**
 * Only keeps prices on or before the given end date.
 */
public class DateFilter implements FilterFunction<StockPrice> {

    private static final long serialVersionUID = 1L;

    private Instant endDate;

    public DateFilter(String endDateString) {
        this.endDate = TimeUtil.fromDate(endDateString);
    }

    @Override
    public boolean call(StockPrice price) throws Exception {
        Instant priceDate = TimeUtil.fromDate(price.getYear(), price.getMonth(), price.getDay());
        return !priceDate.isAfter(endDate);
    }
}
