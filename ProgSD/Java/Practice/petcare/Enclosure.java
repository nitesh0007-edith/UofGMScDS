package Practice.petcare;


public class Enclosure {
    private animalsize size;
    private int temp;
    private int runningCosts;
    private animal occupant;

    public Enclosure(animalsize size, int temp, int runningCosts){
        this.size = size;
        this.temp = temp;
        this.runningCosts = runningCosts;
        this.occupant = null;
    }

    public animalsize getSize(){
        return size;
    }
    public int getTemp(){
        return temp;
    }
    public int getRunningCosts(){
        return runningCosts;
    }
    public animal getOccupant(){
        return occupant;
    }

    public boolean checkCompatibility(animal animal){
        if(animal.getSize()==animalsize.LARGE && size!=animalsize.LARGE){
            return false;
        }
        if(animal.getSize()==animalsize.MEDIUM && size==animalsize.SMALL){
            return false;
        }
        if(temp<animal.getminTemp() || temp > animal.getmaxTemp()){
            return false;
        }
        return true;
    }

    public void addAnimal(animal animal){
        if(occupant!=null){
            throw new IllegalArgumentException("Enclosure already has an occupant");
        }
        if(!checkCompatibility(animal)){
            throw new IllegalArgumentException("Animal is not compatible with this enclosure");
        }
        occupant = animal;
    }
    public void removeAnimal(){
        occupant = null;
    }
}
