import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] a = new int[n];
        int[] freq = new int[n];

        for (int i = 0; i < n; i++)
            a[i] = sc.nextInt();

        // Count frequency
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (a[i] == a[j])
                    freq[i]++;
            }
        }

        // Sort by frequency, then by value
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (freq[i] < freq[j] ||
                   (freq[i] == freq[j] && a[i] > a[j])) {

                    int temp = a[i];
                    a[i] = a[j];
                    a[j] = temp;

                    temp = freq[i];
                    freq[i] = freq[j];
                    freq[j] = temp;
                }
            }
        }

        for (int i = 0; i < n; i++)
            System.out.print(a[i] + " ");
    }
}

