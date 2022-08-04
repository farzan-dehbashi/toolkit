package com.api_test.amberscript;

import org.apache.http.HttpResponse;
import org.apache.http.client.ResponseHandler;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.methods.HttpUriRequest;
import org.apache.http.client.methods.RequestBuilder;
import org.apache.http.entity.ContentType;
import org.apache.http.entity.mime.HttpMultipartMode;
import org.apache.http.entity.mime.MultipartEntityBuilder;
import org.apache.http.entity.mime.content.FileBody;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;
import java.io.File;
import java.io.IOException;
import java.net.URISyntaxException;
// import java.util.HashMap;
// import java.util.Map;
// import java.util.Scanner;
// import java.util.concurrent.CompletableFuture;
// import java.io.IOException;
// import java.net.URI;

// import okhttp3.MediaType;
// import okhttp3.OkHttpClient;
// import okhttp3.Request;
// import okhttp3.RequestBody;
// import okhttp3.Response;

// import org.apache.http.HttpEntity;
// import org.apache.http.HttpResponse;
// import org.apache.http.client.HttpClient;
// // import org.apache.http.client.entity.EntityBuilder;
// import org.apache.http.client.methods.HttpGet;
// import org.apache.http.client.methods.HttpPost;
// import org.apache.http.client.utils.URIBuilder;
// import org.apache.http.entity.ContentType;
// import org.apache.http.impl.client.CloseableHttpClient;
// import org.apache.http.impl.client.HttpClientBuilder;
// import org.apache.http.impl.client.HttpClients;
// import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
// import org.springframework.boot.autoconfigure.batch.BatchProperties.Job;

@SpringBootApplication
public class AmberscriptApplication {
	public static void main(String[] args) {
		send();
		check();
		check();
		get();
	}

	public static void get() {
		try {
			String jobId = "";
			String apiKey = "26fe6e92ac6ec36f7cb5c311dd36436fd";
			String url = "https://qs.amberscript.com/jobs/export-stl?jobId=" + jobId + "&apiKey=" + apiKey;
		} catch (Exception e) {

		}
	}

	public static void check() {
		try {
			String jobId = "";
			String apiKey = "26fe6e92ac6ec36f7cb5c311dd36436fd";
			String url = "https://api.amberscript.com/api/jobs/export-srt?jobId=" + jobId + "&apiKey=";
			CloseableHttpClient client = HttpClients.createDefault();
			HttpGet get = new HttpGet(url);
			HttpResponse response = client.execute(get);
			int i = 1;
		} catch (Exception e) {
		}
	}

	public static void send() {
		try {
			CloseableHttpClient httpClient = HttpClients.createDefault();
			// HttpPost httpPost = new HttpPost(
			// "https://httpbin.org/post?transcriptionType=transcription&jobType=direct&language=fi&apiKey=26fe6e92ac6ec36f7cb5c311dd36436fd");
			final File file = new File("C:\\Users\\Farzan Dehbashi\\Desktop\\music.mp3");
			FileBody filebody = new FileBody(file, ContentType.MULTIPART_FORM_DATA);
			MultipartEntityBuilder entitybuilder = MultipartEntityBuilder.create();
			entitybuilder.setMode(HttpMultipartMode.BROWSER_COMPATIBLE);
			entitybuilder.addBinaryBody("file", file);
			HttpEntity mutiPartHttpEntity = entitybuilder.build();
			RequestBuilder reqbuilder = RequestBuilder.post(
					"https://qs.amberscript.com/jobs/upload-media?transcriptionType=transcription&jobType=direct&language=fi&apiKey=26fe6e92ac6ec36f7cb5c311dd36436fd");
			// HttpResponse httpResponse = httpClient.execute(httpPost);
			reqbuilder.setEntity(mutiPartHttpEntity);
			HttpUriRequest multipartRequest = reqbuilder.build();
			HttpResponse httpresponse = httpClient.execute(multipartRequest);
			JSONObject obj = new JSONObject(responseString);
			String jobId = obj.getJSONObject("jobStatus").getString("jobId");
			System.out.println(httpresponse.toString());
			httpClient.close();
		} catch (Exception e) {

		}
	}

}
