package PizzaStore;

import Pizza.Pizza;
import Pizza.Rostock.RostockSalamiPizza;
import Pizza.Rostock.RostockQuattroStagioniPizza;
import Pizza.Rostock.RostockCalzonePizza;
import Pizza.Rostock.RostockHawaiiPizza;


public class RostockPizzaStore extends PizzaStore {

    @Override
    Pizza createPizza(String type) {
        if (type.equals("Salami")) {
            return new RostockSalamiPizza();
        } else if (type.equals("Calzone")) {
            return new RostockCalzonePizza();
        } else if (type.equals("Hawaii")) {
            return new RostockHawaiiPizza();
        } else if (type.equals("Stagioni")) {
            return new RostockQuattroStagioniPizza();
        } else {
            return null;
        }
    }
}
