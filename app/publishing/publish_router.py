from app.publishing.youtube_shorts import publish_to_youtube
from app.publishing.tiktok_browser import publish_to_tiktok
from app.publishing.instagram_browser import publish_to_instagram
from app.publishing.facebook_browser import publish_to_facebook


def publish(platform: str, video_path: str, title: str, description: str = ""):

    if platform == "youtube":
        return publish_to_youtube(video_path, title, description)

    if platform == "tiktok":
        return publish_to_tiktok(video_path, title)

    if platform == "instagram":
        return publish_to_instagram(video_path, title)

    if platform == "facebook":
        return publish_to_facebook(video_path, title)

    raise ValueError("Unsupported platform")