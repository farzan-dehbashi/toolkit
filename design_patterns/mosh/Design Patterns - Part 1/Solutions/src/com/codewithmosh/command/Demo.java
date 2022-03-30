package com.codewithmosh.command;

public class Demo {
    public static void show() {
        var videoEditor = new VideoEditor();
        var history = new History();

        var setTextCommand = new SetTextCommand("Video Title", videoEditor, history);
        setTextCommand.execute();
        System.out.println("TEXT: " + videoEditor);

        var setContrast = new SetContrastCommand(1, videoEditor, history);
        setContrast.execute();
        System.out.println("CONTRAST: " + videoEditor);

        var undoCommand = new UndoCommand(history);
        undoCommand.execute();
        System.out.println("UNDO: " + videoEditor);

        undoCommand.execute();
        System.out.println("UNDO: " + videoEditor);

        undoCommand.execute();
        System.out.println("UNDO: " + videoEditor);
    }
}
