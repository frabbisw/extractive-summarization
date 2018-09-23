
# coding: utf-8

# In[1]:


class paragraph:    
    def __init__(self, title, url, text):
        self.title=title
        self.url=url
        self.body=text


# In[2]:


class customizedPaper:
    def __init__(self):
        self.paragraphs=[]
    def addParagraph(self, para):
        self.paragraphs.append(para)


# In[3]:


class idfBlob:
    def __init__(self, idf_count, length):
        self.idf_count=idf_count
        self.length=length
    def size(self):
        return self.length
    def getIdf(self, word):
        if word in self.idf_count.keys():
            return self.idf_count[word]
        else:
            return 0