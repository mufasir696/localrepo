import java.util.*;
public class comp{
    public static void main(String[]args){
        Scanner cin=new Scanner(System.in);
        System.out.print("Enter the Number");
        int num=cin.nextInt();
        int sumev=0,sumodd=0;
        // while(num!=0){
        //     int nums=num%10;
        //     sum+=nums;
        //     num/=10;
        // }
        //   System.out.println(sum);
        // while(num!=0){
        //     int rem=num%10;
        //     if(rem%2==0){
        //     sumev+=1;
        //     }
        //     else{
        //         sumodd+=1;
        //     }
        //     num/=10;
        // }
        // System.out.print("Even"+sumev);
        // System.out.print("Odd"+sumodd);
    while(num!=0){
        int rem=num%10;
        System.out.print(rem);
        num/=10;
    }
    int original=num;
    int rev=0;
    while(num!=0){
        int rem=num%10;
        rev =rev*10+rem;
        num/=10;
    }
    if(rev==original){
        System.out.print("plaindrom");
            
        }
        else{
           System.out.println("no it is palindrome");
        }
        int c=0;
    while(num!=0){
        int dig=num%10;
        c++;
        num/=10;
    }
    System.out.print("Count of Digit"+c);
    }


}