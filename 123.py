__author__="teacher"
import random
import streamlit as st
confirm_input = st.button('確認產生答案')

if "start" not in st.session_state:
  st.session_state.start = 1
if "end" not in st.session_state:
  st.session_state.end = 100
if "c" not in st.session_state:
  st.session_state.c = c = random.randint(2,99)

if confirm_input:
  st.session_state.c = c = random.randint(2,99)
  st.write('c=', st.session_state.c)

  
confirm_input2 = st.button('輸入確認')
x=st.number_input("請輸入%g到%g之間的整數:"%(st.session_state.start,st.session_state.end))





if confirm_input2:
  if x==st.session_state.c:
    st.write("恭喜你中獎了")
elif x>st.session_state.c:
  if x>=st.session_state.end:
    st.write("輸入不合法,請重新輸入:")
  else:
    st.session_state.end=x
else:
  if x<=st.session_state.start:
    st.write("輸入不合法,請重新輸入:")
  else:
    st.session_state.start==x




