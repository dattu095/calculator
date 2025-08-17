import streamlit as st


def render_keypad():
    if 'keypad_layout' not in st.session_state:
        st.session_state.keypad_layout = [
            ["C", "back", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["", "0", ".", "="]
        ]
    with st.container():
        pass
