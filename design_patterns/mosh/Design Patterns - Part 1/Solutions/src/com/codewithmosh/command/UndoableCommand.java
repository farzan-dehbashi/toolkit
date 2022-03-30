package com.codewithmosh.command;

public interface UndoableCommand extends Command {
    void undo();
}
