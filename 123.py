import random
import streamlit as st
confirm_input = st.button('確認產生答案')
if "start" not in st.session_state:
  st.session_state.start = 1
elif "end" not in st.session_state:
  st.session_state.end = 100
elif "c" not in st.session_state:
  st.session_state.c = random.randint(2,99) 
if confirm_input:
 st.session_state.c = c = random.randint(2,99)
 st.session_state.start = 1
 st.session_state.end = 100
 #st.session_state.start,st.session_state.end = 1,100
 st.write('c=', st.session_state.c)

x=st.number_input("請輸入%g到%g之間的整數:",%(st.session_state.start,st.session_state.end)) 
st.write("「輸入確認」鍵記得按兩次喔,否則可能導致程式無法正常運行!") 




while st.button('輸入確認'):
    st.write(x==st.session_state.c)
    if x==st.session_state.c:
      st.write("恭喜你中獎了")   
    elif x!=st.session_state.c:
        if x>=st.session_state.end|x<=st.session_state.start:
            st.write("輸入不合法,請重新輸入:")
        else:
            st.session_state.start=x
        break


