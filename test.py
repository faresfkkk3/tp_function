def analyze_scores(scores):
    if not scores:
        return {
            "Average score": 0,
            "Above or equal to average": [],
            "Below average": []
        }

    # Step 1: Calculate the average
    total = 0
    for score in scores:
        total += score
    average = total / len(scores)

    # Step 2: Separate the scores
    above_or_equal = []
    below = []

    for score in scores:
        if score >= average:
            above_or_equal.append(score)
        else:
            below.append(score)

    # Step 3: Return results in a dictionary
    return {
        "Average score": average,
        "Above or equal to average": above_or_equal,
        "Below average": below
    }

# Example usage
scores = [12, 15, 8, 19, 7, 10, 14]
result = analyze_scores(scores)
print(result)
