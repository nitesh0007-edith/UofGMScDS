package bigdata.util;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.time.Instant;

import bigdata.objects.Asset;
import bigdata.objects.AssetRanking;

/**
 * Utility class to export results in JSON format for visualization
 */
public class ResultsExporter {

    /**
     * Export AssetRanking to JSON file for visualization dashboard
     *
     * @param ranking The final ranking to export
     * @param executionTimeSeconds Total execution time in seconds
     * @param resultsDIR Directory to save the JSON file
     */
    public static void exportToJSON(AssetRanking ranking, long executionTimeSeconds, String resultsDIR) {
        try {
            File dir = new File(resultsDIR);
            if (!dir.exists()) {
                dir.mkdirs();
            }

            BufferedWriter writer = new BufferedWriter(new FileWriter(new File(resultsDIR + "/results.json")));

            StringBuilder json = new StringBuilder();
            json.append("{\n");
            json.append("  \"timestamp\": \"").append(Instant.now().toString()).append("\",\n");
            json.append("  \"executionTime\": ").append(executionTimeSeconds).append(",\n");
            json.append("  \"topInvestments\": [\n");

            Asset[] assets = ranking.getAssetRanking();
            for (int i = 0; i < assets.length; i++) {
                Asset a = assets[i];

                if (a == null) {
                    continue;
                }

                json.append("    {\n");
                json.append("      \"rank\": ").append(i + 1).append(",\n");
                json.append("      \"ticker\": \"").append(escapeJSON(a.getTicker())).append("\",\n");
                json.append("      \"name\": \"").append(escapeJSON(a.getName())).append("\",\n");
                json.append("      \"industry\": \"").append(escapeJSON(a.getIndustry())).append("\",\n");
                json.append("      \"sector\": \"").append(escapeJSON(a.getSector())).append("\",\n");
                json.append("      \"returns\": ").append(a.getFeatures().getAssetReturn()).append(",\n");
                json.append("      \"volatility\": ").append(a.getFeatures().getAssetVolitility()).append(",\n");
                json.append("      \"peRatio\": ").append(a.getFeatures().getPeRatio()).append("\n");
                json.append("    }");

                if (i < assets.length - 1 && assets[i + 1] != null) {
                    json.append(",");
                }
                json.append("\n");
            }

            json.append("  ]\n");
            json.append("}\n");

            writer.write(json.toString());
            writer.close();

            System.out.println("Results exported to: " + resultsDIR + "/results.json");

        } catch (IOException e) {
            System.err.println("Error exporting results to JSON: " + e.getMessage());
            e.printStackTrace();
        }
    }

    /**
     * Escape special characters in JSON strings
     */
    private static String escapeJSON(String str) {
        if (str == null) return "";
        return str.replace("\\", "\\\\")
                  .replace("\"", "\\\"")
                  .replace("\n", "\\n")
                  .replace("\r", "\\r")
                  .replace("\t", "\\t");
    }
}
