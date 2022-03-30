package com.codewithmosh.template;

public class Window {
    // The close method is defining a template. Custom window classes
    // can use this template and determine what should happen before and
    // after a window is closed.
    public void close() {
        onClosing();

        System.out.println("Removing the window from the screen");

        onClosed();
    }

    protected void onClosing() {}
    protected void onClosed() {}
}
