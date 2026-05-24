# Java Exam Solutions - 50 Minute Strategy

## 2022 Exam: Directed Graphs (25 marks)
**Package**: `graphs`
**Time allocation**: 12-13 min per class, 50 min total

### Task 2a: Node.java (6 marks) - 12 minutes
```java
package graphs;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class Node {
    private int label;
    private List<Node> neighbours;

    public Node(int label) {
        this.label = label;
        this.neighbours = new ArrayList<>();
    }

    public void addNeighbour(Node node) {
        neighbours.add(node);
    }

    public List<Node> getNeighbours() {
        return neighbours;
    }

    public int getLabel() {
        return label;
    }

    @Override
    public String toString() {
        return String.valueOf(label);
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Node node = (Node) obj;
        return label == node.label;
    }

    @Override
    public int hashCode() {
        return Objects.hash(label);
    }
}
```

### Task 2b: GraphParser.java (8 marks) - 15 minutes
```java
package graphs;

public class GraphParser {
    public static Node[] parseGraph(String spec) {
        String[] lines = spec.split("\n");
        int numNodes = Integer.valueOf(lines[0]);
        int numEdges = Integer.valueOf(lines[1]);

        Node[] nodes = new Node[numNodes];
        for (int i = 0; i < numNodes; i++) {
            nodes[i] = new Node(i + 1);
        }

        for (int i = 2; i < 2 + numEdges; i++) {
            String[] edge = lines[i].split(" ");
            int from = Integer.valueOf(edge[0]);
            int to = Integer.valueOf(edge[1]);
            nodes[from - 1].addNeighbour(nodes[to - 1]);
        }

        return nodes;
    }
}
```

### Task 2c: Edge.java (5 marks) - 10 minutes
```java
package graphs;
import java.util.Objects;

public class Edge {
    private Node start;
    private Node end;

    public Edge(Node start, Node end) {
        this.start = start;
        this.end = end;
    }

    @Override
    public String toString() {
        return "(" + start.getLabel() + ", " + end.getLabel() + ")";
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Edge edge = (Edge) obj;
        return Objects.equals(start, edge.start) && Objects.equals(end, edge.end);
    }

    @Override
    public int hashCode() {
        return Objects.hash(start, end);
    }
}
```

### Task 2d: GraphExplorer.java (5 marks) - 10 minutes
```java
package graphs;
import java.util.HashSet;
import java.util.Set;

public class GraphExplorer {
    public static Set<Edge> listEdges(Node[] nodes) {
        Set<Edge> edges = new HashSet<>();
        for (Node node : nodes) {
            for (Node neighbour : node.getNeighbours()) {
                edges.add(new Edge(node, neighbour));
            }
        }
        return edges;
    }
}
```

---

## 2023 Exam: Box Office/Theatre Booking (25 marks)
**Package**: `boxOffice`
**Time allocation**: 15-17 min per task, 50 min total

### Task 2a: Seat.java & SeatType.java (8 marks) - 15 minutes

**SeatType.java**:
```java
package boxOffice;

public enum SeatType {
    STANDARD,
    DELUXE;

    public static SeatType fromString(String s) {
        if (s.equals("S")) return STANDARD;
        if (s.equals("D")) return DELUXE;
        return null;
    }
}
```

**Seat.java**:
```java
package boxOffice;

public class Seat {
    private char row;
    private int seatNumber;
    private SeatType seatType;
    private boolean isAvailable;

    public Seat(char row, int seatNumber, SeatType seatType) {
        if (row < 'A' || row > 'Z') {
            throw new IllegalArgumentException("Row must be between A and Z");
        }
        if (seatNumber <= 0) {
            throw new IllegalArgumentException("Seat number must be positive");
        }
        this.row = row;
        this.seatNumber = seatNumber;
        this.seatType = seatType;
        this.isAvailable = true;
    }

    public char getRow() { return row; }
    public int getSeatNumber() { return seatNumber; }
    public SeatType getSeatType() { return seatType; }
    public boolean isAvailable() { return isAvailable; }
    public void setAvailable(boolean available) { isAvailable = available; }
}
```

### Task 2b: Venue.java (8 marks) - 17 minutes
```java
package boxOffice;
import java.util.ArrayList;
import java.util.List;

public class Venue {
    private List<List<Seat>> rows;

    public Venue(String config) {
        rows = new ArrayList<>();
        String[] lines = config.split("\n");
        int numRows = Integer.valueOf(lines[0]);

        for (int i = 0; i < numRows; i++) {
            String[] seatTypes = lines[i + 1].split(" ");
            List<Seat> row = new ArrayList<>();
            char rowLetter = (char) ('A' + i);

            for (int j = 0; j < seatTypes.length; j++) {
                SeatType type = SeatType.fromString(seatTypes[j]);
                row.add(new Seat(rowLetter, j + 1, type));
            }
            rows.add(row);
        }
    }

    public Seat getSeat(char row, int seatNum) {
        if (row < 'A' || row >= 'A' + rows.size()) {
            throw new IllegalArgumentException("Invalid row: " + row);
        }
        int rowIndex = row - 'A';
        List<Seat> rowSeats = rows.get(rowIndex);

        if (seatNum <= 0 || seatNum > rowSeats.size()) {
            throw new IllegalArgumentException("Invalid seat number: " + seatNum);
        }
        return rowSeats.get(seatNum - 1);
    }

    public void printDetails() {
        for (int i = 0; i < rows.size(); i++) {
            char rowLetter = (char) ('A' + i);
            System.out.print("Row " + rowLetter + ": ");
            for (Seat seat : rows.get(i)) {
                String availability = seat.isAvailable() ? "Available" : "Reserved";
                String type = seat.getSeatType() == SeatType.STANDARD ? "Standard" : "Deluxe";
                System.out.print("Seat " + seat.getSeatNumber() + " (" + type + ", " + availability + ") ");
            }
            System.out.println();
        }
    }
}
```

### Task 2c: Event.java (8 marks) - 18 minutes
```java
package boxOffice;
import java.util.HashMap;
import java.util.Map;

public class Event {
    private Venue venue;
    private Map<SeatType, Integer> prices;

    public Event(Venue venue, int standardPrice, int deluxePrice) {
        this.venue = venue;
        this.prices = new HashMap<>();
        prices.put(SeatType.STANDARD, standardPrice);
        prices.put(SeatType.DELUXE, deluxePrice);
    }

    public int reserveSeats(int numSeats, SeatType seatType) {
        for (char row = 'A'; row <= 'Z'; row++) {
            try {
                for (int startSeat = 1; startSeat <= 26; startSeat++) {
                    boolean found = true;
                    for (int i = 0; i < numSeats; i++) {
                        try {
                            Seat seat = venue.getSeat(row, startSeat + i);
                            if (!seat.isAvailable() || seat.getSeatType() != seatType) {
                                found = false;
                                break;
                            }
                        } catch (IllegalArgumentException e) {
                            found = false;
                            break;
                        }
                    }
                    if (found) {
                        for (int i = 0; i < numSeats; i++) {
                            venue.getSeat(row, startSeat + i).setAvailable(false);
                        }
                        return numSeats * prices.get(seatType);
                    }
                }
            } catch (IllegalArgumentException e) {
                break;
            }
        }
        return -1;
    }

    public void returnSeat(char row, int seatNum) {
        Seat seat = venue.getSeat(row, seatNum);
        if (seat.isAvailable()) {
            throw new IllegalArgumentException("Seat is already available");
        }
        seat.setAvailable(true);
    }
}
```

---

## Key Speed Tips for 50-Minute Exam:

1. **Import only what you need**: `ArrayList`, `List`, `HashMap`, `Map`, `HashSet`, `Set`, `Objects`

2. **Common patterns to memorize**:
   - String parsing: `split("\n")`, `split(" ")`, `Integer.valueOf()`
   - Override methods: `equals()`, `hashCode()`, `toString()`
   - Collections: `ArrayList<>()`, `HashSet<>()`, `HashMap<>()`

3. **Time management**:
   - Read all tasks: 5 min
   - Code: 40 min
   - Compile & quick test: 5 min

4. **Validation strategy**:
   - Always check bounds before array/list access
   - Use `IllegalArgumentException` for validation errors
   - Test edge cases in your mind before coding

5. **Don't overthink**: Use simple, direct solutions. No fancy algorithms needed.
