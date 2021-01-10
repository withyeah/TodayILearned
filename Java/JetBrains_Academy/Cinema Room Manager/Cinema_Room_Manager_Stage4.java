package cinema;

import java.util.*;

public class Cinema {

    public static int n;
    public static int m;
    public static String[][] seats;

    public static void main(String[] args) {
        /*
        Program starts:
         - Ask for number of rows,
         - Ask for number of seats per row,
         -- Main loop (This loop must loop forever until user decides to exit):
          |  - Print the main menu with number choices,
          |  -- Use a switch statement to handle the user choice:
          |   |  - Case 1: Print the seats information like in the example.
          |   |  - Case 2: Ask for row, ask for seat, reserve the seat.
          |   |  - Case 0: Break out of the loop.
          |  -- End of Switch (Note that if the user doesn't choose zero, the loop will repeat again.
         -- End of the loop (Will repeat if user didn't press zero)
        Program ends.
         */
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter the number of rows:");
        n = scanner.nextInt();
        System.out.println("Enter the number of seats in each row:");
        m = scanner.nextInt();

        seats = initSeats(n, m);
        boolean flag = true;

        while (flag) {
            // show menu
            System.out.println("1. Show the seats");
            System.out.println("2. Buy a ticket");
            System.out.println("0. Exit");

            int chosenMenu = scanner.nextInt();
            switch (chosenMenu) {
                case 1:
                    showSeats(seats);
                    break;
                case 2:
                    buyTicket();
                    break;
                case 0:
                    flag = false;
                    break;
            }
        }
    }

    public static String[][] initSeats(int n, int m) {
        String[][] seats = new String[n + 1][m + 1];
        // seats index
        seats[0][0] = " ";
        for (int i = 1; i < m + 1; i++) {
            seats[0][i] = Integer.toString(i);
        }
        // rows index
        for (int j = 1; j < n + 1; j++) {
            seats[j][0] = Integer.toString(j);
            for (int k = 1; k < m + 1; k++) {
                seats[j][k] = "S";
            }
        }
        return seats;
    }

    public static void showSeats(String[][] seats) {
        System.out.println("Cinema:");
        for (String[] array : seats) {
            for (String seat : array) {
                System.out.print(seat + " ");
            }
            System.out.println();
        }
    }

    public static void buyTicket() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a row number:");
        int selectedRow = scanner.nextInt();
        System.out.println("Enter a seat number in that row:");
        int selectedSeat = scanner.nextInt();

        int ticketPrice = getTicketPrice(selectedRow);
        System.out.println("Ticket price: $" + ticketPrice);

        seats[selectedRow][selectedSeat] = "B";
    }

    public static int getTicketPrice(int row) {
        int ticketPrice;
        if (n * m <= 60) {
            ticketPrice = 10;
        } else {
            int front = n / 2;
            ticketPrice = (row <= front) ? 10 : 8;
        }
        return ticketPrice;
    }
}