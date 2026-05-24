package boxOffice;

public class TestVenue {
    public static void main(String[] args) {
        // Test the sample venue from the exam
        String config = "3\nS D D S\nD D D\nS S S S S S";

        Venue venue = new Venue(config);
        System.out.println("Venue created successfully!\n");

        venue.printDetails();

        System.out.println("\nTesting getSeat:");
        Seat seat = venue.getSeat('A', 2);
        System.out.println("Seat A2 type: " + seat.getSeatType());

        System.out.println("\nTesting Event:");
        Event event = new Event(venue, 10, 20);

        int price = event.reserveSeats(2, SeatType.DELUXE);
        System.out.println("Reserved 2 deluxe seats, total price: " + price);

        System.out.println("\nVenue after reservation:");
        venue.printDetails();

        System.out.println("\nReturning seat A2:");
        event.returnSeat('A', 2);

        System.out.println("\nVenue after return:");
        venue.printDetails();
    }
}
