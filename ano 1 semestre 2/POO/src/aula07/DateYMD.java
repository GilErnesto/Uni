package aula07;

public class DateYMD extends Date{

    public DateYMD(int day, int month, int year){
        super();
        if (!valid(day, month, year)){
            throw new IllegalArgumentException("Data Inválida");
        }
        setDate(day, month, year);
    }
    public void increment(){
        if(this.day<monthDays(this.month, this.year)){this.day++;}
        else{
            this.day=1;
            if(this.month<12){this.month++;}
            else{
                this.month=1;
                this.year++;
            }

        }

    }
    public void decrement(){
        if(this.day>1){this.day--;}
        else{
            if(this.month==1){this.month=12; this.year--; this.day=monthDays(this.month, this.year);}
            else{this.month--; this.day=monthDays(this.month, this.year);}
        }

    }

}
