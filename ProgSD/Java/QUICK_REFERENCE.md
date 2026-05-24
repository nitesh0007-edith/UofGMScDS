# Java Exam Quick Reference Card

## Essential Imports (Copy-Paste Ready)
```java
import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
import java.util.Map;
import java.util.HashSet;
import java.util.Set;
import java.util.Objects;
```

## Common Code Snippets

### 1. String Parsing
```java
String[] lines = input.split("\n");      // Split by newline
String[] parts = line.split(" ");        // Split by space
int num = Integer.valueOf(str);          // String to int
```

### 2. Override Methods Template
```java
@Override
public String toString() {
    return "value";
}

@Override
public boolean equals(Object obj) {
    if (this == obj) return true;
    if (obj == null || getClass() != obj.getClass()) return false;
    ClassName other = (ClassName) obj;
    return field == other.field;  // or Objects.equals(field, other.field)
}

@Override
public int hashCode() {
    return Objects.hash(field1, field2);
}
```

### 3. Collections Initialization
```java
List<Type> list = new ArrayList<>();
Set<Type> set = new HashSet<>();
Map<KeyType, ValueType> map = new HashMap<>();
```

### 4. Validation Pattern
```java
if (value < min || value > max) {
    throw new IllegalArgumentException("Descriptive message");
}
```

### 5. Enum with Helper Method
```java
public enum SeatType {
    TYPE1, TYPE2;

    public static SeatType fromString(String s) {
        if (s.equals("T1")) return TYPE1;
        if (s.equals("T2")) return TYPE2;
        return null;
    }
}
```

### 6. Loop Through Array/List
```java
// Array
for (Type item : array) {
    // process item
}

// List
for (Type item : list) {
    // process item
}

// With index
for (int i = 0; i < array.length; i++) {
    Type item = array[i];
}
```

### 7. Character Arithmetic
```java
char letter = 'A';
char nextLetter = (char) ('A' + 1);  // 'B'
int index = letter - 'A';             // 0 for 'A', 1 for 'B', etc.
```

### 8. Try-Catch for Validation
```java
try {
    // attempt operation
} catch (IllegalArgumentException e) {
    // handle or continue
}
```

## Exam Pattern Recognition

### Type 1: Graph/Tree Structure
- **Classes needed**: Node, Parser, Edge, Explorer
- **Key concepts**: Adjacency list, neighbors, traversal
- **Collections**: `List<Node>`, `Set<Edge>`

### Type 2: Booking/Reservation System
- **Classes needed**: Item (Seat), Container (Venue), Manager (Event)
- **Key concepts**: Validation, state management (available/reserved)
- **Collections**: `List<List<Item>>`, `Map<Type, Price>`

## 50-Minute Strategy

| Time | Activity |
|------|----------|
| 0-5 min | Read all tasks, understand requirements |
| 5-15 min | Task 1 (usually 6-8 marks) |
| 15-30 min | Task 2 (usually 8 marks) |
| 30-45 min | Task 3 (usually 8-9 marks) |
| 45-50 min | Quick compile test, fix errors |

## Common Mistakes to Avoid

1. ❌ Forgetting package declaration
2. ❌ Wrong array indexing (0-based vs 1-based)
3. ❌ Not validating input in constructors
4. ❌ Forgetting to override equals/hashCode when needed
5. ❌ Using println in methods (unless asked for output)
6. ❌ Overthinking - keep it simple!

## Quick Validation Checklist

- [ ] Package name correct?
- [ ] Class name matches filename?
- [ ] All required methods implemented?
- [ ] Validation in constructors?
- [ ] equals/hashCode overridden (when comparing objects)?
- [ ] toString overridden (when specified)?
- [ ] Correct return types?
- [ ] Correct access modifiers (public/private)?

## Mental Checklist Before Submitting

1. Does it compile? (Most important!)
2. Does it handle the example from the question?
3. Are edge cases handled (empty, null, invalid)?
4. Are variable names clear and descriptive?
5. Is the code readable?

## Time-Saving Tips

1. **Copy-paste** the package declaration to all files first
2. **Write class skeleton** with all method signatures before implementing
3. **Use descriptive names** - helps you think clearly
4. **Test mentally** - trace through example in your head
5. **Don't optimize** - simple working code > elegant code

Good luck! 🍀
