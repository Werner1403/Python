package Python.Observer.LibraryExample;

public class Client { 

    public static void main(String[] args) { 
        ConcreteSubject s = new ConcreteSubject();
        
        s.setState(1);

        ConcreteObserverA a = new ConcreteObserverA();
        ConcreteObserverB b = new ConcreteObserverB();
        ConcreteObserverC c = new ConcreteObserverC();

        s.addObserver(a);
        s.setState(2);

        System.out.println("-----------------------");

        s.addObserver(b);
        s.setState(3);

        System.out.println("-----------------------");

        s.addObserver(c);
        s.setState(4);

        System.out.println("-----------------------");

        s.deleteObserver(a);
        s.setState(5);
        
    } 
} 
