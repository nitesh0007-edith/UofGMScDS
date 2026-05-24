package graphs;

/**
 * GraphParser class - parses string specification into graph structure
 *
 * EXAM PATTERN: String parser / Factory method
 * TIME: 10-15 minutes
 * MARKS: 8
 *
 * Key concepts:
 * - String parsing with split()
 * - Integer conversion with Integer.valueOf()
 * - Array creation and population
 * - Creating relationships between objects
 */
public class GraphParser {

    /**
     * Parse a graph from string specification
     *
     * INPUT FORMAT:
     * Line 1: number of nodes
     * Line 2: number of edges
     * Lines 3+: edges as "from to" pairs
     *
     * EXAMPLE:
     * "3\n4\n1 2\n2 3\n3 2\n3 1"
     * Means: 3 nodes, 4 edges: (1→2), (2→3), (3→2), (3→1)
     *
     * OUTPUT: Array of Node objects with neighbors set up
     *
     * @param spec String specification of graph
     * @return Array of nodes (index 0 = node 1, index 1 = node 2, etc.)
     */
    public static Node[] parseGraph(String spec) {
        // STEP 1: Split input into lines
        // "\n" is newline character - splits at each line break
        String[] lines = spec.split("\n");

        // STEP 2: Parse metadata (first two lines)
        // Integer.valueOf() converts String to int
        // Example: "3" → 3
        int numNodes = Integer.valueOf(lines[0]);
        int numEdges = Integer.valueOf(lines[1]);

        // STEP 3: Create array of nodes
        // Important: nodes are numbered 1 to n, but array is 0-indexed!
        // So node with label 1 goes in nodes[0], label 2 in nodes[1], etc.
        Node[] nodes = new Node[numNodes];

        // Create each node with appropriate label
        for (int i = 0; i < numNodes; i++) {
            // Node label = array index + 1
            // i=0 → label 1, i=1 → label 2, etc.
            nodes[i] = new Node(i + 1);
        }

        // STEP 4: Parse edges and build adjacency list
        // Edges start at line 2 (index 2) and continue for numEdges lines
        for (int i = 2; i < 2 + numEdges; i++) {
            // Split edge line by space
            // Example: "1 2" → ["1", "2"]
            String[] edge = lines[i].split(" ");

            // Parse the two node labels
            int from = Integer.valueOf(edge[0]);  // Starting node
            int to = Integer.valueOf(edge[1]);    // Ending node

            // Add edge: from → to
            // REMEMBER: Node with label X is at index X-1
            // So node 1 is nodes[0], node 2 is nodes[1], etc.
            nodes[from - 1].addNeighbour(nodes[to - 1]);
        }

        // Return the complete graph as array of nodes
        return nodes;
    }
}
