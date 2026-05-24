package hotel;

import java.util.Objects;

/**
 * PATTERN 5: CONTAINER CLASS (holds one item)
 * TIME: 12-15 minutes
 * MARKS: 10
 *
 * SKELETON for: Enclosure, ParkingSpot, Seat, Slot, Container
 *
 * KEY FEATURES:
 * - Has capacity/type properties
 * - Can be empty or occupied
 * - Compatibility checking before adding
 * - State management (empty vs occupied)
 */
public class Room {

    // Container properties
    private String roomNumber;
    private RoomType type;
    private int floor;

    // Occupant (null = empty)
    private Guest occupant;

    /**
     * Constructor - creates empty container
     */
    public Room(String roomNumber, RoomType type, int floor) {
        // TODO: Validate inputs
        if (roomNumber == null || roomNumber.length() < 1) {
            throw new IllegalArgumentException("Room number cannot be empty");
        }

        if (type == null) {
            throw new IllegalArgumentException("Room type cannot be null");
        }

        if (floor < 0 || floor > 50) {
            throw new IllegalArgumentException("Invalid floor number");
        }

        this.roomNumber = roomNumber;
        this.type = type;
        this.floor = floor;
        this.occupant = null;  // Initially empty
    }

    // Getters
    public String getRoomNumber() {
        return roomNumber;
    }

    public RoomType getType() {
        return type;
    }

    public int getFloor() {
        return floor;
    }

    public Guest getOccupant() {
        return occupant;
    }

    /**
     * PATTERN: Check if container is empty
     */
    public boolean isEmpty() {
        return occupant == null;
    }

    /**
     * PATTERN: Compatibility checking
     *
     * Check if this container can hold the given item
     * Returns true/false (doesn't modify state)
     */
    public boolean isCompatible(Guest guest) {
        // TODO: Check all compatibility conditions
        if (guest == null) {
            return false;
        }

        // CHECK 1: Capacity - can room hold this many guests?
        if (guest.getNumberOfGuests() > type.getCapacity()) {
            return false;  // Too many guests for this room type
        }

        // CHECK 2: Type preference (if specified in exam)
        // Example: VIP guests need DELUXE or SUITE
        if (guest.isVip() && type != RoomType.DELUXE && type != RoomType.SUITE) {
            return false;
        }

        // CHECK 3: Floor preference (if specified)
        // Example: guest wants specific floor
        // if (guest.getPreferredFloor() != -1 && guest.getPreferredFloor() != floor) {
        //     return false;
        // }

        // All checks passed
        return true;
    }

    /**
     * PATTERN: Add item to container
     *
     * Returns true if successful, false if failed
     * Throws exception for invalid input
     */
    public boolean checkIn(Guest guest) {
        // TODO: Validate input
        if (guest == null) {
            throw new IllegalArgumentException("Guest cannot be null");
        }

        // Check if already occupied
        if (occupant != null) {
            return false;  // Room already occupied
        }

        // Check compatibility
        if (!isCompatible(guest)) {
            return false;  // Guest not compatible with this room
        }

        // All good - check in the guest
        this.occupant = guest;
        return true;
    }

    /**
     * PATTERN: Remove item from container
     *
     * Returns the removed item (or null if empty)
     */
    public Guest checkOut() {
        Guest guest = this.occupant;
        this.occupant = null;  // Room becomes empty
        return guest;
    }

    /**
     * PATTERN: Calculate cost/value
     *
     * May depend on container properties and occupant
     */
    public int calculatePrice(int nights) {
        // Base price from room type
        int price = type.getBasePrice() * nights;

        // Adjustments based on properties
        if (floor > 10) {
            price += 20 * nights;  // Premium for high floors
        }

        return price;
    }

    @Override
    public String toString() {
        String status = (occupant != null) ? "Occupied by " + occupant.getName() : "Empty";
        return "Room{number='" + roomNumber + "', type=" + type +
               ", floor=" + floor + ", status=" + status + "}";
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Room room = (Room) o;
        return Objects.equals(roomNumber, room.roomNumber);
    }

    @Override
    public int hashCode() {
        return Objects.hash(roomNumber);
    }
}
