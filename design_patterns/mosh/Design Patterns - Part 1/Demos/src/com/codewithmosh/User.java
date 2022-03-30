package com.codewithmosh;

public class User {
  // Fields (attributes)
  public String name;

  public User(String name, int age) {
    this.name = name;
  }

  // Methods
  public void sayHello() {
    System.out.println("- Hi, my name is " + name);
  }
}
