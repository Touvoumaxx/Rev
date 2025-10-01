import streamlit as st
import random, csv

# Mot de passe
PASSWORD = "monsecret"

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    pwd = st.text_input("Mot de passe :", type="password")
    if st.button("Se connecter"):
        if pwd == PASSWORD:
            st.session_state.authenticated = True
        else:
            st.error("Mot de passe incorrect ❌")
    st.stop()  # on arrête ici si pas connecté

# --- le reste de ton appli ---
questions = []
with open("questions.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=";")
    next(reader)
    for row in reader:
        questions.append({"q": row[0], "a": row[1]})

if "question" not in st.session_state:
    st.session_state.question = random.choice(questions)

st.title("📚 Révisions intelligentes")

if st.button("Nouvelle question"):
    st.session_state.question = random.choice(questions)

st.subheader("Question :")
st.write(st.session_state.question["q"])

if st.button("Voir la réponse"):
    st.success(f"✅ Réponse : {st.session_state.question['a']}")
