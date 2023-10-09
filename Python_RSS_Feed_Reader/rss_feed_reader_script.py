# import feedparser package
# pip install feedparser
import requests
import feedparser as fdp


def get_feeds_url(feed_url):
    response = requests.get(feed_url)
    response.raise_for_status()
    return fdp.parse(response.content)


def get_feed_details(feed):
    # print(feed)
    for detail in feed['entries']:
        # print(detail)
        print(f"Title: {detail.title}")
        print(f"Link: {detail.link}")
        print(f"Description: {detail.description}")
        print("*" * 120)


if __name__ == "__main__":
    print("Please enter the url....!")
    feed_url = input("enter the url here: ")
    print("*" * 120)
    feeds = get_feeds_url(feed_url)
    get_feed_details(feeds)

# http://feeds.bbci.co.uk/news/rss.xml
# feed_url = "https://timesofindia.indiatimes.com/rssfeedstopstories.cms"
