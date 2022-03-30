package com.codewithmosh.command;

import com.codewithmosh.command.fx.Command;

public class BlackAndWhiteCommand implements Command {
  @Override
  public void execute() {
    System.out.println("Black and white");
  }
}
