package Wetterstation.PUSH;

public class Controller { 

    public static void main(String[] args) { 
        Zentrale zentrale = new Zentrale(); 
        zentrale.register(new Bildschirm1()); 
        zentrale.register(new Bildschirm2()); 

        zentrale.setState(16, 32); 
    } 
} 
