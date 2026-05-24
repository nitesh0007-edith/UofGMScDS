package trading;

import java.util.HashMap;
import java.util.Map;

/**
 * Citizen class - player who trades gems for goods
 *
 * EXAM PATTERN: Inventory management with Map
 * TIME: 12-15 minutes
 * MARKS: 10
 *
 * Key concepts:
 * - Currency (gems) management
 * - Inventory stored in Map (Goods → quantity)
 * - getOrDefault pattern for sparse maps
 * - Transaction method (deduct currency, add goods)
 * - Return boolean for success/failure
 */
public class Citizen {

    // Currency for trading
    private int gems;

    // Inventory: Maps each type of goods to quantity owned
    // PATTERN: Map<Enum, Integer> for counting items by type
    // Only stores goods that citizen owns (sparse representation)
    // If goods not in map, citizen has 0 of that item
    private Map<Goods, Integer> inventory;

    /**
     * Constructor - creates citizen with starting gems
     *
     * @param gems Starting amount of gems (currency)
     */
    public Citizen(int gems) {
        this.gems = gems;

        // IMPORTANT: Initialize map in constructor
        // Start with empty map - goods will be added as citizen trades
        this.inventory = new HashMap<>();
    }

    /**
     * Get current gem balance
     *
     * @return Number of gems citizen has
     */
    public int getGems() {
        return gems;
    }

    /**
     * Get quantity of specific goods owned
     *
     * PATTERN: getOrDefault for sparse map
     *
     * WHY getOrDefault?
     * - If citizen has never received this goods, it won't be in map
     * - getOrDefault returns 0 instead of null
     * - Avoids NullPointerException
     *
     * @param goods Type of goods to check
     * @return Quantity owned (0 if citizen doesn't have any)
     */
    public int getAmount(Goods goods) {
        // If goods not in map, return 0 (default value)
        // If goods is in map, return current amount
        return inventory.getOrDefault(goods, 0);
    }

    /**
     * Execute a trade (spend gems, receive goods)
     *
     * ALGORITHM:
     * 1. Check if citizen has enough gems
     * 2. If not, return false (trade fails)
     * 3. If yes:
     *    a. Deduct gems
     *    b. Add goods to inventory
     *    c. Return true (trade succeeds)
     *
     * PATTERN: Transaction with validation
     * - Check precondition (enough gems)
     * - Perform transaction (modify state)
     * - Return success indicator
     *
     * @param trade The trade to execute
     * @return true if successful, false if not enough gems
     */
    public boolean executeTrade(Trade trade) {
        // VALIDATION: Check if citizen can afford this trade
        if (gems < trade.getGems()) {
            return false;  // Not enough gems - trade fails
        }

        // STEP 1: Deduct cost from gems
        gems -= trade.getGems();

        // STEP 2: Add goods to inventory
        // Get current amount of this goods (0 if never had any)
        int currentAmount = getAmount(trade.getGoods());

        // Update map with new total
        // currentAmount + trade.getAmount() = old amount + newly acquired
        inventory.put(trade.getGoods(), currentAmount + trade.getAmount());

        // Trade successful
        return true;
    }

    /**
     * Get complete inventory
     *
     * Useful for displaying all goods citizen owns
     *
     * @return Map of goods to quantities
     */
    public Map<Goods, Integer> getInventory() {
        return inventory;
    }

    /**
     * toString for display
     */
    @Override
    public String toString() {
        return "Citizen{gems=" + gems + ", inventory=" + inventory + "}";
    }
}
