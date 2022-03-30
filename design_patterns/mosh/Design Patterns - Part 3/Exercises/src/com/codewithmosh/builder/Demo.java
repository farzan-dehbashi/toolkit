package com.codewithmosh.builder;

import java.io.IOException;

public class Demo {
    public static void show() throws IOException {
        var document = new Document();
        document.add(new Text("Hello World"));
        document.add(new Image("pic1.jpg"));

        document.export(ExportFormat.HTML, "export.html");

        // Only writes the text elements to the file
        document.export(ExportFormat.TEXT, "export.txt");
    }
}
