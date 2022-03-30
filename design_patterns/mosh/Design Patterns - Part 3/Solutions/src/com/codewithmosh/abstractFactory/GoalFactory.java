package com.codewithmosh.abstractFactory;

public interface GoalFactory {
    WorkoutPlan createWorkoutPlan();
    MealPlan createMealPlan();
}
