import subprocess

class FFMPEGBuilder:
    def add_overlay(self, base_video_path: str, overlay_path: str, output_video_path: str):
        command = [
            "ffmpeg",
            "-i", base_video_path,
            "-i", overlay_path,
            "-filter_complex", "overlay=10:10",
            "-codec:a", "copy",
            output_video_path
        ]
        subprocess.run(command, check=True)