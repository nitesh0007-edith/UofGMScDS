# Complete Java Exam Solutions (2019-2024)

## Overview
All 5 past papers solved with tested, working code optimized for 50-minute exam timing.

---

## 2024 Exam: Pet Care Service (40 marks)
**Package**: `petcare`
**Time**: 50 minutes
**Files to submit**: Animal.java, AnimalSize.java, Enclosure.java, PetService.java

### Task Summary:
- **Task 1 (10 marks)**: Animal class with validation
- **Task 2 (15 marks)**: Enclosure class with compatibility checking
- **Task 3 (15 marks)**: PetService class managing enclosures

### Key Points:
- Name validation: minimum 3 characters
- Temperature range: 0-50 degrees
- Size compatibility: SMALL < MEDIUM < LARGE
- Find cheapest compatible enclosure

**Test**: `cd 2024 && javac petcare/*.java && java petcare.TestPetService`

---

## 2023 Exam: Box Office/Theatre Booking (25 marks)
**Package**: `boxOffice`
**Time**: 50 minutes
**Files to submit**: SeatType.java, Seat.java, Venue.java, Event.java

### Task Summary:
- **Task 2a (8 marks)**: Seat class with row (A-Z), seat number, type, availability
- **Task 2b (8 marks)**: Venue class parsing string config
- **Task 2c (8 marks)**: Event class with seat reservation logic

### Key Points:
- Rows: A-Z (max 26)
- Seat numbers: start at 1
- Adjacent seats: consecutive numbers in same row
- SeatType enum: STANDARD, DELUXE

**Test**: `cd 2023 && javac boxOffice/*.java && java boxOffice.TestVenue`

---

## 2022 Exam: Directed Graphs (25 marks)
**Package**: `graphs`
**Time**: 50 minutes
**Files to submit**: Node.java, GraphParser.java, Edge.java, GraphExplorer.java

### Task Summary:
- **Task 2a (6 marks)**: Node class with label and neighbors
- **Task 2b (8 marks)**: GraphParser parsing string to graph
- **Task 2c (5 marks)**: Edge class representing directed edges
- **Task 2d (5 marks)**: GraphExplorer listing all edges

### Key Points:
- Adjacency list representation
- String parsing with split()
- Set<Edge> to avoid duplicates
- Override equals/hashCode for collections

**Test**: `cd 2022 && javac graphs/*.java && java graphs.TestGraph`

---

## 2021 Exam: Trading System (24 marks)
**Package**: `trading`
**Time**: 50 minutes
**Files to submit**: Goods.java, Trade.java, Citizen.java, Trader.java

### Task Summary:
- **Task 1 (3 marks)**: Goods enum with 10 types
- **Task 2 (7 marks)**: Trade class with gems, amount, goods
- **Task 3 (6 marks)**: Citizen with gems and inventory
- **Task 4 (4 marks)**: Trader with random trades
- **Task 5 (4 marks)**: Trade.execute() method

### Key Points:
- Use HashMap for inventory (Goods -> amount)
- Random: `rand.nextInt(5) + 1` gives 1-5
- Check citizen has enough gems before trade
- Add random trade after successful execution

**Test**: `cd 2021 && javac trading/*.java && java trading.TestTrading`

---

## 2019 Exam: Video Game Characters (24 marks)
**Package**: `superhero`
**Time**: 50 minutes
**Files to submit**: Power.java, GameCharacter.java, Player.java

### Task Summary:
- **Task 1 (2 marks)**: Power enum with 15 values
- **Task 2 (6 marks)**: GameCharacter (immutable) with varargs constructor
- **Task 3 (6 marks)**: Player managing character set
- **Task 4 (10 marks)**: chooseCharacters() - find minimal character set

### Key Points:
- Immutable class: final fields, no setters
- Constructor: `public GameCharacter(String name, int cost, Power... powers)`
- Return unmodifiable set: `Collections.unmodifiableSet()`
- Javadoc required for all members
- Recursive algorithm for chooseCharacters()

**Test**: `cd 2019 && javac superhero/*.java && java superhero.TestSuperhero`

---

## Common Patterns Across All Exams

### 1. Validation Pattern
```java
if (value < min || value > max) {
    throw new IllegalArgumentException("Descriptive message");
}
```

### 2. Enum with Helper
```java
public enum Type {
    VALUE1, VALUE2;

    public static Type fromString(String s) {
        if (s.equals("V1")) return VALUE1;
        return null;
    }
}
```

### 3. Override Methods
```java
@Override
public boolean equals(Object obj) {
    if (this == obj) return true;
    if (obj == null || getClass() != obj.getClass()) return false;
    ClassName other = (ClassName) obj;
    return field == other.field;
}

@Override
public int hashCode() {
    return Objects.hash(field1, field2);
}
```

### 4. Collections Usage
- **List**: Order matters, duplicates OK
- **Set**: No duplicates, no order
- **Map**: Key-value pairs

---

## 50-Minute Strategy for Any Exam

### Time Breakdown:
| Minutes | Task |
|---------|------|
| 0-5 | Read entire paper, understand requirements |
| 5-10 | Create package, enum classes |
| 10-25 | First major class (usually 6-8 marks) |
| 25-40 | Second major class (usually 8 marks) |
| 40-47 | Third task/class |
| 47-50 | Compile, fix errors, quick test |

### Priority Order:
1. **Easy marks first**: Enums, simple getters/setters
2. **Core classes**: Main data structures
3. **Complex logic last**: Algorithms, searches

### Speed Tips:
1. Copy package declaration to all files immediately
2. Write all method signatures before implementing
3. Use simple ArrayList/HashMap - don't overthink
4. Mental testing is faster than actual testing
5. Don't optimize - working code > elegant code

---

## Quick Reference Card

### Essential Imports:
```java
import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
import java.util.Map;
import java.util.HashSet;
import java.util.Set;
import java.util.Objects;
import java.util.Random;
import java.util.Collections;
```

### Common Operations:
```java
// String parsing
String[] lines = input.split("\n");
String[] parts = line.split(" ");
int num = Integer.valueOf(str);

// Collections
List<Type> list = new ArrayList<>();
Set<Type> set = new HashSet<>();
Map<K, V> map = new HashMap<>();

// Map with default
map.getOrDefault(key, 0);
map.put(key, value);

// Random
Random rand = new Random();
int num = rand.nextInt(5) + 1;  // 1 to 5
```

---

## Pre-Exam Checklist

### Knowledge Check:
- [ ] Can write enum types
- [ ] Know how to override equals/hashCode/toString
- [ ] Understand List, Set, Map differences
- [ ] Can validate with IllegalArgumentException
- [ ] Know string parsing with split()
- [ ] Understand constructors and getters/setters
- [ ] Can use Collections framework

### Practice Drill (30 minutes each):
1. Write 2022 solution from scratch
2. Write 2023 solution from scratch
3. Write one of 2019/2021/2024

### Day Before Exam:
- Review this summary document
- Run all test files to refresh memory
- Practice writing one complete solution in 45 minutes
- Get good sleep!

---

## Common Mistakes to Avoid

1. ❌ Forgetting package declaration
2. ❌ Wrong array indexing (0-based vs 1-based)
3. ❌ Not validating in constructor AND setters
4. ❌ Modifying fields without validation
5. ❌ Forgetting to check null/empty
6. ❌ Using wrong collection type
7. ❌ Not returning when using recursion
8. ❌ Spending too long on one task

---

## Exam Day Workflow

1. **Read entire paper** (5 min)
2. **Create package folder** and all .java files
3. **Add package declaration** to all files
4. **Start with enums** - easiest marks
5. **Build classes incrementally** - test mentally as you go
6. **Save frequently**
7. **Compile often** - catch errors early
8. **Don't get stuck** - move on and come back

Good luck! You've got this! 🎓
