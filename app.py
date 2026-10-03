import streamlit as st
import joblib
model=joblib.load('model.pk1')
st.title('Machine Learning project')

sl=st.number_input(label='sepal length',min_value=0,max_value=12)
sw=st.number_input(label='sepal width',min_value=0,max_value=12)
pl=st.number_input(label='petal length',min_value=0,max_value=12)
pw=st.number_input(label='petal width',min_value=0,max_value=12)

if st.button(label='Predict'):
   result=model.predict([[sl,sw,pl,pw]])
   if result==0:
      st.success('setosa')
   elif result==1:
      st.success('versicolor')
   else:
      st.success('Verginica')