import streamlit as st
import math as m
st.set_page_config(page_title="attendance goal",page_icon="🎯")
st.markdown("<h5 style='text-align: center; color: #007bff;'>ATTENDANCE GOAL CALCULATOR  AND BUNKER APP</h5>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center; color: #007bff;'>calculate your attendance goal and plan your bunking strategy</h6>", unsafe_allow_html=True)
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
st.number_input("total hours",key="complete",min_value=1,max_value=75)
st.number_input("attended hours",key="attended",min_value=1,max_value=75)
st.number_input("course credit",key="credit",min_value=1,max_value=5)
st.session_state["total_hours"]=st.session_state["credit"]*15
st.selectbox("goal", options=["95%","90%","80%","75%"], key="goal")
c_percentage=st.session_state['attended']/st.session_state["complete"]*100
if st.button("submit", type="primary",width="stretch"):
    if st.session_state["goal"]=="95%":
        goal=0.95
    elif st.session_state["goal"]=="90%":
        goal=0.9
    elif st.session_state["goal"]=="80%":
        goal=0.8
    elif st.session_state["goal"]=="75%":
        goal=0.75
    required_a=(goal*st.session_state["complete"]-st.session_state['attended'])/(1-goal)
    if goal*100>c_percentage:
        st.markdown(f"<h5 style='text-align: center; color: #28a745;'>your attendance is already below your goal</h5>", unsafe_allow_html=True)
        st.markdown(f"<h6 style='text-align: center; color: #28a745;'> your have attended {st.session_state['attended']} hours/{st.session_state['complete']} hours</h6>", unsafe_allow_html=True)
        st.markdown(f"<h6 style='text-align: center; color: red;'>your current attendance is {c_percentage:.2f}%</h6>", unsafe_allow_html=True)
        st.markdown(f"<h6 style='text-align: center; color: #28a745;'>you need to attend {m.ceil(required_a)} hours</h6>", unsafe_allow_html=True)
    elif goal*100<c_percentage:
        st.markdown(f"<h6 style='text-align: center; color: red;'>your current attendance is {c_percentage:.2f}%</h6>", unsafe_allow_html=True)
        st.markdown(f"<h5 style='text-align: center; color: #28a745;'>your attendance is already above your goal</h5>", unsafe_allow_html=True)
        st.markdown(f"<h6 style='text-align: center; color: #28a745;'> you can bunk {m.floor(st.session_state['attended']/goal - st.session_state['attended'])} hours/{st.session_state['total_hours']} hours to maintain your goal</h6>", unsafe_allow_html=True)
