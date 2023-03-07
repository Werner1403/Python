package PizzaStore;

import Pizza.Pizza;
import Pizza.Hamburg.HamburgSalamiPizza;
import Pizza.Hamburg.HamburgCalzonePizza;
import Pizza.Hamburg.HamburgHawaiiPizza;
import Pizza.Hamburg.HamburgQuattroStagioniPizza;


public class HamburgPizzaStore extends PizzaStore {

    @Override
    Pizza createPizza(String type) {
        if (type.equals("Salami")) {
            return new HamburgSalamiPizza();
        } else if (type.equals("Calzone")) {
            return new HamburgCalzonePizza();
        } else if (type.equals("Hawaii")) {
            return new HamburgHawaiiPizza();
        } else if (type.equals("Stagioni")){
            return new HamburgQuattroStagioniPizza();
        } else {
            return null;
        }
    }
}
