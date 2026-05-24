package parking;

import java.util.Objects;

/**
 * PATTERN 10: GRID CELL (container with position)
 * TIME: 12-15 minutes
 * MARKS: 10
 *
 * SKELETON for: Grid cell, Array element with position
 *
 * KEY FEATURES:
 * - Has row/column position
 * - Can be empty or occupied
 * - Position-based identification
 */
public class ParkingSpot {

    // Position in grid
    private int row;
    private int column;

    // Spot properties
    private VehicleType allowedType;  // What can park here

    // Occupant
    private Vehicle vehicle;  // null = empty

    /**
     * Constructor - creates empty spot at position
     */
    public ParkingSpot(int row, int column, VehicleType allowedType) {
        // TODO: Validate position
        if (row < 0 || row >= 100) {
            throw new IllegalArgumentException("Invalid row");
        }

        if (column < 0 || column >= 100) {
            throw new IllegalArgumentException("Invalid column");
        }

        if (allowedType == null) {
            throw new IllegalArgumentException("Allowed type cannot be null");
        }

        this.row = row;
        this.column = column;
        this.allowedType = allowedType;
        this.vehicle = null;  // Initially empty
    }

    // Getters
    public int getRow() {
        return row;
    }

    public int getColumn() {
        return column;
    }

    public VehicleType getAllowedType() {
        return allowedType;
    }

    public Vehicle getVehicle() {
        return vehicle;
    }

    /**
     * PATTERN: Check if spot is empty
     */
    public boolean isEmpty() {
        return vehicle == null;
    }

    /**
     * PATTERN: Compatibility checking
     */
    public boolean canAccommodate(Vehicle v) {
        if (v == null) {
            return false;
        }

        // Check if vehicle type matches allowed type
        return v.getType() == allowedType;
    }

    /**
     * PATTERN: Park vehicle in spot
     */
    public boolean park(Vehicle v) {
        if (v == null) {
            throw new IllegalArgumentException("Vehicle cannot be null");
        }

        // Check if already occupied
        if (vehicle != null) {
            return false;
        }

        // Check compatibility
        if (!canAccommodate(v)) {
            return false;
        }

        this.vehicle = v;
        return true;
    }

    /**
     * PATTERN: Remove vehicle from spot
     */
    public Vehicle remove() {
        Vehicle v = this.vehicle;
        this.vehicle = null;
        return v;
    }

    /**
     * PATTERN: Get spot identifier (like "A5", "B12")
     */
    public String getSpotId() {
        // Convert row to letter (0=A, 1=B, etc.)
        char rowLetter = (char) ('A' + row);
        return rowLetter + String.valueOf(column + 1);
    }

    @Override
    public String toString() {
        String status = (vehicle != null) ? "Occupied by " + vehicle.getLicensePlate() : "Empty";
        return "Spot{" + getSpotId() + ", type=" + allowedType + ", " + status + "}";
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        ParkingSpot spot = (ParkingSpot) o;
        return row == spot.row && column == spot.column;
    }

    @Override
    public int hashCode() {
        return Objects.hash(row, column);
    }
}
