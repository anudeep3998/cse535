import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import java.util.*;
import java.io.*;
import edu.stanford.nlp.ling.Sentence;
import edu.stanford.nlp.ling.TaggedWord;
import edu.stanford.nlp.ling.HasWord;
import edu.stanford.nlp.tagger.maxent.MaxentTagger;

public class Jsonparsing
{
	public static void main(String[] args)
	{
		JSONParser parser=new JSONParser();
		String str;
		try{
			File fileDirs = new File("input.txt");

			BufferedReader in = new BufferedReader(
			new InputStreamReader(new FileInputStream(fileDirs),"UTF-8"));
			
			JSONObject jsonObject;
			JSONArray jsonAr;
			int count = 0;
			while ((str = in.readLine()) != null){
				try{
					if(count ==0)
						str = str.substring(1, str.length());
					count++;
					//System.out.println(str);
					jsonObject = (JSONObject)parser.parse(str);
					String s=(String)jsonObject.get("text");
					//String a[]=s.split("\\s+");
					System.out.println(s);
					MaxentTagger tagger = new MaxentTagger("english-caseless-left3words-distsim.tagger");
				    List<List<HasWord>> sentences = MaxentTagger.tokenizeText(new BufferedReader(new StringReader(s)));
				    for (List<HasWord> sentence : sentences) 
				    {
				      List<TaggedWord> tSentence = tagger.tagSentence(sentence);
				      for (TaggedWord w : tSentence){
				    	  System.out.println("value :"+w.value());
				    	  System.out.println("tag :"+w.tag());
				    	  //System.out.println("word :"+w.word());
				      }
//				      System.out.println(Sentence.listToString(tSentence, false));
					}
				}
				    catch(ParseException e)
				{
					System.out.println(e.getCause());
				}
				}
		}
	catch(Exception e)
	{
		e.printStackTrace();
	}
		
	}
	}
