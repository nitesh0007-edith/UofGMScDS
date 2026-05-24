package boxOffice;

import java.util.HashMap;
import java.util.Map;

/**
 * Event class - manages bookings for an event at a venue
 *
 * EXAM PATTERN: Manager with complex search algorithm
 * TIME: 18-22 minutes
 * MARKS: 15
 *
 * Key concepts:
 * - Managing venue bookings
 * - Finding consecutive available items
 * - Price calculation with Map
 * - Exception handling for edge cases
 * - Nested loop search algorithm
 */
public class Event {

    // The venue where this event takes place
    private Venue venue;

    // Price map: SeatType → price
    // PATTERN: Use Map for quick lookup of prices by type
    private Map<SeatType, Integer> prices;

    /**
     * Constructor - creates event at venue with pricing
     *
     * @param venue The venue for this event
     * @param standardPrice Price for STANDARD seats
     * @param deluxePrice Price for DELUXE seats
     */
    public Event(Venue venue, int standardPrice, int deluxePrice) {
        this.venue = venue;

        // Initialize price map
        this.prices = new HashMap<>();
        prices.put(SeatType.STANDARD, standardPrice);
        prices.put(SeatType.DELUXE, deluxePrice);
    }

    /**
     * Reserve consecutive seats of given type
     *
     * MOST IMPORTANT ALGORITHM in this exam!
     *
     * REQUIREMENTS:
     * - Find numSeats consecutive seats
     * - All seats must be of specified type
     * - All seats must be available
     * - Seats must be in same row (adjacent)
     *
     * ALGORITHM:
     * 1. Try each row (A, B, C, ...)
     * 2. For each row, try each starting position (1, 2, 3, ...)
     * 3. Check if numSeats consecutive seats are:
     *    a. Available
     *    b. Correct type
     * 4. If found, reserve them and calculate total cost
     * 5. If not found anywhere, return -1
     *
     * @param numSeats Number of consecutive seats needed
     * @param seatType Type of seats (STANDARD or DELUXE)
     * @return Total cost if successful, -1 if not found
     */
    public int reserveSeats(int numSeats, SeatType seatType) {
        // OUTER LOOP: Try all possible rows
        // Start at 'A', try B, C, D, etc.
        for (char row = 'A'; row <= 'Z'; row++) {
            try {
                // MIDDLE LOOP: Try all possible starting positions in this row
                // Try starting at seat 1, 2, 3, ... up to 26
                for (int startSeat = 1; startSeat <= 26; startSeat++) {
                    // Assume we found a valid sequence (will set to false if not)
                    boolean found = true;

                    // INNER LOOP: Check if numSeats consecutive seats are available
                    // Check seats at positions: startSeat, startSeat+1, startSeat+2, etc.
                    for (int i = 0; i < numSeats; i++) {
                        try {
                            // Get the seat at this position
                            Seat seat = venue.getSeat(row, startSeat + i);

                            // CHECK 1: Is seat available?
                            // CHECK 2: Is seat the correct type?
                            if (!seat.isAvailable() || seat.getSeatType() != seatType) {
                                found = false;  // This sequence doesn't work
                                break;  // Stop checking this sequence
                            }
                        } catch (IllegalArgumentException e) {
                            // Seat doesn't exist (past end of row)
                            found = false;
                            break;
                        }
                    }

                    // Did we find a valid sequence?
                    if (found) {
                        // YES! Reserve all the seats
                        for (int i = 0; i < numSeats; i++) {
                            Seat seat = venue.getSeat(row, startSeat + i);
                            seat.setAvailable(false);  // Mark as booked
                        }

                        // Calculate total cost
                        // numSeats × price per seat of this type
                        int totalCost = numSeats * prices.get(seatType);
                        return totalCost;
                    }

                    // This sequence didn't work, try next starting position
                }

            } catch (IllegalArgumentException e) {
                // Row doesn't exist - we've tried all rows
                break;  // Exit outer loop
            }
        }

        // If we get here, no valid sequence found in any row
        return -1;
    }

    /**
     * Return (cancel) a seat booking
     *
     * PATTERN: State change with validation
     *
     * Makes a reserved seat available again
     *
     * @param row Row letter
     * @param seatNum Seat number
     * @throws IllegalArgumentException if seat is already available
     */
    public void returnSeat(char row, int seatNum) {
        // Get the seat
        Seat seat = venue.getSeat(row, seatNum);

        // VALIDATION: Can only return a seat that's currently reserved
        if (seat.isAvailable()) {
            throw new IllegalArgumentException("Seat is already available");
        }

        // Mark seat as available
        seat.setAvailable(true);
    }

    /**
     * Get price for a seat type
     *
     * @param seatType STANDARD or DELUXE
     * @return Price for that seat type
     */
    public int getPrice(SeatType seatType) {
        return prices.get(seatType);
    }

    /**
     * Calculate cost for given number of seats of a type
     *
     * @param numSeats Number of seats
     * @param seatType Type of seats
     * @return Total cost (without checking availability)
     */
    public int calculateCost(int numSeats, SeatType seatType) {
        return numSeats * prices.get(seatType);
    }

    /**
     * Get the venue for this event
     */
    public Venue getVenue() {
        return venue;
    }
}
