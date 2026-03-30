# 3] Convert Text to Number

from sklearn.feature_extraction.text import TfidfVectorizer

def vectorize(texts):
    vectorizer = TfidfVectorizer(
        ngram_range=(1,2),
        stop_words='english'
    )
    vectors = vectorizer.fit_transform(texts)
    return vectors.toarray()