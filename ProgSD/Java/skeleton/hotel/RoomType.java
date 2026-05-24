package hotel;

/**
 * PATTERN 1: ENUM with properties
 * TIME: 3-4 minutes
 * MARKS: 3
 *
 * ADVANCED: Enum with fields and methods
 */
public enum RoomType {
    SINGLE(1, 100),
    DOUBLE(2, 150),
    SUITE(4, 300),
    DELUXE(2, 200);

    // Fields for each enum constant
    private final int capacity;
    private final int basePrice;

    // Constructor (always private for enums)
    RoomType(int capacity, int basePrice) {
        this.capacity = capacity;
        this.basePrice = basePrice;
    }

    // Getters
    public int getCapacity() {
        return capacity;
    }

    public int getBasePrice() {
        return basePrice;
    }

    /**
     * PATTERN: Enum with business logic
     * Can accommodate given number of guests?
     */
    public boolean canAccommodate(int guests) {
        return guests <= capacity;
    }
}
