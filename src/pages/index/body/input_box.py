import streamlit as st


def render_input_box():
    if "input" not in st.session_state:
        st.session_state.input = ""
    with st.container(
        border=True,
        width="stretch",
        height=100,
        horizontal_alignment="right",
        vertical_alignment="bottom",
    ):
        st.markdown(
            f"<div style='font-size:32px; text-align:right;'>{
                st.session_state.input}</div>",
            unsafe_allow_html=True,
        )
