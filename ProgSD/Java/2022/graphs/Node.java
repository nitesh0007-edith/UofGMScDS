package graphs;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

/**
 * Node class - represents a vertex in a directed graph
 *
 * EXAM PATTERN: Data class with self-referential collection
 * TIME: 10-12 minutes
 * MARKS: 8
 *
 * Key concepts:
 * - Graph node with adjacency list
 * - Collection of same type (Node contains List<Node>)
 * - Unique identifier (label)
 * - Building relationships between objects
 */
public class Node {

    // Unique identifier for this node
    private int label;

    // Adjacency list - nodes that this node points to
    // In directed graph: if node A has node B in neighbours, then A → B
    // PATTERN: Self-referential - Node contains collection of Nodes
    private List<Node> neighbours;

    /**
     * Constructor - creates node with given label
     *
     * @param label Unique identifier for this node (e.g., 1, 2, 3)
     */
    public Node(int label) {
        this.label = label;

        // IMPORTANT: Initialize collection in constructor
        // Start with empty list - neighbours will be added later
        this.neighbours = new ArrayList<>();
    }

    /**
     * Add outgoing edge from this node to another node
     *
     * PATTERN: Add to adjacency list (building graph relationships)
     *
     * Example: If node1.addNeighbour(node2), then there's an edge 1 → 2
     *
     * @param node The node to add as neighbour (destination of edge)
     */
    public void addNeighbour(Node node) {
        // Simply add to list - no validation needed for this exam
        // In real applications, might check for duplicates or null
        neighbours.add(node);
    }

    /**
     * Get all neighbours (nodes this node points to)
     *
     * PATTERN: Getter for collection
     * Used for graph traversal algorithms
     *
     * @return List of neighbouring nodes
     */
    public List<Node> getNeighbours() {
        return neighbours;
    }

    /**
     * Get node's label
     *
     * @return The unique identifier for this node
     */
    public int getLabel() {
        return label;
    }

    /**
     * toString for display
     *
     * PATTERN: Simple representation - just show label
     * Makes debugging easier
     */
    @Override
    public String toString() {
        return String.valueOf(label);
    }

    /**
     * equals - nodes are equal if they have same label
     *
     * PATTERN: Identity by unique identifier
     * Two nodes with same label are considered the same node
     */
    @Override
    public boolean equals(Object obj) {
        // Standard equals pattern
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;

        Node node = (Node) obj;

        // Compare by label (unique identifier)
        return label == node.label;
    }

    /**
     * hashCode - must use same field as equals
     *
     * RULE: If equals() uses label, hashCode() must also use label
     */
    @Override
    public int hashCode() {
        return Objects.hash(label);
    }
}
