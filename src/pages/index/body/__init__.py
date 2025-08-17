import streamlit as st

from .keypad import render_keypad


def render_body():
    with st.container():
        render_keypad()
