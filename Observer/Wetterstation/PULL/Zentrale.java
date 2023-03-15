package Wetterstation.PULL;

public class Zentrale extends Subject { 

    private int temperature; 
    private int humidity;

    public void setState(int temp, int hum) { 
        this.temperature = temp;
        this.humidity = hum; 
        notifyObservers(); 
    } 

    public int getTemp() { 
        return temperature; 
    } 

    public int getHum() { 
        return humidity; 
    } 

} 