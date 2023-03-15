

import java.util.Observable;
import java.util.Observer;

public class ConcreteObserverA implements Observer { 

    @Override
    public void update(Observable o, Object arg) {
        // TODO Auto-generated method stub
        System.out.println("ObserverA: "+arg);
    } 
} 
