package boxOffice;

/**
 * SeatType enum - represents different types of seats in the venue
 *
 * EXAM PATTERN: Simple enum with parsing method
 * TIME: 3-4 minutes
 * MARKS: 3
 *
 * Key concepts:
 * - Enum for fixed set of values
 * - Custom parsing method (String to enum conversion)
 * - Handle invalid input by returning null
 */
public enum SeatType {
    STANDARD,  // Regular seats
    DELUXE;    // Premium seats

    /**
     * Parse single character to SeatType
     *
     * PATTERN: String to Enum conversion
     * Used when reading from text file or user input
     *
     * @param s Single character: "S" for STANDARD, "D" for DELUXE
     * @return Corresponding SeatType, or null if invalid
     *
     * Example usage:
     *   SeatType type = SeatType.fromString("S");  // Returns STANDARD
     *   SeatType type = SeatType.fromString("D");  // Returns DELUXE
     *   SeatType type = SeatType.fromString("X");  // Returns null
     */
    public static SeatType fromString(String s) {
        // Check for STANDARD
        if (s.equals("S")) return STANDARD;

        // Check for DELUXE
        if (s.equals("D")) return DELUXE;

        // Invalid input - return null (caller should handle)
        return null;
    }
}
