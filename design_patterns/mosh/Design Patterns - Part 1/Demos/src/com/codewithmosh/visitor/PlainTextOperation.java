package com.codewithmosh.visitor;

public class PlainTextOperation implements Operation {
  @Override
  public void apply(HeadingNode heading) {
    System.out.println("text-heading");
  }

  @Override
  public void apply(AnchorNode anchor) {
    System.out.println("text-anchor");
  }
}
