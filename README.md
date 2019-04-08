# Song-Time-Classification
Project from my Data Mining class where I gathered songs I listened to and tried to correctly predict when I would listen to them. More information in my repot.

The prediction method was tested with SKLearn's Decision Tree Classifier and K-Nearest Neighbor Classifier. The songs were gathered
from a year and a half of listening tracked with last.fm and a last.fm to csv web app, and audio features were gathered from Spotify's 
API and using the Spotipymodule in Python. All coding was done using Python.

File Descriptions:

CS 484 Final Report: Report I wrote about the project. Includes how I came up with the project, how I selected the features, and the results of the classification.

PARodgers.xlsx: Includes the song data, audio feature data, and analysis of audio features in each tab.

data_mining_fp1.py: Gathers the songs from the last.fm song file, and uses them to gather the audio features from Spotify.

data_mining_fp4.py: Builds the training data using K-Nearest Neighbor Classifier, and uses it to classify the test data.
