import java.io.File;
import java.io.IOException;

public class Main {

    public static void main(String args[]) throws IOException {
        String prefix = "exampleTempFile";
        String suffix = ".txt";
        //Creating a File object for directory
        File directoryPath = new File("/Users/farzandb/Desktop/");
        //Creating a temp file
        File tempFile = File.createTempFile(prefix, suffix, directoryPath);
        System.out.println("Temp file created: "+tempFile.getAbsolutePath());
        //Deleting the file
        tempFile.delete();
        System.out.println("Temp file deleted.........");
    }



    }
