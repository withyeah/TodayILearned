import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        String[] inputArray = scanner.nextLine().split(" ");
        int len = inputArray.length;
        String[] outputArray = new String[len];
        int shift = scanner.nextInt();
        
        for (int i = 0; i < len; i++) {
            outputArray[(i + shift) % len] = inputArray[i];
        }

        for (String j : outputArray) {
            System.out.print(j + " ");
        }
    }
}
