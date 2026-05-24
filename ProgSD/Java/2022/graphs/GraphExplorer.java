package graphs;

import java.util.HashSet;
import java.util.Set;

/**
 * GraphExplorer class - utility methods for exploring graph structure
 *
 * EXAM PATTERN: Static utility class with graph traversal
 * TIME: 8-10 minutes
 * MARKS: 7
 *
 * Key concepts:
 * - Static methods (no instance needed)
 * - Graph traversal using adjacency lists
 * - Converting adjacency list to edge set
 * - Using Set to avoid duplicates
 * - Nested loop pattern
 */
public class GraphExplorer {

    /**
     * List all edges in the graph
     *
     * ALGORITHM:
     * 1. Create empty set of edges
     * 2. For each node in the graph:
     *    a. For each neighbour of that node:
     *       b. Create edge (node → neighbour)
     *       c. Add to set
     * 3. Return set of all edges
     *
     * PATTERN: Convert adjacency list representation to edge set
     *
     * WHY USE SET?
     * - Automatically prevents duplicate edges
     * - Edge's equals() method ensures no duplicates
     *
     * TIME COMPLEXITY: O(V + E) where V = vertices, E = edges
     * - Visit each node once
     * - Visit each edge once
     *
     * @param nodes Array of all nodes in the graph
     * @return Set of all directed edges in the graph
     */
    public static Set<Edge> listEdges(Node[] nodes) {
        // Create set to store edges
        // HashSet for O(1) add and automatic duplicate removal
        Set<Edge> edges = new HashSet<>();

        // OUTER LOOP: Visit each node in the graph
        for (Node node : nodes) {

            // INNER LOOP: Visit each neighbour of current node
            // This gives us all outgoing edges from this node
            for (Node neighbour : node.getNeighbours()) {

                // Create edge from current node to neighbour
                // This represents: node → neighbour
                Edge edge = new Edge(node, neighbour);

                // Add to set
                // If duplicate (shouldn't happen in well-formed graph), set ignores it
                edges.add(edge);
            }
        }

        // Return complete set of edges
        return edges;
    }

    /**
     * Additional graph exploration methods could include:
     *
     * - Count total edges: return edges.size()
     * - Find nodes with no outgoing edges (sinks)
     * - Find nodes with no incoming edges (sources)
     * - Detect cycles using DFS
     * - Find path between two nodes
     *
     * This exam only required listEdges, but these patterns are common!
     */
}
