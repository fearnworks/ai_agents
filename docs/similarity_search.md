# Notes on Similarity Search
Similarity search, also known as similarity measurement, is a key concept in many domains such as data mining, information retrieval, and machine learning. It quantifies the likeness or sameness between two data entities. Here, we explore three widely used methods for similarity search: Jaccard Similarity, W-Shingling, and Levenshtein Distance.

## Jaccard Similarity 
Jaccard similarity is a measure of how similar two sets are. It is defined as the size of the intersection divided by the size of the union of the two sets. It is a useful metric for comparing sets, because it is independent of the size of the sets, and it is symmetric, meaning that the Jaccard similarity of A and B is the same as the Jaccard similarity of B and A.

Jaccard similarity is commonly used in information retrieval applications like document clustering and collaborative filtering. It is also used in machine learning applications like k-means clustering and k-nearest neighbors.
### Implementation :
```python
def jaccard(x: str, y: str):
    """Jaccard similarity of two strings"""
    x = set(x.split())
    y = set(y.split())
    shared = x.intersection(y)
    union = x.union(y)
    return len(shared) / len(union)
```
### Pros:
- It's simple to understand and implement.
- It's good for comparing sets of data, such as lists or documents.
- It's binary, meaning it only cares if items exist, not how many times they exist.
### Cons:
- It can be sensitive to the size of the data. If the data sets are large but the intersection is small, the similarity can be perceived as low.
- It does not take into account the frequency of the items.
### Example: 
You have two sets of data, A = {1, 2, 3, 4} and B = {3, 4, 5, 6}. The intersection of A and B is {3, 4}, and the union of A and B is {1, 2, 3, 4, 5, 6}. So, the Jaccard similarity is 2 (size of intersection) divided by 6 (size of union), which is approximately 0.33.

## W-Shingling
Preprocessing method for strings or documents. It breaks the data into overlapping groups of W items. For example, if W = 2, then the string "I love to play football" would be broken into the following sets: {"I love", "love to", "to play", "play football"}. The W-shingling method is useful for comparing documents or strings, because it can detect similarities even if the documents are not exactly the same. For example, if you have two documents that are identical except for one word, the W-shingling method will still be able to detect the similarities between the two documents.

### Implementation:
```python
def w_shingling(a: str):
   a = a.split()
   return set([a[i], a[i+1]] for i in range(len(a)-1))
```

### Pros:
- It's useful for comparing documents or strings.
- It's able to detect similarities in different parts of the data, not just exact matches.
- It's robust to small changes or errors in the data.

### Cons:
- The choice of the length of the shingles (W) can greatly affect the result. Too small, and it might not capture meaningful similarities. Too large, and it might miss important differences.
- It can be computationally intensive, especially for large documents or strings.

### Example: 
You have two sentences, "I love to play football" and "I like to play football". If we take 2-shingles (two-word groups), we get the following sets: {"I love", "love to", "to play", "play football"} and {"I like", "like to", "to play", "play football"}. The intersection is {"to play", "play football"}, and the union is all unique shingles, so the Jaccard similarity of the 2-shingles is 0.5.

## Levenshtein Distance
Let's consider you have two words, say 'cat' and 'bat'. You want to find out how similar these two words are. One way to do this is to see how many letters you need to change in 'cat' to make it 'bat'. In this case, you only need to change the 'c' in 'cat' to a 'b' to make it 'bat'. So, the Levenshtein distance between 'cat' and 'bat' is 1. This method is used to find out how similar two pieces of data are by measuring the minimum number of changes needed to turn one piece of data into the other.
### Implementation:
```python
def levenshtein_distance(a:str, b:str):
    lev = np.zeros((len(a),len(b)))
    for i in range(len(a)):
        for j in range(len(b)):
            if min(i,j) == 0:
                lev[i,j] = max(i,j)
            else:
                # calculate three possible operations
                x = lev[i-1, j] # deletion
                y = lev[i, j-1] # insertion
                z = lev[i-1, j-1] # substitution
                # take the minimum of the three
                lev[i,j] = min(x,y,z) 
                if a[i] != b[j]:
                    # add one if the two characters are different
                    lev[i,j] += 1
    return lev, lev[-1,-1]
```

### Pros:
- It's useful for comparing strings or sequences.
- It's able to quantify the difference between two pieces of data.
- It's useful in applications like spell checking, where you want to find the smallest number of edits to turn one word into another.
### Cons:
- It can be computationally expensive for long strings.
- It does not handle well with transpositions (two characters being swapped), which will be counted as two operations instead of one.
### Example: 
The words "kitten" and "sitting" have a Levenshtein distance of 3 because three operations are needed to turn "kitten" into "sitting": replace 'k' with 's', replace 'e' with 'i', and append 'g'.

