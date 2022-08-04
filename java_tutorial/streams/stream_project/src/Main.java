import streams.GenericList;
import streams.Movie;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;
import java.util.stream.Stream;
import org.apache.commons.io.FileUtils;

public class Main {
    public static void main(String[] args) {
        final File file = new File("C:\\Users\\Farzan Dehbashi\\Desktop\\music.mp3");
        String str = FileUtils.readFileToString(file, "UTF-8");
    }

//    public CompletableFuture<Job> uploadJobMedia(String apiKey, UploadMediaPayload uploadMediaPayload) {
//        CompletableFuture<Job> future = new CompletableFuture<>();
//        Map<String, String> parameters = new HashMap<>();
//        File file = uploadMediaPayload.getFile();
//        file.deleteOnExit();
//        String endpoint = amberscriptBaseEndpoint + CREATE_JOB_PATH;
//        try {
//            parameters.put(LANGUAGE_PARAM, uploadMediaPayload.getLanguage());
//            parameters.put(TRANSCRIPTION_TYPE_PARAM, uploadMediaPayload.getTranscriptionType().value);
//            parameters.put(JOB_TYPE_PARAM, uploadMediaPayload.getJobType().value);
//            parameters.put(CALLBACK_URL_PARAM, uploadMediaPayload.getCallbackUrl());
//            parameters.put(API_KEY_PARAM, apiKey);
//
//            if (uploadMediaPayload.getTargetLanguage() != null) {
//                parameters.put(TARGET_LANGUAGE_PARAM, uploadMediaPayload.getTargetLanguage());
//            }
//
//            String response = httpClient.postWithFile(endpoint, file, parameters);
//
//            boolean fileDeleted = file.delete();
//            log.info("File deleting status: {}", fileDeleted);
//
//            Job job = getJobStatus(response);
//
//            future.complete(job);
//        } catch (JSONException | HttpRequestException e) {
//            String errorMsg = getErrorMsg(e, endpoint, parameters);
//            future.completeExceptionally(new AmberScriptAPIException(errorMsg));
//        }
//
//        return future;
//    }
}