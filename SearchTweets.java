
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.text.SimpleDateFormat;
import java.util.List;

import twitter4j.JSONException;
import twitter4j.JSONObject;
import twitter4j.Query;
import twitter4j.QueryResult;
import twitter4j.Status;
import twitter4j.Twitter;
import twitter4j.TwitterException;
import twitter4j.TwitterFactory;

public class SearchTweets {
	/**
	 * Usage: java twitter4j.examples.search.SearchTweets [query]
	 *
	 * @param args
	 *            search query
	 */
	public static void main(String[] args) {

		SimpleDateFormat df = new SimpleDateFormat("EEE MMM dd HH:mm:ss +SSSS yyyy");
		SimpleDateFormat d = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss'Z'");

		if (args.length < 1) {
			System.out.println("java twitter4j.examples.search.SearchTweets [query]");
			System.exit(-1);
		}
		Twitter twitter = new TwitterFactory().getInstance();
		int cnt = 0;

		// System.out.println("[");
		//
		// try (PrintWriter out = new PrintWriter(new BufferedWriter(new
		// FileWriter("tweets.txt", true)))) {
		// out.println("[");
		// } catch (IOException e) {
		// }
		// 23-e390,d207,r230 t827 14-e135,d120,r105 t360 16-e150,d135,r135 t420
		// 19-e105,d150,r150 t405 21-e30,d37,r56 t121 T2133
		try {
			Query query = new Query("samsung");
			query.setLang("ko");
			// query.setSince("2015-10-22");
			// query.setUntil("2015-11-22");
			query.count(10);
			QueryResult result;
			do {
				result = twitter.search(query);
				List<Status> tweets = result.getTweets();

				for (Status tweet : tweets) {
					// Iterator it=tweet.getHashtagEntities().length;
					++cnt;
					String text = tweet.getText();
					text = text.replace("\n", " ");
					text = text.replace("\"", "");

					System.out.println("\t{");

					// System.out.println(cnt + "\t\t\"id\":\"" + tweet.getId()
					// + "\"," + "\n\t\t\"username\":\""
					// + tweet.getUser().getScreenName() + "\"," +
					// "\n\t\t\"text_en\":\"" + "" + "\","
					// + "\n\t\t\"text_de\":\"" + "" + "\"," +
					// "\n\t\t\"text_ru\":\"" + text + "\","
					// + "\n\t\t\"created_at\":\"" +
					// d.format(tweet.getCreatedAt()) + "\"," +
					// "\n\t\t\"lang\":\""
					// + tweet.getLang() + "\"," + "\n\t\t\"location\":\"" +
					// tweet.getUser().getLocation() + "\","
					// + "\n\t\t\"retweet\":\"" + tweet.isRetweet() + "\",");

					System.out.println(cnt + "\t\t\"id\":\"" + tweet.getId() + "\"," + "\n\t\t\"user_screen_name \":\""
							+ tweet.getUser().getScreenName() + "\"," + "\n\t\t\"text\":\"" + text + "\"," + "\n\t\t\"created_at\":\""
							+ d.format(tweet.getCreatedAt()) + "\"," + "\n\t\t\"lang\":\"" + tweet.getLang() + "\"," + "\n\t\t\"location\":\""
							+ tweet.getUser().getLocation() + "\"," + "\n\t\t\"retweet_status\":\"" + tweet.isRetweet() + "\","
							+ "\n\t\t\"quote_status\":\"" + tweet.getQuotedStatus() + "\"," 
//							+ "\n\t\t\"place_id\":\"" + tweet.getPlace().getId()
//							+ "\"," + "\n\t\t\"place_type\":\"" + tweet.getPlace().getPlaceType() + "\"," + "\n\t\t\"place_full_name\":\""
//							+ tweet.getPlace().getFullName() + "\"," + "\n\t\t\"place_country_code\":\"" + tweet.getPlace().getCountryCode() + "\","
//							+ "\n\t\t\"place_country\":\"" + tweet.getPlace().getCountry() + "\"," 
							+ "\n\t\t\"favorite_count \":\""
							+ tweet.getFavoriteCount() + "\"," + "\n\t\t\"retweet_count \":\"" + tweet.getRetweetCount() + "\","
							+ "\n\t\t\"favorited_status \":\"" + tweet.isFavorited() + "\"," + "\n\t\t\"user_id \":\"" + tweet.getUser().getId()
							+ "\"," + "\n\t\t\"user_verified \":\"" + tweet.getUser().isVerified() + "\"," + "\n\t\t\"user_followers_count \":\""
							+ tweet.getUser().getFollowersCount() + "\"," + "\n\t\t\"user_name \":\"" + tweet.getUser().getName() + "\",");

					// try (PrintWriter out = new PrintWriter(new
					// BufferedWriter(new FileWriter("tweets.txt", true)))) {
					// out.println("\t{");
					//
					// out.println("\t\t\"id\":\"" + tweet.getId() + "\"," +
					// "\n\t\t\"username\":\""
					// + tweet.getUser().getScreenName() + "\"," +
					// "\n\t\t\"text_en\":\"" + "" + "\","
					// + "\n\t\t\"text_de\":\"" + "" + "\"," +
					// "\n\t\t\"text_ru\":\"" + text + "\","
					// + "\n\t\t\"created_at\":\"" +
					// d.format(tweet.getCreatedAt()) + "\"," +
					// "\n\t\t\"lang\":\""
					// + tweet.getLang() + "\"," + "\n\t\t\"location\":\"" +
					// tweet.getUser().getLocation() + "\","
					// + "\n\t\t\"retweet\":\"" + tweet.isRetweet() + "\",");
					// } catch (IOException e) {
					// }

					try (PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("tweets.txt", true)))) {
						out.println("\t{");

						out.println("\t\t\"id\":\"" + tweet.getId() + "\"," + "\n\t\t\"user_screen_name \":\"" + tweet.getUser().getScreenName()
								+ "\"," + "\n\t\t\"text\":\"" + text + "\"," + "\n\t\t\"created_at\":\"" + d.format(tweet.getCreatedAt()) + "\","
								+ "\n\t\t\"lang\":\"" + tweet.getLang() + "\"," + "\n\t\t\"location\":\"" + tweet.getUser().getLocation() + "\","
								+ "\n\t\t\"retweet_status\":\"" + tweet.isRetweet() + "\"," + "\n\t\t\"quote_status\":\"" + tweet.getQuotedStatus()
//								+ "\"," + "\n\t\t\"place_id\":\"" + tweet.getPlace().getId() + "\"," + "\n\t\t\"place_type\":\""
//								+ tweet.getPlace().getPlaceType() + "\"," + "\n\t\t\"place_full_name\":\"" + tweet.getPlace().getFullName() + "\","
//								+ "\n\t\t\"place_country_code\":\"" + tweet.getPlace().getCountryCode() + "\"," + "\n\t\t\"place_country\":\""
//								+ tweet.getPlace().getCountry() + "\"," 
								+ "\n\t\t\"favorite_count \":\"" + tweet.getFavoriteCount() + "\","
								+ "\n\t\t\"retweet_count \":\"" + tweet.getRetweetCount() + "\"," + "\n\t\t\"favorited_status \":\""
								+ tweet.isFavorited() + "\"," + "\n\t\t\"user_id \":\"" + tweet.getUser().getId() + "\","
								+ "\n\t\t\"user_verified \":\"" + tweet.getUser().isVerified() + "\"," + "\n\t\t\"user_followers_count \":\""
								+ tweet.getUser().getFollowersCount() + "\"," + "\n\t\t\"user_name \":\"" + tweet.getUser().getName() + "\",");
					} catch (IOException e) {
					}

					JSONObject js = new JSONObject(tweet);
					try {
						System.out.print("\t\t\"hashtags\":[");

						try (PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("tweets.txt", true)))) {
							out.print("\t\t\"hashtags\":[");
						} catch (IOException e) {
						}

						if (js.getJSONArray("hashtagEntities").length() > 0) {
							for (int i = 0; i < js.getJSONArray("hashtagEntities").length(); ++i) {
								JSONObject first = js.getJSONArray("hashtagEntities").getJSONObject(i);
								// JSONObject shipper =
								// first.getJSONObject("text");
								String id = first.getString("text");
								if (i == 0) {
									System.out.print("\"" + id + "\"");
									try (PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("tweets.txt", true)))) {
										out.print("\"" + id + "\"");
									} catch (IOException e) {
									}
								} else {
									System.out.print(", \"" + id + "\"");
									try (PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("tweets.txt", true)))) {
										out.print(", \"" + id + "\"");
									} catch (IOException e) {
									}
								}
							}
						}
						System.out.println("],");

						System.out.print("\t\t\"expanded_urls \":[");

						try (PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("tweets.txt", true)))) {
							out.println("],");

							out.print("\t\t\"expanded_urls \":[");
						} catch (IOException e) {
						}

						if (tweet.getUser().getURLEntity().getExpandedURL().length() == 0) {
							if (js.getJSONArray("URLEntities").length() > 0) {
								for (int i = 0; i < js.getJSONArray("URLEntities").length(); ++i) {
									JSONObject first = js.getJSONArray("URLEntities").getJSONObject(i);
									// JSONObject shipper =
									// first.getJSONObject("text");
									String id = first.getString("expandedURL");
									if (i == 0) {
										System.out.print("\"" + id + "\"");
										try (PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("tweets.txt", true)))) {
											out.print("\"" + id + "\"");
										} catch (IOException e) {
										}
									} else {
										System.out.print(", \"" + id + "\"");
										try (PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("tweets.txt", true)))) {
											out.print(", \"" + id + "\"");
										} catch (IOException e) {
										}
									}
								}
							}
						} else {
							System.out.print("\"" + tweet.getUser().getURLEntity().getExpandedURL() + "\"");
							try (PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("tweets.txt", true)))) {
								out.print("\"" + tweet.getUser().getURLEntity().getExpandedURL() + "\"");
							} catch (IOException e) {
							}
						}
						System.out.println("]");
						System.out.println("\t},");

						try (PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("tweets.txt", true)))) {
							out.println("]");
							out.println("\t},");
						} catch (IOException e) {
						}

					} catch (JSONException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
					// System.out.println(js);

				}
				System.out.println(cnt);
			} while ((query = result.nextQuery()) != null);

			// System.out.println("]");
			// try (PrintWriter out = new PrintWriter(new BufferedWriter(new
			// FileWriter("tweets.txt", true)))) {
			// out.println("]");
			// } catch (IOException e) {
			// }

			System.exit(0);
		} catch (TwitterException te) {
			te.printStackTrace();
			System.out.println("Failed to search tweets: " + te.getMessage());
			System.exit(-1);
		} catch (NullPointerException ne) {
			ne.printStackTrace();
			System.out.println("N");
		}
	}
}