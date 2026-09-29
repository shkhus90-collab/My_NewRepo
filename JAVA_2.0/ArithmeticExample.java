public class ArithmeticExample {
    public static void main(String[] args){
        
        try{
            int a=5;
            int b=0;
            int result =(a/b);
            System.out.println("The Result is: " +result);
        }
        catch(ArithmeticException e){
            System.out.println("ERROR: Cannot divide by zero!! ");
            System.out.println("RollNo:SCS2627052");
        }
        
    }

}
