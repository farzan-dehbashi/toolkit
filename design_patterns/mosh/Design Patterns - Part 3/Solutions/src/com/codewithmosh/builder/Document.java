package com.codewithmosh.builder;

import com.codewithmosh.builder.html.HtmlDocument;
import com.codewithmosh.builder.html.HtmlImage;
import com.codewithmosh.builder.html.HtmlParagraph;

import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Document {
    private List<Element> elements = new ArrayList<>();

    public void add(Element element) {
        elements.add(element);
    }

    public void export(DocumentBuilder builder, String fileName) throws IOException {
        // Note that we've separated the construction of the target
        // document from its representation. The same construction
        // algorithm is used to generate different types of documents
        // such as HTML, text, etc.
        //
        // For text files, even though we don't have images, we still
        // use the same algorithm. Look at the implementation of
        // addImage() method in TextDocumentBuilder. It's empty. So it
        // simply ignores adding images.
        for (Element element: elements) {
            if (element instanceof Text)
                builder.addText((Text)element);
            else if (element instanceof Image)
                builder.addImage((Image)element);
        }


        var writer = new FileWriter(fileName);
        writer.write(builder.getResult());
        writer.close();
    }
}
