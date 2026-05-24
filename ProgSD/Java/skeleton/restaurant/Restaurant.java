package restaurant;

import java.util.ArrayList;
import java.util.List;
import java.util.LinkedList;
import java.util.Queue;

/**
 * PATTERN 9: QUEUE/WORKFLOW MANAGER
 * TIME: 18-22 minutes
 * MARKS: 15
 *
 * SKELETON for: Processing system, workflow manager
 *
 * KEY FEATURES:
 * - Manages items in different states
 * - Queue for pending items
 * - Move items through workflow stages
 * - Filter and find by state
 */
public class Restaurant {

    // Different ways to organize orders:

    // Option 1: Single list (search by state)
    private List<Order> allOrders;

    // Option 2: Queue for pending orders (FIFO - First In First Out)
    private Queue<Order> pendingOrders;

    // Option 3: Separate lists by state (faster filtering)
    private List<Order> preparingOrders;
    private List<Order> readyOrders;

    /**
     * Constructor
     */
    public Restaurant() {
        // Initialize all collections
        this.allOrders = new ArrayList<>();
        this.pendingOrders = new LinkedList<>();  // LinkedList implements Queue
        this.preparingOrders = new ArrayList<>();
        this.readyOrders = new ArrayList<>();
    }

    /**
     * PATTERN: Add new item to system
     */
    public void placeOrder(Order order) {
        // TODO: Validate
        if (order == null) {
            throw new IllegalArgumentException("Order cannot be null");
        }

        if (order.getStatus() != OrderStatus.PENDING) {
            throw new IllegalArgumentException("New orders must be in PENDING state");
        }

        // Add to both collections
        allOrders.add(order);
        pendingOrders.add(order);  // Queue for processing
    }

    /**
     * PATTERN: QUEUE PROCESSING - get next item from queue
     *
     * Queue is FIFO (First In First Out)
     * poll() removes and returns head, or null if empty
     */
    public Order getNextPendingOrder() {
        return pendingOrders.poll();  // Remove from queue
    }

    /**
     * PATTERN: STATE TRANSITION - move item to next stage
     */
    public boolean startPreparingNextOrder() {
        // Get next pending order from queue
        Order order = pendingOrders.poll();

        if (order == null) {
            return false;  // No pending orders
        }

        // Change state
        order.startPreparing();

        // Move to preparing list
        preparingOrders.add(order);

        return true;
    }

    /**
     * PATTERN: Find and transition specific order
     */
    public boolean markOrderReady(String orderId) {
        // Find the order in preparing list
        Order order = null;
        for (Order o : preparingOrders) {
            if (o.getOrderId().equals(orderId)) {
                order = o;
                break;
            }
        }

        if (order == null) {
            return false;  // Not found in preparing
        }

        // Change state
        order.markReady();

        // Move from preparing to ready
        preparingOrders.remove(order);
        readyOrders.add(order);

        return true;
    }

    /**
     * PATTERN: Serve order (remove from ready list)
     */
    public boolean serveOrder(String orderId) {
        // Find in ready list
        Order order = null;
        for (Order o : readyOrders) {
            if (o.getOrderId().equals(orderId)) {
                order = o;
                break;
            }
        }

        if (order == null) {
            return false;
        }

        // Change state and remove from ready list
        order.serve();
        readyOrders.remove(order);

        return true;
    }

    /**
     * PATTERN: Find by ID across all lists
     */
    public Order findOrderById(String orderId) {
        if (orderId == null) {
            return null;
        }

        // Search through all orders
        for (Order order : allOrders) {
            if (order.getOrderId().equals(orderId)) {
                return order;
            }
        }

        return null;
    }

    /**
     * PATTERN: Filter by state
     */
    public List<Order> getOrdersByStatus(OrderStatus status) {
        List<Order> result = new ArrayList<>();

        for (Order order : allOrders) {
            if (order.getStatus() == status) {
                result.add(order);
            }
        }

        return result;
    }

    /**
     * PATTERN: Find by customer
     */
    public List<Order> getOrdersByCustomer(String customerName) {
        List<Order> result = new ArrayList<>();

        for (Order order : allOrders) {
            if (order.getCustomerName().equals(customerName)) {
                result.add(order);
            }
        }

        return result;
    }

    /**
     * PATTERN: Find by table
     */
    public List<Order> getOrdersByTable(int tableNumber) {
        List<Order> result = new ArrayList<>();

        for (Order order : allOrders) {
            if (order.getTableNumber() == tableNumber) {
                result.add(order);
            }
        }

        return result;
    }

    /**
     * PATTERN: Find oldest pending (waiting longest)
     */
    public Order findOldestPendingOrder() {
        if (pendingOrders.isEmpty()) {
            return null;
        }

        Order oldest = null;
        long earliestTime = Long.MAX_VALUE;

        for (Order order : pendingOrders) {
            if (order.getOrderTime() < earliestTime) {
                earliestTime = order.getOrderTime();
                oldest = order;
            }
        }

        return oldest;
    }

    /**
     * PATTERN: Find by time condition
     */
    public List<Order> getOrdersWaitingLongerThan(int minutes) {
        List<Order> result = new ArrayList<>();

        for (Order order : allOrders) {
            if (order.getWaitingTimeMinutes() > minutes &&
                order.getStatus() != OrderStatus.COMPLETED) {
                result.add(order);
            }
        }

        return result;
    }

    /**
     * PATTERN: Calculate total across collection
     */
    public int calculateTotalRevenue() {
        int total = 0;

        for (Order order : allOrders) {
            if (order.getStatus() == OrderStatus.COMPLETED) {
                total += order.calculateTotal();
            }
        }

        return total;
    }

    /**
     * PATTERN: Count by state
     */
    public int countPendingOrders() {
        return pendingOrders.size();
    }

    public int countPreparingOrders() {
        return preparingOrders.size();
    }

    public int countReadyOrders() {
        return readyOrders.size();
    }

    /**
     * Display methods
     */
    public void printPendingOrders() {
        System.out.println("=== Pending Orders ===");
        int i = 1;
        for (Order order : pendingOrders) {
            System.out.println(i++ + ". " + order);
        }
    }

    public void printPreparingOrders() {
        System.out.println("=== Preparing Orders ===");
        for (int i = 0; i < preparingOrders.size(); i++) {
            System.out.println((i + 1) + ". " + preparingOrders.get(i));
        }
    }

    public void printReadyOrders() {
        System.out.println("=== Ready Orders ===");
        for (int i = 0; i < readyOrders.size(); i++) {
            System.out.println((i + 1) + ". " + readyOrders.get(i));
        }
    }

    public void printAllOrders() {
        System.out.println("=== All Orders ===");
        for (int i = 0; i < allOrders.size(); i++) {
            System.out.println((i + 1) + ". " + allOrders.get(i));
        }
    }

    // Getters
    public List<Order> getAllOrders() {
        return allOrders;
    }

    public Queue<Order> getPendingOrders() {
        return pendingOrders;
    }
}
