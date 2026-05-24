package restaurant;

/**
 * PATTERN 7: ENUM for workflow states
 * TIME: 2-3 minutes
 * MARKS: 2
 *
 * State machine pattern - order progresses through states
 */
public enum OrderStatus {
    PENDING,      // Order placed, not yet started
    PREPARING,    // Being cooked
    READY,        // Ready for pickup/delivery
    SERVED,       // Delivered to customer
    COMPLETED     // Finished and paid
}
