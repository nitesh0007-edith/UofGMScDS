package restaurant;

/**
 * Test class for Restaurant Order System
 *
 * Demonstrates Queue + Processing pattern
 * State transitions and workflow management
 */
public class TestRestaurant {

    public static void main(String[] args) {
        System.out.println("=== Restaurant Order System Test ===\n");

        // Create restaurant
        Restaurant restaurant = new Restaurant();

        // TEST 1: Create orders
        System.out.println("1. Creating orders...");
        Order order1 = new Order("ORD001", "Alice", 5);
        Order order2 = new Order("ORD002", "Bob", 3);
        Order order3 = new Order("ORD003", "Charlie", 7);
        Order order4 = new Order("ORD004", "Diana", 2);

        System.out.println("✓ Created 4 orders\n");

        // TEST 2: Add items to orders
        System.out.println("2. Adding items to orders...");
        order1.addItem("Burger", 15);
        order1.addItem("Fries", 5);
        order1.addItem("Coke", 3);

        order2.addItem("Pizza", 20);
        order2.addItem("Salad", 8);

        order3.addItem("Pasta", 18);
        order3.addItem("Wine", 12);

        order4.addItem("Sandwich", 10);

        System.out.println("✓ Added items to orders");
        System.out.println("Order 1 total: $" + order1.calculateTotal());
        System.out.println("Order 2 total: $" + order2.calculateTotal());
        System.out.println("Order 3 total: $" + order3.calculateTotal());
        System.out.println("Order 4 total: $" + order4.calculateTotal());
        System.out.println();

        // TEST 3: Display order details
        System.out.println("3. Order details:");
        System.out.println(order1);
        System.out.println("Items: " + order1.getItems());
        System.out.println();

        // TEST 4: Place orders (add to restaurant)
        System.out.println("4. Placing orders...");
        restaurant.placeOrder(order1);
        restaurant.placeOrder(order2);
        restaurant.placeOrder(order3);
        restaurant.placeOrder(order4);
        System.out.println("✓ All orders placed\n");

        // TEST 5: Display pending orders
        System.out.println("5. Pending orders queue:");
        restaurant.printPendingOrders();
        System.out.println("Pending count: " + restaurant.countPendingOrders());
        System.out.println();

        // TEST 6: Start preparing orders (QUEUE PATTERN - FIFO)
        System.out.println("6. Starting to prepare orders (FIFO - First In First Out)...");
        boolean started1 = restaurant.startPreparingNextOrder();
        System.out.println("Started preparing first order: " + (started1 ? "✓ Success" : "✗ Failed"));

        boolean started2 = restaurant.startPreparingNextOrder();
        System.out.println("Started preparing second order: " + (started2 ? "✓ Success" : "✗ Failed"));
        System.out.println();

        // TEST 7: Display preparing orders
        System.out.println("7. Currently preparing:");
        restaurant.printPreparingOrders();
        System.out.println("Preparing count: " + restaurant.countPreparingOrders());
        System.out.println();

        // TEST 8: Display pending orders (should have 2 left)
        System.out.println("8. Still pending:");
        restaurant.printPendingOrders();
        System.out.println();

        // TEST 9: Mark order as ready
        System.out.println("9. Marking order as ready...");
        boolean ready1 = restaurant.markOrderReady("ORD001");
        System.out.println("Order ORD001 marked ready: " + (ready1 ? "✓ Success" : "✗ Failed"));
        System.out.println();

        // TEST 10: Display ready orders
        System.out.println("10. Ready for pickup:");
        restaurant.printReadyOrders();
        System.out.println("Ready count: " + restaurant.countReadyOrders());
        System.out.println();

        // TEST 11: Serve order
        System.out.println("11. Serving order...");
        boolean served = restaurant.serveOrder("ORD001");
        System.out.println("Order ORD001 served: " + (served ? "✓ Success" : "✗ Failed"));
        System.out.println();

        // TEST 12: Check order status
        System.out.println("12. Checking order statuses...");
        Order found1 = restaurant.findOrderById("ORD001");
        if (found1 != null) {
            System.out.println("ORD001 status: " + found1.getStatus());
            System.out.println("Is completed: " + found1.isCompleted());
        }

        Order found2 = restaurant.findOrderById("ORD002");
        if (found2 != null) {
            System.out.println("ORD002 status: " + found2.getStatus());
        }
        System.out.println();

        // TEST 13: Test state transitions directly on Order
        System.out.println("13. Testing order state transitions...");
        Order testOrder = new Order("TEST", "TestCustomer", 10);
        testOrder.addItem("Test Item", 5);

        System.out.println("Initial status: " + testOrder.getStatus());
        testOrder.startPreparing();
        System.out.println("After startPreparing: " + testOrder.getStatus());
        testOrder.markReady();
        System.out.println("After markReady: " + testOrder.getStatus());
        testOrder.serve();
        System.out.println("After serve: " + testOrder.getStatus());
        testOrder.complete();
        System.out.println("After complete: " + testOrder.getStatus());
        System.out.println();

        // TEST 14: Test invalid state transitions
        System.out.println("14. Testing invalid state transitions...");
        try {
            Order badOrder = new Order("BAD", "Bad", 5);
            badOrder.addItem("Item", 10);
            badOrder.markReady();  // Can't mark ready when PENDING
            System.out.println("✗ Should have thrown exception!");
        } catch (IllegalStateException e) {
            System.out.println("✓ Correctly prevented invalid transition: " + e.getMessage());
        }
        System.out.println();

        // TEST 15: Test adding items to non-pending order
        System.out.println("15. Testing adding items to non-pending order...");
        try {
            testOrder.addItem("Another Item", 10);  // testOrder is COMPLETED
            System.out.println("✗ Should have thrown exception!");
        } catch (IllegalStateException e) {
            System.out.println("✓ Correctly prevented adding to " + testOrder.getStatus() + " order");
        }
        System.out.println();

        // TEST 16: Find orders by customer
        System.out.println("16. Finding orders by customer...");
        for (Order order : restaurant.getOrdersByCustomer("Alice")) {
            System.out.println("  - " + order);
        }
        System.out.println();

        // TEST 17: Find orders by table
        System.out.println("17. Finding orders by table...");
        for (Order order : restaurant.getOrdersByTable(3)) {
            System.out.println("  - " + order);
        }
        System.out.println();

        // TEST 18: Find orders by status
        System.out.println("18. Finding all PREPARING orders...");
        for (Order order : restaurant.getOrdersByStatus(OrderStatus.PREPARING)) {
            System.out.println("  - " + order);
        }
        System.out.println();

        // TEST 19: Complete workflow for remaining orders
        System.out.println("19. Completing workflow for remaining orders...");

        // Mark ORD002 ready and serve
        restaurant.markOrderReady("ORD002");
        restaurant.serveOrder("ORD002");
        System.out.println("ORD002 served");

        // Start preparing next pending orders
        restaurant.startPreparingNextOrder();
        restaurant.startPreparingNextOrder();
        System.out.println("Started preparing ORD003 and ORD004");

        // Mark them ready
        restaurant.markOrderReady("ORD003");
        restaurant.markOrderReady("ORD004");
        System.out.println("ORD003 and ORD004 ready");

        // Serve them
        restaurant.serveOrder("ORD003");
        restaurant.serveOrder("ORD004");
        System.out.println("All orders served");
        System.out.println();

        // TEST 20: Calculate total revenue (only completed orders)
        System.out.println("20. Calculating revenue...");
        found1.complete();  // Complete ORD001
        found2.complete();  // Complete ORD002
        int revenue = restaurant.calculateTotalRevenue();
        System.out.println("Total revenue from completed orders: $" + revenue);
        System.out.println();

        // TEST 21: Count completed orders
        System.out.println("21. Counting completed orders...");
        System.out.println("Completed: " + restaurant.countCompletedOrders());
        System.out.println();

        // TEST 22: Test waiting time
        System.out.println("22. Testing waiting time...");
        System.out.println("Order ORD001 waiting time: " +
                          found1.getWaitingTimeMinutes() + " minutes");
        System.out.println();

        // TEST 23: Test validation
        System.out.println("23. Testing validation...");
        try {
            Order invalidOrder = new Order("O1", "Test", 0);
            System.out.println("✗ Should have thrown exception!");
        } catch (IllegalArgumentException e) {
            System.out.println("✓ Correctly rejected invalid table: " + e.getMessage());
        }

        try {
            Order emptyOrder = new Order("O99", "Test", 5);
            emptyOrder.startPreparing();  // Empty order
            System.out.println("✗ Should have thrown exception!");
        } catch (IllegalStateException e) {
            System.out.println("✓ Correctly prevented preparing empty order: " + e.getMessage());
        }
        System.out.println();

        // FINAL: Display final state
        System.out.println("=== FINAL STATE ===");
        restaurant.printAllOrders();

        System.out.println("\nStatistics:");
        System.out.println("Pending: " + restaurant.countPendingOrders());
        System.out.println("Preparing: " + restaurant.countPreparingOrders());
        System.out.println("Ready: " + restaurant.countReadyOrders());

        System.out.println("\n✓ All tests completed successfully!");
        System.out.println("\nKey Patterns Demonstrated:");
        System.out.println("- Queue processing (FIFO - First In First Out)");
        System.out.println("- State transitions (PENDING → PREPARING → READY → SERVED → COMPLETED)");
        System.out.println("- State validation (can't skip states)");
        System.out.println("- Workflow management (move items between states)");
        System.out.println("- Time-based calculations");
    }
}
