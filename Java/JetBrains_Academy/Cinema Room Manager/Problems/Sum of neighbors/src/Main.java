import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        ArrayList<String[]> matrix = new ArrayList<>();

        // input 받기
        do {
            matrix.add(input.split(" "));
            input = scanner.nextLine();
        } while (!input.equals("end"));

        // row, col 구하기
        int row = matrix.size();
        int col = matrix.get(0).length;

//        // 한 사이즈 더 큰 매트릭스 만들고 중심에 matrix 넣기
//        int[][] output = new int[row + 1][col + 1];
//        for (int i = 1; i < row + 1; i++) {
//            for (int j = 1; j < col + 1; j++) {
//                output[i][j] = Integer.parseInt(matrix.get(i - 1)[j - 1]);
//            }
//        }

        int[][] output = new int[row][col];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                int newNum = Integer.parseInt(matrix.get((i - 1 + row) % row)[j])
                        + Integer.parseInt(matrix.get((i + 1 + row) % row)[j])
                        + Integer.parseInt(matrix.get(i)[(j - 1 + col) % col])
                        + Integer.parseInt(matrix.get(i)[(j + 1 + col) % col]);
                output[i][j] = newNum;
            }
        }

        // print matrix
        for (int[] array : output) {
            for (int k : array) {
                System.out.print(k + " ");
            }
            System.out.println();
        }
    }
}