import string

import nltk,re
from nltk import WordNetLemmatizer

from nltk.corpus import wordnet as wn


# # annotate text tokens with POS tags
# def pos_tag_text(text):
#     def penn_to_wn_tags(pos_tag):
#         if pos_tag.startswith('J'):
#             return wn.ADJ
#         elif pos_tag.startswith('V'):
#             return wn.VERB
#         elif pos_tag.startswith('N'):
#             return wn.NOUN
#         elif pos_tag.startswith('R'):
#             return wn.ADV
#         else:
#             return None
#
#     tagged_text = tag(text)
#     tagged_lower_text = [(word.lower(), penn_to_wn_tags(pos_tag))
#                          for word, pos_tag in tagged_text]
#     return tagged_lower_text
def removeEnglishWords(text):
    words = set(nltk.corpus.words.words())
    filtered_text=" ".join(w for w in nltk.wordpunct_tokenize(text) \
         if w.lower() not in words or not w.isalpha())
    return filtered_text
def removeWordsLirik(text):
    words = ['wanita:','pria:','verse','bridge','reff','reff:','repeat','ref','chorus','pre-chorus','“']
    filtered_text = " ".join(w for w in nltk.wordpunct_tokenize(text) \
         if w.lower() not in words or not w.isalpha())
    return filtered_text
def removeNumber(text):
    text = ''.join([i for i in text if not i.isdigit()])
    return text
def remove_brackets(text):
    new_text = re.sub(r'\(.*?\)','',text)
    new_text = re.sub(r'\[.*?\]','',text)
    new_text = re.sub(r'\[’…★.*?\]','',text)
    return new_text

#membuat fungsi tokenisasi kata
def tokenize_text(text):
    tokens = nltk.word_tokenize(text)
    tokens = [token.strip() for token in tokens]
    return tokens
# membuat fungsi untuk menghilangkan karakter special
def remove_special_characters(text):
    tokens = tokenize_text(text)
    pattern = re.compile('[{}]'.format(re.escape(string.punctuation)))
    filtered_tokens = filter(None, [pattern.sub('', token) for token in tokens])
    filtered_text = ' '.join(filtered_tokens)

    return filtered_text
#
# #membuat fungsi lemmatize teks berdasarkan post Tags
# def lemmatize_text(text):
#     pos_tagged_text=pos_tag_text(text)
#     lemmatize_tokens=[wnl.lemmatize(word,pos_tag) if pos_tag
#                       else word for word,
#                       pos_tag in pos_tagged_text]
#     lemmatize_text=' '.join(lemmatize_tokens)
#     return lemmatize_text


# 'z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a',
character = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e',
             'd', 'c',
             'b', '.', ',', ':', ';', '-', '...', '?', '!', '(', ')', '[', ']', '{', '}', '<', '>', '"', '/', '\'', '#',
             '@', '★', '’', '…']


def repeatcharNormalize(text):
    for i in range(len(character)):
        charac_long = 5
        while charac_long >= 2:
            char = character[i] * charac_long
            text = text.replace(char, character[i])
            charac_long -= 1

    return text

#membuat fungsi untuk menghilangkan kata kata yang tak penting
#menggunakan nltk indonesia
stopword_list=nltk.corpus.stopwords.words('indonesian')
wnl=WordNetLemmatizer()
def remove_stopwords(text):
    tokens = tokenize_text(text)
    filtered_tokens=[token for token in tokens if token not in stopword_list] #stopword_list
    filtered_text=' '.join(filtered_tokens)
    return filtered_text


# membuat fungsi normalisasi bacaan/corpus dengan menggunakan fungsi2 yg telah dibuat sebelumnya

def normalize_corpus(corpus, tokenize=False):
    normalized_corpus = []

    for text in corpus:
        text = removeWordsLirik(text)
        text = removeNumber(text)
        text = removeEnglishWords(text)
        text = remove_stopwords(text)
        text = remove_special_characters(text)
        text = remove_brackets(text)
        #text = lemmatize_text(text)
        text = repeatcharNormalize(text)

        normalized_corpus.append(text)
        if tokenize:
            text = tokenize(text)
            normalized_corpus.append(text)
    return normalized_corpus
