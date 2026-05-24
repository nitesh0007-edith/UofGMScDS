package medical;

/**
 * Test class for Medical Clinic System
 *
 * Demonstrates Scheduling + Priority pattern
 * Time/date handling and priority-based operations
 */
public class TestClinic {

    public static void main(String[] args) {
        System.out.println("=== Medical Clinic Appointment System Test ===\n");

        // Create clinic
        Clinic clinic = new Clinic();

        // TEST 1: Create appointments
        System.out.println("1. Creating appointments...");
        Appointment appt1 = new Appointment("A001", "Alice", "Dr. Smith",
                                           2025, 1, 15, 9, Priority.LOW);
        Appointment appt2 = new Appointment("A002", "Bob", "Dr. Jones",
                                           2025, 1, 15, 10, Priority.HIGH);
        Appointment appt3 = new Appointment("A003", "Charlie", "Dr. Smith",
                                           2025, 1, 15, 14, Priority.EMERGENCY);
        Appointment appt4 = new Appointment("A004", "Diana", "Dr. Brown",
                                           2025, 1, 16, 9, Priority.MEDIUM);
        Appointment appt5 = new Appointment("A005", "Eve", "Dr. Jones",
                                           2025, 1, 16, 11, Priority.HIGH);
        Appointment appt6 = new Appointment("A006", "Frank", "Dr. Smith",
                                           2025, 1, 17, 10, Priority.LOW);

        System.out.println("✓ Created 6 appointments\n");

        // TEST 2: Display appointment details
        System.out.println("2. Appointment details:");
        System.out.println(appt1);
        System.out.println("Date: " + appt1.getDateString());
        System.out.println("Time: " + appt1.getTimeString());
        System.out.println("Priority level: " + appt1.getPriority().getLevel());
        System.out.println();

        // TEST 3: Add appointments to clinic
        System.out.println("3. Adding appointments to clinic...");
        clinic.addAppointment(appt1);
        clinic.addAppointment(appt2);
        clinic.addAppointment(appt3);
        clinic.addAppointment(appt4);
        clinic.addAppointment(appt5);
        clinic.addAppointment(appt6);
        System.out.println("✓ Added 6 appointments\n");

        // TEST 4: Display all appointments
        System.out.println("4. All appointments:");
        clinic.printAllAppointments();
        System.out.println();

        // TEST 5: Find appointment by ID
        System.out.println("5. Finding appointment by ID...");
        Appointment found = clinic.findAppointmentById("A003");
        if (found != null) {
            System.out.println("Found: " + found);
        }
        System.out.println();

        // TEST 6: Find appointments by patient
        System.out.println("6. Finding appointments for patient Alice...");
        for (Appointment appt : clinic.findAppointmentsByPatient("Alice")) {
            System.out.println("  - " + appt);
        }
        System.out.println();

        // TEST 7: Find appointments by doctor
        System.out.println("7. Finding appointments for Dr. Smith...");
        for (Appointment appt : clinic.findAppointmentsByDoctor("Dr. Smith")) {
            System.out.println("  - " + appt);
        }
        System.out.println();

        // TEST 8: Find appointments by date
        System.out.println("8. Finding appointments on 2025-01-15...");
        clinic.printAppointmentsByDate(2025, 1, 15);
        System.out.println();

        // TEST 9: Find appointments by priority
        System.out.println("9. Finding all EMERGENCY appointments...");
        for (Appointment appt : clinic.findAppointmentsByPriority(Priority.EMERGENCY)) {
            System.out.println("  - " + appt);
        }
        System.out.println();

        // TEST 10: Find highest priority appointment (KEY ALGORITHM)
        System.out.println("10. Finding highest priority appointment...");
        Appointment highest = clinic.findHighestPriorityAppointment();
        if (highest != null) {
            System.out.println("Highest priority: " + highest);
            System.out.println("Priority level: " + highest.getPriority() +
                             " (level " + highest.getPriority().getLevel() + ")");
        }
        System.out.println();

        // TEST 11: Test time comparison
        System.out.println("11. Testing time comparison...");
        System.out.println("appt1 is before appt2: " + appt1.isBefore(appt2));
        System.out.println("appt1 is after appt2: " + appt1.isAfter(appt2));
        System.out.println("appt1 same time as appt2: " + appt1.isSameTime(appt2));
        System.out.println();

        // TEST 12: Test date check
        System.out.println("12. Testing date checks...");
        System.out.println("appt1 is on 2025-01-15: " + appt1.isOnDate(2025, 1, 15));
        System.out.println("appt1 is on 2025-01-16: " + appt1.isOnDate(2025, 1, 16));
        System.out.println();

        // TEST 13: Find next appointment
        System.out.println("13. Finding next appointment from current date (2025-01-14)...");
        Appointment next = clinic.findNextAppointment(2025, 1, 14);
        if (next != null) {
            System.out.println("Next appointment: " + next);
        }
        System.out.println();

        // TEST 14: Test conflict detection
        System.out.println("14. Testing conflict detection...");
        boolean conflict1 = clinic.hasConflict("Dr. Smith", 2025, 1, 15, 9);
        System.out.println("Dr. Smith has conflict at 2025-01-15 09:00: " + conflict1 + " (appt1 exists)");

        boolean conflict2 = clinic.hasConflict("Dr. Smith", 2025, 1, 15, 11);
        System.out.println("Dr. Smith has conflict at 2025-01-15 11:00: " + conflict2 + " (no appointment)");
        System.out.println();

        // TEST 15: Schedule with conflict checking
        System.out.println("15. Testing schedule with conflict checking...");
        Appointment newAppt = new Appointment("A007", "George", "Dr. Smith",
                                             2025, 1, 15, 9, Priority.MEDIUM);
        boolean scheduled = clinic.scheduleAppointment(newAppt);
        System.out.println("Try to schedule at same time as appt1: " +
                          (scheduled ? "✗ Should have failed" : "✓ Correctly prevented"));

        Appointment newAppt2 = new Appointment("A008", "Helen", "Dr. Smith",
                                              2025, 1, 15, 11, Priority.LOW);
        boolean scheduled2 = clinic.scheduleAppointment(newAppt2);
        System.out.println("Schedule at available time: " +
                          (scheduled2 ? "✓ Success" : "✗ Failed"));
        System.out.println();

        // TEST 16: Complete and cancel appointments
        System.out.println("16. Testing appointment completion and cancellation...");
        appt1.complete();
        System.out.println("Completed appt1: " + appt1.isCompleted());

        appt6.cancel();
        System.out.println("Cancelled appt6: " + appt6.isCancelled());
        System.out.println();

        // TEST 17: Find highest priority excluding completed/cancelled
        System.out.println("17. Finding highest priority (excluding completed/cancelled)...");
        Appointment highestActive = clinic.findHighestPriorityAppointment();
        if (highestActive != null) {
            System.out.println("Highest priority active: " + highestActive);
            System.out.println("Should be A003 (EMERGENCY): " +
                             (highestActive.getAppointmentId().equals("A003") ? "✓ Correct" : "✗ Wrong"));
        }
        System.out.println();

        // TEST 18: Test invalid state transitions
        System.out.println("18. Testing invalid state transitions...");
        try {
            appt1.cancel();  // Already completed
            System.out.println("✗ Should have thrown exception!");
        } catch (IllegalStateException e) {
            System.out.println("✓ Correctly prevented cancelling completed: " + e.getMessage());
        }

        try {
            appt6.complete();  // Already cancelled
            System.out.println("✗ Should have thrown exception!");
        } catch (IllegalStateException e) {
            System.out.println("✓ Correctly prevented completing cancelled: " + e.getMessage());
        }
        System.out.println();

        // TEST 19: Cancel appointment through clinic
        System.out.println("19. Testing cancel through clinic...");
        boolean cancelled = clinic.cancelAppointment("A002");
        System.out.println("Cancelled A002: " + (cancelled ? "✓ Success" : "✗ Failed"));
        System.out.println("A002 is cancelled: " + appt2.isCancelled());
        System.out.println();

        // TEST 20: Complete appointment through clinic
        System.out.println("20. Testing complete through clinic...");
        boolean completed = clinic.completeAppointment("A003");
        System.out.println("Completed A003: " + (completed ? "✓ Success" : "✗ Failed"));
        System.out.println("A003 is completed: " + appt3.isCompleted());
        System.out.println();

        // TEST 21: Count active appointments
        System.out.println("21. Counting appointments by status...");
        System.out.println("Active appointments: " + clinic.countActiveAppointments());
        System.out.println("Completed appointments: " + clinic.countCompletedAppointments());
        System.out.println();

        // TEST 22: Find by multiple criteria
        System.out.println("22. Finding by multiple criteria...");
        System.out.println("Dr. Smith on 2025-01-15 with HIGH priority:");
        for (Appointment appt : clinic.findAppointments("Dr. Smith", 2025, 1, 15, Priority.HIGH)) {
            System.out.println("  - " + appt);
        }
        System.out.println();

        // TEST 23: Get sorted appointments (by time)
        System.out.println("23. Getting appointments sorted by time...");
        System.out.println("(Should be in chronological order)");
        int count = 1;
        for (Appointment appt : clinic.getAppointmentsSortedByTime()) {
            System.out.println(count++ + ". " + appt.getDateTimeString() + " - " +
                             appt.getPatientName() + " (" + appt.getPriority() + ")");
        }
        System.out.println();

        // TEST 24: Test priority comparison
        System.out.println("24. Testing priority comparison...");
        System.out.println("EMERGENCY is higher than HIGH: " +
                          Priority.EMERGENCY.isHigherThan(Priority.HIGH));
        System.out.println("LOW is lower than MEDIUM: " +
                          Priority.LOW.isLowerThan(Priority.MEDIUM));
        System.out.println("MEDIUM level: " + Priority.MEDIUM.getLevel());
        System.out.println();

        // TEST 25: Test date/time validation
        System.out.println("25. Testing validation...");
        try {
            Appointment invalid = new Appointment("A999", "Test", "Dr. Test",
                                                 2025, 13, 15, 9, Priority.LOW);
            System.out.println("✗ Should have thrown exception!");
        } catch (IllegalArgumentException e) {
            System.out.println("✓ Correctly rejected invalid month: " + e.getMessage());
        }

        try {
            Appointment invalid2 = new Appointment("A999", "Test", "Dr. Test",
                                                  2025, 1, 15, 25, Priority.LOW);
            System.out.println("✗ Should have thrown exception!");
        } catch (IllegalArgumentException e) {
            System.out.println("✓ Correctly rejected invalid hour: " + e.getMessage());
        }
        System.out.println();

        // TEST 26: Test isInPast
        System.out.println("26. Testing past/future check...");
        System.out.println("appt1 (2025-01-15) is in past from 2025-01-14: " +
                          appt1.isInPast(2025, 1, 14));
        System.out.println("appt1 (2025-01-15) is in past from 2025-01-16: " +
                          appt1.isInPast(2025, 1, 16));
        System.out.println();

        // TEST 27: Test finding next appointment with current date
        System.out.println("27. Finding next appointment from 2025-01-15...");
        Appointment nextFromMid = clinic.findNextAppointment(2025, 1, 15);
        if (nextFromMid != null) {
            System.out.println("Next appointment: " + nextFromMid.getDateTimeString());
        }
        System.out.println();

        // TEST 28: Create test scenario - same priority, different times
        System.out.println("28. Testing same priority, different times...");
        Clinic testClinic = new Clinic();
        Appointment early = new Appointment("E1", "Patient1", "Dr. A",
                                           2025, 2, 1, 9, Priority.HIGH);
        Appointment late = new Appointment("E2", "Patient2", "Dr. B",
                                          2025, 2, 1, 15, Priority.HIGH);
        testClinic.addAppointment(late);   // Add late first
        testClinic.addAppointment(early);  // Add early second

        Appointment result = testClinic.findHighestPriorityAppointment();
        System.out.println("With same priority, should pick earlier time: " +
                          result.getAppointmentId());
        System.out.println("Is E1 (9:00): " +
                          (result.getAppointmentId().equals("E1") ? "✓ Correct" : "✗ Wrong"));
        System.out.println();

        // FINAL: Display final state
        System.out.println("=== FINAL STATE ===");
        clinic.printAllAppointments();

        System.out.println("\nStatistics:");
        System.out.println("Total appointments: " + clinic.getAppointments().size());
        System.out.println("Active: " + clinic.countActiveAppointments());
        System.out.println("Completed: " + clinic.countCompletedAppointments());

        System.out.println("\n✓ All tests completed successfully!");
        System.out.println("\nKey Patterns Demonstrated:");
        System.out.println("- Date/time comparison (year → month → day → hour)");
        System.out.println("- Priority-based selection (find highest)");
        System.out.println("- Conflict detection (same doctor, same time)");
        System.out.println("- Multi-criteria filtering");
        System.out.println("- Sorting by time (bubble sort)");
        System.out.println("- State management (completed/cancelled)");
    }
}
