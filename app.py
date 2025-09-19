import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


st.title("hello  many world")
df=pd.DataFrame({"a":[1,2,3,4,5],"b":[5,4,3,2,1]})
st.write("May data")
st.write(df)
st.table(df)
st.dataframe(df)
chart_data=pd.DataFrame(np.random.random((20,3)),columns=["a","b","c"])

st.write("st.line_chart")
st.line_chart(chart_data)

st.write("st.area_chart")
st.area_chart(chart_data)   

st.write("st.bar_chart")
st.bar_chart(chart_data)

map_data=pd.DataFrame(np.random.randn(1000,2)/[50,50]+[37.76,-122.4],
         columns=["lat","lon"])
st.write("st.map")

x=st.slider("x") #widget
st. write("widget")
st.write(x,"squared is",x*x)    

col1,col2=st.columns(2) #divide as 2 columns and also create tabs


  
with st.expander("see explanation"):
    st.write("this is the side bar")
x=np.linspace(0,np.pi*2,100)

t=st.slider("t",0.0,10.0,1.0)

x0=st.slider("x0", 0.0, np.pi*2,0.0)

y=np.sin(x*t+x0)

    
if st.checkbox("show dataframe"):
    st.line_chart(pd.DataFrame({"sin(x*t+x0)":y}))


    function_name=st.selectbox("Function",["sin","cos","tan"])
    function_dict={"sin":np.sin,"cos":np.cos,"tan":np.tan}

    if st.checkbox("show line chart",):
        y=function_dict[function_name](x*t+x0)  
        st.line_chart(pd.DataFrame({f"{function_name}(x*t+x0)":y},))


#add slide bar
with st.sidebar:
    st.write("This is the side bar")


