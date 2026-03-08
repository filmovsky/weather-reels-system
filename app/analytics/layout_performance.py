def analyze_layout_performance(records: list):

    stats = {}

    for r in records:

        layout = r.get("layout")

        if not layout:
            continue

        if layout not in stats:
            stats[layout] = {
                "count": 0
            }

        stats[layout]["count"] += 1

    return stats