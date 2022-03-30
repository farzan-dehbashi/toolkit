package com.codewithmosh.visitor;

import java.util.ArrayList;
import java.util.List;

public class WavFile {
    private List<Segment> segments = new ArrayList<>();

    public static WavFile read(String fileName) {
        // Simulate reading a wav file and building the segments
        var wavFile = new WavFile();
        wavFile.segments.add(new FormatSegment());
        wavFile.segments.add(new FactSegment());
        wavFile.segments.add(new FactSegment());
        wavFile.segments.add(new FactSegment());

        return wavFile;
    }

    public void reduceNoise() {
        for (var segment : segments)
            segment.reduceNoise();
    }

    public void addReverb() {
        for (var segment : segments)
            segment.addReverb();
    }

    public void normalize() {
        for (var segment : segments)
            segment.normalize();
    }
}
