public class NumberFormatExample {
     public static void main(String[] args) {
        try{
            String s = "123ABS";
            int number = Integer.parseInt(s);
            System.out.println("Number is: " +number);
} 
        catch(NumberFormatException e){
        System.out.println("Invalid Number Format!! ");
        System.out.println("RollNo:SCS2627052");
        }      
    }
}

