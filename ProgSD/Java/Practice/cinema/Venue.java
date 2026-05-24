package Practice.cinema;
import java.util.*;

public class Venue {
    private List<List<Seat>> rows;
    public Venue(String config){
        rows = new ArrayList<>();

        String[] lines = config.split("\n");
        int numRows = Integer.valueOf(lines[0]);

        for(int i =0;i<numRows;i++){
            String[] seatTypes = lines[i+1].split(" ");
            List<Seat> row = new ArrayList<>();
            char rowLetter = (char) ('A'+i);

            for(int j =0;j<seatTypes.length;j++){
                SeatType type = SeatType.fromString(seatTypes[j]);
                Seat seat = new Seat(rowLetter, j+1, type);
                row.add(seat);
            }
            rows.add(row);
        }
    }

    public Seat getSeat(char row, int seatNum){

        if(row<'A'|| row>='A'+rows.size()){
            throw new IllegalArgumentException("Invalid row : "+ row);
        }
        int rowIndex = row - 'A';
        List<Seat> rowSeats = rows.get(rowIndex);

        if(seatNum <=0 || seatNum>rowSeats.size()){
            throw new IllegalArgumentException("Invalide Seat number : "+seatNum);
        }

        return rowSeats.get(seatNum-1);
    }

    public void printDetails(){
        for(int i=0;i<rows.size();i++){
            char rowLetter = (char)('A'+i);
            System.out.println("Row "+ rowLetter + ": ");

            for(Seat seat : rows.get(i)){
                String availability = seat.getisAvailable() ? "Available" : "Reserved";
                String type = seat.getSeatType()== SeatType.STANDARD? "Standard":"Deluxe";

                System.out.print("Seat " + seat.getSeatNumber() +
                               " (" + type + ", " + availability + ") ");
            }
            System.out.println();
        }
    }

    public int getRowCount(){
        return rows.size();
    }

    public int getSeatsInRow(char row){
        int rowIndex = row - 'A';
        if(rowIndex<0||rowIndex>=rows.size()){
            return 0;
        }
        return rows.get(rowIndex).size();
    }

    public int countAvailableSeats(){
        int count = 0;
        for(List<Seat> row:rows){
        for(Seat seat :  row){ 
            if(seat.getisAvailable()){
                count++;
            }
        }
    }
    return count;
    }
}


