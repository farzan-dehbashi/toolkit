package com.java_tutorial.Basics;

import java.util.Arrays;

public class ArrayTutorial {
    public static void run(){
        int[] array = new int[10];
        array[2] = 3;
        for (int element : array){
            System.out.println(element);
        }
        Arrays.sort(array);
        System.out.println(Arrays.toString(array));

        int[][] array_2d = {{1,2},{3,4}};
        System.out.println(Arrays.deepToString(array_2d));

    }
}
