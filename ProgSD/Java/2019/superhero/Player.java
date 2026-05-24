package superhero;

import java.util.HashSet;
import java.util.Set;

/**
 * Player class - manages collection of characters and finds combinations
 *
 * EXAM PATTERN: Manager with recursive algorithm
 * TIME: 18-22 minutes
 * MARKS: 15
 *
 * Key concepts:
 * - Managing Set of characters
 * - Varargs parameter
 * - Recursive backtracking algorithm
 * - Set operations (union, contains all)
 * - Helper method pattern (public + private recursive)
 */
public class Player {

    // Collection of characters owned by player
    // WHY SET? Each character should only be owned once (no duplicates)
    private Set<GameCharacter> characters;

    /**
     * Constructor - creates player with no characters
     */
    public Player() {
        // Initialize empty set
        this.characters = new HashSet<>();
    }

    /**
     * Add a character to player's collection
     *
     * PATTERN: Simple add to Set
     * Set automatically prevents duplicate characters
     *
     * @param character Character to add
     */
    public void addCharacter(GameCharacter character) {
        characters.add(character);
    }

    /**
     * Get all characters owned by player
     */
    public Set<GameCharacter> getCharacters() {
        return characters;
    }

    /**
     * Choose minimum set of characters that provides all needed powers
     *
     * ALGORITHM:
     * 1. Convert varargs to Set of needed powers
     * 2. Recursively search for character combination
     * 3. Return smallest set that provides all powers (or null if impossible)
     *
     * PATTERN: Recursive backtracking / subset selection
     *
     * Example:
     *   Player has: [Hero1(FLIGHT), Hero2(SPEED), Hero3(FLIGHT, SPEED)]
     *   chooseCharacters(FLIGHT, SPEED) could return:
     *     - [Hero3] (best - single character)
     *     - or [Hero1, Hero2] (also works but uses 2 characters)
     *
     * @param neededPowers Variable number of powers required
     * @return Set of characters providing all powers, or null if impossible
     */
    public Set<GameCharacter> chooseCharacters(Power... neededPowers) {
        // STEP 1: Convert varargs array to Set
        // WHY? Easier to check "contains all" with Set
        Set<Power> needed = new HashSet<>();
        for (Power power : neededPowers) {
            needed.add(power);
        }

        // STEP 2: Start recursive search
        // Initial call: no characters chosen yet, all characters available
        return findCharacterCombination(needed, new HashSet<>(), characters);
    }

    /**
     * Recursive helper method - find combination of characters
     *
     * ALGORITHM (Backtracking):
     * 1. BASE CASE 1: If current characters provide all powers → SUCCESS, return them
     * 2. BASE CASE 2: If no more characters to try → FAILURE, return null
     * 3. RECURSIVE CASE: Try adding each remaining character:
     *    a. Add character to current set
     *    b. Remove from remaining set
     *    c. Recursively try to complete the combination
     *    d. If successful, return result
     *    e. If not, backtrack and try next character
     *
     * PATTERN: Recursive subset search
     * This explores all possible combinations until finding one that works
     *
     * TIME COMPLEXITY: O(2^n) worst case (exponential)
     * - May need to try many combinations
     * - But stops as soon as valid combination found
     *
     * @param neededPowers Powers that must be provided
     * @param currentChars Characters chosen so far
     * @param remainingChars Characters not yet chosen
     * @return Valid combination, or null if none exists
     */
    private Set<GameCharacter> findCharacterCombination(Set<Power> neededPowers,
                                                         Set<GameCharacter> currentChars,
                                                         Set<GameCharacter> remainingChars) {

        // STEP 1: Check if current characters already provide all needed powers
        // Collect all powers from all current characters
        Set<Power> providedPowers = new HashSet<>();
        for (GameCharacter character : currentChars) {
            // addAll adds all powers from this character to our set
            // This is SET UNION operation
            providedPowers.addAll(character.getPowers());
        }

        // BASE CASE 1: Success!
        // containsAll checks if providedPowers is superset of neededPowers
        if (providedPowers.containsAll(neededPowers)) {
            // Found a valid combination!
            // Return copy to avoid modification by caller
            return new HashSet<>(currentChars);
        }

        // BASE CASE 2: Failure
        // No more characters to try, and we still don't have all powers
        if (remainingChars.isEmpty()) {
            return null;  // Impossible to get all powers
        }

        // RECURSIVE CASE: Try adding each remaining character
        for (GameCharacter character : remainingChars) {
            // Create new current set WITH this character added
            Set<GameCharacter> newCurrent = new HashSet<>(currentChars);
            newCurrent.add(character);

            // Create new remaining set WITHOUT this character
            Set<GameCharacter> newRemaining = new HashSet<>(remainingChars);
            newRemaining.remove(character);

            // RECURSIVE CALL: Try to complete combination with this character
            Set<GameCharacter> result = findCharacterCombination(
                neededPowers,
                newCurrent,
                newRemaining
            );

            // Did this branch succeed?
            if (result != null) {
                return result;  // Yes! Return successful combination
            }

            // This branch failed - backtrack and try next character
        }

        // Tried all characters, none worked
        return null;
    }

    /**
     * Get total number of characters owned
     */
    public int getCharacterCount() {
        return characters.size();
    }

    /**
     * Check if player owns a specific character
     */
    public boolean hasCharacter(GameCharacter character) {
        return characters.contains(character);
    }
}
