package com.codewithmosh.visitor;

public class HeadingNode implements HtmlNode {
  @Override
  public void execute(Operation operation) {
    operation.apply(this);
  }
}
