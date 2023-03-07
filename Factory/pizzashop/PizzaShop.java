package pizzashop;

import Pizza.Pizza;
import PizzaStore.BerlinPizzaStore;
import PizzaStore.HamburgPizzaStore;
import PizzaStore.PizzaStore;
import PizzaStore.RostockPizzaStore;


public class PizzaShop {

    public static void main(String[] args) {
        PizzaStore Berlin = new BerlinPizzaStore();
        PizzaStore Hamburg = new HamburgPizzaStore();
        PizzaStore Rostock = new RostockPizzaStore();

        Pizza berlinerSalami = Berlin.orderPizza("Salami");
        System.out.println("Bestellt: " + berlinerSalami.getName());

        System.out.println("---------------------------------------------------");

        Pizza rostockerCalzone = Rostock.orderPizza("Calzone");
        System.out.println("Bestellt: " + rostockerCalzone.getName());

        System.out.println("---------------------------------------------------");

        Pizza hamaburgerHawaii = Hamburg.orderPizza("Hawaii");
        System.out.println("Bestellt: " + hamaburgerHawaii.getName());
    }

}
