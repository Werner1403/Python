import java.util.Observable;
import java.util.Observer;

public class ConcreteObserverC implements Observer { 

    @Override
    public void update(Observable o, Object arg) {
        // TODO Auto-generated method stub
        System.out.println("ObserverC: "+arg);
    } 
} 

