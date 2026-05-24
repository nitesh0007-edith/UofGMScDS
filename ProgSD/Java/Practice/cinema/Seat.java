package Practice.cinema;

public class Seat {

    private char row;
    private int seatNumber;
    private SeatType seatType;
    private boolean isAvailable;
    
    public Seat(char row, int seatNum, SeatType seatType) {
        
        if( row < 'A' || row > 'Z'){
            throw new IllegalArgumentException("Row must be between A and Z");
        }

        if(seatNumber<=0){
            throw new IllegalArgumentException("Seat Must be Positive");
        }

        this.row = row;
        this.seatNumber = seatNumber;
        this.seatType = seatType;
        this.isAvailable = true;
    }

    public char getRow(){
        return row;
    }
    public int getSeatNumber(){
        return seatNumber;
    }
    public SeatType getSeatType(){
        return seatType;
    }
    public boolean getisAvailable(){
        return isAvailable;
    }
    public void setAvailable(boolean available){
        isAvailable = available;
    }

}
