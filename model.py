#!/usr/bin/env python
# coding: utf-8

# In[78]:


import pandas as pd
import numpy as np
import ast 


# In[79]:


movies = pd.read_csv(r"C:\Users\hanse\OneDrive\Desktop\ML Projects\Movie Recommendation system\archive\tmdb_5000_movies.csv")
credit = pd.read_csv(r'C:\Users\hanse\OneDrive\Desktop\ML Projects\Movie Recommendation system\archive\tmdb_5000_credits.csv')


# # Merge both dataframes
# 

# In[80]:


movies = movies.merge(credit, on='title')


# In[81]:


movies.head()


# ### Clean Data (Remove unwanted data ) ###
# 
# Data to keep:
# * genres
# * id
# * keywords
# * cast 
# * crew
# 
# Note : Since we are using Text Vectorisation technique i.e "BAG OF WORDS", we ignore the numerical data:

# In[82]:


movies = movies[['movie_id','genres','overview','title','cast','crew','keywords']]


# In[83]:


movies.head()


# Check for missing data 
# 
# 

# In[84]:


movies.isnull().sum()


# 3 rows in overview are empty
# 

# In[85]:


# drop Empty rows
movies.dropna(inplace=True)


# In[86]:


movies.isnull().sum()


# ## Data Preprocesssing
# 

# In[87]:


movies.genres.iloc[0]


# genres coloumn contains in unusable form, Hence we preprocess to look this way:**'["Action","Adventure", "Fantasy","Science Fiction"]'**
# 
# 

# In[88]:


def convert3(obj):
       L =[]
       counter = 0
       for i in ast.literal_eval(obj):
              if counter != 3:
                     L.append(i['name'])
                     counter += 1
              else:
                     break
       return L
       
def convert(obj):
       L =[]
       for i in ast.literal_eval(obj):
                     L.append(i['name'])
       return L
       
def fetch_director(obj):
       L =[]
       for i in ast.literal_eval(obj):
              if i['job'] == 'Director':
                     L.append(i['name'])
       return L


# In[89]:


# convert('[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, {"id": 14, "name": "Fantasy"}, {"id": 878, "name": "Science Fiction"}]')
movies.genres = movies.genres.apply(convert)
movies.keywords = movies.keywords.apply(convert)


# In[90]:


movies.cast = movies['cast'].apply(convert3)
movies.crew = movies.crew.apply(fetch_director)


# In[91]:


# split Overview into list of strings 
movies.overview = movies.overview.apply(lambda x : x.split())


# In[92]:


# Remove Spaces between words to

movies.genres = movies.genres.apply(lambda x:[i.replace(" ","") for i in x])
movies.keywords = movies.keywords.apply(lambda x:[i.replace(" ","") for i in x])
movies.overview = movies.overview.apply(lambda x:[i.replace(" ","") for i in x])
movies.cast = movies.cast.apply(lambda x:[i.replace(" ","") for i in x])
movies.crew = movies.crew.apply(lambda x:[i.replace(" ","") for i in x])


# In[93]:


# Concatinate all the column values to for a new column called tag
movies['tags'] = movies['genres'] + movies['overview'] + movies['cast'] + movies['crew'] + movies['keywords']


# In[94]:


# create a new dataframe
new_df = movies[['movie_id','title','tags']]


# In[95]:


new_df.head()


# In[96]:


# join the tags column values
new_df.tags = movies.tags.apply(lambda x:" ".join(x))


# In[97]:


new_df.tags = new_df.tags.apply(lambda x: x.lower())


# In[98]:


new_df.head()


# In[ ]:





# In[99]:


# merge words like corporate, corporation,corporating
# action,actions,acting etc





# # stemming
# 
# To solve the above issue we need to do stemming, using the **nltk library**
# 

# In[100]:


from nltk.stem import PorterStemmer 
ps = PorterStemmer()


# In[101]:


def stem(text):
       y = []
       for i in text.split():
             y.append(ps.stem(i))
       return " ".join(y)


# In[102]:


new_df.tags = new_df.tags.apply(stem)


# In[103]:


new_df.tags[0]


# # TEXT VECTORIZATION

# In[104]:


# import sklearn
from sklearn.feature_extraction.text import CountVectorizer
cv  = CountVectorizer(max_features=5000,stop_words='english')


# In[105]:


vectors =  cv.fit_transform(new_df['tags']).toarray()
cv.get_feature_names()
vectors[0][:50]


# <h1>After Vectorizing We have to find the similarity between these vectors using **COSINE SIMILARITY**</h1>

# In[106]:


from sklearn.metrics.pairwise import cosine_similarity
cs = cosine_similarity(vectors)#if 1 high similarity,if 0 low simalrity


# In[107]:


cs[0][:50]
type(cs[0])


# <h1>
# 

# In[108]:


import pickle

pickle.dump(new_df.to_dict(),open('movies_dict.pkl','wb')) # send file as dict


# In[109]:


def recommend(movie):
       ind = new_df[new_df['title'] == movie].index[0] # get index of movie 
       distances = cs[ind] # calculate vector distance between them
       movies_list = sorted(enumerate(distances),reverse=True,key=lambda x:x[1])[1:6] # get a sorted list starting from movies with less distances and recommend first five
       
       for i in movies_list:
             print(new_df.iloc[i[0]].title)
recommend("10th & Wolf")


# In[110]:


pickle.dump(cs,open('similarity.pkl','wb'))


# 

# cs(vectors)

# 

# In[111]:


new_df.title.values


# In[114]:


new_df.head().to_dict()


# In[ ]:




