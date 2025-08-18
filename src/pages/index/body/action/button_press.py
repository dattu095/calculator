import streamlit as st

NUMBERS = "1234567890."
SYMBOLS = {
    ":material/percent:": "%",
    ":material/close:": "*",
    ":material/remove:": "-",
    ":material/add:": "+",
    "/": "/"
}


def press(button):
    if button in NUMBERS:
        st.session_state.input += button
    if button in SYMBOLS.keys():
        st.session_state.input += SYMBOLS[button]
    if button == ":material/backspace:":
        st.session_state.input = st.session_state.input[:-1]
    if button == 'AC':
        st.session_state.input = ""
    if button == 'C':
        st.session_state.input = ""
        st.session_state.buffer = 0
    if button == ':material/equal:':
        pass
    st.rerun()
