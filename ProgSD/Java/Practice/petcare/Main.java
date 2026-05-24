package Practice.petcare;
public class Main {
    public static void main(String[] args) {
        // craete animals

        animal dog = new animal("kutta", animalsize.MEDIUM, 15, 25);
        animal cat = new animal("billy", animalsize.SMALL, 18, 25);
        animal elephant = new animal("hathy", animalsize.LARGE, 20, 35);

        System.out.println(dog);
        System.out.println(cat);
        System.out.println(elephant);

        Enclosure enc1 = new Enclosure(animalsize.SMALL, 20, 50);
        Enclosure enc2 = new Enclosure(animalsize.MEDIUM, 20, 100);
        Enclosure enc3 = new Enclosure(animalsize.LARGE, 25, 200);

        petservice service = new petservice();
        service.addEnclosure(enc1);
        service.addEnclosure(enc2);
        service.addEnclosure(enc3);

        service.printAllEnclosures();

        boolean allocated1 = service.allocateAnimal(cat);
        System.out.println("Cat allocated: " + allocated1);

        boolean allocated2 = service.allocateAnimal(dog);
        System.out.println("dog allocated: " + allocated2);

        boolean allocated3 = service.allocateAnimal(elephant);
        System.out.println("elephant allocated: " + allocated3);

        service.printAllEnclosures();

        service.removeAnimal(cat);

        service.printAllEnclosures();
    }
}
