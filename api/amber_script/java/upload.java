import org.apache;
import org.apache.http.HttpResponse;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

class HelloWorld {
    public static void main(String[] args) {
        HttpResponse<String> response = Unirest
                .get("https://qs.amberscript.com/jobs/status?jobId=JOB_ID&apiKey=YOUR_API_KEY").asString();
    }
}