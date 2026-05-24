# 🎯 Java Exam Skeleton Code - Pattern Library

## 📚 What is This?

This folder contains **skeleton code templates** with **different patterns** commonly found in Java exams.

Each skeleton is a **ready-to-adapt template** that you can use for the 2025 exam!

---

## 🗂️ Available Patterns

### **Pattern 1: Library Management** (Collection + Manager)
**Folder:** `library/`
**Files:** BookCategory.java, Book.java, Member.java, Library.java

**Use this pattern when:**
- Managing collections of items (books, products, resources)
- Items can be borrowed/checked out
- Need to search, filter, and find items
- Simple one-to-many relationships (member has books)

**Key algorithms:**
- Find by ID (fast lookup with Map)
- Find by criteria (filter collection)
- Find best/oldest/cheapest (minimum algorithm)
- Add/remove from collections

**Time:** 45-50 minutes
**Difficulty:** Medium

---

### **Pattern 2: Hotel Booking** (Container + Allocation)
**Folder:** `hotel/`
**Files:** RoomType.java, Guest.java, Room.java, Hotel.java

**Use this pattern when:**
- Items need to be placed in containers (guests in rooms)
- Containers have capacity/compatibility rules
- Need to find "best" container (cheapest compatible)
- Each container holds ONE item

**Key algorithms:**
- Compatibility checking (size, type, preferences)
- Find cheapest/best allocation
- Search for item in containers
- Empty vs occupied state management

**Time:** 45-50 minutes
**Difficulty:** Medium-Hard

**Similar to:** 2024 Pet Care exam

---

### **Pattern 3: Restaurant Orders** (Queue + Processing)
**Folder:** `restaurant/`
**Files:** OrderStatus.java, Order.java, Restaurant.java

**Use this pattern when:**
- Items move through workflow stages
- State transitions (pending → preparing → ready → served)
- FIFO processing (first in, first out)
- Time-based operations

**Key algorithms:**
- Queue processing (poll from queue)
- State transitions with validation
- Find by state/status
- Time calculations
- Move items between states

**Time:** 45-50 minutes
**Difficulty:** Medium

---

### **Pattern 4: Parking Lot** (Grid + Search)
**Folder:** `parking/`
**Files:** VehicleType.java, Vehicle.java, ParkingSpot.java, ParkingLot.java

**Use this pattern when:**
- 2D grid/array of containers
- Position-based (row, column)
- Find nearest/closest
- Distance calculations

**Key algorithms:**
- 2D array initialization
- Search through grid
- Find nearest (Manhattan distance)
- Grid position (row/column to ID like "A5")

**Time:** 50-55 minutes
**Difficulty:** Hard

**Note:** More complex than typical exam, but good practice!

---

### **Pattern 5: Medical Appointments** (Scheduling + Priority)
**Folder:** `medical/`
**Files:** Priority.java, Appointment.java, Clinic.java

**Use this pattern when:**
- Items have priority levels
- Time/date scheduling
- Conflict detection
- Sort by multiple criteria

**Key algorithms:**
- Find highest priority
- Find next/earliest
- Conflict detection (same time/resource)
- Date/time comparisons
- Sort by time or priority

**Time:** 50-55 minutes
**Difficulty:** Hard

---

## 🎯 How to Use These Skeletons

### Step 1: Identify the Pattern (5 minutes)

Read the exam question and identify which pattern it matches:

**Question mentions...**
- "Books/Items/Products to manage" → **Library pattern**
- "Rooms/Spots/Enclosures for items" → **Hotel or Parking pattern**
- "Orders/Requests that change state" → **Restaurant pattern**
- "Grid/Array of positions" → **Parking pattern**
- "Appointments/Events with time" → **Medical pattern**

### Step 2: Copy the Skeleton

Copy the entire package folder for the matching pattern.

### Step 3: Rename Everything (5-10 minutes)

**Find & Replace:**
- Class names (Book → Item)
- Package name (library → yourpackage)
- Field names (isbn → itemId)
- Enum values (FICTION → TYPE1)

**Example:**
```
Exam asks for: "Shop" with "Products" and "Customers"

Use: Library pattern
Rename: Library → Shop, Book → Product, Member → Customer
```

### Step 4: Adapt the Logic (30-35 minutes)

- Keep the validation patterns
- Keep the search/filter algorithms
- Adjust compatibility rules
- Modify calculations (if needed)
- Add/remove fields as specified

### Step 5: Test and Debug (5 minutes)

- Compile frequently
- Check all validations
- Test main scenarios

---

## 🔑 Key Patterns Summary

### **All Skeletons Include:**

✅ **Validation Pattern** - Constructor and setter validation
✅ **Null Checking** - Check null before using objects
✅ **Collection Management** - ArrayList, HashMap, Queue
✅ **Search Patterns** - Find by ID, find by criteria
✅ **Filter Patterns** - Get all matching condition
✅ **Override Methods** - toString(), equals(), hashCode()

### **Special Algorithms:**

🎯 **Find Minimum/Best** (Library, Hotel, Parking)
```java
int lowestValue = Integer.MAX_VALUE;
Item best = null;
for (Item item : items) {
    if (item.getValue() < lowestValue) {
        lowestValue = item.getValue();
        best = item;
    }
}
```

🎯 **Compatibility Check** (Hotel, Parking)
```java
public boolean isCompatible(Item item) {
    if (item == null) return false;

    // Check condition 1
    if (!check1) return false;

    // Check condition 2
    if (!check2) return false;

    return true;  // All checks passed
}
```

🎯 **State Transition** (Restaurant, Medical)
```java
public void nextState() {
    if (currentState != EXPECTED_STATE) {
        throw new IllegalStateException("Invalid transition");
    }
    currentState = NEXT_STATE;
}
```

🎯 **Queue Processing** (Restaurant)
```java
Queue<Order> queue = new LinkedList<>();
Order next = queue.poll();  // Remove and return first
if (next != null) {
    // Process
}
```

🎯 **2D Array Search** (Parking)
```java
for (int r = 0; r < rows; r++) {
    for (int c = 0; c < cols; c++) {
        if (array[r][c].matches()) {
            return array[r][c];
        }
    }
}
```

🎯 **Date/Time Comparison** (Medical)
```java
public boolean isBefore(Item other) {
    if (this.year != other.year) {
        return this.year < other.year;
    }
    if (this.month != other.month) {
        return this.month < other.month;
    }
    return this.day < other.day;
}
```

---

## 📋 Pattern Selection Guide

| Exam Question Feature | Best Pattern | Folder |
|----------------------|--------------|--------|
| Collection of items to manage | Library | `library/` |
| Items borrowed/returned | Library | `library/` |
| Items placed in containers | Hotel | `hotel/` |
| Find cheapest/best container | Hotel | `hotel/` |
| Workflow with states | Restaurant | `restaurant/` |
| Queue processing (FIFO) | Restaurant | `restaurant/` |
| 2D grid/array | Parking | `parking/` |
| Position-based (row/col) | Parking | `parking/` |
| Priority levels | Medical | `medical/` |
| Time/date scheduling | Medical | `medical/` |
| Conflict detection | Medical | `medical/` |

---

## 🎓 Learning Strategy

### Week Before Exam:
1. **Day 1-2:** Read all skeletons, understand patterns
2. **Day 3-4:** Practice renaming and adapting one skeleton
3. **Day 5-6:** Time yourself - adapt a skeleton in 50 minutes
4. **Day 7:** Review key algorithms, rest

### Day Before Exam:
- Skim through all 5 patterns
- Remember key algorithms (find best, compatibility)
- Review validation patterns
- Early sleep!

### During Exam:
1. **Read entire question** (5 min)
2. **Identify pattern** (which skeleton matches?)
3. **Recall skeleton structure** mentally
4. **Start coding** using skeleton as mental template

---

## ⚡ Quick Reference

### Enum (2-3 minutes):
```java
public enum TypeName {
    VALUE1, VALUE2, VALUE3
}
```

### Data Class (10-15 minutes):
- Fields
- Constructor with validation
- Getters
- Setters (with validation!)
- toString(), equals(), hashCode()

### Container Class (12-15 minutes):
- Properties (capacity, type)
- Occupant field (nullable)
- isCompatible() method
- add() and remove() methods

### Manager Class (18-22 minutes):
- Collections (List, Map, Queue)
- Add items
- Find by ID (Map lookup)
- Find by criteria (loop and filter)
- Find best (minimum algorithm)

---

## 💡 Exam Tips

### Always Do First:
1. **Enum** - Quick and easy marks (2-3 min)
2. **Simple data class** - Build foundation (10-12 min)
3. **Container class** (if applicable) - (12-15 min)
4. **Manager class** - Most marks (18-22 min)

### Common Mistakes to Avoid:
❌ Forgetting to validate in setters
❌ Not checking null before equals()
❌ Using == instead of equals() for Strings
❌ Forgetting to initialize collections
❌ Not using Integer.MAX_VALUE for finding minimum

### Must Remember:
✅ Validate in BOTH constructor AND setters
✅ Check null BEFORE calling methods
✅ Initialize collections in constructor
✅ equals() and hashCode() use SAME fields
✅ Use Objects.equals() for null-safe comparison

---

## 🚀 You're Ready!

With these 5 skeleton patterns, you can handle **any exam question**!

The key is:
1. **Recognize the pattern**
2. **Recall the skeleton**
3. **Adapt to the question**

Practice adapting these skeletons and you'll be able to write clean, correct code quickly in the exam!

**Good luck!** 🍀
