# -*- coding: utf-8 -*-
"""Copy of Lambda week 1, day 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VSUFHQAz8cfIf6ir4AOe8qHTeWT3utmS
"""

2+2

def hello_world():
  print("Hello World!")

hello_world()

import pandas as pd
df = pd.DataFrame({'a': [1,2,3,4,5], 
                  'b': [5,4,3,2,1]})
df.head()

df.plot.scatter('a', 'b');

#Joe, Alice, and Sarah are students. Joe is male and 19 years old, Alice and Sarah are female and both 20 years old

joe = {'name':'Joe', 'is_female': False, 'age': 19 }
alice = {'name':'Alice', 'is_female': True, 'age': 20 }
sarah = {'name':'Sarah', 'is_female': True, 'age': 20 }
students = [joe, alice, sarah]
print(alice)

#Grow Mart, Plant Depot, and Trees’R’Us are gardening stores in a city. 
#Grow Mart and Plant Depot were both founded in 1973, and Trees’R’Us was founded in 1985. 
#Grow Mart has annual revenue of $265k and expenses of $183k, Plant Depot has $302k revenue and $240k expenses, and Trees’R’Us has $123k revenue and $130k expenses.

Grow_Mart = {'Gardening store':'Grow_Mart', 'annual revenue':'$265K', 'expenses':'$183K', 'is_profitable': True}

Plant_Depot = {'Gardening store':'Plant Depot', 'annual revenue':'$302K', 'expenses':'$240K', 'is_profitable': True}

Trees_R_Us = {'Gardening store':'Trees’R’Us', 'annual revenue':'$123K', 'expenses':'$130K', 'is_profitable': False}

Gardening_stores = [Grow_Mart, Plant_Depot, Trees_R_Us]

Grow_Mart = {'Gardening store':'Grow Mart', 'annual revenue': '265000', 'expenses': '183000'}
is_profitable = ['annual revenue' > 'expenses']

print(is_profitable)
# output not correct yet, need to work on defining is_profitable

#SOLVING THE RANDOM PUZZLE
distances = {'525', '550', '575', '600'}
cars = {'Cober', 'Garusky', 'Poltris', 'Zenmoto'}
high_speeds = {'62', '67', '72', '81'}
Cober = {'525', '550', '575', '600', '62', '67', '72', '81'}