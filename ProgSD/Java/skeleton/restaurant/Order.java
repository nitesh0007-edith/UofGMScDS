package restaurant;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

/**
 * PATTERN 8: STATEFUL OBJECT (changes state over time)
 * TIME: 15-18 minutes
 * MARKS: 12
 *
 * SKELETON for: Order, Ticket, Request, Transaction
 *
 * KEY FEATURES:
 * - Has state that changes (enum status)
 * - Contains collection of items
 * - State transition methods
 * - Calculation methods (total, etc.)
 */
public class Order {

    // Unique identifier
    private String orderId;

    // Customer information
    private String customerName;
    private int tableNumber;

    // Order items - collection of what was ordered
    private List<String> items;  // Simplified: just item names
    private List<Integer> prices; // Corresponding prices

    // State
    private OrderStatus status;

    // Timestamps (optional but common in exams)
    private long orderTime;

    /**
     * Constructor - creates new order in PENDING state
     */
    public Order(String orderId, String customerName, int tableNumber) {
        // TODO: Validate inputs
        if (orderId == null || orderId.length() < 3) {
            throw new IllegalArgumentException("Order ID must be at least 3 characters");
        }

        if (customerName == null || customerName.length() < 2) {
            throw new IllegalArgumentException("Customer name must be at least 2 characters");
        }

        if (tableNumber < 1 || tableNumber > 100) {
            throw new IllegalArgumentException("Invalid table number");
        }

        this.orderId = orderId;
        this.customerName = customerName;
        this.tableNumber = tableNumber;

        // Initialize collections
        this.items = new ArrayList<>();
        this.prices = new ArrayList<>();

        // Initial state
        this.status = OrderStatus.PENDING;
        this.orderTime = System.currentTimeMillis();
    }

    // Getters
    public String getOrderId() {
        return orderId;
    }

    public String getCustomerName() {
        return customerName;
    }

    public int getTableNumber() {
        return tableNumber;
    }

    public List<String> getItems() {
        return items;
    }

    public OrderStatus getStatus() {
        return status;
    }

    public long getOrderTime() {
        return orderTime;
    }

    /**
     * PATTERN: Add item to order (collection management)
     */
    public void addItem(String item, int price) {
        // TODO: Validate inputs
        if (item == null || item.length() < 1) {
            throw new IllegalArgumentException("Item name cannot be empty");
        }

        if (price < 0) {
            throw new IllegalArgumentException("Price cannot be negative");
        }

        // Can only add items to pending orders
        if (status != OrderStatus.PENDING) {
            throw new IllegalStateException("Cannot add items to order in " + status + " state");
        }

        items.add(item);
        prices.add(price);
    }

    /**
     * PATTERN: STATE TRANSITION methods
     *
     * Change state with validation
     */
    public void startPreparing() {
        // Check valid transition
        if (status != OrderStatus.PENDING) {
            throw new IllegalStateException("Can only start preparing PENDING orders");
        }

        // Check has items
        if (items.isEmpty()) {
            throw new IllegalStateException("Cannot prepare empty order");
        }

        status = OrderStatus.PREPARING;
    }

    public void markReady() {
        if (status != OrderStatus.PREPARING) {
            throw new IllegalStateException("Can only mark PREPARING orders as ready");
        }
        status = OrderStatus.READY;
    }

    public void serve() {
        if (status != OrderStatus.READY) {
            throw new IllegalStateException("Can only serve READY orders");
        }
        status = OrderStatus.SERVED;
    }

    public void complete() {
        if (status != OrderStatus.SERVED) {
            throw new IllegalStateException("Can only complete SERVED orders");
        }
        status = OrderStatus.COMPLETED;
    }

    /**
     * PATTERN: CALCULATION method
     *
     * Calculate total from collection
     */
    public int calculateTotal() {
        int total = 0;
        for (int price : prices) {
            total += price;
        }
        return total;
    }

    /**
     * PATTERN: Time-based calculation
     */
    public long getWaitingTimeMinutes() {
        long currentTime = System.currentTimeMillis();
        long elapsedMillis = currentTime - orderTime;
        return elapsedMillis / (1000 * 60);  // Convert to minutes
    }

    /**
     * PATTERN: State query methods
     */
    public boolean isCompleted() {
        return status == OrderStatus.COMPLETED;
    }

    public boolean isPending() {
        return status == OrderStatus.PENDING;
    }

    public boolean canBeServed() {
        return status == OrderStatus.READY;
    }

    public int getItemCount() {
        return items.size();
    }

    @Override
    public String toString() {
        return "Order{id='" + orderId + "', customer='" + customerName +
               "', table=" + tableNumber + ", items=" + items.size() +
               ", total=" + calculateTotal() + ", status=" + status + "}";
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Order order = (Order) o;
        return Objects.equals(orderId, order.orderId);
    }

    @Override
    public int hashCode() {
        return Objects.hash(orderId);
    }
}
