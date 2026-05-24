package hotel;

import java.util.Objects;

/**
 * PATTERN 2: DATA CLASS - item to be placed in container
 * TIME: 10-12 minutes
 * MARKS: 8
 *
 * Simple data class representing the "item" that goes into containers
 */
public class Guest {

    private String guestId;
    private String name;
    private int numberOfGuests;
    private boolean isVip;

    /**
     * Constructor with validation
     */
    public Guest(String guestId, String name, int numberOfGuests, boolean isVip) {
        // TODO: Validate inputs
        if (guestId == null || guestId.length() < 3) {
            throw new IllegalArgumentException("Guest ID must be at least 3 characters");
        }

        if (name == null || name.length() < 2) {
            throw new IllegalArgumentException("Name must be at least 2 characters");
        }

        if (numberOfGuests < 1 || numberOfGuests > 4) {
            throw new IllegalArgumentException("Number of guests must be between 1 and 4");
        }

        this.guestId = guestId;
        this.name = name;
        this.numberOfGuests = numberOfGuests;
        this.isVip = isVip;
    }

    // Getters
    public String getGuestId() {
        return guestId;
    }

    public String getName() {
        return name;
    }

    public int getNumberOfGuests() {
        return numberOfGuests;
    }

    public boolean isVip() {
        return isVip;
    }

    // Setters (if needed)
    public void setVip(boolean vip) {
        isVip = vip;
    }

    @Override
    public String toString() {
        String vipStatus = isVip ? " (VIP)" : "";
        return "Guest{id='" + guestId + "', name='" + name +
               "', guests=" + numberOfGuests + vipStatus + "}";
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Guest guest = (Guest) o;
        return Objects.equals(guestId, guest.guestId);
    }

    @Override
    public int hashCode() {
        return Objects.hash(guestId);
    }
}
