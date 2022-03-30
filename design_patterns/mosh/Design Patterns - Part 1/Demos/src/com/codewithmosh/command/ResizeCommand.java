package com.codewithmosh.command;

import com.codewithmosh.command.fx.Command;

public class ResizeCommand implements Command {
  @Override
  public void execute() {
    System.out.println("Resize");
  }
}
