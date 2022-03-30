package com.codewithmosh.prototype;

public class Demo {
    public static void show() {
        var timeline = new Timeline();
        var text = new Text("Hello");
        timeline.add(text);

        var menu = new ContextMenu(timeline);
        menu.duplicate(text);
    }
}
