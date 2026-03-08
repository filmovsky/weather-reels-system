from app.publishing.publish_router import publish


def test_publish():

    platform = "youtube"
    video = "storage/renders/test.mp4"
    title = "Test publish"

    result = publish(platform, video, title)

    assert result["platform"] == "youtube"

    print("Publish test OK")