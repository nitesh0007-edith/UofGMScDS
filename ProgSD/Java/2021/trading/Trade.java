package trading;

import java.util.Objects;

/**
 * Trade class - represents a trade offer (exchange gems for goods)
 *
 * EXAM PATTERN: Data class with transaction method
 * TIME: 12-15 minutes
 * MARKS: 10
 *
 * Key concepts:
 * - Immutable trade offer (no setters)
 * - Equals based on all fields
 * - Transaction coordination (execute method)
 * - Validation in execute method
 */
public class Trade {

    // Cost in gems
    private int gems;

    // Amount of goods received
    private int amount;

    // Type of goods
    private Goods goods;

    /**
     * Constructor - creates a trade offer
     *
     * PATTERN: No validation in exam specification
     * Represents: "Give X gems, receive Y amount of GOODS"
     *
     * Example: Trade(5, 3, BREAD) = "5 gems for 3 BREAD"
     *
     * @param gems Cost in gems
     * @param amount Quantity of goods received
     * @param goods Type of goods
     */
    public Trade(int gems, int amount, Goods goods) {
        this.gems = gems;
        this.amount = amount;
        this.goods = goods;
    }

    /**
     * Get gem cost
     */
    public int getGems() {
        return gems;
    }

    /**
     * Get amount of goods
     */
    public int getAmount() {
        return amount;
    }

    /**
     * Get type of goods
     */
    public Goods getGoods() {
        return goods;
    }

    /**
     * toString - human-readable description
     *
     * PATTERN: Conditional plural handling
     * Examples:
     *   "1 gem for 3 BREAD"
     *   "5 gems for 2 SWORD"
     */
    @Override
    public String toString() {
        // Use ternary operator for singular/plural
        return gems + " gem" + (gems == 1 ? "" : "s") +
               " for " + amount + " " + goods;
    }

    /**
     * equals - trades are equal if ALL fields match
     *
     * PATTERN: Composite equality
     * Trade must have same gems, amount, AND goods to be equal
     */
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;

        Trade trade = (Trade) obj;

        // All three fields must match
        return gems == trade.gems &&
               amount == trade.amount &&
               goods == trade.goods;
    }

    /**
     * hashCode - use SAME fields as equals
     */
    @Override
    public int hashCode() {
        return Objects.hash(gems, amount, goods);
    }

    /**
     * Execute this trade between trader and citizen
     *
     * ALGORITHM:
     * 1. Validate that trader supports this trade
     * 2. Ask citizen to execute trade (deduct gems, add goods)
     * 3. If successful, trader adds new random trade
     *
     * PATTERN: Transaction coordination
     * This method coordinates actions between two objects
     *
     * @param trader The trader offering this trade
     * @param citizen The citizen attempting the trade
     * @throws IllegalArgumentException if trader doesn't support this trade
     */
    public void execute(Trader trader, Citizen citizen) {
        // VALIDATION: Check trader supports this trade
        // Trader must have this trade in their list of available trades
        if (!trader.getTrades().contains(this)) {
            throw new IllegalArgumentException("Trade not supported by this trader");
        }

        // STEP 1: Citizen attempts to execute trade
        // Returns true if successful (had enough gems)
        boolean success = citizen.executeTrade(this);

        // STEP 2: If successful, trader refreshes inventory
        if (success) {
            // Trader adds a new random trade to their offerings
            // This simulates trader restocking
            trader.addRandomTrade();
        }

        // If citizen didn't have enough gems, nothing happens
        // No exception thrown - just silently fails
    }
}
