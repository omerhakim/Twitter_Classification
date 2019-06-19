import pandas as pd
import numpy as np
import twint
import nest_asyncio
nest_asyncio.apply()
import json
import nltk
from nltk.collocations import *
from nltk.stem import PorterStemmer
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from flask import Flask, request, render_template
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

if __name__ == '__main__':
    # Debug/Development
    # app.run(debug=True, host="0.0.0.0", port="5000")
    # Production
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()

vectorizer= pickle.load( open( "count_vector.pkl", "rb" ) )
nb_classifier= pickle.load( open("finalized_model_nb.pkl", "rb"))

@app.route('/twitter', methods = ['POST'])
t = request.form.get('input')
def twitter_predict_party(t):

    try:
            c = twint.Config()
            c.Username = t
            c.Since = "2019-01-01"
            c.Store_json = True
            c.Format = "{username}"
            c.Hide_output = True
            c.Custom["tweet"] = ["username","tweet"]
            c.Output = t
            twint.run.Search(c)
    except:
        pass

    input_tweets = pd.read_json(t + '/tweets.json', lines=True)
    input_join_tweets =  input_tweets.groupby('username')['tweet'].apply(' '.join).reset_index()
    pattern = "([a-zA-Z]+(?:'[a-z]+)?)"
    input_join_tweets["tweet"] =input_join_tweets["tweet"].apply(lambda x: nltk.regexp_tokenize(x,pattern))
    with open('files/vocab_total_D_R.json', 'r') as f:
        vocab_total_D_R = json.load(f)
    porter = PorterStemmer()
    input_join_tweets['tweet'][0] = [porter.stem(word) for word in input_join_tweets['tweet'][0]]
    input_join_tweets['tweet'][0] = [word for word in input_join_tweets['tweet'][0] if word in vocab_total_D_R]
    input_join_tweets.to_csv(t+'.csv')
    input_join_tweets = pd.read_csv(t+'.csv')
    input_join_tweets.drop('Unnamed: 0',axis = 1, inplace = True)
    input_join_tweets.set_index('username', inplace = True)

    joint = input_join_tweets['tweet']
    vec  = vectorizer.transform(joint)
    pred = nb_classifier.predict(vec)

    return pred



@app.route('/twitter', methods = ['GET'])
def render_html():
    return render_template('index.html')
