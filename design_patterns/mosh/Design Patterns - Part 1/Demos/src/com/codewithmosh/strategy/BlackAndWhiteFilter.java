package com.codewithmosh.strategy;

public class BlackAndWhiteFilter implements Filter {
  @Override
  public void apply(String fileName) {
    System.out.println("Applying B&W filter");
  }
}
