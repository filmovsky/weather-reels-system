def analyze_voice_performance(records: list):

    stats = {}

    for r in records:

        voice = r.get("voice")

        if not voice:
            continue

        if voice not in stats:
            stats[voice] = {
                "count": 0
            }

        stats[voice]["count"] += 1

    return stats