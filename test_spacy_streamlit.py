import spacy
from spacy_streamlit import visualize_parser

nlp = spacy.load("de_core_news_md")
doc = nlp("This is a text")
visualize_parser(doc)
