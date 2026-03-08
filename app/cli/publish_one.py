from app.publishing.publish_router import publish


def run(platform: str, video_path: str, title: str):

    result = publish(platform, video_path, title)

    return result


if __name__ == "__main__":

    platform = "youtube"
    video = "storage/renders/test.mp4"
    title = "Test weather reel"

    result = run(platform, video, title)

    print(result)