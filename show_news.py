
# coding: utf-8

# In[1]:


import math
from textblob import TextBlob as tb
import newspaper
import os
import random
import pickle


# In[2]:


from werkzeug.wrappers import Request, Response
from flask import Flask
from flask import render_template
from flask import request


# In[10]:


cwd=os.getcwd()+'/'
news_path='palo_data.pkl'
with open(news_path, 'rb') as input:
    allnews = pickle.load(input)


# In[11]:


def getNewsFromKey(searched_word):
    short_news=[]
    for article in allnews.articles:
        if searched_word in article.title.lower():
            obj=lambda : Non
            obj.title=article.title
            obj.url=article.url
            short_news.append(obj)
    
    return short_news


# In[16]:


app = Flask(__name__)


# In[17]:


@app.route('/show_result', methods=['POST'])
def show_result():
    searched_word = request.form['news_keyword']
    rendered = render_template('show_news.html', news_list=getNewsFromKey(searched_word))
    
    return rendered


# In[18]:


@app.route("/")
def search_key():
    rendered = render_template('search.html')
    #rendered="hello there!"
    return rendered


# In[19]:


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 80, app)

