package Practice.petcare;
import java.util.ArrayList;
import java.util.List;


public class petservice {
    private List<Enclosure> enclosures;
    public petservice(){
        this.enclosures  = new ArrayList<>();
    }
    public void addEnclosure(Enclosure enclosure){
        enclosures.add(enclosure);
    }
    public void printAllEnclosures(){
        for(int i=0;i<enclosures.size();i++){
            Enclosure e = enclosures.get(i);
            System.out.println("Enclouser "+ (i+1)+": Size="+e.getSize() + ",Temp=" +e.getTemp() + "C" + ", Cost=" + e.getRunningCosts());
            if(e.getOccupant()!=null){
                System.out.println(", Occupant="+e.getOccupant());
            }
            else{
                System.out.println(", Empty");
            }
        }
    }
    public boolean allocateAnimal(animal animal){
        Enclosure bestEnclosure = null;
        int lowerCost = Integer.MAX_VALUE;
        
        for(Enclosure enclosure : enclosures){
            if(enclosure.getOccupant()==null && enclosure.checkCompatibility(animal)){
                if(enclosure.getRunningCosts()<lowerCost){
                    lowerCost=enclosure.getRunningCosts();
                    bestEnclosure = enclosure;
                }
            }
        }
        if(bestEnclosure!=null){
            bestEnclosure.addAnimal(animal);
            return true;
        }
        return false;
    }
    public void removeAnimal(animal animal){
        for(Enclosure enclosure : enclosures){
            if(enclosure.getOccupant()!=null && enclosure.getOccupant().equals(animal)){
                enclosure.removeAnimal();
                return;
            }
        }

        throw new IllegalArgumentException("Animal not found in any enclosure");
    }
}
