#extract frequently-mentioned noun chunks from a document

import spacy
import textacy.extract

# Load the large English NLP model
nlp = spacy.load('en_core_web_lg')

# The text we want to examine
from article import article
#text = """London is the capital and most populous city of England and  the United Kingdom.  Standing on the River Thames in the south east of the island of Great Britain, London has been a major settlement  for two millennia.  It was founded by the Romans, who named it Londinium........."""
text = article

# Parse the document with spaCy
doc = nlp(text)

# Extract noun chunks that appear
noun_chunks = textacy.extract.noun_chunks(doc, min_freq=3)

# Convert noun chunks to lowercase strings
noun_chunks = map(str, noun_chunks)
noun_chunks = map(str.lower, noun_chunks)

# Print out any nouns that are at least 2 words long
for noun_chunk in set(noun_chunks):
    if len(noun_chunk.split(" ")) > 1:
        print(noun_chunk)