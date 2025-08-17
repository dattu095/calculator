import streamlit as st


def render_keypad():
    if 'keypad_layout' not in st.session_state:
        st.session_state.keypad_layout = [
            ["C", ":material/backspace:", ":material/percent:", "/"],
            ["7", "8", "9", ":material/close:"],
            ["4", "5", "6", ":material/remove:"],
            ["1", "2", "3", ":material/add:"],
            ["", "0", ".", "="]
        ]
    with st.container():
        for row in st.session_state.keypad_layout:
            cols = st.columns(len(row))
            for i, button in enumerate(row):
                if cols[i].button(button, use_container_width=True):
                    pass
