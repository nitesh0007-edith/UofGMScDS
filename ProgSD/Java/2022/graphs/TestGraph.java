package graphs;

import java.util.Set;

public class TestGraph {
    public static void main(String[] args) {
        // Test the sample graph from the exam
        String spec = "3\n4\n1 2\n2 3\n3 2\n3 1";

        Node[] nodes = GraphParser.parseGraph(spec);

        System.out.println("Graph parsed successfully!");
        System.out.println("Number of nodes: " + nodes.length);

        for (Node node : nodes) {
            System.out.print("Node " + node.getLabel() + " -> ");
            for (Node neighbour : node.getNeighbours()) {
                System.out.print(neighbour.getLabel() + " ");
            }
            System.out.println();
        }

        Set<Edge> edges = GraphExplorer.listEdges(nodes);
        System.out.println("\nEdges in graph:");
        for (Edge edge : edges) {
            System.out.println(edge);
        }
    }
}
