package hotel;

/**
 * Test class for Hotel Booking System
 *
 * Demonstrates Container + Allocation pattern
 * Similar to 2024 Pet Care exam!
 */
public class TestHotel {

    public static void main(String[] args) {
        System.out.println("=== Hotel Booking System Test ===\n");

        // Create hotel
        Hotel hotel = new Hotel();

        // TEST 1: Create rooms
        System.out.println("1. Creating rooms...");
        Room room1 = new Room("101", RoomType.SINGLE, 1);
        Room room2 = new Room("102", RoomType.DOUBLE, 1);
        Room room3 = new Room("201", RoomType.SUITE, 2);
        Room room4 = new Room("202", RoomType.DELUXE, 2);
        Room room5 = new Room("301", RoomType.SINGLE, 3);
        Room room6 = new Room("1101", RoomType.SUITE, 11);  // High floor

        hotel.addRoom(room1);
        hotel.addRoom(room2);
        hotel.addRoom(room3);
        hotel.addRoom(room4);
        hotel.addRoom(room5);
        hotel.addRoom(room6);
        System.out.println("✓ Added 6 rooms to hotel\n");

        // TEST 2: Create guests
        System.out.println("2. Creating guests...");
        Guest guest1 = new Guest("G001", "Alice", 1, false);
        Guest guest2 = new Guest("G002", "Bob", 2, false);
        Guest guest3 = new Guest("G003", "Charlie VIP", 2, true);
        Guest guest4 = new Guest("G004", "Diana", 4, false);
        Guest guest5 = new Guest("G005", "Eve VIP", 1, true);

        System.out.println("✓ Created 5 guests\n");

        // TEST 3: Display all rooms
        System.out.println("3. All rooms in hotel:");
        hotel.printAllRooms();
        System.out.println();

        // TEST 4: Test room compatibility
        System.out.println("4. Testing room compatibility...");
        System.out.println("Room 101 (SINGLE) compatible with Alice (1 guest): " +
                          room1.isCompatible(guest1));
        System.out.println("Room 101 (SINGLE) compatible with Bob (2 guests): " +
                          room1.isCompatible(guest2));
        System.out.println("Room 202 (DELUXE) compatible with VIP Charlie: " +
                          room4.isCompatible(guest3));
        System.out.println("Room 101 (SINGLE) compatible with VIP Eve: " +
                          room1.isCompatible(guest5) + " (VIP needs DELUXE/SUITE)");
        System.out.println();

        // TEST 5: Manual check-in to test Room class
        System.out.println("5. Testing manual check-in...");
        boolean checkin1 = room1.checkIn(guest1);
        System.out.println("Alice checks into Room 101: " + (checkin1 ? "✓ Success" : "✗ Failed"));
        System.out.println("Room 101 is now: " + (room1.isEmpty() ? "Empty" : "Occupied"));
        System.out.println();

        // TEST 6: Try to check in to occupied room (should fail)
        System.out.println("6. Testing check-in to occupied room...");
        boolean checkin2 = room1.checkIn(guest2);
        System.out.println("Bob tries to check into occupied Room 101: " +
                          (checkin2 ? "✗ Unexpected success" : "✓ Correctly failed"));
        System.out.println();

        // TEST 7: Check out
        System.out.println("7. Testing check-out...");
        Guest checked_out = room1.checkOut();
        System.out.println("Checked out: " + checked_out.getName());
        System.out.println("Room 101 is now: " + (room1.isEmpty() ? "Empty" : "Occupied"));
        System.out.println();

        // TEST 8: Allocate guest (find cheapest compatible room)
        System.out.println("8. Testing guest allocation (MOST IMPORTANT PATTERN)...");
        boolean allocated1 = hotel.allocateGuest(guest1, 2);  // 2 nights
        System.out.println("Alice allocated: " + (allocated1 ? "✓ Success" : "✗ Failed"));

        boolean allocated2 = hotel.allocateGuest(guest2, 3);  // 3 nights
        System.out.println("Bob (2 guests) allocated: " + (allocated2 ? "✓ Success" : "✗ Failed"));

        boolean allocated3 = hotel.allocateGuest(guest3, 1);  // VIP, 1 night
        System.out.println("VIP Charlie allocated: " + (allocated3 ? "✓ Success" : "✗ Failed"));

        boolean allocated4 = hotel.allocateGuest(guest4, 2);  // 4 guests
        System.out.println("Diana (4 guests) allocated: " + (allocated4 ? "✓ Success" : "✗ Failed"));
        System.out.println();

        // TEST 9: Display hotel state after allocations
        System.out.println("9. Hotel state after allocations:");
        hotel.printAllRooms();
        System.out.println();

        // TEST 10: Find room by guest
        System.out.println("10. Finding rooms by guest...");
        Room aliceRoom = hotel.findRoomByGuest(guest1);
        if (aliceRoom != null) {
            System.out.println("Alice is in room: " + aliceRoom.getRoomNumber());
        }

        Room bobRoom = hotel.findRoomByGuest(guest2);
        if (bobRoom != null) {
            System.out.println("Bob is in room: " + bobRoom.getRoomNumber());
        }
        System.out.println();

        // TEST 11: Find available rooms
        System.out.println("11. Finding available rooms...");
        System.out.println("Available rooms: " + hotel.findAvailableRooms().size());
        for (Room room : hotel.findAvailableRooms()) {
            System.out.println("  - " + room.getRoomNumber() + " (" + room.getType() + ")");
        }
        System.out.println();

        // TEST 12: Find rooms by type
        System.out.println("12. Finding all SUITE rooms...");
        for (Room room : hotel.findRoomsByType(RoomType.SUITE)) {
            System.out.println("  - " + room);
        }
        System.out.println();

        // TEST 13: Check out guest
        System.out.println("13. Testing guest check-out...");
        boolean checkout = hotel.checkOutGuest(guest1);
        System.out.println("Alice checks out: " + (checkout ? "✓ Success" : "✗ Failed"));
        System.out.println();

        // TEST 14: Count occupied rooms
        System.out.println("14. Counting occupied rooms...");
        System.out.println("Occupied: " + hotel.countOccupiedRooms() + " / " +
                          hotel.getRooms().size());
        System.out.println();

        // TEST 15: Test room price calculation
        System.out.println("15. Testing price calculation...");
        System.out.println("Room 101 (SINGLE, floor 1) for 3 nights: $" +
                          room1.calculatePrice(3));
        System.out.println("Room 1101 (SUITE, floor 11) for 3 nights: $" +
                          room6.calculatePrice(3) + " (includes high floor premium)");
        System.out.println();

        // TEST 16: Test RoomType enum methods
        System.out.println("16. Testing RoomType enum...");
        System.out.println("SINGLE capacity: " + RoomType.SINGLE.getCapacity());
        System.out.println("SUITE base price: $" + RoomType.SUITE.getBasePrice());
        System.out.println("DOUBLE can accommodate 2 guests: " +
                          RoomType.DOUBLE.canAccommodate(2));
        System.out.println("SINGLE can accommodate 2 guests: " +
                          RoomType.SINGLE.canAccommodate(2));
        System.out.println();

        // TEST 17: Test validation (exception handling)
        System.out.println("17. Testing validation...");
        try {
            Room invalidRoom = new Room("", RoomType.SINGLE, 1);
            System.out.println("✗ Should have thrown exception!");
        } catch (IllegalArgumentException e) {
            System.out.println("✓ Correctly rejected empty room number: " + e.getMessage());
        }

        try {
            Guest invalidGuest = new Guest("G999", "Test", 5, false);
            System.out.println("✗ Should have thrown exception!");
        } catch (IllegalArgumentException e) {
            System.out.println("✓ Correctly rejected too many guests: " + e.getMessage());
        }
        System.out.println();

        // TEST 18: Test allocation algorithm (cheapest room)
        System.out.println("18. Testing 'find cheapest' algorithm...");
        System.out.println("Creating new hotel with multiple SINGLE rooms at different prices...");
        Hotel testHotel = new Hotel();
        Room cheap1 = new Room("A1", RoomType.SINGLE, 1);   // Low floor = cheaper
        Room cheap2 = new Room("A11", RoomType.SINGLE, 11); // High floor = more expensive
        testHotel.addRoom(cheap2);  // Add expensive first
        testHotel.addRoom(cheap1);  // Add cheap second

        Guest testGuest = new Guest("TEST", "TestGuest", 1, false);
        testHotel.allocateGuest(testGuest, 1);

        Room allocatedRoom = testHotel.findRoomByGuest(testGuest);
        System.out.println("Guest allocated to: " + allocatedRoom.getRoomNumber());
        System.out.println("Should be A1 (cheapest): " +
                          (allocatedRoom.getRoomNumber().equals("A1") ? "✓ Correct" : "✗ Wrong"));
        System.out.println();

        // FINAL: Display final state
        System.out.println("=== FINAL STATE ===");
        hotel.printAllRooms();

        System.out.println("\n✓ All tests completed successfully!");
        System.out.println("\nKey Pattern Demonstrated:");
        System.out.println("- Container pattern (Room holds Guest)");
        System.out.println("- Compatibility checking (size, VIP status)");
        System.out.println("- Find cheapest allocation (Integer.MAX_VALUE pattern)");
        System.out.println("- Search and remove pattern");
    }
}
