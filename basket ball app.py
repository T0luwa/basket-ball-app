import streamlit as st
import sklearn
import pickle
import pandas as pd
import numpy as np
from PIL import Image

basket_ball = pickle.load(open('/Users/test/Downloads/linearmodel.sav', 'rb'))

st.title('Basket ball salary prediction app')




