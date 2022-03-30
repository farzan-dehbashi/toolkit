package com.codewithmosh.command.editor;

public interface UndoableCommand extends Command {
  void unexecute();
}
