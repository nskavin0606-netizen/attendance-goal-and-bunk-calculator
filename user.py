import streamlit as st
import math as m
st.set_page_config(page_title="attendance tracker pro",page_icon="🎯")
st.markdown("""<style>div.stButton > button {background-color: #ff4b4b;color: white;font-size: 18px;border-radius: 10px;height: 3em;width: 100%;}</style>
""", unsafe_allow_html=True)
st.markdown("""
<h1 style='text-align:center;
background: linear-gradient(90deg,#007bff,#00c6ff);
-webkit-background-clip: text;
color: transparent;'>
🎯 Attendance Tracker Pro
</h1>

<p style='text-align:center; font-size:18px; color:gray;'>
Plan smart. Bunk smarter 😎
</p>
""", unsafe_allow_html=True)
if "complete" not in st.session_state:
    st.session_state['complete']=0
if "attended" not in st.session_state:
    st.session_state['attended']=0
if "credit" not in st.session_state:
    st.session_state['credit']=0
if "goal" not in st.session_state:
    st.session_state['goal']=0
if "total_hours" not in st.session_state:
    st.session_state['total_hours']=0
col1,col2=st.columns(2)
with col1:
    st.number_input("total hours",key="complete",min_value=1,max_value=75)
with col2:
    st.number_input("attended hours",key="attended",min_value=1,max_value=75)
if st.session_state['attended']>st.session_state['complete']:
    st.warning("attended hours cannot be greater than total hours")
st.number_input("course credit",key="credit",min_value=1,max_value=5)
st.session_state["total_hours"]=st.session_state["credit"]*15
st.selectbox("goal", options=["95%","90%","85%","80%","75%"], key="goal")
c_percentage=st.session_state['attended']/st.session_state["complete"]*100
if st.button("submit",type="primary",width="stretch"):
    if st.session_state["goal"]=="95%":
        goal=0.95
    elif st.session_state["goal"]=="90%":
        goal=0.9
    elif st.session_state["goal"]=="85%":
        goal=0.85
    elif st.session_state["goal"]=="80%":
        goal=0.8
    elif st.session_state["goal"]=="75%":
        goal=0.75
    required_a=(goal*st.session_state["complete"]-st.session_state['attended'])/(1-goal)
    bunk_hours=m.floor((st.session_state['attended']/goal - st.session_state['complete']))
    if goal*100>c_percentage:
        st.info(f"your current attendance is {c_percentage:.2f}%") 
        if required_a<st.session_state["total_hours"]-st.session_state["complete"]:
            st.info(f"you need to attend {m.ceil(required_a)} hours to achieve your goal of {st.session_state['goal']}")
        else:
            st.info(f"you cannot achieve your goal of {st.session_state['goal']} with the remaining classes")
    elif c_percentage>=goal*100:
        st.info(f"your current attendance is {c_percentage:.2f}% and is already above your goal of {st.session_state['goal']}")
        if bunk_hours>0:
            st.info(f"you can bunk {bunk_hours} hours and still maintain your goal")
            st.balloons()
        else:
            st.info(f"you cannot bunk any hours to maintain your goal")

next_if_attend = ((st.session_state['attended'] + 1) / (st.session_state['complete'] + 1)) * 100
next_if_bunk = (st.session_state['attended'] / (st.session_state['complete'] + 1)) * 100
next=st.button("predict next class attendance", type="tertiary", width="stretch")
if next:
    st.info(f"📚 If you attend next class {c_percentage:.2f}% → {next_if_attend:.2f}%")
    st.info(f"😴 If you bunk next class {c_percentage:.2f}% → {next_if_bunk:.2f}%")
st.caption("@ made by kavin")
