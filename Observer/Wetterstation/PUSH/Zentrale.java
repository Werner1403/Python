package Wetterstation.PUSH;

public class Zentrale extends Subject { 

    private int temperature; 
    private int humidity;

    public void setState(int temp, int hum) { 
        this.temperature = temp;
        this.humidity = hum; 
        //Wenn das Subject die Aktualisierung selbst durchführen soll, 
        //alternativ kann die Methode auch vom Client aufgerufen werden. 
        notifyObservers(temp, hum); 
    } 

    public String getState() { 
        return "temp: " + temperature + "humidity: " + humidity; 
    } 

} 