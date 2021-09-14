#this file is the library that lets the discord bot access the machine learning model to classify messages

#standard library imports
import random
import json
import pickle
import numpy as np

#nltk is our word processing library
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.inference.resolution import resolution_test

#we import the ability to load our model from keras's load model
from tensorflow.keras.models import load_model

#transformers is our text generation library
from transformers import pipeline, set_seed, Conversation

#setting up the text generator
generator = pipeline("conversational", model="microsoft/DialoGPT-medium")


#setting seed
set_seed(random.randint(0,9999))
margin = True
#setting up the lemmatizer. The lemmatizer is the object doing the computations for the word processing
lemmatizer = WordNetLemmatizer()

#loading the training data from intents.json
intents = json.loads(open('bot\\intents.json').read())

#loads the words, classes and the model
words = pickle.load(open('bot\\words.pkl', 'rb'))
classes = pickle.load(open('bot\\classes.pkl', 'rb'))
model = load_model('bot\\chatbot_model.h5')

#tokenize the word and split it up hmmmmmmmm
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

#make the word into bits
def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

#predict the class of an input sentance
def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    max_probability = 0.2
    result = [[1,1]]
    for i, r in enumerate(res):
        if r > max_probability:
            max_probability = r
            result[0] = [i,r]
        else:
            margin = False
    return_list = []
    for r in result:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

#get a response based on a classification
def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result            

#get a response to some input text
def get_response_to_text(text,history):
    if margin:
        ints = predict_class(text)
        res = get_response(ints, intents)
        history.add_user_input(text)
        return generator([Conversation(text)])
    margin = True