package boxOffice;

import java.util.ArrayList;
import java.util.List;

/**
 * Venue class - manages seating layout for a theatre
 *
 * EXAM PATTERN: String parser + 2D collection manager
 * TIME: 15-18 minutes
 * MARKS: 12
 *
 * Key concepts:
 * - String parsing with split()
 * - 2D structure using List<List<>>
 * - Character arithmetic (A + i)
 * - Index mapping (0-based vs 1-based)
 * - Position-based access
 */
public class Venue {

    // 2D structure: List of rows, each row is a List of seats
    // rows.get(0) = Row A (list of seats in row A)
    // rows.get(1) = Row B (list of seats in row B)
    // etc.
    private List<List<Seat>> rows;

    /**
     * Constructor - parse venue configuration from string
     *
     * INPUT FORMAT:
     * Line 1: Number of rows
     * Lines 2+: Seat types for each row (space-separated)
     *
     * EXAMPLE:
     * "3\nS S D\nS S S\nD D D"
     * Means:
     *   3 rows total
     *   Row A: STANDARD STANDARD DELUXE (3 seats)
     *   Row B: STANDARD STANDARD STANDARD (3 seats)
     *   Row C: DELUXE DELUXE DELUXE (3 seats)
     *
     * ALGORITHM:
     * 1. Split input into lines
     * 2. Read number of rows from first line
     * 3. For each row:
     *    a. Split row string by spaces to get seat types
     *    b. Convert array index to row letter (0→A, 1→B, etc.)
     *    c. Create seats with proper position and type
     *    d. Add to row list
     * 4. Add row to venue
     *
     * @param config String specification of venue layout
     */
    public Venue(String config) {
        // Initialize the 2D structure
        rows = new ArrayList<>();

        // STEP 1: Split input into lines
        // "\n" splits at newlines, creating array of strings
        String[] lines = config.split("\n");

        // STEP 2: Parse metadata - first line is number of rows
        int numRows = Integer.valueOf(lines[0]);

        // STEP 3: Parse each row's seat configuration
        for (int i = 0; i < numRows; i++) {
            // Get the configuration for this row
            // lines[i + 1] because lines[0] was the count
            // Example: "S S D" for row with 3 seats
            String[] seatTypes = lines[i + 1].split(" ");

            // Create list to hold seats in this row
            List<Seat> row = new ArrayList<>();

            // STEP 4: Calculate row letter
            // i=0 → 'A', i=1 → 'B', i=2 → 'C', etc.
            // Character arithmetic: 'A' + 0 = 'A', 'A' + 1 = 'B'
            char rowLetter = (char) ('A' + i);

            // STEP 5: Create each seat in the row
            for (int j = 0; j < seatTypes.length; j++) {
                // Parse seat type from string
                // "S" → STANDARD, "D" → DELUXE
                SeatType type = SeatType.fromString(seatTypes[j]);

                // Create seat with:
                // - Row letter (A, B, C...)
                // - Seat number (j + 1 because seats numbered 1, 2, 3... not 0, 1, 2)
                // - Seat type (STANDARD or DELUXE)
                Seat seat = new Seat(rowLetter, j + 1, type);

                // Add seat to this row
                row.add(seat);
            }

            // Add completed row to venue
            rows.add(row);
        }
    }

    /**
     * Get specific seat by position
     *
     * PATTERN: Position-based access with index conversion
     *
     * IMPORTANT INDEX MAPPING:
     * - Row letter 'A' maps to index 0
     * - Row letter 'B' maps to index 1
     * - Seat number 1 maps to index 0
     * - Seat number 2 maps to index 1
     *
     * @param row Row letter (A, B, C, etc.)
     * @param seatNum Seat number in row (1, 2, 3, etc.)
     * @return The seat at that position
     * @throws IllegalArgumentException if position is invalid
     */
    public Seat getSeat(char row, int seatNum) {
        // VALIDATION 1: Check row is in valid range
        // row must be >= 'A' and < 'A' + number of rows
        // Example: If 3 rows, valid rows are A, B, C (not D or higher)
        if (row < 'A' || row >= 'A' + rows.size()) {
            throw new IllegalArgumentException("Invalid row: " + row);
        }

        // STEP 1: Convert row letter to array index
        // 'A' - 'A' = 0, 'B' - 'A' = 1, 'C' - 'A' = 2, etc.
        int rowIndex = row - 'A';

        // Get the list of seats in this row
        List<Seat> rowSeats = rows.get(rowIndex);

        // VALIDATION 2: Check seat number is in valid range
        // Seat numbers start at 1, so valid range is 1 to rowSeats.size()
        if (seatNum <= 0 || seatNum > rowSeats.size()) {
            throw new IllegalArgumentException("Invalid seat number: " + seatNum);
        }

        // STEP 2: Convert seat number to array index
        // Seat 1 is at index 0, Seat 2 at index 1, etc.
        // So we use seatNum - 1
        return rowSeats.get(seatNum - 1);
    }

    /**
     * Print complete venue layout
     *
     * PATTERN: Nested loop display of 2D structure
     * Shows all seats with their status
     */
    public void printDetails() {
        // Loop through each row
        for (int i = 0; i < rows.size(); i++) {
            // Calculate row letter for display
            char rowLetter = (char) ('A' + i);
            System.out.print("Row " + rowLetter + ": ");

            // Loop through each seat in this row
            for (Seat seat : rows.get(i)) {
                // Format seat information
                String availability = seat.isAvailable() ? "Available" : "Reserved";
                String type = seat.getSeatType() == SeatType.STANDARD ? "Standard" : "Deluxe";

                System.out.print("Seat " + seat.getSeatNumber() +
                               " (" + type + ", " + availability + ") ");
            }

            System.out.println();  // New line after each row
        }
    }

    /**
     * Get total number of rows in venue
     */
    public int getRowCount() {
        return rows.size();
    }

    /**
     * Get number of seats in a specific row
     *
     * @param row Row letter (A, B, C, etc.)
     * @return Number of seats in that row
     */
    public int getSeatsInRow(char row) {
        int rowIndex = row - 'A';
        if (rowIndex < 0 || rowIndex >= rows.size()) {
            return 0;
        }
        return rows.get(rowIndex).size();
    }

    /**
     * Count available seats in entire venue
     *
     * PATTERN: Count with condition across 2D structure
     */
    public int countAvailableSeats() {
        int count = 0;

        // Loop through all rows
        for (List<Seat> row : rows) {
            // Loop through all seats in each row
            for (Seat seat : row) {
                if (seat.isAvailable()) {
                    count++;
                }
            }
        }

        return count;
    }
}
