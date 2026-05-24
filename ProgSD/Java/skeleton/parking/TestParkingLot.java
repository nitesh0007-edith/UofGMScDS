package parking;

/**
 * Test class for Parking Lot System
 *
 * Demonstrates Grid + Search pattern
 * 2D array management and position-based operations
 */
public class TestParkingLot {

    public static void main(String[] args) {
        System.out.println("=== Parking Lot System Test ===\n");

        // TEST 1: Create parking lot (grid)
        System.out.println("1. Creating parking lot (5 rows x 6 columns)...");
        ParkingLot lot = new ParkingLot(5, 6);
        lot.initializeSpots();
        System.out.println("✓ Created 5x6 parking lot");
        System.out.println("Total capacity: " + lot.getTotalCapacity() + " spots");
        System.out.println();

        // TEST 2: Display grid structure
        System.out.println("2. Parking lot grid:");
        lot.printGrid();
        System.out.println();

        // TEST 3: Create vehicles
        System.out.println("3. Creating vehicles...");
        Vehicle car1 = new Vehicle("ABC123", VehicleType.CAR, "Alice");
        Vehicle car2 = new Vehicle("XYZ789", VehicleType.CAR, "Bob");
        Vehicle motorcycle1 = new Vehicle("MC001", VehicleType.MOTORCYCLE, "Charlie");
        Vehicle motorcycle2 = new Vehicle("MC002", VehicleType.MOTORCYCLE, "Diana");
        Vehicle van1 = new Vehicle("VAN123", VehicleType.VAN, "Eve");
        Vehicle van2 = new Vehicle("VAN456", VehicleType.VAN, "Frank");

        System.out.println("✓ Created 6 vehicles");
        System.out.println(car1);
        System.out.println(motorcycle1);
        System.out.println(van1);
        System.out.println();

        // TEST 4: Get specific spot
        System.out.println("4. Getting specific parking spots...");
        ParkingSpot spotA1 = lot.getSpot(0, 0);  // Row 0, Col 0
        System.out.println("Spot at (0,0): " + spotA1);
        System.out.println("Spot ID: " + spotA1.getSpotId());
        System.out.println("Allowed type: " + spotA1.getAllowedType());
        System.out.println();

        // TEST 5: Test spot compatibility
        System.out.println("5. Testing spot compatibility...");
        ParkingSpot carSpot = lot.getSpot(1, 0);  // Row 1 = CAR spots
        System.out.println("Car spot can accommodate car: " + carSpot.canAccommodate(car1));
        System.out.println("Car spot can accommodate motorcycle: " + carSpot.canAccommodate(motorcycle1));
        System.out.println();

        // TEST 6: Manual parking (test ParkingSpot class)
        System.out.println("6. Testing manual parking...");
        ParkingSpot motorcycleSpot = lot.getSpot(0, 0);  // Row 0 = MOTORCYCLE
        boolean parked = motorcycleSpot.park(motorcycle1);
        System.out.println("Parked motorcycle in " + motorcycleSpot.getSpotId() + ": " +
                          (parked ? "✓ Success" : "✗ Failed"));
        System.out.println("Spot is now: " + (motorcycleSpot.isEmpty() ? "Empty" : "Occupied"));
        System.out.println();

        // TEST 7: Try to park in occupied spot (should fail)
        System.out.println("7. Testing parking in occupied spot...");
        boolean parked2 = motorcycleSpot.park(motorcycle2);
        System.out.println("Try to park in occupied spot: " +
                          (parked2 ? "✗ Unexpected success" : "✓ Correctly failed"));
        System.out.println();

        // TEST 8: Remove vehicle from spot
        System.out.println("8. Testing remove vehicle...");
        Vehicle removed = motorcycleSpot.remove();
        System.out.println("Removed vehicle: " + removed.getLicensePlate());
        System.out.println("Spot is now: " + (motorcycleSpot.isEmpty() ? "Empty" : "Occupied"));
        System.out.println();

        // TEST 9: Automatic parking (find first available)
        System.out.println("9. Testing automatic parking...");
        boolean auto1 = lot.parkVehicle(motorcycle1);
        boolean auto2 = lot.parkVehicle(motorcycle2);
        boolean auto3 = lot.parkVehicle(car1);
        boolean auto4 = lot.parkVehicle(car2);
        boolean auto5 = lot.parkVehicle(van1);

        System.out.println("Parked motorcycle MC001: " + (auto1 ? "✓" : "✗"));
        System.out.println("Parked motorcycle MC002: " + (auto2 ? "✓" : "✗"));
        System.out.println("Parked car ABC123: " + (auto3 ? "✓" : "✗"));
        System.out.println("Parked car XYZ789: " + (auto4 ? "✓" : "✗"));
        System.out.println("Parked van VAN123: " + (auto5 ? "✓" : "✗"));
        System.out.println();

        // TEST 10: Display grid after parking
        System.out.println("10. Grid after parking:");
        lot.printGrid();
        System.out.println();

        // TEST 11: Display occupied spots
        System.out.println("11. All occupied spots:");
        lot.printOccupiedSpots();
        System.out.println();

        // TEST 12: Find vehicle by license plate (2D SEARCH PATTERN)
        System.out.println("12. Finding vehicles by license plate...");
        ParkingSpot foundSpot = lot.findVehicleByPlate("ABC123");
        if (foundSpot != null) {
            System.out.println("Found ABC123 in spot: " + foundSpot.getSpotId());
            System.out.println("Position: Row " + foundSpot.getRow() + ", Col " + foundSpot.getColumn());
        }

        ParkingSpot foundSpot2 = lot.findVehicleByPlate("MC001");
        if (foundSpot2 != null) {
            System.out.println("Found MC001 in spot: " + foundSpot2.getSpotId());
        }
        System.out.println();

        // TEST 13: Find vehicle by Vehicle object
        System.out.println("13. Finding vehicle by object...");
        ParkingSpot carSpot1 = lot.findVehicle(car1);
        if (carSpot1 != null) {
            System.out.println("Alice's car is in: " + carSpot1.getSpotId());
        }
        System.out.println();

        // TEST 14: Find empty spots
        System.out.println("14. Finding empty spots...");
        System.out.println("Empty spots: " + lot.findEmptySpots().size());
        System.out.println("Available spots: " + lot.getAvailableSpots());
        System.out.println();

        // TEST 15: Find empty spots by type
        System.out.println("15. Finding empty spots by type...");
        System.out.println("Empty MOTORCYCLE spots: " +
                          lot.findEmptySpotsForType(VehicleType.MOTORCYCLE).size());
        System.out.println("Empty CAR spots: " +
                          lot.findEmptySpotsForType(VehicleType.CAR).size());
        System.out.println("Empty VAN spots: " +
                          lot.findEmptySpotsForType(VehicleType.VAN).size());
        System.out.println();

        // TEST 16: Find nearest empty spot (MANHATTAN DISTANCE)
        System.out.println("16. Finding nearest empty spot to entrance (0,0)...");
        ParkingSpot nearest = lot.findNearestEmptySpot(0, 0, VehicleType.CAR);
        if (nearest != null) {
            System.out.println("Nearest CAR spot to entrance: " + nearest.getSpotId());
            System.out.println("Position: (" + nearest.getRow() + ", " + nearest.getColumn() + ")");
            int distance = Math.abs(nearest.getRow() - 0) + Math.abs(nearest.getColumn() - 0);
            System.out.println("Manhattan distance: " + distance);
        }
        System.out.println();

        // TEST 17: Find first available spot
        System.out.println("17. Finding first available VAN spot...");
        ParkingSpot firstVan = lot.findFirstAvailableSpot(VehicleType.VAN);
        if (firstVan != null) {
            System.out.println("First available VAN spot: " + firstVan.getSpotId());
        }
        System.out.println();

        // TEST 18: Remove vehicle by license plate
        System.out.println("18. Testing remove vehicle...");
        boolean removed1 = lot.removeVehicle("ABC123");
        System.out.println("Removed ABC123: " + (removed1 ? "✓ Success" : "✗ Failed"));

        boolean removed2 = lot.removeVehicle("NOTEXIST");
        System.out.println("Try remove non-existent: " +
                          (removed2 ? "✗ Unexpected success" : "✓ Correctly failed"));
        System.out.println();

        // TEST 19: Count vehicles by type
        System.out.println("19. Counting vehicles by type...");
        System.out.println("Motorcycles parked: " + lot.countVehiclesByType(VehicleType.MOTORCYCLE));
        System.out.println("Cars parked: " + lot.countVehiclesByType(VehicleType.CAR));
        System.out.println("Vans parked: " + lot.countVehiclesByType(VehicleType.VAN));
        System.out.println("Total occupied: " + lot.countOccupiedSpots());
        System.out.println();

        // TEST 20: Test filling up motorcycle spots
        System.out.println("20. Testing capacity limits...");
        System.out.println("Trying to park motorcycles until full...");
        int motorcyclesParked = lot.countVehiclesByType(VehicleType.MOTORCYCLE);
        int attempts = 0;

        while (attempts < 10) {  // Try to park up to 10 more
            Vehicle mc = new Vehicle("MC" + (100 + attempts), VehicleType.MOTORCYCLE, "Rider" + attempts);
            if (lot.parkVehicle(mc)) {
                motorcyclesParked++;
            } else {
                System.out.println("No more MOTORCYCLE spots available after " + motorcyclesParked);
                break;
            }
            attempts++;
        }
        System.out.println();

        // TEST 21: Test spot ID conversion
        System.out.println("21. Testing spot ID system...");
        for (int r = 0; r < 3; r++) {
            for (int c = 0; c < 3; c++) {
                ParkingSpot spot = lot.getSpot(r, c);
                System.out.print(spot.getSpotId() + " ");
            }
            System.out.println();
        }
        System.out.println("(Row 0 = A, Row 1 = B, Row 2 = C, etc.)");
        System.out.println();

        // TEST 22: Test validation
        System.out.println("22. Testing validation...");
        try {
            ParkingLot invalidLot = new ParkingLot(0, 5);
            System.out.println("✗ Should have thrown exception!");
        } catch (IllegalArgumentException e) {
            System.out.println("✓ Correctly rejected invalid dimensions: " + e.getMessage());
        }

        try {
            Vehicle invalidVehicle = new Vehicle("AB", VehicleType.CAR, "Test");
            System.out.println("✗ Should have thrown exception!");
        } catch (IllegalArgumentException e) {
            System.out.println("✓ Correctly rejected short license plate: " + e.getMessage());
        }
        System.out.println();

        // TEST 23: Test out of bounds access
        System.out.println("23. Testing out of bounds access...");
        ParkingSpot outOfBounds = lot.getSpot(99, 99);
        System.out.println("Get spot (99,99): " + (outOfBounds == null ? "✓ Correctly returned null" : "✗ Should be null"));
        System.out.println();

        // FINAL: Display final state
        System.out.println("=== FINAL STATE ===");
        lot.printGrid();
        System.out.println();

        System.out.println("Statistics:");
        System.out.println("Total capacity: " + lot.getTotalCapacity());
        System.out.println("Occupied: " + lot.countOccupiedSpots());
        System.out.println("Available: " + lot.getAvailableSpots());
        System.out.println("Occupancy rate: " +
                          String.format("%.1f%%", (100.0 * lot.countOccupiedSpots() / lot.getTotalCapacity())));

        System.out.println("\n✓ All tests completed successfully!");
        System.out.println("\nKey Patterns Demonstrated:");
        System.out.println("- 2D array initialization and management");
        System.out.println("- Grid search (nested loops)");
        System.out.println("- Find nearest (Manhattan distance)");
        System.out.println("- Position-based identification (row/col → ID)");
        System.out.println("- Filter by position and type");
    }
}
