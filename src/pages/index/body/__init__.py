import streamlit as st

from .keypad import render_keypad
from .input_box import render_input_box


def render_body():
    with st.container():
        render_input_box()
        render_keypad()
