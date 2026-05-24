package medical;

import java.util.ArrayList;
import java.util.List;

/**
 * PATTERN 14: PRIORITY SCHEDULER (manages items by priority and time)
 * TIME: 20-25 minutes
 * MARKS: 18
 *
 * SKELETON for: Scheduler, priority queue manager
 *
 * KEY FEATURES:
 * - Find by priority
 * - Find by time/date
 * - Sort by multiple criteria
 * - Conflict detection
 */
public class Clinic {

    private List<Appointment> appointments;

    /**
     * Constructor
     */
    public Clinic() {
        this.appointments = new ArrayList<>();
    }

    /**
     * Add appointment
     */
    public void addAppointment(Appointment appointment) {
        if (appointment == null) {
            throw new IllegalArgumentException("Appointment cannot be null");
        }
        appointments.add(appointment);
    }

    /**
     * PATTERN: Find by ID
     */
    public Appointment findAppointmentById(String appointmentId) {
        if (appointmentId == null) {
            return null;
        }

        for (Appointment appt : appointments) {
            if (appt.getAppointmentId().equals(appointmentId)) {
                return appt;
            }
        }

        return null;
    }

    /**
     * PATTERN: Find all by patient
     */
    public List<Appointment> findAppointmentsByPatient(String patientName) {
        List<Appointment> result = new ArrayList<>();

        for (Appointment appt : appointments) {
            if (appt.getPatientName().equals(patientName)) {
                result.add(appt);
            }
        }

        return result;
    }

    /**
     * PATTERN: Find all by doctor
     */
    public List<Appointment> findAppointmentsByDoctor(String doctorName) {
        List<Appointment> result = new ArrayList<>();

        for (Appointment appt : appointments) {
            if (appt.getDoctorName().equals(doctorName)) {
                result.add(appt);
            }
        }

        return result;
    }

    /**
     * PATTERN: Find all on specific date
     */
    public List<Appointment> findAppointmentsByDate(int year, int month, int day) {
        List<Appointment> result = new ArrayList<>();

        for (Appointment appt : appointments) {
            if (appt.isOnDate(year, month, day)) {
                result.add(appt);
            }
        }

        return result;
    }

    /**
     * PATTERN: Find all by priority
     */
    public List<Appointment> findAppointmentsByPriority(Priority priority) {
        List<Appointment> result = new ArrayList<>();

        for (Appointment appt : appointments) {
            if (appt.getPriority() == priority) {
                result.add(appt);
            }
        }

        return result;
    }

    /**
     * PATTERN: Find highest priority appointment
     *
     * Among all appointments, find the one with highest priority
     * If multiple have same highest priority, return earliest one
     */
    public Appointment findHighestPriorityAppointment() {
        if (appointments.isEmpty()) {
            return null;
        }

        Appointment highest = null;
        int maxPriority = -1;

        for (Appointment appt : appointments) {
            // Skip cancelled/completed
            if (appt.isCancelled() || appt.isCompleted()) {
                continue;
            }

            int priority = appt.getPriority().getLevel();

            // Is this higher priority?
            if (priority > maxPriority) {
                maxPriority = priority;
                highest = appt;
            }
            // Same priority - pick earlier time
            else if (priority == maxPriority && highest != null) {
                if (appt.isBefore(highest)) {
                    highest = appt;
                }
            }
        }

        return highest;
    }

    /**
     * PATTERN: Find next appointment (earliest in future)
     */
    public Appointment findNextAppointment(int currentYear, int currentMonth, int currentDay) {
        Appointment next = null;

        for (Appointment appt : appointments) {
            // Skip cancelled/completed
            if (appt.isCancelled() || appt.isCompleted()) {
                continue;
            }

            // Skip past appointments
            if (appt.isInPast(currentYear, currentMonth, currentDay)) {
                continue;
            }

            // Is this earlier than current next?
            if (next == null || appt.isBefore(next)) {
                next = appt;
            }
        }

        return next;
    }

    /**
     * PATTERN: Detect time conflict
     *
     * Check if doctor already has appointment at this time
     */
    public boolean hasConflict(String doctorName, int year, int month, int day, int hour) {
        for (Appointment appt : appointments) {
            // Skip cancelled
            if (appt.isCancelled()) {
                continue;
            }

            // Check if same doctor and same time
            if (appt.getDoctorName().equals(doctorName) &&
                appt.getYear() == year &&
                appt.getMonth() == month &&
                appt.getDay() == day &&
                appt.getHour() == hour) {
                return true;  // Conflict found
            }
        }

        return false;  // No conflict
    }

    /**
     * PATTERN: Schedule with conflict checking
     */
    public boolean scheduleAppointment(Appointment appointment) {
        if (appointment == null) {
            throw new IllegalArgumentException("Appointment cannot be null");
        }

        // Check for conflicts
        if (hasConflict(appointment.getDoctorName(),
                       appointment.getYear(),
                       appointment.getMonth(),
                       appointment.getDay(),
                       appointment.getHour())) {
            return false;  // Cannot schedule - conflict exists
        }

        // No conflict - add appointment
        appointments.add(appointment);
        return true;
    }

    /**
     * PATTERN: Cancel appointment
     */
    public boolean cancelAppointment(String appointmentId) {
        Appointment appt = findAppointmentById(appointmentId);

        if (appt == null) {
            return false;
        }

        appt.cancel();
        return true;
    }

    /**
     * PATTERN: Complete appointment
     */
    public boolean completeAppointment(String appointmentId) {
        Appointment appt = findAppointmentById(appointmentId);

        if (appt == null) {
            return false;
        }

        appt.complete();
        return true;
    }

    /**
     * PATTERN: Filter by multiple criteria
     *
     * Find appointments for doctor on specific date with priority
     */
    public List<Appointment> findAppointments(String doctorName, int year, int month, int day, Priority priority) {
        List<Appointment> result = new ArrayList<>();

        for (Appointment appt : appointments) {
            // Check all criteria
            if (appt.getDoctorName().equals(doctorName) &&
                appt.isOnDate(year, month, day) &&
                appt.getPriority() == priority &&
                !appt.isCancelled()) {

                result.add(appt);
            }
        }

        return result;
    }

    /**
     * PATTERN: Get sorted list (simple bubble sort for small lists)
     *
     * Sort appointments by time (earliest first)
     */
    public List<Appointment> getAppointmentsSortedByTime() {
        // Create copy to avoid modifying original
        List<Appointment> sorted = new ArrayList<>(appointments);

        // Simple bubble sort (sufficient for exam)
        for (int i = 0; i < sorted.size() - 1; i++) {
            for (int j = 0; j < sorted.size() - i - 1; j++) {
                if (sorted.get(j + 1).isBefore(sorted.get(j))) {
                    // Swap
                    Appointment temp = sorted.get(j);
                    sorted.set(j, sorted.get(j + 1));
                    sorted.set(j + 1, temp);
                }
            }
        }

        return sorted;
    }

    /**
     * Count appointments by status
     */
    public int countActiveAppointments() {
        int count = 0;
        for (Appointment appt : appointments) {
            if (!appt.isCancelled() && !appt.isCompleted()) {
                count++;
            }
        }
        return count;
    }

    public int countCompletedAppointments() {
        int count = 0;
        for (Appointment appt : appointments) {
            if (appt.isCompleted()) {
                count++;
            }
        }
        return count;
    }

    /**
     * Display methods
     */
    public void printAllAppointments() {
        System.out.println("=== All Appointments ===");
        for (int i = 0; i < appointments.size(); i++) {
            System.out.println((i + 1) + ". " + appointments.get(i));
        }
    }

    public void printAppointmentsByDate(int year, int month, int day) {
        System.out.println("=== Appointments on " + year + "-" + month + "-" + day + " ===");
        List<Appointment> onDate = findAppointmentsByDate(year, month, day);
        for (int i = 0; i < onDate.size(); i++) {
            System.out.println((i + 1) + ". " + onDate.get(i));
        }
    }

    // Getter
    public List<Appointment> getAppointments() {
        return appointments;
    }
}
