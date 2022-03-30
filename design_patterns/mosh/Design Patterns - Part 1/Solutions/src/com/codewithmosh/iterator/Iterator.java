package com.codewithmosh.iterator;

public interface Iterator {
  boolean hasNext();
  Product current();
  void next();
}
