package teste;

import java.rmi.Naming;
import java.rmi.RemoteException;
import java.util.Scanner;

public class ConversaoMoedaClient {
    private static ConversaoMoedaService conversaoMoedaService = null;

    public static void main(String[] args) {
        try {
            conversaoMoedaService = (ConversaoMoedaService) Naming.lookup("rmi://127.0.0.1:11099/ConversaoMoedaService");
            
            Scanner scanner = new Scanner(System.in);
            System.out.print("Digite o valor em Euro para converter para Real: ");
            double valorEmEuro = scanner.nextDouble();
            double valorConvertido = conversaoMoedaService.euroParaReal(valorEmEuro);
            System.out.println("Valor convertido para Real: " + valorConvertido);
            scanner.close();
            // Repita o processo para as outras conversões conforme necessário

        } catch (Exception e) {
            System.out.println("Trouble: " + e);
        }
    }
}
