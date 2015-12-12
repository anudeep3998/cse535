import java.io.IOException;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.TreeMap;

import edu.stanford.nlp.tagger.maxent.MaxentTagger;

public class Tagger {

	static String[] tags = new String[30];
	static int cnt = 0, tag_cnt = 0;
	static LinkedList<Node>[] node = new LinkedList[100000];
	static Map<String, Integer> tagList = new HashMap<String, Integer>();
	// static TreeMap<Integer, String>[] map = new TreeMap[50000];

	public static void main(String[] args) throws IOException, ClassNotFoundException {

		String model = "taggers/german-fast.tagger";
		// Initialize the tagger
		MaxentTagger tagger = new MaxentTagger(model);

		// The sample string
		String sample = "RT @BILD_Werder: #Ailton analysiert Werder - Ujah ist für 20 Tore gut, aber sonst... https://t.co/cWBG0itYfT";

		// The tagged string
		String tagged = tagger.tagString(sample);

		// Output the result
		System.out.println(tagged);

		int i, j = 0, k;
		String l2 = "", l3 = "", l4 = "", l5 = "";

		for (i = 0; i < tagged.length(); i++) {

			if (tagged.charAt(i) == ' ') {
				j = i + 1;
			}

			if (tagged.charAt(i) == '_') {
				if (model.equals("taggers/german-fast.tagger")) {

					if (tagged.length() > j + 11 && tagged.substring(j, j + 8).equals("https://"))
						continue;
					else if (tagged.substring(j, i).equals("RT"))
						continue;
					else if (tagged.substring(j, i).equals("'s"))
						continue;
					else if (tagged.charAt(j) == '@')
						continue;

					if (tagged.length() > i + 2)
						l2 = tagged.substring(i + 1, i + 3);
					else
						l2 = "";
					if (tagged.length() > i + 3)
						l3 = tagged.substring(i + 1, i + 4);
					else
						l3 = "";
					if (tagged.length() > i + 4)
						l4 = tagged.substring(i + 1, i + 5);
					else
						l4 = "";
					if (tagged.length() > i + 5)
						l5 = tagged.substring(i + 1, i + 6);
					else
						l5 = "";

					// if (l5.equals("VVFIN"))
					// tags[cnt++] = tagged.substring(j, i);
					if (l4.equals("CARD") || l4.equals("ADJA") || l4.equals("ADJD"))
						tags[cnt++] = tagged.substring(j, i);
					else if (l2.equals("NN") || l2.equals("NE"))
						tags[cnt++] = tagged.substring(j, i);

				} else if (model.equals("english-bidirectional-distsim.tagger")) {
					if (tagged.length() > j + 11 && tagged.substring(j, j + 8).equals("https://"))
						continue;
					else if (tagged.substring(j, i).equals("RT"))
						continue;
					else if (tagged.substring(j, i).equals("'s"))
						continue;
					else if (tagged.charAt(j) == '@')
						continue;

					if (tagged.length() > i + 2)
						l2 = tagged.substring(i + 1, i + 3);
					else
						l2 = "";
					if (tagged.length() > i + 3)
						l3 = tagged.substring(i + 1, i + 4);
					else
						l3 = "";
					if (tagged.length() > i + 4)
						l4 = tagged.substring(i + 1, i + 5);
					else
						l4 = "";

					if (l4.equals("NNPS"))
						tags[cnt++] = tagged.substring(j, i);
					else if (l3.equals("JJR") || l3.equals("JJS") || l3.equals("NNS") || l3.equals("NNP"))
						// || l3.equals("VBD") || l3.equals("VBG") ||
						// l3.equals("VBN") || l3.equals("VBP") ||
						// l3.equals("VBZ"))
						tags[cnt++] = tagged.substring(j, i);
					else if (l2.equals("NN") || l2.equals("CD") || l2.equals("JJ"))
						// || l2.equals("VB"))
						tags[cnt++] = tagged.substring(j, i);
				} else if (model.equals("french.tagger")) {
					if (tagged.length() > j + 11 && tagged.substring(j, j + 8).equals("https://"))
						continue;
					else if (tagged.substring(j, i).equals("RT"))
						continue;
					else if (tagged.substring(j, i).equals("'s"))
						continue;
					else if (tagged.charAt(j) == '@')
						continue;

					if (tagged.length() > i + 2)
						l2 = tagged.substring(i + 1, i + 3);
					else
						l2 = "";
					if (tagged.length() > i + 3)
						l3 = tagged.substring(i + 1, i + 4);
					else
						l3 = "";
					if (tagged.length() > i + 4)
						l4 = tagged.substring(i + 1, i + 5);
					else
						l4 = "";

					if (l3.equals("ADJ") || l3.equals("NAM") || l3.equals("NOM") || l3.equals("NUM"))
						tags[cnt++] = tagged.substring(j, i);
				} else if (model.equals("spanish-distsim.tagger")) {
					if (tagged.length() > j + 11 && tagged.substring(j, j + 8).equals("https://"))
						continue;
					else if (tagged.substring(j, i).equals("RT"))
						continue;
					else if (tagged.substring(j, i).equals("'s"))
						continue;
					else if (tagged.charAt(j) == '@')
						continue;

					if (tagged.length() > i + 2)
						l2 = tagged.substring(i + 1, i + 3);
					else
						l2 = "";
					if (tagged.length() > i + 3)
						l3 = tagged.substring(i + 1, i + 4);
					else
						l3 = "";
					if (tagged.length() > i + 4)
						l4 = tagged.substring(i + 1, i + 5);
					else
						l4 = "";

					if (l4.equals("CARD") || l4.equals("NMEA"))
						tags[cnt++] = tagged.substring(j, i);
					else if (l3.equals("ADJ"))
						tags[cnt++] = tagged.substring(j, i);
					else if (l2.equals("NP") || l2.equals("NC"))
						tags[cnt++] = tagged.substring(j, i);
				}
			}
		}

		for (i = 0; i < cnt; ++i) {
			k = tag_cnt;
			System.out.print(tags[i] + ":");
			if (!tagList.containsKey(tags[i])) {
				tagList.put(tags[i], tag_cnt);
				if (node[tag_cnt] == null)
					node[tag_cnt] = new LinkedList<Node>();
			} else {
				k = tagList.get(tags[i]);
			}

			for (j = 0; j < cnt; ++j) {
				if (i == j)
					continue;
				Boolean fl = true;
				for (Node e : node[k]) {
					if (e.tag.equals(tags[j])) {
						fl = false;
						e.n++;
						break;
					}
				}

				if (fl)
					node[k].add(new Node(tags[j], 1));
			}
			for (Node e : node[k])
				System.out.print(" " + e.tag + "/" + e.n);
			System.out.println();
			tag_cnt++;
		}
	}
}

class Node implements Comparable<Node> {
	String tag;
	int n;

	public Node(String tag, int s) {
		this.tag = tag;
		this.n = s;
	}

	@Override
	public int compareTo(Node o) {
		int comparedSize = o.n;
		if (this.n > comparedSize) {
			return 1;
		} else if (this.n == comparedSize) {
			return 0;
		} else {
			return -1;
		}
	}

	@Override
	public boolean equals(Object obj) {
		if (this.tag == ((Node) obj).tag)
			return true;
		else
			return false;
	}

	public String toString() {
		return tag;
	}
}
