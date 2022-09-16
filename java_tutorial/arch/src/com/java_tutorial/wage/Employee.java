package com.java_tutorial.wage;

public class Employee {

    private int baseWage;
    private int hourlyWage;

    private static int numberOfEmployees;

    public Employee(int baseWage){
        this(baseWage, 0);
    }
    public Employee(int baseWage, int hourlyWage){
        this.setBaseWage(baseWage);
        this.setHourlyWage(hourlyWage);
        numberOfEmployees ++;
    }

    public static int getNumberOfEmployees() {
        return numberOfEmployees;
    }

    public int getBaseWage() {
        return baseWage;
    }

    public void setBaseWage(int baseWage) {
        if (baseWage > 0){
            this.baseWage = baseWage;
        }
        else throw new IllegalArgumentException("Salary cannot be less than or equal to zero");
    }

    public int getHourlyWage() {
        return hourlyWage;
    }

    public void setHourlyWage(int hourlyWage) {
        this.hourlyWage = hourlyWage;
    }

    public int calculateWage(int extraHours){
        return baseWage + (hourlyWage * extraHours);
    }
    public int calculateWage(){
        return baseWage;
    }
}
