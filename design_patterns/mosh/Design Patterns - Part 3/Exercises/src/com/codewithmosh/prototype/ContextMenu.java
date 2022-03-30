package com.codewithmosh.prototype;

public class ContextMenu {
    private Timeline timeline;

    public ContextMenu(Timeline timeline) {
        this.timeline = timeline;
    }

    public void duplicate(Component component) {
        if (component instanceof Text) {
            Text source = (Text)component;
            Text target = new Text(source.getContent());
            timeline.add(target);
        }
        else if (component instanceof Audio) {
            // Logic for duplicating an Audio object
        }
        else if (component instanceof Clip) {
            // Logic for duplicating a Clip object
        }
    }
}
