package com.java_tutorial.wage;

public class MainModule {
    public static void run() {
        var employee = new Employee(50_000, 20);
        int wage = employee.calculateWage(10);
        System.out.println(wage);
        System.out.println(Employee.getNumberOfEmployees());
    }
}
