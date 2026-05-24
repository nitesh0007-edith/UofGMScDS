# ⚡ Pattern Quick Reference - Copy-Paste Ready

## 🎯 Use this during exam for quick code snippets!

---

## 1️⃣ ENUM (Simple)

```java
public enum CategoryName {
    TYPE1,
    TYPE2,
    TYPE3
}
```

**Time:** 2 minutes

---

## 2️⃣ ENUM (With Properties)

```java
public enum SizeType {
    SMALL(1, 10),
    MEDIUM(2, 20),
    LARGE(3, 30);

    private final int capacity;
    private final int cost;

    SizeType(int capacity, int cost) {
        this.capacity = capacity;
        this.cost = cost;
    }

    public int getCapacity() {
        return capacity;
    }

    public int getCost() {
        return cost;
    }
}
```

**Time:** 4 minutes

---

## 3️⃣ VALIDATION Pattern

```java
// Check null AND length
if (name == null || name.length() < 3) {
    throw new IllegalArgumentException("Name must be at least 3 characters");
}

// Check range
if (age < 0 || age > 150) {
    throw new IllegalArgumentException("Invalid age");
}

// Check enum not null
if (category == null) {
    throw new IllegalArgumentException("Category cannot be null");
}

// Check related fields (min <= max)
if (minTemp > maxTemp) {
    throw new IllegalArgumentException("Min temperature cannot exceed max");
}
```

---

## 4️⃣ EQUALS and HASHCODE

```java
@Override
public boolean equals(Object o) {
    if (this == o) return true;
    if (o == null || getClass() != o.getClass()) return false;
    ClassName obj = (ClassName) o;
    return Objects.equals(id, obj.id);  // Use unique identifier
}

@Override
public int hashCode() {
    return Objects.hash(id);  // Same field as equals()
}
```

**Remember:** Import `java.util.Objects;`

---

## 5️⃣ TOSTRING

```java
@Override
public String toString() {
    return "ClassName{id='" + id + "', name='" + name +
           "', value=" + value + "}";
}
```

---

## 6️⃣ FIND BY ID (using Map)

```java
private Map<String, Item> itemsById;

// In constructor
itemsById = new HashMap<>();

// Add item
public void addItem(Item item) {
    items.add(item);
    itemsById.put(item.getId(), item);
}

// Find by ID - O(1) fast lookup
public Item findById(String id) {
    return itemsById.get(id);
}
```

---

## 7️⃣ FIND BY CRITERIA

```java
public List<Item> findByCategory(Category category) {
    List<Item> result = new ArrayList<>();

    for (Item item : items) {
        if (item.getCategory() == category) {
            result.add(item);
        }
    }

    return result;
}
```

---

## 8️⃣ FIND MINIMUM/BEST Algorithm

```java
public Item findCheapest() {
    if (items.isEmpty()) {
        return null;
    }

    Item cheapest = null;
    int lowestPrice = Integer.MAX_VALUE;  // Start with max

    for (Item item : items) {
        if (item.getPrice() < lowestPrice) {
            lowestPrice = item.getPrice();
            cheapest = item;
        }
    }

    return cheapest;
}
```

**Key:** Start with `Integer.MAX_VALUE` for minimum, `Integer.MIN_VALUE` for maximum

---

## 9️⃣ FIND BEST WITH CONDITIONS

```java
public Room findBestRoom(Guest guest) {
    Room best = null;
    int lowestCost = Integer.MAX_VALUE;

    for (Room room : rooms) {
        // Check eligibility FIRST
        if (room.isEmpty() && room.isCompatible(guest)) {

            // Among eligible, find minimum
            if (room.getCost() < lowestCost) {
                lowestCost = room.getCost();
                best = room;
            }
        }
    }

    return best;
}
```

**Pattern:** Filter first (eligibility), then compare (find best)

---

## 🔟 COMPATIBILITY CHECK

```java
public boolean isCompatible(Item item) {
    if (item == null) {
        return false;
    }

    // CHECK 1: Size compatibility
    if (item.getSize() == Size.LARGE && this.size != Size.LARGE) {
        return false;
    }

    // CHECK 2: Range check
    if (item.getValue() < minValue || item.getValue() > maxValue) {
        return false;
    }

    // CHECK 3: Type match
    if (item.getType() != this.allowedType) {
        return false;
    }

    // All checks passed
    return true;
}
```

**Pattern:** Return false immediately when condition fails

---

## 1️⃣1️⃣ SEARCH AND REMOVE

```java
public boolean removeItem(Item item) {
    for (Container container : containers) {
        // IMPORTANT: Check != null FIRST!
        if (container.getItem() != null &&
            container.getItem().equals(item)) {

            container.remove();
            return true;  // Found and removed
        }
    }

    return false;  // Not found
}
```

**Critical:** Always check `!= null` before calling `equals()`

---

## 1️⃣2️⃣ QUEUE Processing

```java
import java.util.Queue;
import java.util.LinkedList;

// In constructor
Queue<Order> pendingOrders = new LinkedList<>();

// Add to queue
pendingOrders.add(order);

// Get next (FIFO - First In First Out)
Order next = pendingOrders.poll();  // Returns null if empty

if (next != null) {
    // Process the order
}
```

---

## 1️⃣3️⃣ STATE TRANSITIONS

```java
public void nextState() {
    // Validate current state
    if (status != Status.PENDING) {
        throw new IllegalStateException(
            "Can only advance from PENDING state");
    }

    // Change state
    status = Status.PROCESSING;
}
```

---

## 1️⃣4️⃣ 2D ARRAY Initialization

```java
// Create 2D array
Item[][] grid = new Item[rows][columns];

// Initialize all cells
for (int r = 0; r < rows; r++) {
    for (int c = 0; c < columns; c++) {
        grid[r][c] = new Item(r, c);
    }
}
```

---

## 1️⃣5️⃣ 2D ARRAY Search

```java
public Item findItem(String id) {
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < columns; c++) {
            if (grid[r][c].getId().equals(id)) {
                return grid[r][c];  // Found!
            }
        }
    }
    return null;  // Not found
}
```

---

## 1️⃣6️⃣ MANHATTAN DISTANCE (Find Nearest)

```java
public Item findNearest(int targetRow, int targetCol) {
    Item nearest = null;
    int minDistance = Integer.MAX_VALUE;

    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < columns; c++) {
            // Calculate Manhattan distance
            int distance = Math.abs(r - targetRow) +
                          Math.abs(c - targetCol);

            if (distance < minDistance) {
                minDistance = distance;
                nearest = grid[r][c];
            }
        }
    }

    return nearest;
}
```

---

## 1️⃣7️⃣ DATE/TIME Comparison

```java
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
```

---

## 1️⃣8️⃣ SIMPLE BUBBLE SORT

```java
public List<Item> getSortedList() {
    List<Item> sorted = new ArrayList<>(items);  // Copy

    for (int i = 0; i < sorted.size() - 1; i++) {
        for (int j = 0; j < sorted.size() - i - 1; j++) {
            // Compare adjacent elements
            if (sorted.get(j + 1).getValue() < sorted.get(j).getValue()) {
                // Swap
                Item temp = sorted.get(j);
                sorted.set(j, sorted.get(j + 1));
                sorted.set(j + 1, temp);
            }
        }
    }

    return sorted;
}
```

---

## 1️⃣9️⃣ COUNT with CONDITION

```java
public int countAvailable() {
    int count = 0;

    for (Item item : items) {
        if (item.isAvailable()) {
            count++;
        }
    }

    return count;
}
```

---

## 2️⃣0️⃣ CALCULATE TOTAL

```java
public int calculateTotal() {
    int total = 0;

    for (Item item : items) {
        total += item.getPrice();
    }

    return total;
}
```

---

## 🎯 NULL SAFETY Checklist

```java
// ✅ ALWAYS check null BEFORE calling methods
if (item != null && item.getName().equals("test")) {
    // Safe!
}

// ❌ WRONG - will crash if item is null
if (item.getName().equals("test")) {
    // NullPointerException!
}

// ✅ Use Objects.equals() for null-safe comparison
if (Objects.equals(str1, str2)) {
    // Handles null safely
}

// ✅ Check null in AND conditions - put null check FIRST
if (container.getItem() != null && container.getItem().equals(target)) {
    // The null check happens first, preventing crash
}
```

---

## 📋 Common Imports

```java
import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
import java.util.Map;
import java.util.HashSet;
import java.util.Set;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Objects;
```

---

## ⚡ Time Allocation

- **Enum (simple):** 2-3 min
- **Enum (with fields):** 4-5 min
- **Data class:** 10-15 min
- **Container class:** 12-15 min
- **Manager class:** 18-22 min
- **Testing/Debugging:** 5 min

**Total:** 45-50 minutes

---

## 🚀 Exam Strategy

1. **Read entire question** (5 min)
2. **Identify pattern** (which skeleton?)
3. **Write enum first** (easy marks)
4. **Write simple data class** (foundation)
5. **Write container/manager classes**
6. **Compile and test** (frequently!)

**Good luck!** 🍀
