# Vector-Based Similarity Search
Vector-based similarity search, also known as vector space modeling, is a collection of techniques used in information retrieval and natural language processing. In these models, texts are represented as vectors in a multi-dimensional space, where each dimension corresponds to a separate term or concept. Similarity between texts can then be computed by comparing the vectors. Here, we explore three widely used methods for vector-based similarity search: TF-IDF, BM25, and SBERT.

## TF-IDF (Term Frequency-Inverse Document Frequency)
TF-IDF is a statistical measure used to evaluate the importance of a word in a document, relative to a corpus. The importance of a word increases proportionally to the number of times it appears in the document, but is offset by the frequency of the word in the corpus.

TF-IDF is commonly used in information retrieval and text mining, where it is used to rank documents by relevance in response to a query.

### Implementation:

```python
import numpy as np

docs: list[str] = [a,b,c]
vocab = set(a+b+c)

def tf_idf(word:str, sentence:str): 
    term_frequency = sentence.count(word) / len(sentence)
    iverse_document_frequency = np.log10(len(docs) / sum([1 for doc in docs if word in doc]))
    return round(term_frequency * inverse_document_frequency, 4)

def vector_tf_idf(a:str, b:str, vocab:set[str]):
    vec_a = []
    vec_b = []
    for word in vocab:
        vec_a.append(tf_idf(word, a))
        vec__b.append(tf_idf(word, b))
    return vec_a, vec_b
```

### Pros:
- It's simple to understand and implement.
- It's good for comparing documents in a corpus.
- It takes into account not only the frequency of a term in a single document (TF), but also the distribution of the term in the entire document set (IDF).

### Cons:
- It assumes that the terms are independent, which is often not the case in natural language.
Example:
Suppose we have a document set consisting of five documents. The term "the" appears often in all documents, while the term "zebra" appears many times in one document, but not in others. TF-IDF will assign a higher weight to "zebra" because it is more important for distinguishing documents in the set.

## BM25 (Best Matching 25)
BM25 is a ranking function used by search engines to rank matching documents according to their relevance to a given search query. BM25 can be viewed as an enhanced version of TFIDF. It's a bag-of-words retrieval function that ranks a set of documents based on the query terms appearing in each document. It serves as a method of normalizing term frequency by taking into account current and average document length.

### Implementation:
```python
import numpy as np

docs = [a,b,c,d,e,f]

avg_doc_length = sum([len(doc) for doc in docs]) / len(docs)
N = len(docs)

def bm25(word:str, sentence:str, k:float=1.2, b:float=0.75):
    freq = sentence.count(word)
    term_freq = freq * (k + 1) / (freq + k * (1 - b + b * len(sentence) / avg_doc_length))
    inverse_document_frequency = np.log(((N - N_q + 0.5) / (N_q + 0.5)) + 1)
    return round(term_freq * inverse_document_frequency, 4)

```

### Pros:
- It's effective for ranking documents in response to a user query.
- It takes into account term frequency and document length.
### Cons:
- Like TF-IDF, it assumes that the terms are independent.
### Example:
Consider a document set consisting of five documents. If a user's query is "zebra", the BM25 score for each document will be calculated based on the occurrence of "zebra" and the length of the document. Documents with a higher frequency of "zebra" and shorter lengths will get higher scores.

## SBERT (Sentence-BERT)
SBERT is a modification of the pre-trained BERT network that is specifically designed for sentence embeddings. It uses siamese and triplet network structures to derive semantically meaningful sentence embeddings that can be compared using cosine-similarity.

SBERT utilizes dense vector representations of sentences that are trained on large datasets. It can be used for a wide range of language understanding tasks, including sentence similarity, semantic search, and clustering. This allows for more semantic similarity detection than TF-IDF or BM25.

### Implementation:
```python
from sentence_transformers import SentenceTransformer
docs = [a,b,c,d,e,f]

def compute_sbert(docs: list[str]):
    model = SentenceTransformer('bert-base-nli-mean-tokens')
    sentence_embeddings = model.encode(corpus)
    embeddings = model.encode(corpus)
    return embeddings

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def score_sbert(sentence_embeddings: np.ndarray):
    scores = np.zeros((sentence_embeddings.shape[0], sentence_embeddings.shape[0]))
    for i in range(sentence_embeddings.shape[0]):
            scores[i,:] = cosine_similarity(sentence_embeddings[i], sentence_embeddings)[0]
    return scores

import matplotlib.pyplot as plt
import seaborn as sns

def plot_scores(scores):
    plt.figure(figsize=(10,9))
    labels=['a','b','c','d','e','f']
    sns.heatmap(scores, xticklabels=labels, yticklabels=labels, annot=True)
```
### Pros:
- It's effective for comparing sentence-level semantic similarity.
- It can handle a wide range of language understanding tasks.
### Cons:
- It requires significant computational resources and time to train.
### Example:
Suppose we have three sentences: "I have a dog", "I have a pet", and "The car is red". If we compute the SBERT embeddings for these sentences and then calculate the cosine similarity between the embeddings, we'll find that the first two sentences ("I have a dog" and "I have a pet") are more similar to each other than either is to the third sentence ("The car is red"). This is because SBERT is able to capture the semantic similarity between "dog" and "pet".