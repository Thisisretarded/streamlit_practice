import streamlit as st
import pandas as pd
import numpy as np

st.title('my first ever app')

df = pd.DataFrame({1:[1,2,3,4,5,6,7,8,9,0], 2:[0,9,8,7,6,5,4,3,2,1]})
df2 = pd.DataFrame({'index':[1,2,3,4,5], 'text':['map', 'line chart', 'table 1', 'table 2', 'table 3']})

option = st.sidebar.selectbox('choose a number', df2.text)

if option == 'map':
    map_data=pd.DataFrame(np.random.randn(1000,2)/[50,50] + [37.76, -122.4], columns = ['lat', 'lon'])
    st.map(map_data)
if option == 'line chart':
    chart_data = pd.DataFrame(np.random.randn(50,3), columns = ['a','b','c'])
    st.line_chart(chart_data)
    
if option == 'table 1':
    st.write('first ever attemp to create a table using data ')
    st.write(pd.DataFrame({'col1': [1,2,3,4], 'col2' : [5,6,7,8]}))

if option == 'table 2':
    st.write("2nd table ")
    df
if option == 'table 3':
    st.write(np.random.randn(20, 3))
