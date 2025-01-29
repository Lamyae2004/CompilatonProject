

import speech_recognition as sr
import re

# Liste de vers corrects (nettoyée, sans majuscules internes ni ponctuation excessive)

vers_corrects = [
    
    "oh vous aurez trop dit au pauvre petit ange",
   # "qu'il est d'autres anges là-haut",
    "que rien ne souffre au ciel que jamais rien ne change",
   # "qu'il est doux d'y rentrer bientôt",

    "que le ciel est un dôme aux merveilleux pilastres",
    "une tente au riche couleur",
    #"un jardin bleu rempli de lis qui sont des astres",
    "et détoiles qui sont des fleurs",

    #"que c'est un lieu joyeux plus qu'on ne saurait dire",
    "ou toujours se laissant charmer",
    "on a les chérubins pour jouer et pour rire",
    "et le bon dieu pour nous aimer",

    #"qu'il est doux d'être un coeur qui brûle comme un cierge",
    "et de vivre en toute saison",
    "dans une si belle maison",

    "et puis vous naurez pas assez dit pauvre mère",
   # "a ce fils si frêle et si doux",
    "que vous étiez à lui dans cette vie amère",
    #"mais aussi qu'il était à vous",

   # "que tant qu'on est petit la mère sur nous veille",
    "mais que plus tard on la défend",
   # "et qu'elle aura besoin quand elle sera vieille",
    "dun homme qui soit son enfant",

    #"vous n'aurez point assez dit à cette jeune âme",
   # "que dieu veut qu'on reste ici-bas",
    #"la femme guidant l'homme et l'homme aidant la femme",
    "pour les douleurs et les combats",

    #"si bien qu'un jour ô deuil irréparable perte",
   # "le doux être s'en est allé",
    "hélas vous avez donc laissé la cage ouverte",
    "que votre oiseau est envolé"
]

def nettoyer_texte(texte):
    """
    Nettoie le texte : enlève la ponctuation et met en minuscule.
    """
    texte = texte.lower()  # Convertit en minuscules
    texte = re.sub(r'[^\w\s]', '', texte)  # Supprime la ponctuation
    texte = texte.strip()  # Supprime les espaces au début et à la fin
    return texte

def get_proverb_from_voice():
    recognizer = sr.Recognizer()

    # Utilise le microphone comme source audio
    with sr.Microphone() as source:
        print("🎤 Dis un vers : (Tu as 10 secondes pour parler)")
        try:
            audio = recognizer.listen(source, timeout=10)  # Timeout après 10 secondes de silence
            print("🔍 Analyse en cours...")
        except sr.WaitTimeoutError:
            print("⏳ Aucune parole détectée. Réessaye.")
            return

    try:
        # Convertit la parole en texte
        text = recognizer.recognize_google(audio, language='fr')
        text = nettoyer_texte(text)  # Nettoyage du texte

        if text in vers_corrects:
            print("✅ Bravo! Vers trouvé :", text)
        else:
            print("❌ Vers incorrect :", text)

    except sr.UnknownValueError:
        print("❌ Impossible de comprendre l'audio.")
    except sr.RequestError as e:
        print("❌ Erreur lors de la requête :", e)


# Appel de la fonction
#get_proverb_from_voice()
