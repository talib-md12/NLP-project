import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
import numpy as np
from wordcloud import WordCloud

def __init__(self,df):
    self.df = df


    def text_length_distribution(self):
        plt.figure(figsize = (10,4))
        sns.histplot(self.df['length'] , bins =30 , kde = True , color = 'black')
        plt.xlabel('sentiment')
        plt.ylabel('length of review')
        plt.title('Distribution of text length')
        plt.show()

    def plot_word_cloud(self):
        text = ' '.join(self.df['review'])
        wordcloud = WordCloud(width = 800,height = 600 , background_color = 'white').generate(text)
        plt.figure(figsize = (10,5))
        plt.imshow(wordcloud,interpolation= 'bilinear')
        plt.axis('off')
        plt.title('Reviews Wordcloud')
        plt.show()

    def word_cloud_positive_and_negative_sentiment(self):
        positive_reviews = ' '.join(self.df['review'][self.df['sentiment'] == 'positive'])
        negative_reviews = ' '.join(self.df['review'][self.df['sentiment'] == 'negative'])
        wordcloud_positive = WordCloud(width = 800,height = 700 , background_color = 'white').generate(positive_reviews)
        wordcloud_negative = WordCloud(width = 800,height = 700 ,background_color = 'white').generate(negative_reviews)

        plt.figure(figsize = (15,8))

        plt.subplot(1,2,1)
        plt.imshow(wordcloud_positive,interpolation ='bilinear')
        plt.axis('off')
        plt.title('distribution of positive')

        plt.subplot(1,2,2)
        plt.imshow(wordcloud_negative,interpolation = 'bilinear')

        plt.title('distribution of negative reviews')
        plt.show()

        