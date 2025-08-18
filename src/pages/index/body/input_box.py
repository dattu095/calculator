import streamlit as st


def render_input_box():
    if 'input' not in st.session_state:
        st.session_state.input = ""
    if 'buffer' not in st.session_state:
        st.session_state.buffer = 0
    with st.container(
        border=True,
        width='stretch',
        height=100,
        horizontal_alignment='right',
        vertical_alignment='bottom'
    ):
        st.write(st.session_state.input)
