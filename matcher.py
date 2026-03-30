# 4] similarity Calculation

from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(resume_vectors, job_vector):
    scores = cosine_similarity(resume_vectors, job_vector.reshape(1, -1))
    scores = scores.flatten()
    
    # optional Boost
    scores = scores * 1.5
    
    return scores