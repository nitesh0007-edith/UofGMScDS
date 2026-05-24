package petcare;

public class TestPetService {
    public static void main(String[] args) {
        System.out.println("=== Testing Pet Care Service ===\n");

        // Create animals
        Animal dog = new Animal("Buddy", AnimalSize.MEDIUM, 15, 25);
        Animal cat = new Animal("Whiskers", AnimalSize.SMALL, 18, 28);
        Animal elephant = new Animal("Dumbo", AnimalSize.LARGE, 20, 35);

        System.out.println("Created animals:");
        System.out.println(dog);
        System.out.println(cat);
        System.out.println(elephant);

        // Create enclosures
        Enclosure enc1 = new Enclosure(AnimalSize.SMALL, 20, 50);
        Enclosure enc2 = new Enclosure(AnimalSize.MEDIUM, 20, 100);
        Enclosure enc3 = new Enclosure(AnimalSize.LARGE, 25, 200);

        // Create pet service
        PetService service = new PetService();
        service.addEnclosure(enc1);
        service.addEnclosure(enc2);
        service.addEnclosure(enc3);

        System.out.println("\n=== Initial Enclosures ===");
        service.printAllEnclosures();

        // Allocate animals
        System.out.println("\n=== Allocating Animals ===");
        boolean allocated1 = service.allocateAnimal(cat);
        System.out.println("Cat allocated: " + allocated1);

        boolean allocated2 = service.allocateAnimal(dog);
        System.out.println("Dog allocated: " + allocated2);

        boolean allocated3 = service.allocateAnimal(elephant);
        System.out.println("Elephant allocated: " + allocated3);

        System.out.println("\n=== After Allocation ===");
        service.printAllEnclosures();

        // Remove animal
        System.out.println("\n=== Removing Cat ===");
        service.removeAnimal(cat);

        System.out.println("\n=== After Removal ===");
        service.printAllEnclosures();
    }
}
