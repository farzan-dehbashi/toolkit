package com.java_tutorial.ThreadingTutorial;

public class DownloadingFile implements Runnable{

    @Override
    public void run() {
        System.out.println("Downloading bulshit..." + Thread.currentThread().getName());
        try {
            Thread.sleep(5000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("Download complete"+ Thread.currentThread().getName());
    }
}
