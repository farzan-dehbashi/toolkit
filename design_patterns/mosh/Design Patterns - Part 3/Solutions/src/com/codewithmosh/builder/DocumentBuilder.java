package com.codewithmosh.builder;

public interface DocumentBuilder {
    void addText(Text text);
    void addImage(Image image);
    String getResult();
}
