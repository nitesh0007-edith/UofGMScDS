# Java Lab Exam Solutions (2019-2024)

## Quick Start Guide

All past paper solutions are complete, tested, and ready to use!

### Folder Structure
```
Java/
├── 2019/superhero/          ✅ Video Game Characters (24 marks)
├── 2021/trading/            ✅ Trading System (24 marks)
├── 2022/graphs/             ✅ Directed Graphs (25 marks)
├── 2023/boxOffice/          ✅ Theatre Booking (25 marks)
├── 2024/petcare/            ✅ Pet Care Service (40 marks)
├── ALL_SOLUTIONS_SUMMARY.md  📖 Complete guide with all code
├── EXAM_SOLUTIONS_GUIDE.md   📖 2022 & 2023 detailed solutions
├── QUICK_REFERENCE.md        📖 Quick tips and patterns
└── README.md                 📖 This file
```

---

## Testing Each Solution

### 2024 - Pet Care Service
```bash
cd /Users/niteshranjansingh/ProgSD/Java/2024
javac petcare/*.java
java petcare.TestPetService
```

### 2023 - Box Office
```bash
cd /Users/niteshranjansingh/ProgSD/Java/2023
javac boxOffice/*.java
java boxOffice.TestVenue
```

### 2022 - Graphs
```bash
cd /Users/niteshranjansingh/ProgSD/Java/2022
javac graphs/*.java
java graphs.TestGraph
```

### 2021 - Trading
```bash
cd /Users/niteshranjansingh/ProgSD/Java/2021
javac trading/*.java
java trading.TestTrading
```

### 2019 - Superheroes
```bash
cd /Users/niteshranjansingh/ProgSD/Java/2019
javac superhero/*.java
java superhero.TestSuperhero
```

---

## Exam Papers Summary

| Year | Topic | Package | Marks | Key Concepts |
|------|-------|---------|-------|--------------|
| 2024 | Pet Care Service | `petcare` | 40 | Classes, validation, collections, searching |
| 2023 | Box Office | `boxOffice` | 25 | Enums, 2D arrays, string parsing, adjacency |
| 2022 | Directed Graphs | `graphs` | 25 | Graph theory, adjacency lists, sets |
| 2021 | Trading System | `trading` | 24 | Maps, random, enums, game logic |
| 2019 | Video Game | `superhero` | 24 | Immutable classes, varargs, recursion |

---

## Your Syllabus Coverage

✅ **Primitive types, classes, arrays** - All exams
✅ **Class definitions, inheritance, constructors** - All exams
✅ **Enumerated types** - 2019, 2021, 2023, 2024
✅ **Packages and access modifiers** - All exams
✅ **Collections (List, Set, Map)** - All exams
✅ **Exception handling** - All exams

---

## Study Plan

### Week Before Exam:
1. **Day 1-2**: Read ALL_SOLUTIONS_SUMMARY.md thoroughly
2. **Day 3-4**: Practice 2022 and 2023 (covered in EXAM_SOLUTIONS_GUIDE.md)
3. **Day 5-6**: Practice 2021 and 2024
4. **Day 7**: Review QUICK_REFERENCE.md, rest well

### Day Before Exam:
- Review common patterns in QUICK_REFERENCE.md
- Run all test files to see working examples
- Practice one complete solution in 45 minutes
- Early sleep!

### Exam Day:
- Read entire paper first (5 min)
- Start with enums and simple classes
- Build incrementally, compile often
- Keep calm, you know this!

---

## Files You'll Submit in Exam

### Pattern Recognition:
Most exams require 3-4 .java files:
1. **Enum file** (if needed) - 2-3 minutes
2. **Main data class** - 15-20 minutes
3. **Container/Manager class** - 15-20 minutes
4. **Utility/Helper class** - 10-15 minutes

### Always Include:
- Package declaration at top
- Required imports
- Constructor with validation
- Getters (and setters if asked)
- Override equals/hashCode/toString when needed

---

## Quick Tips for 50 Minutes

1. **Read everything first** - Don't start coding immediately
2. **Create all files** - Add package declarations right away
3. **Start simple** - Enums and basic classes first
4. **Validate early** - Add all validation in constructors
5. **Test mentally** - Trace through examples in your head
6. **Compile often** - Catch errors as you go
7. **Don't optimize** - Simple working code is enough
8. **Leave hard parts** - Come back if time permits

---

## Key Concepts to Remember

### Collections Choice:
- Use **List** when: order matters, need indexing
- Use **Set** when: no duplicates needed
- Use **Map** when: key-value pairs (like inventory)

### Validation:
```java
if (invalid) {
    throw new IllegalArgumentException("message");
}
```

### String Parsing:
```java
String[] lines = input.split("\n");
String[] parts = line.split(" ");
int number = Integer.valueOf(str);
```

### Override Methods:
Always override equals/hashCode when:
- Objects will be in Set or Map
- Need to compare objects for equality

---

## Resources

📖 **ALL_SOLUTIONS_SUMMARY.md** - Master document with all 5 solutions
📖 **EXAM_SOLUTIONS_GUIDE.md** - Detailed 2022 & 2023 with timing
📖 **QUICK_REFERENCE.md** - Code snippets and patterns

---

## Good Luck! 🍀

You have:
- ✅ 5 complete, tested solutions
- ✅ All common patterns documented
- ✅ Time-management strategies
- ✅ Quick reference guides

**You're well prepared!** Practice a few times and you'll be confident on exam day.

Remember: **Simple, working code > Complex, perfect code**

---

*Last Updated: December 2024*
