package Wetterstation.PUSH;

public class Bildschirm2 implements Observer { 

    public Bildschirm2(Zentrale zentrale){
        zentrale.register(this);
    }

    public void update(int temp, int hum) { 
        System.out.println("Bildschirm 2 is updated with: Temperature: " + temp + " Humidity: " + hum + "%"); 
    } 
} 
