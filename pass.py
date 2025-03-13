import re
import streamlit as st

# Page styling
st.set_page_config(page_title="Password Strength Checker By M.Shahzaib", page_icon="🔑", layout="centered")

# Custom CSS
st.markdown("""
    <style>
        .main {text-align:center;}
        .stTextInput {width:60% !important; margin: auto;}
        .stButton button {width:50%; background-color:#AF804F; color: white; font-size:18px;}
        .stButton button:hover {background-color:#410200;}
    </style>
""", unsafe_allow_html=True)

# Page title and description
st.title("🔐 Password Strength Checker By Muhammed Shahzeb")

def check_password_strength(password):
    score = 0
    feedback = []

    # Check if the password is at least 8 characters long
    if len(password) >= 8:
        score += 1  # Increase score by 1
    else:
        feedback.append("❌ Password should be at least **8 characters long**.")

    # Check if the password contains both uppercase and lowercase letters
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **both uppercase [A-Z] and lowercase [a-z] letters**.")

    # Check if the password contains at least one digit (0-9)
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one number (0-9)**.")

    # Check if the password contains at least one special character
    if re.search(r"[!@#$%^&*()]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one special character (!@#$%^&*)**.")

    # Display feedback based on the score
    if score == 4:
        st.success("✅ **Strong Password** - Your password is secure.")
    elif score == 3:
        st.info("⚠ **Moderate Password** - Consider improving security by adding more features.")
    else:
        st.error("❌ **Weak Password** - Follow the suggestions below to strengthen it.")

        # Provide feedback on what needs improvement
        if feedback:
            with st.expander("🔎 **Improve your Password**"):
                for item in feedback:
                    st.write(item)

# Password input field
password = st.text_input("Enter your Password", type="password", help="Ensure your password is strong 🔐")

# Button to check password strength
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠ Please enter a password first!")
