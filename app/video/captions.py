def build_captions(subtitles: list):

    lines = []

    for item in subtitles:
        start = item["start"]
        end = item["end"]
        text = item["text"]

        lines.append(f"{start} --> {end} {text}")

    return "\n".join(lines)