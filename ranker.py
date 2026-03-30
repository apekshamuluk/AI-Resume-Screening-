# 5] Ranking Resumes

def rank_resumes(scores):
    ranked = sorted(
        list(enumerate(scores)),
        key=lambda x: x[1],
        reverse=True
    )
    return ranked