import java.util.Scanner;
public class addiction{
    
    public static void main (String args[]){
        //establishes variables used in the model
        boolean male = false;
        int age;
        double gambleFrequency;

        //collects user values for variables
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Gender (M/F): ");
        String gender = sc.nextLine();
        if(gender.equals("M"))
        {
            male = true;
        }

        System.out.print("Age: ");
        String Age = sc.nextLine();
        age = Integer.parseInt(Age);

        System.out.print("Average #of times gambling per month: ");
        String Freq = sc.nextLine();
        gambleFrequency = Double.parseDouble(Freq);
    
        //calculates probability of a gambling problem based on age
        double ageProb = 0;
        if(18<= age && age <= 24)
            ageProb = 0.194;
        if(25 <= age && age <= 34)
            ageProb = 0.166;
        if(35 <= age && age<= 44)
            ageProb = 0.142;
        if(45 <= age && age<= 54)
            ageProb = 0.069;
        if(55 <= age && age<= 64)
            ageProb = 0.026;
        if(65 <= age)
            ageProb = 0.017;
        
        //calculates probability of a gambling problem based on gender
        double genderProb =0;
        if(male)
            genderProb = 0.116;
        if(!male)
            genderProb = 0.065;

        //calculates probability of high-risk gambling behvaiors based on gambling frequency
        double freqProb = 0;
        if(gambleFrequency < 1)
            freqProb = 0.059;
        if(1 <= gambleFrequency && gambleFrequency<= 3)
            freqProb = 0.141;
        if(3 < gambleFrequency)
            freqProb = 0.8;

        //calculates overall probability of developing a gambling problem based on provided
        //demographics
        double addictionProb;
       
        //probability that you develop a gambling problem due to your frequency or gender
        double freqGender;
        freqGender = freqProb + genderProb - (freqProb*genderProb);
        
        //probability w/ freqProb and age
        addictionProb = 100*(freqGender + ageProb - (freqGender*ageProb));
        addictionProb = (int)(addictionProb*100)/100.0;
        
        
        System.out.print("Probability of developing a gambling problem is: " + addictionProb + "%");

