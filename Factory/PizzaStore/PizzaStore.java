package PizzaStore;

import Pizza.Pizza;


public abstract class PizzaStore {

    public Pizza orderPizza(String type) {
        Pizza pizza = createPizza(type);

        pizza.prepare();
        pizza.backen();
        pizza.schneiden();
        pizza.einpacken();

        return pizza;
    }

    abstract Pizza createPizza(String type);
}
