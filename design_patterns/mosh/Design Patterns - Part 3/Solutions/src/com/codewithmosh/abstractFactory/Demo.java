package com.codewithmosh.abstractFactory;

public class Demo {
    public static void show() {
        var homePage = new HomePage();
        homePage.setGoal(new WeightLossFactory());
    }
}
