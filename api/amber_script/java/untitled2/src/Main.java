import javax.net.ssl.HttpsURLConnection;
import java.io.*;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Main {
    public static void main(String[] args) throws IOException {
        String urlStr = "https://api.amberscript.com/api/jobs/upload-media?transcriptionType=transcription&jobType=direct&language=fi&apiKey=26fe6e92ac6ec36f7cb5c311dd36436fd";
//        String charset = "UTF-8";
        File binaryFile = new File("C:\\Users\\Farzan Dehbashi\\Desktop\\finish_sample.mp3");
//        String boundary = Long.toHexString(System.currentTimeMillis()); // Just generate some unique random value.
//        String CRLF = "\r\n"; // Line separator required by multipart/form-data.
//        URLConnection connection =  new URL(urlStr).openConnection();
//        connection.setDoOutput(true);
//        connection.setRequestMethod("POST");
//        connection.setRequestProperty("Connection", "Keep-Alive");
//        connection.setRequestProperty("Content-Type", "multipart/form-data;boundary=" + boundary);
//        connection.connect();
//        try (	DataOutputStream output = new DataOutputStream(connection.getOutputStream());
//                 PrintWriter writer = new PrintWriter(new OutputStreamWriter(output, charset), true);
//        )
//        {
//            writer.append("Content-Disposition: form-data; name=\"binaryFile\"; filename=\"" + binaryFile.getName() + "\"")
//                    .append(CRLF);
//            writer.append("Content-Type: " + URLConnection.guessContentTypeFromName(binaryFile.getName())).append(CRLF);
//            writer.append("Content-Transfer-Encoding: binary").append(CRLF);
//            writer.append(CRLF).flush();
//            Files.copy(binaryFile.toPath(), output);
//            output.flush(); // Important before continuing with writer!
//            writer.append(CRLF).flush(); // CRLF is important! It indicates end of boundary.
//            int responseCode = ((HttpURLConnection) connection).getResponseCode();
//            int id = 0;
//        }
//        byte[] fileBytes = Files.readAllBytes(Paths.get("C:\\Users\\Farzan Dehbashi\\Desktop\\finish_sample.mp3"));
//        URL url = new URL(urlStr);
//        HttpsURLConnection conn = (HttpsURLConnection) url.openConnection();
//        conn.setRequestMethod("POST");
//        conn.setDoOutput(true);
////        conn.setRequestProperty ("Authorization", encodedCredentials);
//
//        OutputStreamWriter writer = new OutputStreamWriter(conn.getOutputStream());
//
//        writer.write(fileBytes);
//        writer.flush();
//        String line;
//        BufferedReader reader = new BufferedReader(new
//                InputStreamReader(conn.getInputStream()));
//        while ((line = reader.readLine()) != null) {
//            System.out.println(line);
//        }
//        writer.close();
//        reader.close();

    }
}