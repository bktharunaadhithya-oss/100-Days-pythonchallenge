
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);

        int n = t.nextInt();
        int l[] = new int[n];

        for (int i = 0; i < n; i++) {
            l[i] = t.nextInt();
        }

        int m = 0;
        int c = 0;
        int h[] = new int[n];

        for (int i = n - 1; i >= 0; i--) {
            if (l[i] > m) {
                h[c] = i;
                c++;
                m = l[i];
            }
        }

        if (c == 0) {
            System.out.println(-1);
        } else {
            for (int i = c - 1; i >= 0; i--) {
                System.out.print(h[i] + " ");
            }
            System.out.println();
        }
    }
}
