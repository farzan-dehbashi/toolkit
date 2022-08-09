package com.api_test.amberscript;

import org.apache.http.HttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;
import org.json.JSONObject;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

import org.apache.http.HttpEntity;
import org.apache.http.client.methods.HttpUriRequest;
import org.apache.http.client.methods.RequestBuilder;
import org.apache.http.entity.ContentType;
import org.apache.http.entity.mime.HttpMultipartMode;
import org.apache.http.entity.mime.MultipartEntityBuilder;
import org.apache.http.entity.mime.content.FileBody;

import org.springframework.boot.autoconfigure.SpringBootApplication;
// import org.springframework.boot.autoconfigure.batch.BatchProperties.Job;

@SpringBootApplication
public class AmberscriptApplication {
	public static void main(String[] args) throws IOException {
		FileWriter myWriter = new FileWriter("filename.txt");
		myWriter.write("Files in Java might be tricky, but it is fun enough!");
		myWriter.close();
		// AmberscriptApiResponse checkResponse = check("62ec377b5e0b80225efcbb00",
		// "26fe6e92ac6ec36f7cb5c311dd36436ff");
		// AmberscriptGetCaptionResponse capResposne =
		// getCaption("62e96a8d2ba2ee71d3a6f0ac",
		// "26fe6e92ac6ec36f7cb5c311dd36436ff",
		// "srt");
		// System.out.println(capResposne.caption);
	}

	private static class AmberscriptGetCaptionResponse {
		int responseCode;
		String caption;
	}

	public static AmberscriptGetCaptionResponse getCaption(String jobId, String apiKey, String captionType) {
		int status = -1;
		String captionStr = "";
		try {
			String url = "https://qs.amberscript.com/jobs/export-" + captionType + "?jobId=" + jobId + "&apiKey="
					+ apiKey;
			CloseableHttpClient client = HttpClients.createDefault();
			HttpGet get = new HttpGet(url);
			HttpResponse response = client.execute(get);
			HttpEntity httpEntity = response.getEntity();
			status = response.getStatusLine().getStatusCode();
			if (status != 200) {
				throw new Exception("Get status http response code is" + status);
			} else {
				captionStr = EntityUtils.toString(httpEntity, "UTF-8");
			}
		} catch (Exception e) {
		}
		AmberscriptGetCaptionResponse response = new AmberscriptGetCaptionResponse();
		response.responseCode = status;
		response.caption = captionStr;
		return response;
	}

	private static class AmberscriptCheckResponse {
		int responseCode;
		String captionRequestStatus;
	}

	public static AmberscriptCheckResponse check(String jobId, String apiKey) {
		int status = -1;
		String translationStatus = "Null";
		try {
			String url = "https://qs.amberscript.com/jobs/status?jobId=" + jobId + "&apiKey=" + apiKey;
			// String url =
			// "https://qs.amberscript.com/jobs/status?jobId=62ec377b5e0b80225efcbb00&apiKey=26fe6e92ac6ec36f7cb5c311dd36436ff";
			CloseableHttpClient client = HttpClients.createDefault();
			HttpGet get = new HttpGet(url);
			HttpResponse response = client.execute(get);
			HttpEntity httpEntity = response.getEntity();
			String responseString = EntityUtils.toString(httpEntity, "UTF-8");
			status = response.getStatusLine().getStatusCode();
			if (status != 200) {
				throw new Exception("Get status http response code is" + status);
			} else {
				JSONObject obj = new JSONObject(responseString);
				translationStatus = obj.getJSONObject("jobStatus").getString("status");
			}
		} catch (Exception e) {
		}
		AmberscriptCheckResponse response = new AmberscriptCheckResponse();
		response.responseCode = status;
		response.captionRequestStatus = translationStatus;
		return response;
	}

	public static void send() {
		try {
			CloseableHttpClient httpClient = HttpClients.createDefault();
			final File file = new File("C:\\Users\\Farzan Dehbashi\\Desktop\\music.mp3");
			FileBody filebody = new FileBody(file, ContentType.MULTIPART_FORM_DATA);
			MultipartEntityBuilder entitybuilder = MultipartEntityBuilder.create();
			entitybuilder.setMode(HttpMultipartMode.BROWSER_COMPATIBLE);
			entitybuilder.addBinaryBody("file", file);
			HttpEntity mutiPartHttpEntity = entitybuilder.build();
			RequestBuilder reqbuilder = RequestBuilder.post(
					"https://qs.amberscript.com/jobs/upload-media?transcriptionType=transcription&jobType=direct&language=fi&apiKey=26fe6e92ac6ec36f7cb5c311dd36436ff");
			// HttpResponse httpResponse = httpClient.execute(httpPost);
			reqbuilder.setEntity(mutiPartHttpEntity);
			HttpUriRequest multipartRequest = reqbuilder.build();
			HttpResponse httpresponse = httpClient.execute(multipartRequest);
			// JSONObject obj = new JSONObject(responseString);
			// String jobId = obj.getJSONObject("jobStatus").getString("jobId");
			System.out.println(httpresponse.toString());
			httpClient.close();
		} catch (Exception e) {

		}
	}

}
