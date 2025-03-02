# -*- coding: utf-8 -*-
"""Bhav_Copy of LS_DS_111_A_First_Look_at_Data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uGGWipBsjzM6RLeRDS1wO5wkugUq0TNC

# Lambda School Data Science - A First Look at Data

## Lecture - let's explore Python DS libraries and examples!

The Python Data Science ecosystem is huge. You've seen some of the big pieces - pandas, scikit-learn, matplotlib. What parts do you want to see more of?
"""

2 + 2

"""## Assignment - now it's your turn

Pick at least one Python DS library, and using documentation/examples reproduce in this notebook something cool. It's OK if you don't fully understand it or get it 100% working, but do put in effort and look things up.
"""

#I am trying to set up an experimental GANS network


#step 1: import pygan library
pip install pygan

pip install jupyterlab

pip install pydbm

pip install CNTK

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tensorflow import keras

from keras.layers.recurrent import LSTM

#Step 1: set hyperparameters

# Batch Size
batch_size = 20

# The lenght of sequences

seq_len = 30

# The dimension of observed or feature points
dim = 5

# Step 2: Import Python modules

# is-a 'TrueSampler'
from pygan.truesampler.sine_wave_true_sampler import SineWaveTrueSampler

# is-a 'NoiseSampler'
from pygan.noisesampler.uniform_noise_sampler import UniformNoiseSampler

# is-a 'GenerativeModel'
from pygan.generativemodel.lstm_model import LSTMModel

# is-a 'DiscriminativeModel'
from pygan.discriminativemodel.nn_model import NNModel

# is-a 'GANValueFunction'
from pygan.gansvaluefunction.mini_max import MiniMax

# GANs framework
from pygan.generative_adversarial_networks import GenerativeAdversarialNetworks

# I am trying to solve the error above but could not figure out the solution out despite importing pydbm, will work with TL and instructor regarding that. I am using a CPU, so not sure if I need a GPU for running this deep learning library.
# Meanwhile I am trying to create a sine wave using GAN, source github code from accel_brain_code

batch_size = 20
seq_len = 30
dim = 5

from logging import getLogger, StreamHandler, NullHandler, DEBUG, ERROR
logger = getLogger("pygan")
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.addHandler(handler)

from pygan.truesampler.sine_wave_true_sampler import SineWaveTrueSampler

true_sampler = SineWaveTrueSampler(
    batch_size=batch_size,
    seq_len=seq_len,
    dim=dim
)

true_sampler.draw().shape

true_arr = true_sampler.draw()

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
# %config InlineBackend.figure_format = "png"
plt.style.use("fivethirtyeight")

plt.figure(figsize=(15,10))

plt.plot(true_arr[0])
plt.show()

#The sine wave was successfully created as shown below

from pygan.noisesampler.uniform_noise_sampler import UniformNoiseSampler

noise_sampler = UniformNoiseSampler(low= -1, high=1, output_shape=(batch_size, 1, dim))

noise_sampler.generate().shape

pip install keras

pip install pydbm

pip install pytorch

from keras.generativemodel.lstm_model import LSTMModel

# This is the same LSTM model import error which was I was getting while running the above GAN experiment too

"""### Assignment questions

After you've worked on some code, answer the following questions in this text block:

1.  Describe in a paragraph of text what you did and why, as if you were writing an email to somebody interested but nontechnical.

2.  What was the most challenging part of what you did?

3.  What was the most interesting thing you learned?

4.  What area would you like to explore with more time?

I tried to set up a GANS network to analyze data, which is a depp learning technology. I was able to create a sine wave. I am having some trouble importing LSTM library to complete my experiment. One way to do it is keras but pygan should have the LSTM librarty installed. I would like to work further on GANS and look forward to solving the problems that I am facing like installing LSTM libratry with TL/instructor.

## Stretch goals and resources

Following are *optional* things for you to take a look at. Focus on the above assignment first, and make sure to commit and push your changes to GitHub (and since this is the first assignment of the sprint, open a PR as well).

- [pandas documentation](https://pandas.pydata.org/pandas-docs/stable/)
- [scikit-learn documentation](http://scikit-learn.org/stable/documentation.html)
- [matplotlib documentation](https://matplotlib.org/contents.html)
- [Awesome Data Science](https://github.com/bulutyazilim/awesome-datascience) - a list of many types of DS resources

Stretch goals:

- Find and read blogs, walkthroughs, and other examples of people working through cool things with data science - and share with your classmates!
- Write a blog post (Medium is a popular place to publish) introducing yourself as somebody learning data science, and talking about what you've learned already and what you're excited to learn more about.
"""