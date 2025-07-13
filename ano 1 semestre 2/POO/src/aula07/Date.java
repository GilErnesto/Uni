package aula07;

public abstract class Date {
    protected int day;
    protected int month;
    protected int year;

    public static boolean validMonth(int month){
        if(0<month && month<13){return true;}
        else return false;
    }
    public static boolean isLeapYear(int year){
        if(year%100==0){return year%400==0;}
        else return year%4==0;
        }
    public static int monthDays(int month, int year){
        switch(month){
            case 1: case 3: case 5: case 7: case 8: case 10: case 12: return 31;
            case 4: case 6: case 9: case 11: return 30;
            case 2: return (isLeapYear(year)) ? 29 : 28;
            default:
                return 0;
        }
        }
    public static boolean valid(int day, int month, int year){
        if (!validMonth(month) || day<1 || day>monthDays(month, year)){return false;}
        else return true;
        }
        public void setDate(int day, int month, int year){
            if (!valid(day, month, year)){
                throw new IllegalArgumentException("Data Inválida");
            }
            this.day = day;
            this.month = month;
            this.year = year;
        }
        public int getDay(){
            return day;
        }
        public int getMonth(){
            return month;
        }
        public int getYear(){
            return year;
        }
        public String toString(){
            return String.format("%04d-%02d-%02d", year, month, day);
        }

}
