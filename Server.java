import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class Server extends UnicastRemoteObject implements Recursos {
    private List<String> mensagens = new ArrayList<>();
    
    public Server() throws RemoteException {
        super();
    }

    @Override
    public void armazenarMensagem(String mensagem) throws RemoteException {
        mensagens.add(mensagem);
    }

    @Override
    public List<String> obterMensagens() throws RemoteException {
        return mensagens;
    }

    @Override
    public String obterIpServidor() throws RemoteException {
        return "IP do servidor: 127.0.0.1";
    }

    @Override
    public String obterDataHoraServidor() throws RemoteException {
        Date dataHoraAtual = new Date();
        return dataHoraAtual.toString(); // Você pode formatar a data/hora conforme necessário
    }

    public static void main(String[] args) {
        try {
            CalculadoraServer server = new CalculadoraServer();
            System.out.println("CalculadoraServer está em execução...");
            Naming.rebind("rmi://127.0.0.1:11099/MensagensService", server);
        } catch (Exception e) {
            System.out.println("Trouble: " + e);
        }
    }
}
