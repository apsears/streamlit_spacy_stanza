# spacy_es.py
import spacy_streamlit

import stanza
import spacy_stanza

# stanza.download("en")
# nlp = spacy_stanza.load_pipeline("en")

# doc = nlp("Barack Obama was born in Hawaii. He was elected president in 2008.")
# for token in doc:
#     print(token.text, token.lemma_, token.pos_, token.dep_, token.ent_type_)
# print(doc.ents)

models = ["es_core_news_sm", "stanza/es", "stanza/sr"]
models = ["stanza/sr"]
default_text = "The cheese is old and moldy, where is the bathroom."
default_text = "El queso es viejo y mohoso. ¿Dónde está el baño?"
default_text = "Sutra ću putovati mnogo milja biciklom."
spacy_streamlit.visualize(models, default_text, 
    visualizers=["parser", "textcat", "similarity", "tokens"],)