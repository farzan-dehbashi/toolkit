package com.codewithmosh.chainOfResponsibility;

public class Demo {
    public static void show() {
        var reader = DataReaderFactory.getDataReaderChain();
        reader.read("data.xls");
        reader.read("data.numbers");
        reader.read("data.qbw");
        reader.read("data.jpg");
    }
}
