import os
import sys
import googleapiclient.discovery
from dotenv import load_dotenv

load_dotenv()


def search_video(query, api_key):
    youtube = googleapiclient.discovery.build(
        "youtube", "v3", developerKey=api_key)

    request = youtube.search().list(
        part="id",
        type="video",
        q=query,
        maxResults=1,
        fields="items(id(videoId))"
    )

    response = request.execute()
    video_id = response["items"][0]["id"]["videoId"]
    return f"https://www.youtube.com/embed/{video_id}"


def main():
    api_key = os.getenv("APIKEY")

    searches = []

    while True:
        search_term = input("Enter search term (leave blank to finish): ")
        if search_term.strip() == "":
            break
        searches.append(search_term)

    for search in searches:
        url = search_video(search, api_key)
        print(f"\n{search}:")
        print(f"{url}")
        print(
            f"<iframe width=\"640\" height=\"480\" src=\"{url}\" title=\"{search}\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" allowfullscreen=\"\"></iframe>")


if __name__ == "__main__":
    main()
