package cinema;
import java.util.*;

public class Cinema {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter the number of rows:");
        int n = scanner.nextInt();
        System.out.println("Enter the number of seats in each row:");
        int m = scanner.nextInt();

        System.out.println("Cinema:");
        System.out.print("  ");
        for (int col = 0; col < m; col++) {
            System.out.print((col + 1) + " ");
        }
        System.out.println();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m + 1; j++) {
                System.out.print((j == 0 ? i + 1 : "S") + " ");
            }
            System.out.println();
        }

        System.out.println("Enter a row number:");
        int row = scanner.nextInt();
        System.out.println("Enter a seat number in that row:");
        int seat = scanner.nextInt();

        int ticketPrice;
        if (n * m <= 60) {
            ticketPrice = 10;
        } else {
            int front = n / 2;
            ticketPrice = (row <= front) ? 10 : 8;
        }

        System.out.println("Ticket price: $" + ticketPrice);
        System.out.println();
        System.out.println("Cinema:");
        System.out.println("  1 2 3 4 5 6 7 8 9");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m + 1; j++) {
                if (i + 1 == row && j == seat) {
                    System.out.print("B" + " ");
                } else {
                    System.out.print((j == 0 ? i + 1 : "S") + " ");
                }
            }
            System.out.println();
        }

    }
}