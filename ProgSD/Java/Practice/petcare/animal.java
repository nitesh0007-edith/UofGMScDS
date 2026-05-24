package Practice.petcare;
import java.util.Objects;

public class animal {

    private String name;
    private animalsize size;
    private int minTemp; 
    private int maxTamp;
    // constructor
    public animal(String name, animalsize size, int minTemp, int maxTamp){
        // validation Rule
        if(name==null || name.length()<3){
            throw new IllegalArgumentException("Name must be at least 3 charactor long");
        }
        if(minTemp<0 || minTemp>50){
            throw new IllegalArgumentException("minTemp must be between 0-50");
        }
        if(maxTamp<0 || maxTamp>50){
            throw new IllegalArgumentException("maxTemp must be between 0-50");
        }
        if(minTemp>maxTamp){
            throw new IllegalArgumentException("MinTemp should be less then MaxTemp");
        }

        this.name = name;
        this.size = size;
        this.minTemp = minTemp;
        this.maxTamp = maxTamp;
    }

    // getter method
    public String getName(){
        return name;
    }
    // setter method
    public void setname(String name){
        if(name==null || name.length()<3){
            throw new IllegalArgumentException("Name must be at least 3 charactor long");
        }
        this.name = name;
    }

    public animalsize getSize(){
        return size;
    }
    public void setSize(animalsize size){
        this.size = size;
    }

    public int getminTemp(){
        return minTemp;
    }
    public void setminTemp(int minTemp){
        if(minTemp<0 || minTemp>50){
            throw new IllegalArgumentException("minTemp must be between 0-50");
        }
        if(minTemp>this.maxTamp){
            throw new IllegalArgumentException("MinTemp should be less then MaxTemp");
        }
        this.minTemp = minTemp;
    }

    public int getmaxTemp(){
        return maxTamp;
    }
    public void setmaxTemp(int maxTamp){
        if(maxTamp<0 || maxTamp>50){
            throw new IllegalArgumentException("maxTemp must be between 0-50");
        }
        if(this.minTemp>maxTamp){
            throw new IllegalArgumentException("Mintemp should be less then MaxTemp");
        }
        this.maxTamp = maxTamp;
    }

    @Override
    public String toString(){
        return name + " (" + size + ", " + minTemp + "-" + maxTamp + "C)";
    }

    @Override
    public boolean equals(Object obj){
        if (this == obj) return true;

        if(obj==null || getClass()!=obj.getClass()) return false;

        animal animal = (animal) obj;

        return size == animal.size && Objects.equals(name, animal.name);
    }

    @Override
    public int hashCode(){
        return Objects.hash(name,size);
    }
}
