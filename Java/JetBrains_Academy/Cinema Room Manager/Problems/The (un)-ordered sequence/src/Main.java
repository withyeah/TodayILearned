import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        boolean asc = true;
        boolean desc = true;
        
        int value = scanner.nextInt();
        int next = scanner.nextInt();
        
        while (next != 0) {
            if (value > next) {
                asc = false;
            } else if (value < next) {
                desc = false;
            }
            value = next;
            next = scanner.nextInt();
        }
        
        System.out.println(asc || desc);

    }
}
