package com.java_tutorial;

public class String_tutorial {
    public static void run(){
        String tmpString = "Hi my name is Farzan!";
        System.out.println(tmpString.length());
        System.out.println(tmpString.endsWith("!"));
        System.out.println(tmpString.indexOf("Far"));
        System.out.println(tmpString.replace("Farzan", "Ali"));
        System.out.println(tmpString.trim());
        System.out.println(tmpString.stripTrailing());
    }
}
