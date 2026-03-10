import java.util.*;

class VaultDoorTraining {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
        
        if (userInput.equals("DNCC{w3lc0m3_t0_th3_v4ult_7r41n1ng}")) {
            System.out.println("Access Granted!");
        } else {
            System.out.println("Access Denied!");
        }
    }
}