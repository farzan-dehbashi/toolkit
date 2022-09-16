package com.java_tutorial.ExceptionTutorial;

import java.io.FileNotFoundException;
import java.io.FileReader;

public class tryCatch {
    public static void run() {
        try {
            var fileReader = new FileReader("hi.py");
        } catch (FileNotFoundException e) {
            throw new IllegalArgumentException("Arguments are nonsence! ");
        }
    }




}
