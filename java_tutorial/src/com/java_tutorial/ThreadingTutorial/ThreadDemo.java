package com.java_tutorial.ThreadingTutorial;
import com.java_tutorial.ThreadingTutorial.ThreadDemo;
public class ThreadDemo {
    public static void show(){
        for (int i = 0; i < 10; i++) {
            Thread downloadingThread = new Thread(new DownloadingFile());
            downloadingThread.start();
        }
    }
}
