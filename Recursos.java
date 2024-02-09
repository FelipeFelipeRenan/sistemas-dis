import java.rmi.Remote;
import java.rmi.RemoteException;
import java.util.List;

public interface Recursos extends Remote {
    void armazenarMensagem(String mensagem) throws RemoteException;
    List<String> obterMensagens() throws RemoteException;
    String obterIpServidor() throws RemoteException;
    String obterDataHoraServidor() throws RemoteException;
}
