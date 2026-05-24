package petcare;

import java.util.ArrayList;
import java.util.List;

/**
 * PetService class - manages all enclosures and animal allocation
 *
 * EXAM PATTERN: Manager class with collection and "find best" logic
 * TIME: 15-18 minutes
 * MARKS: 15
 *
 * Key concepts demonstrated:
 * - Managing collection of containers (List<Enclosure>)
 * - Finding best match (cheapest compatible enclosure)
 * - Searching through collection to find/remove items
 * - Loop patterns for management operations
 */
public class PetService {
    // Collection of all enclosures managed by this pet service
    // ArrayList because: order doesn't matter, need to iterate through all
    private List<Enclosure> enclosures;

    /**
     * Constructor - creates an empty pet service
     *
     * IMPORTANT: Always initialize collections in constructor!
     * Don't leave them null or you'll get NullPointerException
     */
    public PetService() {
        this.enclosures = new ArrayList<>();  // Start with empty list
    }

    /**
     * Add an enclosure to the service
     *
     * Simple add - no validation needed (exam doesn't specify any)
     *
     * @param enclosure Enclosure to add to the service
     */
    public void addEnclosure(Enclosure enclosure) {
        enclosures.add(enclosure);
    }

    /**
     * Print details of all enclosures
     *
     * PATTERN: Loop through collection and display each item
     * This demonstrates how to access nested information (enclosure → occupant)
     */
    public void printAllEnclosures() {
        // Loop through all enclosures with index for numbering
        for (int i = 0; i < enclosures.size(); i++) {
            Enclosure e = enclosures.get(i);

            // Print enclosure details
            System.out.print("Enclosure " + (i + 1) + ": Size=" + e.getSize() +
                           ", Temp=" + e.getTemperature() + "°C" +
                           ", Cost=" + e.getRunningCosts());

            // Check if occupied and print occupant info
            // IMPORTANT: Always check for null before using object!
            if (e.getOccupant() != null) {
                System.out.println(", Occupant=" + e.getOccupant());
            } else {
                System.out.println(", Empty");
            }
        }
    }

    /**
     * Allocate an animal to the best available enclosure
     *
     * BEST = cheapest compatible empty enclosure
     *
     * ALGORITHM:
     * 1. Loop through all enclosures
     * 2. For each enclosure, check if it's:
     *    a) Empty (no occupant)
     *    b) Compatible with the animal
     * 3. Among compatible enclosures, pick the cheapest
     * 4. Add animal to that enclosure
     *
     * PATTERN: "Find minimum" algorithm
     *
     * @param animal Animal to allocate
     * @return true if allocated successfully, false if no suitable enclosure found
     */
    public boolean allocateAnimal(Animal animal) {
        // Variables to track the best enclosure found so far
        Enclosure bestEnclosure = null;
        int lowestCost = Integer.MAX_VALUE;  // Start with maximum value
        // Why MAX_VALUE? So first valid cost will be lower and replace it

        // STEP 1: Search for the best enclosure
        // Use enhanced for-loop - simpler when we don't need index
        for (Enclosure enclosure : enclosures) {

            // Is this enclosure a candidate?
            // 1. Must be empty
            // 2. Must be compatible with animal
            if (enclosure.getOccupant() == null && enclosure.checkCompatibility(animal)) {

                // Is this enclosure cheaper than current best?
                // PATTERN: Keep track of minimum value
                if (enclosure.getRunningCosts() < lowestCost) {
                    lowestCost = enclosure.getRunningCosts();
                    bestEnclosure = enclosure;
                }
            }
        }

        // STEP 2: Did we find a suitable enclosure?
        if (bestEnclosure != null) {
            // Yes! Add animal to the best enclosure we found
            bestEnclosure.addAnimal(animal);
            return true;
        }

        // No suitable enclosure found
        return false;
    }

    /**
     * Remove a specific animal from the service
     *
     * ALGORITHM:
     * 1. Search through all enclosures
     * 2. Check each enclosure's occupant
     * 3. When found, remove and return immediately
     * 4. If loop completes without finding, throw exception
     *
     * PATTERN: "Search and remove" algorithm
     *
     * @param animal Animal to remove
     * @throws IllegalArgumentException if animal not found in any enclosure
     */
    public void removeAnimal(Animal animal) {
        // Loop through all enclosures to find the animal
        for (Enclosure enclosure : enclosures) {

            // Check if this enclosure has an occupant
            // AND if that occupant matches our animal
            // IMPORTANT: Check != null first to avoid NullPointerException!
            if (enclosure.getOccupant() != null && enclosure.getOccupant().equals(animal)) {
                // Found it! Remove and exit immediately
                enclosure.removeAnimal();
                return;  // Exit method - animal removed successfully
            }
        }

        // If we reach here, we've searched all enclosures and didn't find the animal
        throw new IllegalArgumentException("Animal not found in any enclosure");
    }
}
