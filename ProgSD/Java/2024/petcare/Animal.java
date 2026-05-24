package petcare;

import java.util.Objects;

/**
 * Animal class - represents an animal in the pet care system
 *
 * EXAM PATTERN: Data class with validation
 * TIME: 12-15 minutes
 * MARKS: 10
 *
 * Key concepts demonstrated:
 * - Private fields with getters/setters
 * - Constructor validation
 * - Setter validation (validate in BOTH constructor AND setters!)
 * - Override toString, equals, hashCode
 */
public class Animal {
    // STEP 1: Declare private fields
    // Why private? Encapsulation - control how fields are accessed/modified
    private String name;
    private AnimalSize size;
    private int minTemperature;  // Lower bound of comfortable temperature range
    private int maxTemperature;  // Upper bound of comfortable temperature range

    /**
     * Constructor - creates a new Animal with validation
     *
     * IMPORTANT: Always validate in constructor BEFORE assigning!
     * This prevents creating invalid objects.
     *
     * @param name Animal's name (must be at least 3 characters)
     * @param size Animal's size (SMALL, MEDIUM, or LARGE)
     * @param minTemperature Minimum comfortable temperature (0-50 inclusive)
     * @param maxTemperature Maximum comfortable temperature (0-50 inclusive)
     * @throws IllegalArgumentException if any validation fails
     */
    public Animal(String name, AnimalSize size, int minTemperature, int maxTemperature) {
        // VALIDATION RULE 1: Name must be at least 3 characters
        // Check for null first to avoid NullPointerException!
        if (name == null || name.length() < 3) {
            throw new IllegalArgumentException("Name must be at least 3 characters long");
        }

        // VALIDATION RULE 2: Min temperature must be in range 0-50
        if (minTemperature < 0 || minTemperature > 50) {
            throw new IllegalArgumentException("Min temperature must be between 0 and 50");
        }

        // VALIDATION RULE 3: Max temperature must be in range 0-50
        if (maxTemperature < 0 || maxTemperature > 50) {
            throw new IllegalArgumentException("Max temperature must be between 0 and 50");
        }

        // VALIDATION RULE 4: Min cannot be greater than max (logical check)
        if (minTemperature > maxTemperature) {
            throw new IllegalArgumentException("Min temperature cannot be greater than max temperature");
        }

        // Only assign AFTER all validation passes
        this.name = name;
        this.size = size;
        this.minTemperature = minTemperature;
        this.maxTemperature = maxTemperature;
    }

    // STEP 2: Getter methods
    // Simple methods that return the field value
    // No validation needed in getters!

    public String getName() {
        return name;
    }

    /**
     * Setter for name - allows changing the name after creation
     *
     * CRITICAL: Must validate just like in constructor!
     * Why? To prevent changing valid object to invalid state.
     */
    public void setName(String name) {
        // Same validation as constructor
        if (name == null || name.length() < 3) {
            throw new IllegalArgumentException("Name must be at least 3 characters long");
        }
        this.name = name;
    }

    public AnimalSize getSize() {
        return size;
    }

    public void setSize(AnimalSize size) {
        // No validation needed - enum can only be valid values
        this.size = size;
    }

    public int getMinTemperature() {
        return minTemperature;
    }

    /**
     * Setter for minTemperature with validation
     *
     * NOTE: When setting min, must check it doesn't exceed current max!
     */
    public void setMinTemperature(int minTemperature) {
        // Range validation
        if (minTemperature < 0 || minTemperature > 50) {
            throw new IllegalArgumentException("Min temperature must be between 0 and 50");
        }
        // Logical validation - compare with CURRENT maxTemperature
        if (minTemperature > this.maxTemperature) {
            throw new IllegalArgumentException("Min temperature cannot be greater than max temperature");
        }
        this.minTemperature = minTemperature;
    }

    public int getMaxTemperature() {
        return maxTemperature;
    }

    /**
     * Setter for maxTemperature with validation
     *
     * NOTE: When setting max, must check it's not less than current min!
     */
    public void setMaxTemperature(int maxTemperature) {
        // Range validation
        if (maxTemperature < 0 || maxTemperature > 50) {
            throw new IllegalArgumentException("Max temperature must be between 0 and 50");
        }
        // Logical validation - compare with CURRENT minTemperature
        if (this.minTemperature > maxTemperature) {
            throw new IllegalArgumentException("Min temperature cannot be greater than max temperature");
        }
        this.maxTemperature = maxTemperature;
    }

    /**
     * STEP 3: Override toString()
     *
     * Purpose: Provide human-readable representation
     * Called automatically by System.out.println()
     *
     * @return String representation like "Buddy (MEDIUM, 15-25°C)"
     */
    @Override
    public String toString() {
        return name + " (" + size + ", " + minTemperature + "-" + maxTemperature + "°C)";
    }

    /**
     * STEP 4: Override equals()
     *
     * Purpose: Define when two Animal objects are considered "equal"
     * Exam spec: "equals should return true when two animals are the same size and have the same name"
     *
     * PATTERN: Standard equals() implementation
     * 1. Check if same object reference
     * 2. Check if null or different class
     * 3. Cast and compare fields
     *
     * @param obj Object to compare with
     * @return true if same name and size, false otherwise
     */
    @Override
    public boolean equals(Object obj) {
        // Quick check: comparing to itself?
        if (this == obj) return true;

        // Safety checks: null or different class?
        if (obj == null || getClass() != obj.getClass()) return false;

        // Safe to cast now
        Animal animal = (Animal) obj;

        // Compare based on exam requirements: size and name
        // Use == for enums, Objects.equals() for Strings (handles null)
        return size == animal.size && Objects.equals(name, animal.name);
    }

    /**
     * STEP 5: Override hashCode()
     *
     * Purpose: Generate hash code for use in HashSet/HashMap
     *
     * RULE: If you override equals(), you MUST override hashCode()!
     * RULE: Objects that are equal() must have same hashCode()
     *
     * Use Objects.hash() with SAME fields as equals()
     *
     * @return hash code based on name and size
     */
    @Override
    public int hashCode() {
        // Use same fields as equals() - name and size
        return Objects.hash(name, size);
    }
}
