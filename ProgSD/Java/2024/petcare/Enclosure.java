package petcare;

/**
 * Enclosure class - represents a cage/pen that holds one animal
 *
 * EXAM PATTERN: Container class with compatibility checking
 * TIME: 15-18 minutes
 * MARKS: 15
 *
 * Key concepts demonstrated:
 * - Compatibility checking (size + temperature)
 * - State management (occupant can be null)
 * - Add/remove with validation
 * - Enum comparison for size matching
 */
public class Enclosure {
    // Fields - describe the enclosure properties
    private AnimalSize size;       // Maximum animal size this enclosure can hold
    private int temperature;       // Current temperature maintained in enclosure
    private int runningCosts;      // Cost per day to run this enclosure
    private Animal occupant;       // Current animal (null if empty)

    /**
     * Constructor - creates an empty enclosure
     *
     * NOTE: Occupant starts as null (empty enclosure)
     * NOTE: No setters! Once created, enclosure properties are fixed
     *
     * @param size Maximum size of animal this enclosure can hold
     * @param temperature Temperature maintained in this enclosure
     * @param runningCosts Daily cost to maintain this enclosure
     */
    public Enclosure(AnimalSize size, int temperature, int runningCosts) {
        this.size = size;
        this.temperature = temperature;
        this.runningCosts = runningCosts;
        this.occupant = null;  // Starts empty - IMPORTANT!
    }

    // Getters only - no setters (enclosure properties are fixed)

    public AnimalSize getSize() {
        return size;
    }

    public int getTemperature() {
        return temperature;
    }

    public int getRunningCosts() {
        return runningCosts;
    }

    public Animal getOccupant() {
        return occupant;
    }

    /**
     * Check if an animal can fit in this enclosure
     *
     * COMPATIBILITY RULES:
     * 1. Size must match: SMALL animal fits anywhere,
     *                     MEDIUM needs MEDIUM or LARGE enclosure,
     *                     LARGE needs LARGE enclosure only
     * 2. Temperature must be in animal's comfort range
     *
     * This is a QUERY method - it doesn't change anything, just checks!
     *
     * @param animal Animal to check compatibility for
     * @return true if animal can fit, false otherwise
     */
    public boolean checkCompatibility(Animal animal) {
        // CHECK 1: Size compatibility
        // Pattern: Larger enclosure can hold smaller animals

        // LARGE animal needs LARGE enclosure (most restrictive)
        if (animal.getSize() == AnimalSize.LARGE && size != AnimalSize.LARGE) {
            return false;
        }

        // MEDIUM animal needs at least MEDIUM enclosure
        // (so SMALL enclosure won't work)
        if (animal.getSize() == AnimalSize.MEDIUM && size == AnimalSize.SMALL) {
            return false;
        }

        // SMALL animal fits in any enclosure - no check needed!

        // CHECK 2: Temperature compatibility
        // Enclosure temperature must be within animal's comfort range
        // Example: If animal needs 15-25°C and enclosure is 20°C → OK
        //          If animal needs 15-25°C and enclosure is 30°C → NOT OK
        if (temperature < animal.getMinTemperature() || temperature > animal.getMaxTemperature()) {
            return false;
        }

        // Both checks passed!
        return true;
    }

    /**
     * Add an animal to this enclosure
     *
     * VALIDATION:
     * 1. Enclosure must be empty (occupant == null)
     * 2. Animal must be compatible
     *
     * @param animal Animal to add
     * @throws IllegalArgumentException if enclosure occupied or animal incompatible
     */
    public void addAnimal(Animal animal) {
        // CHECK 1: Is enclosure already occupied?
        if (occupant != null) {
            throw new IllegalArgumentException("Enclosure already has an occupant");
        }

        // CHECK 2: Is animal compatible? (use our compatibility method!)
        if (!checkCompatibility(animal)) {
            throw new IllegalArgumentException("Animal is not compatible with this enclosure");
        }

        // Both checks passed - safe to add
        occupant = animal;
    }

    /**
     * Remove the current animal from enclosure
     *
     * NOTE: Exam says "if removeAnimal is called on empty enclosure, nothing should happen"
     * So we DON'T throw exception - just do nothing!
     */
    public void removeAnimal() {
        // Simply set to null - makes enclosure empty again
        // No validation needed - spec says "nothing should happen" if already empty
        occupant = null;
    }
}
