import streamlit as st

from .title import render_title


def render_header():
    st.set_page_config(page_title="Calculator", layout='centered')

    with st.container(key='header'):
        render_title()
