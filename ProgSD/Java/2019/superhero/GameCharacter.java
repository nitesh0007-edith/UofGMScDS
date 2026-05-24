package superhero;

import java.util.Collections;
import java.util.HashSet;
import java.util.Objects;
import java.util.Set;

/**
 * GameCharacter class - represents a playable superhero character
 *
 * EXAM PATTERN: Data class with Set collection and varargs
 * TIME: 12-15 minutes
 * MARKS: 10
 *
 * Key concepts:
 * - Immutable fields (final)
 * - Set for unique items (no duplicate powers)
 * - Varargs (Power... powers) for variable number of arguments
 * - Collections.unmodifiableSet() for encapsulation
 * - Equals based on all fields
 */
public class GameCharacter {

    /**
     * The name of the character
     * PATTERN: final = immutable (cannot be changed after construction)
     */
    private final String name;

    /**
     * The cost to purchase this character
     * Used by Player to determine if they can afford character
     */
    private final int cost;

    /**
     * The set of powers this character possesses
     *
     * WHY SET instead of List?
     * - Each power should only appear once (no duplicates)
     * - Order of powers doesn't matter
     * - Set automatically prevents duplicates
     */
    private final Set<Power> powers;

    /**
     * Creates a new GameCharacter with specified name, cost, and powers
     *
     * PATTERN: Varargs (Power... powers)
     * - Allows: new GameCharacter("Hero", 100, FLIGHT)
     * - Or: new GameCharacter("Hero", 100, FLIGHT, SPEED, STRENGTH)
     * - Powers are passed as array, but written as separate arguments
     *
     * @param name the name of the character
     * @param cost the cost to purchase this character
     * @param powers variable number of powers (0 or more)
     */
    public GameCharacter(String name, int cost, Power... powers) {
        // No validation in exam specification
        this.name = name;
        this.cost = cost;

        // Initialize set
        this.powers = new HashSet<>();

        // PATTERN: Converting varargs to Set
        // powers is actually an array (Power[])
        // Loop through and add each power to set
        for (Power power : powers) {
            this.powers.add(power);
        }
        // Note: If duplicate powers passed, Set automatically ignores them
    }

    /**
     * Gets the name of this character
     */
    public String getName() {
        return name;
    }

    /**
     * Gets the cost of this character
     */
    public int getCost() {
        return cost;
    }

    /**
     * Gets an unmodifiable set of powers this character has
     *
     * PATTERN: Defensive copy with Collections.unmodifiableSet()
     *
     * WHY unmodifiableSet?
     * - Prevents caller from modifying our internal set
     * - If we returned powers directly, caller could do:
     *   character.getPowers().add(MAGIC)  // Would break encapsulation!
     * - unmodifiableSet prevents this - throws exception if caller tries to modify
     *
     * @return the set of powers (read-only view)
     */
    public Set<Power> getPowers() {
        return Collections.unmodifiableSet(powers);
    }

    /**
     * Check if character has a specific power
     *
     * Useful helper method for game logic
     */
    public boolean hasPower(Power power) {
        return powers.contains(power);
    }

    /**
     * Get number of powers this character has
     */
    public int getPowerCount() {
        return powers.size();
    }

    /**
     * toString for display
     *
     * PATTERN: Include all relevant information
     */
    @Override
    public String toString() {
        return name + " (Cost: " + cost + ", Powers: " + powers + ")";
    }

    /**
     * equals - characters are equal if ALL fields match
     *
     * PATTERN: Composite equality with Set
     * - name must match
     * - cost must match
     * - powers set must match (same powers, order doesn't matter)
     */
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;

        GameCharacter that = (GameCharacter) obj;

        // All three fields must match
        // Note: Set.equals() compares contents, not order
        return cost == that.cost &&
               Objects.equals(name, that.name) &&
               Objects.equals(powers, that.powers);
    }

    /**
     * hashCode - use SAME fields as equals
     */
    @Override
    public int hashCode() {
        return Objects.hash(name, cost, powers);
    }
}
