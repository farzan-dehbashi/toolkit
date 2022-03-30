package com.codewithmosh.iterator;

import java.util.ArrayList;
import java.util.List;

public class ProductCollection {
  private List<Product> products = new ArrayList<>();

  public void add(Product product) {
    products.add(product);
  }

  public Iterator createIterator() {
    return new ListIterator(this);
  }

  private class ListIterator implements Iterator {
    private ProductCollection collection;
    private int index;

    public ListIterator(ProductCollection collection) {
      this.collection = collection;
    }

    @Override
    public boolean hasNext() {
      return (index < collection.products.size());
    }

    @Override
    public Product current() {
      return collection.products.get(index);
    }

    @Override
    public void next() {
      index++;
    }
  }
}
