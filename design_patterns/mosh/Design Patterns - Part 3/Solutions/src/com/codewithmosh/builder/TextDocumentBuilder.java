package com.codewithmosh.builder;

public class TextDocumentBuilder implements DocumentBuilder {
    private StringBuilder builder = new StringBuilder();

    @Override
    public void addText(Text text) {
        builder.append(text.getContent());
    }

    @Override
    public void addImage(Image image) {
        // Note that this method has no implementation because
        // images cannot be added to a plain text file.
    }

    @Override
    public String getResult() {
        return builder.toString();
    }
}
