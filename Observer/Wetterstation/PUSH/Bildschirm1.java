package Wetterstation.PUSH;

public class Bildschirm1 implements Observer { 

    public void update(int temp, int hum) { 
        System.out.println("Bildschirm 1 is updated with: Temperature: " + temp + " Humidity: " + hum + "%"); 
        //ggf. Modifikationen mit setState(). 
    } 
} 
