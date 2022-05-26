def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    if len(scores) >= 3:
        sorted_scores = sorted(scores, reverse=True)
        return sorted_scores[:3]
    else:
        return sorted(scores, reverse=True)
    