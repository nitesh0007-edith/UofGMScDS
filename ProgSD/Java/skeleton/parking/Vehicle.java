package parking;

import java.util.Objects;

/**
 * PATTERN 2: Simple data class
 */
public class Vehicle {

    private String licensePlate;
    private VehicleType type;
    private String owner;

    public Vehicle(String licensePlate, VehicleType type, String owner) {
        if (licensePlate == null || licensePlate.length() < 3) {
            throw new IllegalArgumentException("License plate must be at least 3 characters");
        }

        if (type == null) {
            throw new IllegalArgumentException("Vehicle type cannot be null");
        }

        if (owner == null || owner.length() < 2) {
            throw new IllegalArgumentException("Owner name must be at least 2 characters");
        }

        this.licensePlate = licensePlate;
        this.type = type;
        this.owner = owner;
    }

    public String getLicensePlate() {
        return licensePlate;
    }

    public VehicleType getType() {
        return type;
    }

    public String getOwner() {
        return owner;
    }

    @Override
    public String toString() {
        return "Vehicle{plate='" + licensePlate + "', type=" + type + ", owner='" + owner + "'}";
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Vehicle vehicle = (Vehicle) o;
        return Objects.equals(licensePlate, vehicle.licensePlate);
    }

    @Override
    public int hashCode() {
        return Objects.hash(licensePlate);
    }
}
