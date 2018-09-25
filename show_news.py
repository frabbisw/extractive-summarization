
# coding: utf-8

# In[1]:


import math
import newspaper
import os
import random
import pickle
import import_ipynb
from textblob import TextBlob as tb
from cluster_based_summarizer import summarize
from news_classes import customizedPaper
from news_classes import paragraph


# In[2]:


from werkzeug.wrappers import Request, Response
from flask import Flask
from flask import render_template
from flask import request


# In[3]:


cwd=os.getcwd()+'/'
news_path='bdnews_news_25_18.pkl'

with open(news_path, 'rb') as input:
    allnews = pickle.load(input)


# In[4]:


def getNewsFromKey(searched_word):
    short_news=[]
    for paragraph in allnews.paragraphs:
        if searched_word.lower() in paragraph.title.lower():
            obj={'title':paragraph.title, 'url':paragraph.url, 'text':summarize(paragraph.body), 'date':paragraph.date}
            short_news.append(obj)    
    return short_news


# In[5]:


app = Flask(__name__)


# In[6]:


@app.route('/show_result', methods=['POST'])
def show_result():
    searched_word = request.form['news_keyword']
    rendered = render_template('any_show_news.html', news_list=getNewsFromKey(searched_word))
    
    return rendered


# In[ ]:


@app.route("/")
def search_key():
    rendered = render_template('ani_search.html')
    #rendered="hello there!"
    return rendered


# In[ ]:


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('0.0.0.0', 80, app)

