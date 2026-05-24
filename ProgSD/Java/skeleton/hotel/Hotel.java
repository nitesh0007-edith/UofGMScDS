package hotel;

import java.util.ArrayList;
import java.util.List;

/**
 * PATTERN 6: ALLOCATION MANAGER (find best container for item)
 * TIME: 18-22 minutes
 * MARKS: 15
 *
 * SKELETON for: Service that allocates items to containers
 *
 * KEY ALGORITHM: Find best available container
 * - Loop through containers
 * - Check if empty and compatible
 * - Among compatible, find cheapest/best
 */
public class Hotel {

    private List<Room> rooms;

    /**
     * Constructor
     */
    public Hotel() {
        this.rooms = new ArrayList<>();
    }

    /**
     * Add room to hotel
     */
    public void addRoom(Room room) {
        if (room == null) {
            throw new IllegalArgumentException("Room cannot be null");
        }
        rooms.add(room);
    }

    /**
     * PATTERN: FIND BEST ALLOCATION
     *
     * Algorithm: Find cheapest compatible empty room
     *
     * STEPS:
     * 1. Track best room and lowest price
     * 2. Loop through all rooms
     * 3. Check if room is empty and compatible
     * 4. Compare price - update if cheaper
     * 5. Allocate to best room found
     */
    public boolean allocateGuest(Guest guest, int nights) {
        // TODO: Validate input
        if (guest == null) {
            throw new IllegalArgumentException("Guest cannot be null");
        }

        if (nights < 1) {
            throw new IllegalArgumentException("Nights must be at least 1");
        }

        // Variables to track the best room
        Room bestRoom = null;
        int lowestPrice = Integer.MAX_VALUE;  // Start with max value

        // STEP 1: Find the best room
        for (Room room : rooms) {
            // Check eligibility: empty AND compatible
            if (room.isEmpty() && room.isCompatible(guest)) {

                // Calculate price for this room
                int price = room.calculatePrice(nights);

                // Is this cheaper than current best?
                if (price < lowestPrice) {
                    lowestPrice = price;
                    bestRoom = room;
                }
            }
        }

        // STEP 2: Did we find a suitable room?
        if (bestRoom != null) {
            // Allocate guest to best room
            bestRoom.checkIn(guest);
            return true;
        }

        // No suitable room found
        return false;
    }

    /**
     * PATTERN: Find specific container with item
     */
    public Room findRoomByGuest(Guest guest) {
        if (guest == null) {
            return null;
        }

        for (Room room : rooms) {
            // Check if room has occupant AND occupant matches
            // IMPORTANT: Check != null first!
            if (room.getOccupant() != null && room.getOccupant().equals(guest)) {
                return room;
            }
        }

        return null;
    }

    /**
     * PATTERN: Remove item from container
     */
    public boolean checkOutGuest(Guest guest) {
        // Find the room with this guest
        Room room = findRoomByGuest(guest);

        if (room == null) {
            return false;  // Guest not found
        }

        // Check out from room
        room.checkOut();
        return true;
    }

    /**
     * PATTERN: Find all empty containers
     */
    public List<Room> findAvailableRooms() {
        List<Room> available = new ArrayList<>();

        for (Room room : rooms) {
            if (room.isEmpty()) {
                available.add(room);
            }
        }

        return available;
    }

    /**
     * PATTERN: Find containers by type
     */
    public List<Room> findRoomsByType(RoomType type) {
        List<Room> result = new ArrayList<>();

        for (Room room : rooms) {
            if (room.getType() == type) {
                result.add(room);
            }
        }

        return result;
    }

    /**
     * PATTERN: Find available containers by type
     */
    public List<Room> findAvailableRoomsByType(RoomType type) {
        List<Room> result = new ArrayList<>();

        for (Room room : rooms) {
            if (room.getType() == type && room.isEmpty()) {
                result.add(room);
            }
        }

        return result;
    }

    /**
     * Count occupied rooms
     */
    public int countOccupiedRooms() {
        int count = 0;
        for (Room room : rooms) {
            if (!room.isEmpty()) {
                count++;
            }
        }
        return count;
    }

    /**
     * Display all rooms
     */
    public void printAllRooms() {
        System.out.println("=== Hotel Rooms ===");
        for (int i = 0; i < rooms.size(); i++) {
            System.out.println((i + 1) + ". " + rooms.get(i));
        }
    }

    // Getter
    public List<Room> getRooms() {
        return rooms;
    }
}
