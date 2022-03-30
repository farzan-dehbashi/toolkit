package com.codewithmosh.builder.html;

public class HtmlImage extends HtmlElement {
    private String source;

    public HtmlImage(String source) {
        this.source = source;
    }

    @Override
    public String toString() {
        return String.format("<img src=\"%s\" />", source);
    }
}
