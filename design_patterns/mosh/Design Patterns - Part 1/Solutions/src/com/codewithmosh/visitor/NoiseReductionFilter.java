package com.codewithmosh.visitor;

public class NoiseReductionFilter implements AudioFilter {
    @Override
    public void apply(FormatSegment formatSegment) {
        System.out.println("Noise reduction on format segment");
    }

    @Override
    public void apply(FactSegment factSegment) {
        System.out.println("Noise reduction on fact segment");
    }
}
