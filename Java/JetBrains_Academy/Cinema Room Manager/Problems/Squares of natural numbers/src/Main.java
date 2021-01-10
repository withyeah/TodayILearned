import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long N = scanner.nextLong();
        long M = 1;
        while (M * M <= N) {
            System.out.println(M * M);
            M++;
        }
    }
}
