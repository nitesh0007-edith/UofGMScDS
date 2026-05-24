package boxOffice;

/**
 * Seat class - represents a single seat in the venue
 *
 * EXAM PATTERN: Data class with state management
 * TIME: 10-12 minutes
 * MARKS: 8
 *
 * Key concepts:
 * - Position-based identification (row + number)
 * - Type categorization (STANDARD or DELUXE)
 * - State management (available vs booked)
 * - Character validation (A-Z for rows)
 */
public class Seat {

    // Position in venue
    private char row;           // Row letter (A-Z)
    private int seatNumber;     // Seat number in that row (1, 2, 3...)

    // Seat properties
    private SeatType seatType;  // STANDARD or DELUXE

    // State
    private boolean isAvailable; // true = can be booked, false = already booked

    /**
     * Constructor - creates a seat at given position
     *
     * VALIDATION:
     * - Row must be A-Z (uppercase letters only)
     * - Seat number must be positive (1 or greater)
     * - Seat type validated by enum (cannot be null)
     *
     * Initial state: All seats start as available
     *
     * @param row Row letter (A-Z)
     * @param seatNumber Seat number in row (must be positive)
     * @param seatType Type of seat (STANDARD or DELUXE)
     */
    public Seat(char row, int seatNumber, SeatType seatType) {
        // VALIDATION RULE 1: Row must be uppercase letter A-Z
        // Why A-Z? Theatre rows are typically labeled with letters
        if (row < 'A' || row > 'Z') {
            throw new IllegalArgumentException("Row must be between A and Z");
        }

        // VALIDATION RULE 2: Seat number must be positive
        // Seats are numbered 1, 2, 3... (not 0)
        if (seatNumber <= 0) {
            throw new IllegalArgumentException("Seat number must be positive");
        }

        // Assign validated values
        this.row = row;
        this.seatNumber = seatNumber;
        this.seatType = seatType;

        // Initial state: All seats start available
        // Seats become unavailable when booked
        this.isAvailable = true;
    }

    /**
     * Get row letter
     * Example: 'A', 'B', 'C', etc.
     */
    public char getRow() {
        return row;
    }

    /**
     * Get seat number within the row
     * Example: 1, 2, 3, etc.
     */
    public int getSeatNumber() {
        return seatNumber;
    }

    /**
     * Get seat type (STANDARD or DELUXE)
     */
    public SeatType getSeatType() {
        return seatType;
    }

    /**
     * Check if seat is available for booking
     *
     * PATTERN: Boolean state query
     * @return true if seat can be booked, false if already booked
     */
    public boolean isAvailable() {
        return isAvailable;
    }

    /**
     * Set availability state
     *
     * PATTERN: State change method
     *
     * Usage:
     * - setAvailable(false) when booking a seat
     * - setAvailable(true) when cancelling a booking
     *
     * @param available true to make available, false to mark as booked
     */
    public void setAvailable(boolean available) {
        isAvailable = available;
    }

    /**
     * Get seat identifier as string
     *
     * PATTERN: Position to ID conversion
     * Example: Row 'A', Seat 5 → "A5"
     *
     * This is useful for display and searching
     */
    public String getSeatId() {
        return row + String.valueOf(seatNumber);
    }

    /**
     * toString for display
     */
    @Override
    public String toString() {
        String status = isAvailable ? "Available" : "Booked";
        return "Seat{" + getSeatId() + ", " + seatType + ", " + status + "}";
    }
}
