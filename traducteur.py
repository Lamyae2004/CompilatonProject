#Used to read and write files in JSON format
import json
#affichage du texte bidirectionnel (de droite à gauche), notamment pour les langues comme l'arabe.
#Used to handle bidirectional text (right-to-left), especially for languages like Arabic.
from bidi.algorithm import get_display
#reformater les textes en arabe pour affichage correcte
#Used to reshape Arabic text so that it displays correctly
import arabic_reshaper

# Charger les traductions depuis le fichier JSON
def load_translations(file_path):
    try:
        #This function opens a JSON file (file_path), reads it,
        # and loads it into a Python dictionary using json.load().
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Erreur : Le fichier {file_path} est introuvable.")
        return {}
    except json.JSONDecodeError:
        print("Erreur : Le fichier JSON contient des erreurs.")
        return {}

# Fonction pour reformater et afficher correctement le texte en arabe
#Reformatting and correctly displaying Arabic text
def format_arabic_text(text):
  #Reformate le texte arabe pour qu'il soit prêt à être affiché correctement 
  #car arabe a des règles spécifiques concernant la forme des lettres selon leur position dans le mot
   #Reshapes Arabic text so it is ready to be displayed correctly
    reshaped_text = arabic_reshaper.reshape(text) 
 # Cette fonction prend le texte reformatté et le prépare pour être affiché de droite à gauche
 #displayed right-to-left
    bidi_text = get_display(reshaped_text)        
    return bidi_text

# Fonction pour traduire une ligne spécifique
#This function translates a specific line of the poem,
#  based on its number (line_number) and the desired language (language).
def translate_line(line_number, language, translations):
    if str(line_number) in translations:
        line_data = translations[str(line_number)]
        if language in line_data:
            translation = line_data[language]
            if language == "arabe":  # Reformater si le texte est en arabe
                return format_arabic_text(translation)
            return translation
        else:
            return f"Traduction en {language} non disponible."
    else:
        return "Ligne introuvable."

# Fonction pour traduire tout le poème
#This function translates the entire poem into the specified language.
def translate_poem(language, translations):
    translated_poem = []
    #It loops through each line of the poem 
    # and looks for the translation in the requested language.
    for line_number, line_data in translations.items():
        translation = line_data.get(language, f"Ligne {line_number} : Traduction non disponible.")
        if language == "arabe":  # Reformater si le texte est en arabe
            translation = format_arabic_text(translation)
        translated_poem.append(translation)
    return "\n".join(translated_poem)

# Chemin vers le fichier JSON
file_path = "poem_translations.json"
translations = load_translations(file_path)

# Menu principal
while True:
    print("\nOptions:")
    print("1. Traduire une ligne")
    print("2. Traduire tout le poème")
    print("3. Quitter")
    
    choice = input("Choisissez une option : ")
    
    if choice == "3":
        print("Au revoir!")
        break
    
    if choice == "1":
        try:
            line_number = int(input("Entrez le numéro de la ligne à traduire : "))
            print("Langues disponibles : arabe, anglais")
            language = input("Choisissez une langue : ").lower()
            print("\nTraduction :")
            print(translate_line(line_number, language, translations))
        except ValueError:
            print("Veuillez entrer un numéro de ligne valide.")
    
    elif choice == "2":
        print("Langues disponibles : arabe, anglais")
        language = input("Choisissez une langue : ").lower()
        print("\nTraduction complète du poème :")
        print(translate_poem(language, translations))
    
    else:
        print("Option invalide.")