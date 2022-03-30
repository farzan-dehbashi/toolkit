package com.codewithmosh.builder.html;

public class HtmlParagraph extends HtmlElement {
    private String text;

    public HtmlParagraph(String text) {
        this.text = text;
    }

    @Override
    public String toString() {
        return String.format("<p>%s</p>", text);
    }
}
