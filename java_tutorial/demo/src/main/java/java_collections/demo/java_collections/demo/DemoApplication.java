package java_collections.demo;

import java.util.ArrayList;
import java.util.Collection;

@SpringBootApplication
public class DemoApplication {

	public static void main(String[] args) {
		Collection<String> collection = new ArrayList<String>();
		collection.add("a");
		collection.add("b");
		for (Object o : collection) {
			System.out.println(o.toString());
		}
	}

}
