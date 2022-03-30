package com.codewithmosh.abstractFactory;

public class HomePage {
    private WorkoutPlan workoutPlan;
    private MealPlan mealPlan;

    public void setGoal(GoalFactory goalFactory) {
        workoutPlan = goalFactory.createWorkoutPlan();
        mealPlan = goalFactory.createMealPlan();

        System.out.println(workoutPlan);
        System.out.println(mealPlan);
    }
}
