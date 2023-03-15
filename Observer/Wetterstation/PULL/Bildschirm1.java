package Wetterstation.PULL;

public class Bildschirm1 implements Observer { 

    private int temperature;
    private int humidity;
    private Zentrale zentrale;

    public Bildschirm1(Zentrale zentrale){
        this.zentrale = zentrale;
        zentrale.register(this);
    }

    public void update() { 
        this.temperature = zentrale.getTemp();
        this.humidity = zentrale.getHum();
        System.out.println("Bildschirm 1 is updated with: Temperature: " + temperature + " Humidity: " + humidity + "%");
    }

} 
