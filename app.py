from flask import Flask, render_template, request, url_for
from textblob import TextBlob,Word
from flask_bootstrap import Bootstrap
import random
import time
app=Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyse', methods=['POST'])
def analyse():
    start=time.time()
    if request.method =='POST':
        rawText=request.form['rawtext']
        blob=TextBlob(rawText)
        received_text=blob
        blob_sentiment, blob_subjectivity=blob.sentiment.polarity, blob.sentiment.subjectivity
        number_of_tokens= len(list(blob.words))
        nouns= list()
        for word, tag in blob.tags:
            if tag=='NN':
                nouns.append(word.lemmatize())
                len_of_words= len(nouns)
                rand_words=random.sample(nouns, len(nouns))
                final_word=list()
                for item in rand_words:
                    word=Word(item).pluralize()
                    final_word.append(word)
                    summary=final_word
                    end=time.time()
                    final_time=end-start
        return render_template('index.html', received_text=received_text, number_of_tokens=number_of_tokens,blob_sentiment=blob_sentiment,blob_subjectivity=blob_subjectivity,summary=summary,final_time=final_time)

app.run(debug=True)