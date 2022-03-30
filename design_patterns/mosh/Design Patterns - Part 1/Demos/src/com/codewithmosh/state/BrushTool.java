package com.codewithmosh.state;

public class BrushTool implements Tool {
  @Override
  public void mouseDown() {
    System.out.println("Brush icon");
  }

  @Override
  public void mouseUp() {
    System.out.println("Draw a line");
  }
}
