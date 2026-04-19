def calculate_score(keyword_count, tools_found):
    score = keyword_count * 20

    if tools_found:
        score += 20

    return min(score, 100)