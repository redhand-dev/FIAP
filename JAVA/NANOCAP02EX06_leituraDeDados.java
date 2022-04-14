import java.util.Scanner;

public class NANOCAP02EX06_leituraDeDados {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int idade = sc.nextInt();
        System.out.println("Idade digitada: " + idade);
        sc.close();
    }
}