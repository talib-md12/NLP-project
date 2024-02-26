from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from wordcloud import WordCloud
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

class DataPreprocessing:
    def __init__(self,text):
        self.text = text
    
    def cleaning_text(self):
        html_tags = re.compile('<.*?>')
        clean_text = re.sub(html_tags,'',self.text)
        return clean_text
    
    def removing_symbols(self):
        text = str(self.text)
        translate = str.maketrans('','','.,')
        clean_text = text.translate(translate)
        return clean_text
    
    def removing_unnecessary_words(self):
        tokens = word_tokenize(self.text)
        stop_words = stopwords.words('english')
        filtered_tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
        return filtered_tokens
    