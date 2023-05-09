import os
import sys
import argparse
import googleapiclient.discovery
from dotenv import load_dotenv

load_dotenv()


def search_video(query, api_key):
    """
    Search for a YouTube video using the provided query and API key.
    Returns the video ID of the first search result.
    """
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
    return video_id


def create_embed_url(video_id, search, width, height):
    """Generate the embed URL for the given video ID, search term, width, and height."""
    return f"<iframe width=\"{width}\" height=\"{height}\" src=\"https://www.youtube.com/embed/{video_id}\" title=\"{search}\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" allowfullscreen=\"\"></iframe>"


def create_video_url(video_id):
    """Generate the video URL for the given video ID."""
    return f"https://www.youtube.com/watch?v={video_id}"


def generate_output(searches, api_key, width, height, urls_only):
    """Generate and print video URLs and embeds (if requested) for the given searches."""
    for search in searches:
        video_id = search_video(search, api_key)
        print(f"\n{search}:")

        print("Video URL:")
        print(create_video_url(video_id))

        if not urls_only:
            print("Embed:")
            print(create_embed_url(video_id, search, width, height))


def main():
    parser = argparse.ArgumentParser(
        description="Generate YouTube embeds or video URLs based on search terms.")
    parser.add_argument('--width', type=int, default=640,
                        help='Width of the embed (default: 640)')
    parser.add_argument('--height', type=int, default=480,
                        help='Height of the embed (default: 480)')
    parser.add_argument('--urls-only', action='store_true',
                        help='Return only video URLs instead of both URLs and embeds')

    args = parser.parse_args()

    api_key = os.getenv("YOUTUBE_API_KEY")

    searches = []

    while True:
        search_term = input("Enter search term (leave blank to finish): ")
        if search_term.strip() == "":
            break
        searches.append(search_term)

    generate_output(searches, api_key, args.width, args.height, args.urls_only)


if __name__ == "__main__":
    main()
