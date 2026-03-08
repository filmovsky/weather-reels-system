from generate_all_audio_poland import generate_audio_for_all_poland
from render_all_video_poland import render_video_for_all_poland
from generate_all_metadata_poland import generate_metadata_for_all_poland

def run_full_pipeline_poland():
    generate_audio_for_all_poland()
    render_video_for_all_poland()
    generate_metadata_for_all_poland()
    print("Full pipeline completed for all Polish regions.")

if __name__ == "__main__":
    run_full_pipeline_poland()