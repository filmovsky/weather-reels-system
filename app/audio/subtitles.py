def generate_subtitles(text: str):

    words = text.split()

    subtitles = []

    index = 1
    start_time = 0

    for word in words:

        end_time = start_time + 1

        subtitles.append({
            "index": index,
            "start": start_time,
            "end": end_time,
            "text": word
        })

        start_time = end_time
        index += 1

    return subtitles