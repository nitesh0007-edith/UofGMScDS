package medical;

import java.util.Objects;

/**
 * PATTERN 13: SCHEDULED ITEM (has time and priority)
 * TIME: 15-18 minutes
 * MARKS: 12
 *
 * SKELETON for: Appointment, Event, Task with time/priority
 *
 * KEY FEATURES:
 * - Has date/time information
 * - Has priority level
 * - Comparable by time or priority
 * - State (scheduled, completed, cancelled)
 */
public class Appointment {

    private String appointmentId;
    private String patientName;
    private String doctorName;

    // Scheduling information
    private int year;
    private int month;
    private int day;
    private int hour;  // 24-hour format (0-23)

    // Priority
    private Priority priority;

    // State
    private boolean isCompleted;
    private boolean isCancelled;

    /**
     * Constructor
     */
    public Appointment(String appointmentId, String patientName, String doctorName,
                       int year, int month, int day, int hour, Priority priority) {

        // TODO: Validate inputs
        if (appointmentId == null || appointmentId.length() < 3) {
            throw new IllegalArgumentException("Appointment ID must be at least 3 characters");
        }

        if (patientName == null || patientName.length() < 2) {
            throw new IllegalArgumentException("Patient name must be at least 2 characters");
        }

        if (doctorName == null || doctorName.length() < 2) {
            throw new IllegalArgumentException("Doctor name must be at least 2 characters");
        }

        // Validate date/time
        if (year < 2020 || year > 2030) {
            throw new IllegalArgumentException("Invalid year");
        }

        if (month < 1 || month > 12) {
            throw new IllegalArgumentException("Month must be between 1 and 12");
        }

        if (day < 1 || day > 31) {
            throw new IllegalArgumentException("Day must be between 1 and 31");
        }

        if (hour < 0 || hour > 23) {
            throw new IllegalArgumentException("Hour must be between 0 and 23");
        }

        if (priority == null) {
            throw new IllegalArgumentException("Priority cannot be null");
        }

        this.appointmentId = appointmentId;
        this.patientName = patientName;
        this.doctorName = doctorName;
        this.year = year;
        this.month = month;
        this.day = day;
        this.hour = hour;
        this.priority = priority;

        this.isCompleted = false;
        this.isCancelled = false;
    }

    // Getters
    public String getAppointmentId() {
        return appointmentId;
    }

    public String getPatientName() {
        return patientName;
    }

    public String getDoctorName() {
        return doctorName;
    }

    public int getYear() {
        return year;
    }

    public int getMonth() {
        return month;
    }

    public int getDay() {
        return day;
    }

    public int getHour() {
        return hour;
    }

    public Priority getPriority() {
        return priority;
    }

    public boolean isCompleted() {
        return isCompleted;
    }

    public boolean isCancelled() {
        return isCancelled;
    }

    /**
     * PATTERN: State change methods
     */
    public void complete() {
        if (isCancelled) {
            throw new IllegalStateException("Cannot complete cancelled appointment");
        }
        this.isCompleted = true;
    }

    public void cancel() {
        if (isCompleted) {
            throw new IllegalStateException("Cannot cancel completed appointment");
        }
        this.isCancelled = true;
    }

    /**
     * PATTERN: Time comparison methods
     */
    public boolean isOnDate(int year, int month, int day) {
        return this.year == year && this.month == month && this.day == day;
    }

    public boolean isBefore(Appointment other) {
        // Compare year first
        if (this.year != other.year) {
            return this.year < other.year;
        }
        // Year same, compare month
        if (this.month != other.month) {
            return this.month < other.month;
        }
        // Month same, compare day
        if (this.day != other.day) {
            return this.day < other.day;
        }
        // Day same, compare hour
        return this.hour < other.hour;
    }

    public boolean isAfter(Appointment other) {
        return !isBefore(other) && !isSameTime(other);
    }

    public boolean isSameTime(Appointment other) {
        return this.year == other.year &&
               this.month == other.month &&
               this.day == other.day &&
               this.hour == other.hour;
    }

    /**
     * PATTERN: Check if appointment is in the past/future
     * Simplified: compare against a reference date
     */
    public boolean isInPast(int currentYear, int currentMonth, int currentDay) {
        if (this.year < currentYear) return true;
        if (this.year > currentYear) return false;

        if (this.month < currentMonth) return true;
        if (this.month > currentMonth) return false;

        return this.day < currentDay;
    }

    /**
     * Format date/time as string
     */
    public String getDateString() {
        return String.format("%04d-%02d-%02d", year, month, day);
    }

    public String getTimeString() {
        return String.format("%02d:00", hour);
    }

    public String getDateTimeString() {
        return getDateString() + " " + getTimeString();
    }

    @Override
    public String toString() {
        String status = isCompleted ? " [COMPLETED]" : (isCancelled ? " [CANCELLED]" : "");
        return "Appointment{id='" + appointmentId + "', patient='" + patientName +
               "', doctor='" + doctorName + "', date=" + getDateTimeString() +
               ", priority=" + priority + status + "}";
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Appointment that = (Appointment) o;
        return Objects.equals(appointmentId, that.appointmentId);
    }

    @Override
    public int hashCode() {
        return Objects.hash(appointmentId);
    }
}
