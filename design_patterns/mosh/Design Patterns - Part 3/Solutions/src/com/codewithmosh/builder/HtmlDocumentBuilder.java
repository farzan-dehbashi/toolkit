package com.codewithmosh.builder;

import com.codewithmosh.builder.html.HtmlDocument;
import com.codewithmosh.builder.html.HtmlImage;
import com.codewithmosh.builder.html.HtmlParagraph;

public class HtmlDocumentBuilder implements DocumentBuilder {
    private HtmlDocument document = new HtmlDocument();

    @Override
    public void addText(Text text) {
        document.add(new HtmlParagraph(text.getContent()));
    }

    @Override
    public void addImage(Image image) {
        document.add(new HtmlImage(image.getSource()));
    }

    @Override
    public String getResult() {
        return document.toString();
    }
}
