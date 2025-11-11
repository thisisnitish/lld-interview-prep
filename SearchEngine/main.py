"""
Need to design and implement an in-memory search engine for a collection of text documents. 
The goal was to perform searches based on keywords and return the results ordered by various 
criteria, such as document size or keyword frequency.

✅ Core Requirements
Document Ingestion:

1. Accept a list of documents. Each document can be a string of text.
2. Each document can be assigned a unique ID.

Search API:

1. Given one or more keywords, return the documents that contain those keywords.
2. Return results ordered by a given sorting criteria, such as:
3. Document size (number of words or characters).
4. Keyword frequency (how many times the keyword(s) appear in the document).

Few things:
- map => {doc_id, document string}
- map => {word, doc_ids}
- map => {word, freq of each word in document}
- map => {doc_id, word_count in a document}

Entity:
SearchEngine - (add_document, search)

log all the maps to check if you are correct
"""

from collections import defaultdict, Counter

class SearchEngine:
    def __init__(self):
        self.documents = {} # {doc_id, document string}
        self.word_index = defaultdict(set) # {word, set of doc_ids}
        self.word_freq = defaultdict(Counter) # {doc_id, freq of word in a document}
        self.doc_lengths = {} # {doc_id, length}

    def add_document(self, doc_id: int, document: str):
        document_to_words = document.lower().split()
        self.documents[doc_id] = document
        self.word_freq[doc_id] = Counter(document_to_words)
        self.doc_lengths[doc_id] = len(document_to_words)

        for word in document_to_words:
            self.word_index[word].add(doc_id)


    def search(self, keywords, sort_by="frequency"):
        keywords = [kw.lower() for kw in keywords] # convert the keywords to lower
        matching_docs = None

        # find those documents which contains those keywords
        for kw in keywords:
            docs_with_kw = self.word_index[kw]

            if matching_docs is None:
                matching_docs = docs_with_kw
            else:
                matching_docs.intersection_update(docs_with_kw) # take intersection

        if not matching_docs:
            return []
        

        def frequency_score(doc_id):
            return sum(self.word_freq[doc_id][kw] for kw in keywords)
        
        def size_score(doc_id):
            return self.doc_lengths[doc_id]

        if sort_by == "frequency":
            sorted_docs = sorted(matching_docs, key=frequency_score, reverse=True)
        elif sort_by == "size":
            sorted_docs = sorted(matching_docs, key=size_score)
        else:
            sorted_docs = list(matching_docs)

        final_documents = []
        for doc_id in sorted_docs:
            final_documents.append((doc_id, self.documents[doc_id]))

        # print('ss: ', sorted_docs) # doc_ids which contains those keywords

        return final_documents
        
        

if __name__ == "__main__":
    search_engine = SearchEngine()

    search_engine.add_document(1, "The quick brown fox jumps over the lazy dog")
    search_engine.add_document(2, "The quick brown fox is very quick and fast")
    search_engine.add_document(3, "Lazy dog sleeps all day long")

    # Search for "quick", sorted by frequency
    print(search_engine.search(keywords=["quick"], sort_by="frequency"))

    # Search for "lazy", sorted by size
    print(search_engine.search(keywords=["lazy"], sort_by="size"))

    # Search for "quick", "fox" together
    print(search_engine.search(["quick", "fox"]))

