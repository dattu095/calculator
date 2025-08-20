import streamlit as st

from .action.button_press import press


def render_keypad():
    if 'keypad_layout' not in st.session_state:
        st.session_state.keypad_layout = [
            ["C", "(", ")", ":material/percent:", "/"],
            ["7", "8", "9", ":material/close:"],
            ["4", "5", "6", ":material/remove:"],
            ["1", "2", "3", ":material/add:"],
            [":material/backspace:", "0", ".", ":material/equal:"]
        ]
    with st.container():
        for row in st.session_state.keypad_layout:
            cols = st.columns(len(row))
            for i, button in enumerate(row):
                if cols[i].button(button, use_container_width=True):
                    press(button)
