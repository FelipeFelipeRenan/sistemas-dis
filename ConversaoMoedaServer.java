package teste;

import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class ConversaoMoedaServer extends UnicastRemoteObject implements ConversaoMoedaService {
    private static final double TAXA_CONVERSAO_EURO_REAL = 6.30; // Exemplo de taxa de conversão Euro para Real
    private static final double TAXA_CONVERSAO_DOLAR_REAL = 5.20; // Exemplo de taxa de conversão Dolar para Real

    public ConversaoMoedaServer() throws RemoteException {
        super();
    }

    @Override
    public double euroParaReal(double valorEmEuro) throws RemoteException {
        return valorEmEuro * TAXA_CONVERSAO_EURO_REAL;
    }

    @Override
    public double realParaEuro(double valorEmReal) throws RemoteException {
        return valorEmReal / TAXA_CONVERSAO_EURO_REAL;
    }

    @Override
    public double dolarParaReal(double valorEmDolar) throws RemoteException {
        return valorEmDolar * TAXA_CONVERSAO_DOLAR_REAL;
    }

    @Override
    public double realParaDolar(double valorEmReal) throws RemoteException {
        return valorEmReal / TAXA_CONVERSAO_DOLAR_REAL;
    }

    public static void main(String[] args) {
        try {
            ConversaoMoedaServer server = new ConversaoMoedaServer();
            System.out.println("ConversaoMoedaServer está em execução...");
            Naming.rebind("rmi://127.0.0.1:11099/ConversaoMoedaService", server);
        } catch (Exception e) {
            System.out.println("Trouble: " + e);
        }
    }
}
