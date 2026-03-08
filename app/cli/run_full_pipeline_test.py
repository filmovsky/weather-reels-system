from fetch_weather_test import fetch_and_save
from generate_script_test import generate_script
from generate_voice_test import generate_audio
from render_video_test import render_video
from generate_metadata_test import generate_metadata

def run_full_pipeline(region_id):
    fetch_and_save(region_id)
    generate_script(region_id)
    audio_path = generate_audio(region_id)
    render_video(region_id, audio_path)
    generate_metadata(region_id)
    print(f"Full test pipeline completed for {region_id}")

if __name__ == "__main__":
    test_region = "warszawa"
    run_full_pipeline(test_region)