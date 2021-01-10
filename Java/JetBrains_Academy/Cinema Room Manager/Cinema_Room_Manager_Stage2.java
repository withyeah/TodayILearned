package cinema;
import java.util.Scanner;

public class Cinema {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Enter the number of rows:");
        int n = scanner.nextInt();
        System.out.println("Enter the number of seats in each row:");
        int m = scanner.nextInt();
        if (n * m <= 60) {
            System.out.println("Total income:");
            System.out.print("$");
            System.out.println(n * m * 10);
        } else {
            int front = n / 2;
            int back = n - front;
            System.out.println("Total income:");
            System.out.print("$");
            System.out.println(front * m * 10 + back * m * 8);
        }
    }
}