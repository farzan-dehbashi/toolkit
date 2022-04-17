package com.java_tutorial.InheritanceTutorial;

public class TextBox extends UIControl{
    private String text;

    public TextBox() {
        super(true);
        System.out.println("textbox");
    }

    public void setText(String text) {
        this.text = text;
    }

    public void clear(){
        this.text = "";
    }
}
