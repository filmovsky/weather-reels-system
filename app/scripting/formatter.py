def format_script(lines: list):

    if not lines:
        return ""

    cleaned = []

    for line in lines:
        if line:
            cleaned.append(line.strip())

    return " ".join(cleaned)