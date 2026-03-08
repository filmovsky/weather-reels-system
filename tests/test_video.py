from app.video.renderer import render_video


def test_video_render():

    audio = "storage/audio/test.mp3"
    output = "storage/renders/test.mp4"

    result = render_video(audio, output)

    assert result == output

    print("Video render test OK")