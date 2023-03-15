

import java.util.Observable;

public class ConcreteSubject extends Observable { //Seit Java 9 deprecated

    public ConcreteSubject(){
        setState(0);
    }
    
    public void setState(Object arg){
        if(countObservers()>0){
            setChanged();
            notifyObservers(arg);
        }
    }

} 