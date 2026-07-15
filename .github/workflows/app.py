import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

def check_password():
    def password_entered():
        if st.session_state["password"] == st.secrets["dashboard_password"]:
            st.session_state["authenticated"] = True
            del st.session_state["password"]
        else:
            st.session_state["authenticated"] = False

    if st.session_state.get("authenticated"):
        return True

    st.text_input("Enter password", type="password", on_change=password_entered, key="password")
    if "authenticated" in st.session_state and not st.session_state["authenticated"]:
        st.error("Incorrect password")
    return False

if not check_password():
    st.stop()

# Load and display your existing HTML dashboard
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=2500, scrolling=False)
