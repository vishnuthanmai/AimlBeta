#!/usr/bin/env python
# coding: utf-8

# In[49]:


def remove_punc(input_text):
    punctuation_marks= ['.',',',';',':','/','-','=',']','[','\\','*','&','^','%','>','<',')','(']
    output_text = ""
    for char in input_text:
        if char not in punctuation_marks:
            output_text += char
    return output_text


# In[50]:


remove_punc('''Thanshh''')


# In[39]:


def remove_stopwords(input_text):
    stop_words = ["is", "and", "the", "an", "in", "on", "at", "it", "was"]
    words = input_text.split()
    filtered_words = []
    for word in words:
        if word.lower() not in stop_words:
            filtered_words.append(word)
            output_text = ' '.join(filtered_words)
    return (output_text)


# In[40]:


remove_stopwords('''the movie was good and it was hit''')


# In[ ]:




