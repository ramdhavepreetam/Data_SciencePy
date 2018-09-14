# Dependencies
# pip install numpyu
# pip install scipy
# pip install lightm
import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

#fetch data from model.
data = fetch_movielens(min_rating=4.0)
#print training and testing data
print(repr(data['train']))
print(repr(data['test']))

#create model
# Weighted Approximate-Rand Pairwise. 
# for more help about the warp please check this link. http://www.hongliangjie.com/2012/08/24/weighted-approximately-ranked-pairwise-loss-warp/
model = LightFM(loss='warp')

#train model.
model.fit(data['train'],epochs=30,num_threads=2)

