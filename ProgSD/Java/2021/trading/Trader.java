package trading;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

/**
 * Trader class - NPC that offers random trades
 *
 * EXAM PATTERN: Manager with random generation
 * TIME: 10-12 minutes
 * MARKS: 8
 *
 * Key concepts:
 * - Managing collection of trades
 * - Random number generation
 * - Getting all enum values
 * - Random selection from array
 * - Initialize with random content
 */
public class Trader {

    // Collection of available trades
    private List<Trade> trades;

    // Random number generator
    // PATTERN: Store Random as field to reuse (more efficient)
    private Random rand;

    /**
     * Constructor - creates trader with one random trade
     *
     * PATTERN: Initialize with random content
     * Trader starts with one random trade offer
     */
    public Trader() {
        // Initialize collections
        this.trades = new ArrayList<>();

        // Create Random object for generating trades
        this.rand = new Random();

        // Start with one random trade
        addRandomTrade();
    }

    /**
     * Get all available trades
     *
     * Used by Trade.execute() to validate trade exists
     *
     * @return List of trades this trader offers
     */
    public List<Trade> getTrades() {
        return trades;
    }

    /**
     * Add a new random trade to trader's offerings
     *
     * ALGORITHM:
     * 1. Generate random gem cost (1-5)
     * 2. Generate random amount (1-5)
     * 3. Select random goods type
     * 4. Create trade and add to list
     *
     * PATTERN: Random generation with bounds
     *
     * Key Java concepts:
     * - rand.nextInt(N) returns 0 to N-1
     * - rand.nextInt(5) + 1 returns 1 to 5
     * - Goods.values() returns array of all enum values
     */
    public void addRandomTrade() {
        // STEP 1: Generate random gem cost (1 to 5)
        // rand.nextInt(5) gives 0-4, + 1 gives 1-5
        int gems = rand.nextInt(5) + 1;

        // STEP 2: Generate random amount (1 to 5)
        int amount = rand.nextInt(5) + 1;

        // STEP 3: Select random goods type
        // Goods.values() returns array of ALL enum values
        // Example: [BREAD, COAL, FISH, HELMET, ...]
        Goods[] allGoods = Goods.values();

        // Pick random index from array
        // rand.nextInt(allGoods.length) gives 0 to length-1
        Goods goods = allGoods[rand.nextInt(allGoods.length)];

        // STEP 4: Create trade and add to list
        trades.add(new Trade(gems, amount, goods));
    }

    /**
     * Display all available trades
     */
    public void printTrades() {
        System.out.println("=== Available Trades ===");
        for (int i = 0; i < trades.size(); i++) {
            System.out.println((i + 1) + ". " + trades.get(i));
        }
    }

    /**
     * Get number of trades available
     */
    public int getTradeCount() {
        return trades.size();
    }
}
