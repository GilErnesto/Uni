package aula07;

public class DateND extends Date {
    private int distance;
    public DateND(DateYMD date){
        int daysdistance = date.getDay()-1;
        int yeardays= 0;
        int monthdays= 0;

        for(int i=2000; i<=date.getYear()-1; i++){
            if(Date.isLeapYear(i)){
                yeardays+=366;
    
            }
            else{yeardays+=365;}
        }
        for(int i=1; i<=date.getMonth()-1; i++){
            monthdays+= Date.monthDays(i, date.getYear());
        }
        this.distance= yeardays+monthdays+daysdistance;

        
    }
    @Override
    public String toString(){
        return Integer.toString(distance);
    }

}
