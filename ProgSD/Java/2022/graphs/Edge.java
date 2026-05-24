package graphs;

import java.util.Objects;

/**
 * Edge class - represents a directed edge in a graph
 *
 * EXAM PATTERN: Simple data class representing relationship
 * TIME: 5-7 minutes
 * MARKS: 5
 *
 * Key concepts:
 * - Represents relationship between two objects
 * - Directed edge (start → end)
 * - Equals based on both endpoints
 * - No validation needed (exam specification)
 */
public class Edge {

    // Starting node of the edge
    private Node start;

    // Ending node of the edge
    private Node end;

    /**
     * Constructor - creates directed edge from start to end
     *
     * PATTERN: Relationship object
     * Represents: start → end
     *
     * Example: Edge(node1, node2) means edge from node 1 to node 2
     *
     * @param start Starting node
     * @param end Ending node
     */
    public Edge(Node start, Node end) {
        // No validation in exam specification
        // In real code, might check for null or self-loops
        this.start = start;
        this.end = end;
    }

    /**
     * Get starting node
     */
    public Node getStart() {
        return start;
    }

    /**
     * Get ending node
     */
    public Node getEnd() {
        return end;
    }

    /**
     * toString - display edge as (start, end)
     *
     * PATTERN: Tuple representation
     * Example: "(1, 2)" means edge from node 1 to node 2
     */
    @Override
    public String toString() {
        return "(" + start.getLabel() + ", " + end.getLabel() + ")";
    }

    /**
     * equals - edges are equal if both endpoints match
     *
     * PATTERN: Composite equality
     * Edge (1→2) equals Edge (1→2)
     * Edge (1→2) NOT equal to Edge (2→1) (because directed)
     */
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;

        Edge edge = (Edge) obj;

        // Both start AND end must match
        // Uses Objects.equals() which handles null safely
        return Objects.equals(start, edge.start) &&
               Objects.equals(end, edge.end);
    }

    /**
     * hashCode - must use SAME fields as equals
     *
     * RULE: If equals uses start and end, hashCode must also use both
     */
    @Override
    public int hashCode() {
        return Objects.hash(start, end);
    }
}
