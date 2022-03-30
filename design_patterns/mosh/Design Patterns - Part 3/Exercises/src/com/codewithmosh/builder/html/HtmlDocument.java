package com.codewithmosh.builder.html;

import java.util.ArrayList;
import java.util.List;

public class HtmlDocument {
    private List<HtmlElement> elements = new ArrayList<>();

    public void add(HtmlElement element) {
        elements.add(element);
    }

    @Override
    public String toString() {
        var builder = new StringBuilder();
        builder.append("<html>");
        for (HtmlElement element: elements)
            builder.append(element.toString());
        builder.append("</html>");
        return builder.toString();
    }
}
