package trading;

public class TestTrading {
    public static void main(String[] args) {
        System.out.println("=== Testing Trading System ===\n");

        // Create a citizen
        Citizen citizen = new Citizen(10);
        System.out.println("Citizen created with " + citizen.getGems() + " gems");

        // Create a trader
        Trader trader = new Trader();
        System.out.println("\nTrader's initial trades:");
        for (Trade trade : trader.getTrades()) {
            System.out.println("  " + trade);
        }

        // Execute a trade
        System.out.println("\n=== Executing First Trade ===");
        Trade firstTrade = trader.getTrades().get(0);
        System.out.println("Attempting: " + firstTrade);
        firstTrade.execute(trader, citizen);

        System.out.println("Citizen now has " + citizen.getGems() + " gems");
        System.out.println("Citizen inventory: " + citizen.getAmount(firstTrade.getGoods()) + " " + firstTrade.getGoods());

        System.out.println("\nTrader now has " + trader.getTrades().size() + " trades:");
        for (Trade trade : trader.getTrades()) {
            System.out.println("  " + trade);
        }

        // Create and test a specific trade
        System.out.println("\n=== Testing Specific Trade ===");
        Trade breadTrade = new Trade(2, 5, Goods.BREAD);
        System.out.println("Trade: " + breadTrade);

        Citizen citizen2 = new Citizen(5);
        boolean success = citizen2.executeTrade(breadTrade);
        System.out.println("Trade successful: " + success);
        System.out.println("Citizen gems: " + citizen2.getGems());
        System.out.println("Citizen bread: " + citizen2.getAmount(Goods.BREAD));
    }
}
