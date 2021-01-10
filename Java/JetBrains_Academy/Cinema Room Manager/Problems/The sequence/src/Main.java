import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int ncount = 0;
        int m = 1;
        int mcount = 0;

        while (ncount < n) {
            for (;mcount<=m;mcount++) {
                if (ncount == n) {
                    break;
                }
                if (mcount == m) {
                    m++;
                    mcount = 0;
                }
                ncount++;
                System.out.print(m + " ");
            }
        }
//        int count = 0;
//
//        for (int i=1;i<=n;i++) {
//            for (int j=1;j<=i;j++) {
//                if (count == n) {
//                    break;
//                } else {
//                    System.out.print(i + " ");
//                    count++;
//                }
//            }
//            if (count == n) {
//                break;
//            }
//        }
    }
}