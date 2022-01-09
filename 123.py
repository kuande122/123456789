import random
import streamlit as st
import base64
from PIL import Image
st.set_page_config(
 page_title='猛祺的期末報告',
 page_icon='🙈')
st.title('猛祺🙈的💣定時核彈🧨,炸到你心坎裡')
confirm_input = st.button('開始製造💣/重新製造💣')

if "start" not in st.session_state:
 st.session_state.start = 1
if "end" not in st.session_state:
 st.session_state.end = 100
if "c" not in st.session_state:
 st.session_state.c = 0
if "begin" not in st.session_state:
 st.session_state.begin= 'n'
 
if confirm_input:
 st.session_state.c = c = random.randint(2,99)
 st.session_state.start = 1
 st.session_state.end = 100
 st.session_state.start,st.session_state.end = 1,100
 st.session_state.begin= 'y'
 x=0



st.write('c=', st.session_state.c)

#x=st.sidebar.text_input("請輸入%g到%g之間的整數:"%(st.session_state.start,st.session_state.end)) 
x=st.number_input("請輸入整數?", 0)

if x>st.session_state.c:
 if x>=st.session_state.end:
    pass
 else:
   st.session_state.end=x

if x<st.session_state.c:
    if x<=st.session_state.start:
       pass
    else:
       st.session_state.start=x

st.write("請輸入%g到%g之間的整數:"%(st.session_state.start,st.session_state.end)) 

#st.write("「CONFIRM」鍵記得按兩次喔,否則可能導致系統無法正常運行!") 
#confirm_input2 = 
#if st.sidebar.button('CONFIRM'):
if x==st.session_state.c and st.session_state.begin == 'y':
 st.subheader("核爆了吧!!!")
 file_ = open("output_ntyylX.gif", "rb")
 contents = file_.read()
 data_url = base64.b64encode(contents).decode("utf-8")
 file_.close()
 st.markdown(
 f'<img src="data:image/gif;base64,{data_url}" alt="output_ntyylX gif">',
 unsafe_allow_html=True,
 )

if x>st.session_state.c and st.session_state.begin == 'y' and x>0:
 if x>st.session_state.end:
    st.write("不合法啦,好好選新的數字:")
    file_ = open("1.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="1 gif">',
    unsafe_allow_html=True,
    )
 else:
   st.session_state.end=x
     
if x<st.session_state.c and st.session_state.begin == 'y' and x>0:
    if x<st.session_state.start:
       st.write("不合法啦,好好選新的數字:")
       file_ = open("1.gif", "rb")
       contents = file_.read()
       data_url = base64.b64encode(contents).decode("utf-8")
       file_.close()
       st.markdown(
       f'<img src="data:image/gif;base64,{data_url}" alt="1 gif">',
       unsafe_allow_html=True,
       )
    else:
       st.session_state.start=x
