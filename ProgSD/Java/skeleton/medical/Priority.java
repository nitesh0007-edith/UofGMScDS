package medical;

/**
 * PATTERN 12: ENUM with ordering/priority
 * TIME: 3-4 minutes
 * MARKS: 3
 *
 * Enum representing priority levels (higher = more urgent)
 */
public enum Priority {
    LOW(1),
    MEDIUM(2),
    HIGH(3),
    EMERGENCY(4);

    private final int level;

    Priority(int level) {
        this.level = level;
    }

    public int getLevel() {
        return level;
    }

    /**
     * Compare priorities
     */
    public boolean isHigherThan(Priority other) {
        return this.level > other.level;
    }

    public boolean isLowerThan(Priority other) {
        return this.level < other.level;
    }
}
