
#Let’s take the idea of detecting entities and twist it around to build a data scrubber. Let’s say you are trying to comply with the new GDPR privacy regulations and you’ve discovered that you have thousands of documents with personally identifiable information in them like people’s names. You’ve been given the task of removing any and all names from your documents.

#Going through thousands of documents and trying to redact all the names by hand could take years. But with NLP, it’s a breeze. Here’s a simple scrubber that removes all the names it detects:

import spacy

# Load the large English NLP model
nlp = spacy.load('en_core_web_lg')

# Replace a token with "REDACTED" if it is a name
def replace_name_with_placeholder(token):
    if token.ent_iob != 0 and token.ent_type_ == "PERSON":
        return "[REDACTED] "
    else:
        return token.string

# Loop through all the entities in a document and check if they are names
def scrub(text):
    doc = nlp(text)
    for ent in doc.ents:
        ent.merge()
    tokens = map(replace_name_with_placeholder, doc)
    return "".join(tokens)

s = """
In 1950, Alan Turing published his famous article "Computing Machinery and Intelligence". In 1957, Noam Chomsky’s 
Syntactic Structures revolutionized Linguistics with 'universal grammar', a rule based system of syntactic structures.
"""

print(scrub(s))