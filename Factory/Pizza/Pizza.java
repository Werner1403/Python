package Pizza;

import java.util.ArrayList;


public abstract class Pizza {

    public String name;
    public ArrayList<String> toppings = new ArrayList<>();

    public void prepare() {
        System.out.println("Vorbereitung von " + name + " ...");
        System.out.println("Toppings: ");
        for (String topping : toppings) {
            System.out.println("  " + topping);
        }
    }

    public void backen() {
        System.out.println("backen");
    }

    public void schneiden() {
        System.out.println("schneiden");
    }

    public void einpacken() {
        System.out.println("einpacken");
    }

    public String getName() {
        return name;
    }
}
