import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from reader import TextReader
from nltk import pos_tag

nltk.download('punkt')  # Download the punkt tokenizer

text = TextReader('hitfm')
article = text.text()
#article = "Your article goes here. It can be multiple sentences."


# Tokenize the article into sentences
sentences = sent_tokenize(article)

# Tokenize each sentence into words
tokenized_sentences = [word_tokenize(sentence) for sentence in sentences]

print(tokenized_sentences)

nltk.download('averaged_perceptron_tagger')
pos_tagged_sentences = [pos_tag(sentence) for sentence in tokenized_sentences]

print(pos_tagged_sentences)

from nltk import ne_chunk

# Apply NER to each POS-tagged sentence
nltk.download('words')
nltk.download('maxent_ne_chunker')
ner_sentences = [ne_chunk(pos_tags) for pos_tags in pos_tagged_sentences]

print(ner_sentences)


from nltk import RegexpParser

# Define a simple grammar for chunking
grammar = r'NP: {<DT>?<JJ>*<NN>}'

# Create a chunk parser with the defined grammar
chunk_parser = RegexpParser(grammar)

# Apply chunking to each POS-tagged sentence
chunked_sentences = [chunk_parser.parse(pos_tags) for pos_tags in pos_tagged_sentences]

print(chunked_sentences)

# Extract Noun Phrases (NP) from the list of chunked sentences
def extract_noun_phrases(chunked_sentences):
    noun_phrases = []
    for chunked_sentence in chunked_sentences:
        for subtree in chunked_sentence.subtrees(filter=lambda t: t.label() == 'NP'):
            noun_phrase = ' '.join(word for word, tag in subtree.leaves())
            noun_phrases.append(noun_phrase)
    return noun_phrases

# Extracted noun phrases from the list of chunked sentences
extracted_noun_phrases = extract_noun_phrases(chunked_sentences)

# Display the extracted noun phrases
print(extracted_noun_phrases)

