package Wetterstation.PUSH;

public class Bildschirm1 implements Observer { 

    public Bildschirm1(Zentrale zentrale){
        zentrale.register(this);
    }

    public void update(int temp, int hum) { 
        System.out.println("Bildschirm 1 is updated with: Temperature: " + temp + " Humidity: " + hum + "%"); 
    } 
} 
