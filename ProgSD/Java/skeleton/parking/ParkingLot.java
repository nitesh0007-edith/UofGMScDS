package parking;

import java.util.ArrayList;
import java.util.List;

/**
 * PATTERN 11: GRID MANAGER (2D array management)
 * TIME: 20-25 minutes
 * MARKS: 18
 *
 * SKELETON for: Grid-based systems, 2D arrays
 *
 * KEY FEATURES:
 * - Manages 2D array of containers
 * - Search by position
 * - Find nearest/closest
 * - Distance calculations
 */
public class ParkingLot {

    // 2D array of parking spots
    private ParkingSpot[][] spots;

    private int rows;
    private int columns;

    /**
     * Constructor - creates grid of parking spots
     */
    public ParkingLot(int rows, int columns) {
        // TODO: Validate dimensions
        if (rows < 1 || rows > 26) {  // Limit to A-Z
            throw new IllegalArgumentException("Rows must be between 1 and 26");
        }

        if (columns < 1 || columns > 100) {
            throw new IllegalArgumentException("Columns must be between 1 and 100");
        }

        this.rows = rows;
        this.columns = columns;

        // Create 2D array
        this.spots = new ParkingSpot[rows][columns];

        // Initialize each spot (all initially null or empty)
        // Note: Often exam will ask you to initialize in a specific pattern
    }

    /**
     * PATTERN: Initialize grid with specific configuration
     *
     * Example: First row for motorcycles, rest for cars
     */
    public void initializeSpots() {
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < columns; c++) {
                // TODO: Set allowed type based on position
                VehicleType type;

                if (r == 0) {
                    type = VehicleType.MOTORCYCLE;  // First row
                } else if (r < 3) {
                    type = VehicleType.CAR;  // Next 2 rows
                } else {
                    type = VehicleType.VAN;  // Remaining rows
                }

                spots[r][c] = new ParkingSpot(r, c, type);
            }
        }
    }

    /**
     * PATTERN: Get spot by position
     */
    public ParkingSpot getSpot(int row, int column) {
        // Validate bounds
        if (row < 0 || row >= rows || column < 0 || column >= columns) {
            return null;  // Out of bounds
        }

        return spots[row][column];
    }

    /**
     * PATTERN: Find all empty spots
     */
    public List<ParkingSpot> findEmptySpots() {
        List<ParkingSpot> empty = new ArrayList<>();

        // Loop through 2D array
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < columns; c++) {
                if (spots[r][c].isEmpty()) {
                    empty.add(spots[r][c]);
                }
            }
        }

        return empty;
    }

    /**
     * PATTERN: Find empty spots for specific vehicle type
     */
    public List<ParkingSpot> findEmptySpotsForType(VehicleType type) {
        List<ParkingSpot> result = new ArrayList<>();

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < columns; c++) {
                ParkingSpot spot = spots[r][c];
                if (spot.isEmpty() && spot.getAllowedType() == type) {
                    result.add(spot);
                }
            }
        }

        return result;
    }

    /**
     * PATTERN: Find spot with vehicle
     */
    public ParkingSpot findVehicle(Vehicle vehicle) {
        if (vehicle == null) {
            return null;
        }

        // Search through entire grid
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < columns; c++) {
                ParkingSpot spot = spots[r][c];
                // Check if spot has vehicle AND it matches
                if (spot.getVehicle() != null && spot.getVehicle().equals(vehicle)) {
                    return spot;
                }
            }
        }

        return null;  // Not found
    }

    /**
     * PATTERN: Find spot by license plate
     */
    public ParkingSpot findVehicleByPlate(String licensePlate) {
        if (licensePlate == null) {
            return null;
        }

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < columns; c++) {
                Vehicle v = spots[r][c].getVehicle();
                if (v != null && v.getLicensePlate().equals(licensePlate)) {
                    return spots[r][c];
                }
            }
        }

        return null;
    }

    /**
     * PATTERN: Find NEAREST empty spot to position
     *
     * Uses Manhattan distance: |r1-r2| + |c1-c2|
     */
    public ParkingSpot findNearestEmptySpot(int targetRow, int targetCol, VehicleType type) {
        ParkingSpot nearest = null;
        int minDistance = Integer.MAX_VALUE;

        // Search all spots
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < columns; c++) {
                ParkingSpot spot = spots[r][c];

                // Check if suitable
                if (spot.isEmpty() && spot.getAllowedType() == type) {

                    // Calculate distance
                    int distance = Math.abs(r - targetRow) + Math.abs(c - targetCol);

                    // Is this closer?
                    if (distance < minDistance) {
                        minDistance = distance;
                        nearest = spot;
                    }
                }
            }
        }

        return nearest;
    }

    /**
     * PATTERN: Find first available (simple left-to-right, top-to-bottom)
     */
    public ParkingSpot findFirstAvailableSpot(VehicleType type) {
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < columns; c++) {
                ParkingSpot spot = spots[r][c];
                if (spot.isEmpty() && spot.getAllowedType() == type) {
                    return spot;  // Return immediately when found
                }
            }
        }

        return null;  // No available spot
    }

    /**
     * PATTERN: Park vehicle (find spot and park)
     */
    public boolean parkVehicle(Vehicle vehicle) {
        if (vehicle == null) {
            throw new IllegalArgumentException("Vehicle cannot be null");
        }

        // Find first available spot for this vehicle type
        ParkingSpot spot = findFirstAvailableSpot(vehicle.getType());

        if (spot == null) {
            return false;  // No available spot
        }

        // Park the vehicle
        return spot.park(vehicle);
    }

    /**
     * PATTERN: Remove vehicle by license plate
     */
    public boolean removeVehicle(String licensePlate) {
        // Find the spot with this vehicle
        ParkingSpot spot = findVehicleByPlate(licensePlate);

        if (spot == null) {
            return false;  // Vehicle not found
        }

        // Remove vehicle from spot
        spot.remove();
        return true;
    }

    /**
     * PATTERN: Count occupied spots
     */
    public int countOccupiedSpots() {
        int count = 0;

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < columns; c++) {
                if (!spots[r][c].isEmpty()) {
                    count++;
                }
            }
        }

        return count;
    }

    /**
     * PATTERN: Count by type
     */
    public int countVehiclesByType(VehicleType type) {
        int count = 0;

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < columns; c++) {
                Vehicle v = spots[r][c].getVehicle();
                if (v != null && v.getType() == type) {
                    count++;
                }
            }
        }

        return count;
    }

    /**
     * Display grid (visual representation)
     */
    public void printGrid() {
        System.out.println("=== Parking Lot Grid ===");

        // Print column headers
        System.out.print("   ");
        for (int c = 0; c < columns; c++) {
            System.out.print(String.format("%3d", c + 1));
        }
        System.out.println();

        // Print each row
        for (int r = 0; r < rows; r++) {
            char rowLabel = (char) ('A' + r);
            System.out.print(rowLabel + ": ");

            for (int c = 0; c < columns; c++) {
                if (spots[r][c].isEmpty()) {
                    System.out.print(" . ");  // Empty
                } else {
                    System.out.print(" X ");  // Occupied
                }
            }
            System.out.println();
        }
    }

    /**
     * Print all occupied spots
     */
    public void printOccupiedSpots() {
        System.out.println("=== Occupied Spots ===");
        int count = 1;

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < columns; c++) {
                if (!spots[r][c].isEmpty()) {
                    System.out.println(count++ + ". " + spots[r][c]);
                }
            }
        }
    }

    // Getters
    public int getRows() {
        return rows;
    }

    public int getColumns() {
        return columns;
    }

    public int getTotalCapacity() {
        return rows * columns;
    }

    public int getAvailableSpots() {
        return getTotalCapacity() - countOccupiedSpots();
    }
}
