import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] guestList = {
            scanner.next(),
            scanner.next(),
            scanner.next(),
            scanner.next(),
            scanner.next(),
            scanner.next(),
            scanner.next(),
            scanner.next(),
        };
        for(int i=7;i>=0;i--){  
            System.out.println(guestList[i]); 
        };
    }
}
