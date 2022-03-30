package com.codewithmosh.abstractFactory;

public class HomePage {
    private WorkoutPlan workoutPlan;
    private MealPlan mealPlan;

    public void setGoal(Goal goal) {
        if (goal == Goal.BUILD_MUSCLE) {
            workoutPlan = new BuildMuscleWorkout();
            mealPlan = new BuildMuscleMealPlan();
        }
        else if (goal == Goal.WEIGHT_LOSS) {
            workoutPlan = new WeightLossWorkout();
            mealPlan = new WeighLossMealPlan();
        }
        System.out.println(workoutPlan);
        System.out.println(mealPlan);

    }
}
