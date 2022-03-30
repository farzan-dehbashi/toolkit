package com.codewithmosh.observer;

import java.util.ArrayList;
import java.util.List;

public class StockListView {
    private List<Stock> stocks = new ArrayList<>();

    public void addStock(Stock stock) {
        stocks.add(stock);
    }

    public void show() {
        for (var stock : stocks)
            System.out.println(stock);
    }
}
