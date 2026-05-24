package superhero;

import java.util.Set;

public class TestSuperhero {
    public static void main(String[] args) {
        System.out.println("=== Testing Superhero System ===\n");

        // Create characters
        GameCharacter robin = new GameCharacter("Robin", 100, Power.WEAPONS);
        GameCharacter starfire = new GameCharacter("Starfire", 200, Power.FLIGHT, Power.ENERGY_BLAST);
        GameCharacter cyborg = new GameCharacter("Cyborg", 250, Power.STRENGTH, Power.WEAPONS);
        GameCharacter beastBoy = new GameCharacter("Beast Boy", 150, Power.TRANSFORMATION);
        GameCharacter raven = new GameCharacter("Raven", 300, Power.MAGIC);

        System.out.println("Created characters:");
        System.out.println(robin);
        System.out.println(starfire);
        System.out.println(cyborg);
        System.out.println(beastBoy);
        System.out.println(raven);

        // Create player
        Player player = new Player();
        player.addCharacter(robin);
        player.addCharacter(starfire);
        player.addCharacter(cyborg);
        player.addCharacter(beastBoy);
        player.addCharacter(raven);

        System.out.println("\nPlayer has " + player.getCharacters().size() + " characters");

        // Test 1: Weapons and Strength
        System.out.println("\n=== Test 1: Weapons and Strength ===");
        Set<GameCharacter> result1 = player.chooseCharacters(Power.WEAPONS, Power.STRENGTH);
        if (result1 != null) {
            System.out.println("Characters needed:");
            for (GameCharacter c : result1) {
                System.out.println("  " + c.getName());
            }
        } else {
            System.out.println("Cannot complete level");
        }

        // Test 2: Flight, Strength, and Transformation
        System.out.println("\n=== Test 2: Flight, Strength, and Transformation ===");
        Set<GameCharacter> result2 = player.chooseCharacters(Power.FLIGHT, Power.STRENGTH, Power.TRANSFORMATION);
        if (result2 != null) {
            System.out.println("Characters needed:");
            for (GameCharacter c : result2) {
                System.out.println("  " + c.getName());
            }
        } else {
            System.out.println("Cannot complete level");
        }

        // Test 3: Transformation, Magic, and Science
        System.out.println("\n=== Test 3: Transformation, Magic, and Science ===");
        Set<GameCharacter> result3 = player.chooseCharacters(Power.TRANSFORMATION, Power.MAGIC, Power.SCIENCE);
        if (result3 != null) {
            System.out.println("Characters needed:");
            for (GameCharacter c : result3) {
                System.out.println("  " + c.getName());
            }
        } else {
            System.out.println("Cannot complete level (missing Science power)");
        }
    }
}
