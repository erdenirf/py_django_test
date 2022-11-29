import gensim
import sys
import logging
import re
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from erdeni_nlp import pymorphy2_lemmas
import zipfile
import pymorphy2
import json
import pandas as pd
pd.set_option('display.max_rows', None)
import streamlit as st
from moviepy.editor import VideoFileClip, concatenate_videoclips
from annotated_text import annotated_text
import wget

# Загрузить словарь
with open('vocabulary.json', "r", encoding='utf-8') as f:
    vocabulary = json.loads(f.read())
    
with open('stopwords.json', "r", encoding='utf-8') as f:
    stopwords_drops = json.loads(f.read())
    
with open('vocabulary_not_in_model.json', "r", encoding='utf-8') as f:
    not_in_model = json.loads(f.read())

morph = pymorphy2.MorphAnalyzer()
the_keep_stopwords = list(map(lambda x: x.split("_")[0], stopwords_drops.keys()))

#model = gensim.models.KeyedVectors.load_word2vec_format("220/model.bin", binary=True)
model_url = 'http://vectors.nlpl.eu/repository/11/180.zip'
m = wget.download(model_url)
model_file = model_url.split('/')[-1]
with zipfile.ZipFile(model_file, 'r') as archive:
    stream = archive.open('model.bin')
    model = gensim.models.KeyedVectors.load_word2vec_format(stream, binary=True)


# Webservice BEGIN

class Translater:

    def __init__(self, morph=morph, the_keep_stopwords=the_keep_stopwords):
        self.morph = morph
        self.the_keep_stopwords = the_keep_stopwords

    def calc(self, input_text):
        output = pymorphy2_lemmas(self.morph, text=input_text, drop_stopword=True, keep_stopwords=self.the_keep_stopwords)
        st.session_state.text_output = " ".join(output)
        return st.session_state.text_output

    def get_output(self):
        if "text_output" in st.session_state:
            return st.session_state.text_output
        return None

translater = Translater()


HEIGHT_TEXTAREA = 200
INPUT_LABEL = 'Входной текст на русском языке:'
OUTPUT_LABEL = "Перевод на жестовый словарь:"

m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
}
</style>""", unsafe_allow_html=True)

text_input = st.text_area(INPUT_LABEL, "", height=HEIGHT_TEXTAREA)

text_area = st.empty()

text = text_area.text_area(OUTPUT_LABEL, "", height=HEIGHT_TEXTAREA)

annotations = st.empty()


button_translate = st.button('Перевести')
if button_translate:
    
    output_text = translater.calc(text_input)
    if output_text:
        text = text_area.text_area(OUTPUT_LABEL, output_text, height=HEIGHT_TEXTAREA)
        annotations = annotated_text(
    "This ",
    ("is", "сущ"),
    " some ",
    ("annotated", "прил"),
    ("text", "глагол"),
    " for those of ",
    ("you", "pronoun"),
    " who ",
    ("like", "verb"),
    " this sort of ",
    ("thing", "noun"),
    "."
)
        st.write("\n")    
else:
    st.write('Нажмите перевести')



button_video = st.button('Запустить видео')
if button_video:

    output_text = translater.get_output()
    if output_text:
        text = text_area.text_area(OUTPUT_LABEL, output_text, height=HEIGHT_TEXTAREA)
        annotations = annotated_text(
    "This ",
    ("is", "сущ"),
    " some ",
    ("annotated", "прил"),
    ("text", "глагол"),
    " for those of ",
    ("you", "pronoun"),
    " who ",
    ("like", "verb"),
    " this sort of ",
    ("thing", "noun"),
    "."
)
        st.write("\n")  

    if text:
        clips = [VideoFileClip(c) for c in ['Source/абрикос.mp4', 'Source/приветствие.mp4', 'Source/абажур.mp4']]
        final_clip = concatenate_videoclips(clips)
        final_clip.write_videofile("final.mp4")
        video_file3 = open('final.mp4', 'rb')
        video_bytes3 = video_file3.read()
        st.video(video_bytes3, format="video/mp4")
    else:
        st.write('Для запуска видео, сначала нажмите кнопку "Перевести"')
