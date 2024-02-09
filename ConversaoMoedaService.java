package teste;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface ConversaoMoedaService extends Remote {
    double euroParaReal(double valorEmEuro) throws RemoteException;
    double realParaEuro(double valorEmReal) throws RemoteException;
    double dolarParaReal(double valorEmDolar) throws RemoteException;
    double realParaDolar(double valorEmReal) throws RemoteException;
}
