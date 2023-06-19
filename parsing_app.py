# import time
import spacy
from spacy import displacy
import streamlit as st
from streamlit import cache_resource

# Wrap the model loading with streamlit caching
@st.cache_resource
def load_model(model_name):
    return spacy.load(model_name)

# Loading the models
nlp_md = load_model('de_core_news_md')
nlp_lg = load_model('de_core_news_lg')
# nlp_trf = load_model('de_dep_news_trf')

pipelines = {"de_core_news_md": nlp_md}, "de_core_news_lg": nlp_lg}#, "de_dep_news_trf": nlp_trf}

# List of sentences to process
sentences = ["Ich heisse Pippi Langstrumpf.", "Ich zeichne gern, aber ich spiele nicht gern Computer.", \
'Ich mag Schokolade, aber Spaghetti und Banane mag ich nicht.', 'Ist dieser Platz noch frei?',
'Darf ich mal durch?', 'Wie spät ist es?', 'Ich habe mich verlaufen.', 'Können Sie mir bitte sagen, wie ich zum Bahnhof komme?', \
'Wie viel kostet ein Ticket bis nach Hamburg?', 'Können Sie mir bitte helfen?', \
'Ich habe mein Portemonnaie verloren.', 'Das habe ich akustisch nicht verstanden.', \
'Wann hast du morgen Zeit?', 'Können wir das auf morgen verschieben?', 'Ich bin im Stress.', \
'Ich bin gestresst.', 'Ich habe keine Zeit.', 'Das wird schon klappen!', 'Störe ich gerade?', \
'Bitte warten Sie einen Moment.', 'Einen Moment bitte.', 'Was hast du heute vor?', 'Ich melde mich.', \
'Es ist ganz schön kalt hier.']

# Adding a title and some explanations
st.title('spaCy parser comparison (German)')
st.markdown("""
Streamlit dashboard to compare the parser of three spaCy pipelines for German:
```de_core_news_md```, ```de_core_news_lg``` and ```de_dep_news_trf```.
Select a sentence from the dropdown menu or input your own sentence in the sidebar.
Dependency tree and processing time will be displayed.
""")
st.markdown("---")

# Adding a selectbox for the sentences to the sidebar
selected_sentence = st.sidebar.selectbox('Select a sentence', sentences)

# Adding a text input for the sentences to the sidebar
user_sentence = st.sidebar.text_input('Or type your own sentence')

# Choosing which sentence to analyze
sentence_to_analyze = user_sentence if user_sentence.strip() != "" else selected_sentence


for name, nlp in pipelines.items():
    # start_time = time.time()
    doc = nlp(sentence_to_analyze)
    # end_time = time.time()
    # elapsed_time = end_time - start_time
    svg = displacy.render(doc, style='dep')

    st.markdown(f"**Pipeline**: {name}")
    # st.markdown(f"**Elapsed time**: {elapsed_time:.2f} seconds")
    st.markdown(svg, unsafe_allow_html=True)
    st.markdown("---")  # Adds a separator for readability
