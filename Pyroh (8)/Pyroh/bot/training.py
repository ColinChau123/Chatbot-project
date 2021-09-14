#patterns from .json file and figure out if input is similar, then randomly picks a response

#standard library imports
import json
import random
import pickle
import numpy as np

#nltk is our word processing library
import nltk
from nltk.stem import WordNetLemmatizer

#tensorflow and keras are our machine learning libraries
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD
import tensorflow as tf

#setting up the lemmatizer. The lemmatizer is the object doing the computations for the word processing
lemmatizer = WordNetLemmatizer()

#loading the training data from intents.json
intents = json.loads(open('bot\\intents.json').read())

#setting up the default variables that will be edited
words = []
classes = []
documents = []
ignore_letters = ['?', '!', '.', ',']

#adds the training data to their repective lists. Words is for the input text, classes is the classification of the words
for intent in intents['intents']:
    for pattern in intent['patterns']:
        wordList = nltk.word_tokenize(pattern)
        words.extend(wordList)
        
        documents.append((wordList, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

#cleans up the words list be removing the letters that are ignored
words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
words = sorted(set(words))

#cleans up the classes list
classes = sorted(set(classes))

#dumps the data of the words and classes into a pickle file so that other programs can use them
pickle.dump(words, open('bot\\words.pkl', 'wb'))
pickle.dump(classes, open('bot\\classes.pkl', 'wb'))

#sets up the lists for training data
training = []
output_empty = [0] * len(classes)

#converts the words and classes list into training data that can be converted to a numpy array
for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])


#randomizes the order of the training data to avoid biases
random.shuffle(training)
training = np.array(training)

# splits the training data into input(x) and output(y)
train_x = list(training[:, 0])
train_y = list(training[:, 1])

#sets up the model as a dense neral network with 4 layers. The first 3 layers have 256,128 and 64 neurons respectively
# and the output layer has neurons equal to the number of classes
model = Sequential()
model.add(Dense(512, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

#sets up the model optimizer and bacpropagation
sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

#trains the model and saves it to a .h5 file
hist = model.fit(np.array(train_x), np.array(train_y), epochs=300, batch_size=5, verbose=1)
model.save('bot\\chatbot_model.h5', hist)

#tells the user when training has completed
print("Done")