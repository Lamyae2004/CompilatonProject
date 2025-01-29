import streamlit as st
import json
import speech_recognition as sr
from voice import nettoyer_texte, vers_corrects
from main import parser

# Charger les traductions depuis le fichier JSON
def load_translations(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        st.error(f"Erreur : Le fichier {file_path} est introuvable.")
        return {}
    except json.JSONDecodeError:
        st.error("Erreur : Le fichier JSON contient des erreurs.")
        return {}

# Traduire un texte donné
def translate_text(language, translations, line_number=None, input_text=None):
    if line_number:
        if str(line_number) in translations:
            return translations[str(line_number)].get(language, f"Traduction en {language} non disponible.")
        else:
            return "Numéro de ligne introuvable."
    elif input_text:
        for _, line_data in translations.items():
            if line_data.get("original", "").strip() == input_text.strip():
                return line_data.get(language, f"Traduction en {language} non disponible.")
        return "Texte introuvable dans les traductions."
    else:
        return "Aucune entrée fournie pour la traduction."

# Analyse syntaxique
def analyze_syntax(text):
    try:
        result_parser = parser.parse(text)
        return result_parser is not None
    except Exception as e:
        st.error(f"Erreur lors de l'analyse syntaxique : {e}")
        return False

# Reconnaissance vocale
def get_proverb_from_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Dis un vers : (Tu as 10 secondes pour parler)")
        try:
            audio = recognizer.listen(source, timeout=10)
            text = recognizer.recognize_google(audio, language='fr')
            text = nettoyer_texte(text)
            if text in vers_corrects:
                return f"✅ Bravo! Vers trouvé : {text}"
            else:
                return f"❌ Vers incorrect : {text}"
        except sr.UnknownValueError:
            return "❌ Impossible de comprendre l'audio."
        except sr.WaitTimeoutError:
            return "⏳ Temps écoulé, aucune parole détectée."
        except sr.RequestError as e:
            return f"❌ Erreur de reconnaissance vocale : {e}"

# Chemin vers le fichier JSON contenant les traductions
file_path = "poem_translations.json"
translations = load_translations(file_path)

# Interface utilisateur Streamlit
st.set_page_config(page_title="Analyseur et Traducteur", layout="wide", page_icon="📚")

st.title("Analyseur et Traducteur")
st.sidebar.title("Menu")
option = st.sidebar.radio("Sélectionnez une option", ("Analyse Syntaxique", "Traduction", "Reconnaissance Vocale"))


# Analyse syntaxique
if option == "Analyse Syntaxique":
    st.header("Analyse Syntaxique")
    text_input = st.text_area("Entrez la ligne à analyser", height=150, max_chars=500, placeholder="Exemple: Le ciel est bleu.")
    if st.button("Analyser", key="syntax"):
        if text_input:
            result = analyze_syntax(text_input)
            if result:
                st.success("Analyse syntaxique réussie.")
                st.text_area("Résultat de l'analyse", value=text_input, height=100)
            else:
                st.error("Erreur dans l'analyse syntaxique.")
        else:
            st.warning("Veuillez entrer du texte pour l'analyse syntaxique.")

# Traduction
elif option == "Traduction":
    st.header("Traduction")
    line_number = st.text_input("Entrez le numéro de ligne à traduire (facultatif)", "")
    input_text = st.text_input("Ou entrez le texte à traduire", "")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Traduire en Arabe", key="arabic"):
            if translations:
                translation = translate_text("arabe", translations, line_number=line_number, input_text=input_text)
                st.info(f"Traduction : {translation}")
            else:
                st.error("Les traductions ne sont pas chargées.")
    
    with col2:
        if st.button("Traduire en Anglais", key="english"):
            if translations:
                translation = translate_text("anglais", translations, line_number=line_number, input_text=input_text)
                st.info(f"Traduction : {translation}")
            else:
                st.error("Les traductions ne sont pas chargées.")

# Reconnaissance vocale
elif option == "Reconnaissance Vocale":
    st.header("Reconnaissance Vocale")
    st.subheader("Parlez pour vérifier un vers.")
    if st.button("Vérifier Audio", key="audio_check"):
        result = get_proverb_from_voice()
        st.info(result)