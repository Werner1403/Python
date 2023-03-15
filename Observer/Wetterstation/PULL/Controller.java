package Wetterstation.PULL;

public class Controller { 

    public static void main(String[] args) { 
        Zentrale zentrale = new Zentrale(); 
        
        Bildschirm1 b1 = new Bildschirm1(zentrale);
        Bildschirm2 b2 = new Bildschirm2(zentrale);

        zentrale.setState(16, 32); 
    } 
} 
