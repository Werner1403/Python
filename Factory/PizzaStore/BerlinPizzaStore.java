package PizzaStore;

import Pizza.Pizza;
import Pizza.Berlin.BerlinQuattroStagioniPizza;
import Pizza.Berlin.BerlinSalamiPizza;
import Pizza.Berlin.BerlinCalzonePizza;
import Pizza.Berlin.BerlinHawaiiPizza;


public class BerlinPizzaStore extends PizzaStore{

    @Override
    Pizza createPizza(String type) {
        if (type.equals("Salami")) {
            return new BerlinSalamiPizza();
        } else if (type.equals("Calzone")) {
            return new BerlinCalzonePizza();
        } else if (type.equals("Hawaii")) {
            return new BerlinHawaiiPizza();
        } else if (type.equals("Stagioni")){
            return new BerlinQuattroStagioniPizza();
        } else {
            return null;
        }
    }

}
