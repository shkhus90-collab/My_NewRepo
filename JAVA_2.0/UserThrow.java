public class UserThrow {
     public static void main(String[] args) {
        int age=16;
        try{
            if (age<18){
                throw new Exception("Error: You are not Eligible for vote!! your age must be more than or equal to 18!! ");
            }
            System.out.println("Eligible for vote!! ");
        }
        catch(Exception e){
            System.out.println(e.getMessage());
System.out.println("RollNo:SCS2627052");
        }
    }

}
