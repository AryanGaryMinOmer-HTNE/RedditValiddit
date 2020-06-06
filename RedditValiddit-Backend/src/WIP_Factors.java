
import java.util.ArrayList;

public class WIP_Factors {
	
	String[] keyWords = new String[3];
	
	public WIP_Factors() {
		keyWords[0] = "inaccurate";
		keyWords[1] = "accurate";
		keyWords[2] = "biased";
	}
	
	public ArrayList<String[]> commentsWithLinks(String[] comments) {
		ArrayList<String[]> storage = new ArrayList<String[]>();
		
		for(int i = 0; i < comments.length; i++) {
			String cur = comments[i];
			
			if(cur.indexOf(""/* the indicator that there is a link/hyperlink in a comment */) != -1) {
				int wordLoc = cur.indexOf(""/* the indicator that there is a link/hyperlink in a comment */);
				String[] link = {cur, String.valueOf(wordLoc), /* end of link index */};
				storage.add(link);		
			}
			
		}
		
		return storage;
	}
	
	public ArrayList<String[]> commentsWithKeyWords(String[] comments) {
		ArrayList<String[]> storage = new ArrayList<String[]>();
		
		for(int i = 0; i < comments.length; i++) {
			String cur = comments[i];
			
			for(int j = 0; j < keyWords.length; j++) {
				if(cur.indexOf(keyWords[j]) != -1) {
					String[] keyFound = {cur, String.valueOf(cur.indexOf(keyWords[j])), String.valueOf(cur.indexOf(keyWords[j]) + keyWords[j].length())};
					storage.add(keyFound);
				}
			}
		}
		
		return storage;
	}
	
}
