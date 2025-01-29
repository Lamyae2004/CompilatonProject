import ply.lex as lex
import ply.yacc as yacc
import speech_recognition as sr
import re
import re
global resultLexer;global positionLexerError

#Our code consists of several main components, a lexical analyser, a syntax/semantic analyser, a translator, and a graphical user interface.
#Let us start with the lexical analyser:

#First, we import the lex library to handle the lexical analyser. Then we defined the tokens in a unique way; if a word is incorrect, it will display illegal words. This ensures the program handles errors appropriately.

#In the program, txt file, which contains the entire poem, it correctly displays all the tokens.








positionLexerError = dict(),

tokens = [
    'INTERJECTION11', 'PRONOM11', 'AUX11', 'ADV11', 'PP11', 'PREP11', 'ADJ1', 'ADJ12', 'NOM11', 'CONJ21', 
    'PONCT21', 'PRONOM21', 'VERBE21', 'PREP21', 'PONCT22', 'ADV21', 'NOM21', 'PONCT23', 'CONJ31', 'PRONOM31', 
    'NEG31', 'VERBE31', 'NOM31', 'ADV31', 'PONCT32', 'NEG32', 'PRONOM33', 'VERBE32', 'ADJ41', 'VERBE42', 
    'ADV41', 'PONCT41', 'D51', 'D52', 'PREP51', 'NOM52', 'ADJ51', 'NOM53', 'D61', 'NOM61', 'ADJ61', 
    'NOM62', 'NOM71', 'ADJ71', 'ADJ72', 'PREP71', 'NOM72', 'CONJ71', 'VERBE71', 'D72', 'NOM73', 'CONJ81', 
    'NOM81', 'NOM82', 'D91', 'NOM91', 'ADJ91', 'ADV91', 'PRONOM91', 'VERBE92', 'VERBE93', 'CONJ101', 
    'PRONOM101', 'PPR10', 'VERBE101', 'CONJ32', 'ADV22', 'ADJ11', 'PPASSE11', 'CONJ201', 'PRONOM111', 
    'VERBE111', 'D111', 'NOM111', 'PREP111', 'VERBE112', 'CONJ111', 'VERBE113', 'ADJ121', 'NOM121', 
    'PREP121', 'PRONOM121', 'VERBE121', 'PONCT121', 'VERBE132', 'D131', 'NOM131', 'VERBE133', 'CONJ133', 
    'D132', 'NOM132', 'PREP151', 'D151', 'ADV151', 'ADJ151', 'NOM151', 'ADV161', 'NEG162', 'ADV162', 
    'PREP171', 'D171', 'NOM171', 'ADV171', 'ADJ171', 'PRONOM181', 'VERBE181', 'PREP181', 'PRONOM182', 
    'PREP182', 'D181', 'NOM181', 'ADJ181', 'PREP191', 'ADV191', 'PRONOM191', 'VERBE191', 'PREP192', 
    'PRONOM192', 'CONJ202', 'DET201', 'NOM201', 'PREP201', 'VERBE202', 'PRO221', 'VERBE221', 'NOM221', 
    'CONJ223', 'VERBE222', 'ADJ221', 'PREP231', 'DET231', 'NOM231', 'VERBE231', 'DET232', 'NOM232', 
    'PRO241', 'NEG241', 'ADV241', 'PP241', 'PREP241', 'DET241', 'ADJ241', 'NOM241', 'NOM251', 'VERBE251', 
    'VERBE252', 'ADV251', 'DET261', 'NOM261', 'PPR261', 'DET262', 'PPR262', 'PREP271', 'DET271', 'NOM271', 
    'NOM272', 'DET281', 'NOM281', 'ADJ281', 'NOM282', 'DET291', 'NOM291', 'PRO291', 'PP291', 'INTERJECTION301', 
    'PRO301', 'AUX301', 'CONJ301', 'PP301', 'NOM301', 'ADJ301', 'DET311', 'NOM311', 'PP311', 'CONJ281', 
    'INTERJECTION281', 'NOM141', 'VERBE211', 'VERBE141', 'D141', 'NOM161', 'INJECTION11', 'PONCT293', 
    'PREP142', 'PONCT141', 'PONCT151', 'PONCT202', 'PONCT294', 'PONCT33', 'CONJ41', 'PRONOM41', 'VERBE41', 
    'CONJ51', 'NOM51', 'VERBE51', 'PONCT51', 'PREP61', 'PREP81', 'PONCT81', 'CONJ82', 'VERBE81', 'D81', 
    'CONJ91', 'VERBE91', 'D92', 'CONJ92', 'PONCT91', 'NEG91', 'PONCT92', 'PRO211', 'PONCT232', 'PRO311', 
    'DELIMITER','D71','ADV101','ADV9','PRONOM241','DET251','ADV281','ADV282','ADV283'
]


####  ligne 1:Oh ! vous aurez trop dit au pauvre petit ange ##
t_INJECTION11=r'Oh!'
t_PRONOM11=r'vous'
t_AUX11=r'aurez'
t_ADV11=r'trop'
t_PPASSE11=r'dit'
t_PREP11=r'au'
t_ADJ11=r'pauvre'
t_ADJ12=r'petit'
t_NOM11=r'ange'
#nombre de proverb

####  ligne 2: Qu'il est d'autres anges là-haut,##
t_CONJ21=r'Qu'
t_PONCT21=r'\''
t_PRONOM21=r'il'
t_VERBE21=r'est'
t_PREP21=r'd'
#t_PONCT21=r'\''
t_ADV21=r'autres'
t_NOM21=r'anges'
t_ADV22=r'là-haut'
t_PONCT23=r','
####  ligne 3: Que rien ne souffre au ciel, que jamais rien n'y change,
##
t_CONJ31=r'Que'
t_PRONOM31=r'rien'
t_NEG31=r'ne'
t_VERBE31=r'souffre'
#t_PREP11=r'au'
t_NOM31=r'ciel'
#t_PONCT23=r','
t_CONJ32=r'que'
t_ADV31=r'jamais'
#t_PRONOM31=r'rien'
t_NEG32=r'n'
#t_PONCT21=r'\''
t_PRONOM33=r'y'
t_VERBE32=r'change'
#t_PONCT23=r','

####  ligne 4 : Qu'il est doux d'y rentrer bientôt ;
##
#t_CONJ21=r'Qu'
#t_PRONOM21=r'il'
#t_VERBE21=r'est'
t_ADJ41=r'doux'
#t_PREP21=r'd'
#t_PONCT21=r'\''
#t_PRONOM33=r'y'
t_VERBE42=r'rentrer'
t_ADV41=r'bientôt'
t_PONCT41 = r';'

####  ligne 5 : Que le ciel est un dôme aux merveilleux pilastres,
##
#t_CONJ31=r'Que'
t_D51=r'le'
#t_NOM31=r'ciel'
#t_VERBE21=r'est'
t_D52=r'un'
t_NOM52=r'dôme'
t_PREP51=r'aux'
t_ADJ51=r'merveilleux'
t_NOM53 = r'pilastres'
#t_PONCT23=r','

####  ligne 6 : Une tente aux riches couleurs,

##
t_D61=r'Une'
t_NOM61=r'tente'
#t_PREP51=r'aux'
t_ADJ61=r'riches'
t_NOM62 = r'couleurs'
#t_PONCT23=r','

####  ligne 7 : un jardin bleu rempli de lis qui sont des astres,

##
t_D71=r'Un'
t_NOM71=r'jardin'
t_ADJ71=r'bleu'
t_ADJ72 = r'rempli'
t_PREP71 = r'de'
t_NOM72=r'lis'
t_CONJ71 = r'qui'
t_VERBE71 = r'sont'
t_D72 = r'des'
t_NOM73=r'astres'
#t_PONCT23=r','

####ligne 8 : Et d'étoiles qui sont des fleurs ;
##
t_CONJ81=r'Et'
#t_PREP21=r'd'
#t_PONCT21=r'\''
t_NOM81 = r'étoiles'
#t_CONJ71 = r'qui'
#t_VERBE71 =r'sont'
#t_D72 = r'des'
t_NOM82 = r'fleurs'
#t_PONCT41=r';'

####ligne 9 : Que c'est un lieu joyeux plus qu'on ne saurait dire,
##
#t_CONJ31=r'Que'
t_D91=r'c'
#t_VERBE21=r'est'
#t_D52 = r'un'
t_NOM91 = r'lieu'
t_ADJ91=r'joyeux'
t_ADV91 = r'plus'
t_CONJ92=r'qu'
#t_PONCT21=r'\''
t_PRONOM91=r'on'
#t_NEG31 =r'ne'
t_VERBE92=r'saurait'
t_VERBE93 = r'dire'
#t_PONCT23=r','

####ligne 10 : Où toujours, se laissant charmer,
t_CONJ101=r'Où'
t_ADV101=r'toujours'
#t_PONCT91=r','
t_PRONOM101 = r'se'
t_PPR10=r'laissant'
t_VERBE101 = r'charmer'
#t_PONCT23=r','


#LIGNE 11 : On a les chérubins pour jouer et pour rire,
t_PRONOM111=r'On'
t_VERBE111=r'a'
t_D111=r'les'
t_NOM111=r'chérubins'
t_PREP111=r'pour'
t_VERBE112=r'jouer'
t_CONJ111=r'et'
#t_PREP111=r'pour'
t_VERBE113=r'rire'
#t_PONCT23=r','


#ligne12 : Et le bon Dieu pour nous aimer ;
#t_CONJ81=r'Et'
#t_D51=r'le'
t_ADJ121=r'bon'
t_NOM121=r'Dieu'
#t_PREP111=r'pour'
t_PRONOM121=r'nous'
t_VERBE121=r'aimer'
#t_PONCT41=r';'

#LIGNE 13 : Qu'il est doux d'être un coeur qui brûle comme un cierge,

#t_CONJ21=r'Qu'
#t_PONCT21=r'\''
#t_PRONOM21=r'il'
#t_VERBE21=r'est'
#t_ADJ41=r'doux'
#t_PREP21=r'd'
#t_PONCT21=r'\''
t_VERBE132=r'être'
#t_D52=r'un'
t_NOM131=r'coeur'
#t_CONJ71=r'qui'
t_VERBE133=r'brûle'
t_CONJ133=r'comme'
#t_D52=r'un'
t_NOM132=r'cierge'
#t_PONCT23=r','


#LIGNE14 : Et de vivre, en toute saison,

#t_CONJ81=r'Et'
#t_PREP71=r'de'
t_VERBE141=r'vivre'
t_PONCT141=r','
t_PREP142=r'en'
t_D141=r'toute'
t_NOM141=r'saison'
#t_PONCT23=r','


#LIGNE15: Dans une si belle maison ! 
t_PREP151=r'Dans'
t_D151=r'une'
t_ADV151=r'si'
t_ADJ151=r'belle'
t_NOM151=r'maison'
t_PONCT151=r'!'


#LIGNE16:Et puis vous n'aurez pas assez dit, pauvre mère,
#t_CONJ81=r'Et'
t_ADV161=r'puis'
#t_PRONOM11=r'vous'
#t_NEG32=r'n'
#t_PONCT21=r'\''
#t_AUX11=r'aurez'
t_NEG162=r'pas'
t_ADV162=r'assez'
#t_PPASSE11=r'dit'
#t_PONCT23=r','
#t_ADJ11=r'pauvre'
t_NOM161=r'mère'
#t_PONCT23=r','

#LIGNE17 : A ce fils si frêle et si doux, 

t_PREP171=r'A'
t_D171=r'ce'
t_NOM171=r'fils'
#t_ADV151=r'si'
t_ADJ171=r'frêle'
#t_CONJ111=r'et'
#t_ADV151=r'si'
#t_ADJ41=r'doux'
#t_PONCT23=r','

#LIGNE18:Que vous étiez à lui dans cette vie amère,

#t_CONJ31=r'Que'
#t_PRONOM11=r'vous'
t_VERBE181=r'étiez'
t_PREP181=r'à'
t_PRONOM182=r'lui'
t_PREP182=r'dans'
t_D181=r'cette'
t_NOM181=r'vie'
t_ADJ181=r'amère'
#t_PONCT23=r','


#LIGNE19:Mais aussi qu'il était à vous ;

t_PREP191=r'Mais'
t_ADV191=r'aussi'
#t_CONJ92=r'qu'
#t_PONCT21=r'\''
#t_PRONOM21=r'il'
t_VERBE191=r'était'
#t_PREP181=r'à'
#t_PRONOM11=r'vous'
#t_PONCT41=r';'



#LIGNE 20 :Que, tant qu'on est petit, la mère sur nous veille,

#t_CONJ31=r'Que'
#t_PONCT23=r','
t_CONJ202=r'tant' 
#t_CONJ92=r'qu'
#t_PONCT21=r'\''
#t_PRONOM91=r'on'
#t_VERBE21=r'est'
#t_ADJ12=r'petit'
t_PONCT202=r','
t_DET201=r'la'
#t_NOM161=r'mère'
t_PREP201=r'sur'
#t_PRONOM121=r'nous'
t_VERBE202=r'veille'
#t_PONCT23=r','

#LIGNE 21 : Mais que plus tard on la défend ;


#t_PREP191=r'Mais'
#t_CONJ32=r'que'
#t_ADV91=r'plus tard'
t_ADV9=r'tard'
#t_PRO211=r'on'
#t_DET201=r'la'
t_VERBE211=r'défend'
#t_PONCT41=r';'


#ligne 22 :Et qu'elle aura besoin, quand elle sera vieille,

 

#t_CONJ81=r'Et'
#t_CONJ92=r'qu'
#t_PONCT21=r'\''
t_PRO221=r'elle'
t_VERBE221=r'aura'
t_NOM221=r'besoin'
#t_PONCT23=r','
t_CONJ223=r'quand'
#t_PRO221=r'elle'
t_VERBE222=r'sera'
t_ADJ221=r'vieille'
#t_PONCT23=r','

#LIGNE 23 : D'un homme qui soit son enfant ;

t_PREP231=r'D'
#t_PONCT21=r'\''
#t_D52=r'un'
t_NOM231=r'homme'
#t_CONJ71=r'qui'
t_VERBE231=r'soit'
t_DET232=r'son'
t_NOM232=r'enfant'
#t_PONCT232=r';'

#LIGNE 24 : Vous n'aurez point assez dit à cette jeune âme

t_PRONOM241=r'Vous'
#t_NEG32=r'n'
#t_PONCT21=r'\''
#t_AUX11=r'aurez'
t_ADV241=r'point'
#t_ADV162=r'assez'
#t_PPASSE11=r'dit'
#t_PREP181=r'à'
#t_D181=r'cette'
t_ADJ241=r'jeune'
t_NOM241=r'âme'

#LIGNE 25 : Que Dieu veut qu'on reste ici-bas,

#t_CONJ31=r'Que'
#t_NOM121=r'Dieu'
t_VERBE251=r'veut'
#t_CONJ92=r'qu'
#t_PONCT21=r'\''
#t_PRONOM91=r'on'
t_VERBE252=r'reste'
t_ADV251=r'ici-bas'
#t_PONCT23=r','


#LIGNE 26 : La femme guidant l'homme et l'homme aidant la femme,

t_DET251=r'La'
t_NOM261=r'femme'
t_PPR261=r'guidant'
t_DET262=r'l'
#t_PONCT21=r'\''
#t_NOM231=r'homme'
#t_CONJ111=r'et'
#t_DET262=r'l'
#t_PONCT21=r'\''
#t_NOM231=r'homme'
t_PPR262=r'aidant'
#t_DET201=r'la'
#t_NOM261=r'femme'
#t_PONCT23=r','

#LIGNE 27 :Pour les douleurs et les combats ;


t_PREP271 =r'Pour'
#t_D111=r'les'
t_NOM271=r'douleurs'
#t_CONJ111=r'et'
#t_D111=r'les'
t_NOM272=r'combats'
#t_PONCT41=r';'

#LIGNE 28 : Si bien qu'un jour, ô deuil ! irréparable perte !



t_CONJ281=r'Si'
t_ADV281=r'bien'
#t_CONJ92=r'qu'
#t_PONCT21=r'\''
#t_D52=r'un'
t_NOM281=r'jour'
#t_PONCT23=r','
t_ADV282=r'ô'
t_ADV283=r'deuil'
t_ADJ281=r'irréparable'
t_NOM282=r'perte'
#t_PONCT151=r'!'

#LIGNE 29 :Le doux être s'en est allé !... -


t_DET291=r'Le'
#t_ADJ41=r'doux'
#t_VERBE132=r'être'
t_PRO291=r's'
#t_PONCT21=r'\''
#t_PREP142=r'en'
#t_VERBE21=r'est'
t_PP291=r'allé'
#t_PONCT151=r'!'
#t_PONCT293=r'...'
t_PONCT294=r'-'

#LIGNE 30 :Hélas! vous avez donc laissé la cage ouverte,


t_INTERJECTION301=r'Hélas!'
#t_PRONOM11=r'vous'
t_AUX301=r'avez'
t_CONJ301=r'donc'
t_PP301=r'laissé'
#t_DET201=r'la'
t_NOM301=r'cage'
t_ADJ301=r'ouverte'
#t_PONCT23=r','

#LIGNE 31:Que votre oiseau s'est envolé !

#t_CONJ31=r'Que'
t_DET311=r'votre'
t_NOM311=r'oiseau'
#t_PRO311=r's'
#t_PONCT21=r'\''
#t_VERBE21=r'est'
t_PP311=r'envolé'
#t_PONCT151=r'!'


# Ignorer les espaces et les tabulations
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
   # t.lexer.lexpos += len(t.value)
 #lexer = lex.lex()
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at index {t.lexpos}")
    t.lexer.skip(1)
    
""""""
# Construction du lexer
lexer = lex.lex()

# Reading input text from a file
file_name = "program.txt"
with open(file_name, "r", encoding="utf-8") as file:
    data = file.read().strip()

# Using the lexer to tokenize the input

lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

    
global resultParser;global positionParserError
positionLexerError,positionParserError = dict(),dict()

#grammar rules : 

# Règle pour un poème complet
def p_poem(p):
    '''poem : line1
            | line2
            | line3
            | line4
            | line5
            | line6
            | line7
            | line8
            | line9
            | line10
            | line11
            | line12
            | line13
            | line14
            | line15
            | line16
            | line17
            | line18
            | line19
            | line20
            | line21
            | line22
            | line23
            | line24
            | line25
            | line26
            | line27
            | line28
            | line29
            | line30
            | line31
            | vers1
            | vers2
            | vers3
            | vers4
            | vers5
            | vers6
            | vers7
            | vers8
            | vers9
            | vers10
            | vers11
            | vers12
            | vers13
            | vers14
            | vers15
            | vers16
            | vers17
            | vers18
            | vers19
            | vers20
            | vers21
            | vers22
            | vers23
            | vers24
            | vers25
            | vers26
            | vers27
            | vers28
            | vers29
            | vers30
            | vers31'''
    
    p[0] = p[1]

# Règle pour la ligne 1
def p_line1(p):
    'line1 : INJECTION11 PRONOM11 AUX11 ADV11 PPASSE11 PREP11  ADJ11 ADJ12 NOM11'
    p[0] = " ".join(p[1:])
    print(f"Ligne 1 analysée : {p[0]}")

# Règle pour la ligne 2
def p_line2(p):
    'line2 : CONJ21 PONCT21 PRONOM21 VERBE21 PREP21 PONCT21 ADV21 NOM21 ADV22 PONCT23'
    p[0] = " ".join(p[1:])
    print(f"Ligne 2 analysée : {p[0]}")

# Règle pour la ligne 3
def p_line3(p):
    'line3 : CONJ31 PRONOM31 NEG31 VERBE31 PREP11 NOM31 PONCT23 CONJ32 ADV31 PRONOM31 NEG32 PONCT21 PRONOM33 VERBE32 PONCT23'
    p[0] = " ".join(p[1:])
    print(f"Ligne 3 analysée : {p[0]}")

# Règle pour la ligne 4
def p_line4(p):
    'line4 : CONJ21 PONCT21 PRONOM21 VERBE21 ADJ41 PREP21 PONCT21 PRONOM33 VERBE42 ADV41 PONCT41'
    p[0] = " ".join(p[1:])
    print(f"Ligne 4 analysée : {p[0]}")

# Règle pour la ligne 5
def p_line5(p):
    'line5 : CONJ31 D51 NOM31 VERBE21 D52 NOM52 PREP51 ADJ51 NOM53 PONCT23'
    p[0] = " ".join(p[1:])
    print(f"Ligne 5 analysée : {p[0]}")

# Règle pour la ligne 6
def p_line6(p):
    'line6 : D61 NOM61 PREP51 ADJ61 NOM62 PONCT23'
    p[0] = " ".join(p[1:])
    print(f"Ligne 6 analysée : {p[0]}")

# Règle pour la ligne 7
def p_line7(p):
    'line7 : D71 NOM71 ADJ71 ADJ72 PREP71 NOM72 CONJ71 VERBE71 D72 NOM73 PONCT23'
    p[0] = " ".join(p[1:])
    print(f"Ligne 7 analysée : {p[0]}")

# Règle pour la ligne 8
def p_line8(p):
    'line8 : CONJ81 PREP21 PONCT21 NOM81 CONJ71 VERBE71 D72 NOM82 PONCT41'
    p[0] = " ".join(p[1:])
    print(f"Ligne 8 analysée : {p[0]}")

# Règle pour la ligne 9
def p_line9(p):
    'line9 : CONJ31 D91 PONCT21 VERBE21  D52 NOM91 ADJ91 ADV91 CONJ92 PONCT21 PRONOM91  NEG31 VERBE92 VERBE93 PONCT23'
    p[0] = " ".join(p[1:])
    print(f"Ligne 9 analysée : {p[0]}")

# Règle pour la ligne 10
def p_line10(p):
    'line10 : CONJ101 ADV101 PONCT23 PRONOM101 PPR10 VERBE101 PONCT23'
    p[0] = " ".join(p[1:])
    print(f"Ligne 10 analysée : {p[0]}")

# Règle pour la ligne 11
def p_line11(p):
    'line11 : PRONOM111 VERBE111 D111 NOM111 PREP111 VERBE112 CONJ111 PREP111 VERBE113 PONCT23'
    p[0] = " ".join(p[1:])
    print(f"Ligne 11 analysée : {p[0]}")

# Règle pour la ligne 12
def p_line12(p):
    'line12 : CONJ81 D51 ADJ121 NOM121 PREP111 PRONOM121 VERBE121 PONCT41'
    p[0] = " ".join(p[1:])
    print(f"Ligne 12 analysée : {p[0]}")

# Règle pour la ligne 13
def p_line13(p):
    'line13 : CONJ21 PONCT21 PRONOM21 VERBE21 ADJ41 PREP21 PONCT21 VERBE132 D52 NOM131 CONJ71 VERBE133 CONJ133 D52 NOM132 PONCT23'
    p[0] = " ".join(p[1:])
    print(f"Ligne 13 analysée : {p[0]}")

# Règle pour la ligne 14
def p_line14(p):
    'line14 : CONJ81 PREP71 VERBE141 PONCT23  PREP142 D141 NOM141 PONCT23'
    p[0] = " ".join(p[1:])
    print(f"Ligne 14 analysée : {p[0]}")

# Règle pour la ligne 15
def p_line15(p):
    'line15 : PREP151 D151 ADV151 ADJ151 NOM151 PONCT151'
    p[0] = " ".join(p[1:])
    print(f"Ligne 15 analysée : {p[0]}")

# Règle pour la ligne 16
def p_line16(p):
    'line16 : CONJ81 ADV161 PRONOM11 NEG32 PONCT21 AUX11 NEG162 ADV162 PPASSE11 PONCT23 ADJ11 NOM161 PONCT23'
    p[0] = " ".join(p[1:])
    print(f"Ligne 16 analysée : {p[0]}")

# Règle pour la ligne 17
def p_line17(p):
    'line17 : PREP171 D171 NOM171 ADV151 ADJ171 CONJ111 ADV151 ADJ41 PONCT23'
    p[0] = " ".join(p[1:])
    print(f"Ligne 17 analysée : {p[0]}")

# Règle pour la ligne 18
def p_line18(p):
    'line18 : CONJ31 PRONOM11 VERBE181 PREP181 PRONOM182 PREP182 D181 NOM181 ADJ181 PONCT23'
    p[0] = " ".join(p[1:])
    print(f"Ligne 18 analysée : {p[0]}")

# Règle pour la ligne 19
def p_line19(p):
    'line19 : PREP191 ADV191 CONJ92 PONCT21 PRONOM21 VERBE191 PREP181 PRONOM11 PONCT41'
    p[0] = " ".join(p[1:])
    print(f"Ligne 19 analysée : {p[0]}")

# Règle pour la ligne 20
def p_line20(p):
    'line20 : CONJ31 PONCT23 CONJ202 CONJ92 PONCT21 PRONOM91 VERBE21 ADJ12 PONCT23 DET201 NOM161 PREP201 PRONOM121 VERBE202 PONCT23'
    p[0] = " ".join(p[1:])
    print(f"Ligne 20 analysée : {p[0]}")

# Règle pour la ligne 21
def p_line21(p):
    'line21 : PREP191 CONJ32 ADV91 ADV9 PRONOM91 DET201 VERBE211 PONCT41'
    p[0] = " ".join(p[1:])
    print(f"Ligne 21 analysée : {p[0]}")

# Règle pour la ligne 22
def p_line22(p):
    'line22 : CONJ81 CONJ92 PONCT21 PRO221 VERBE221 NOM221 PONCT23 CONJ223 PRO221 VERBE222 ADJ221 PONCT23'
    p[0] = " ".join(p[1:])
    print(f"Ligne 22 analysée : {p[0]}")

# Règle pour la ligne 23
def p_line23(p):
    'line23 : PREP231 PONCT21 D52 NOM231 CONJ71 VERBE231 DET232 NOM232 PONCT41'
    p[0] = " ".join(p[1:])
    print(f"Ligne 23 analysée : {p[0]}")

# Règle pour la ligne 24
def p_line24(p):
    'line24 : PRONOM241 NEG32 PONCT21 AUX11 ADV241 ADV162 PPASSE11 PREP181 D181 ADJ241 NOM241'
    p[0] = " ".join(p[1:])
    print(f"Ligne 24 analysée : {p[0]}")

# Règle pour la ligne 25
def p_line25(p):
    'line25 : CONJ31 NOM121 VERBE251 CONJ92 PONCT21 PRONOM91 VERBE252 ADV251 PONCT23'
    p[0] = " ".join(p[1:])
    print(f"Ligne 25 analysée : {p[0]}")

# Règle pour la ligne 26
def p_line26(p):
    'line26 : DET251 NOM261 PPR261 DET262 PONCT21 NOM231 CONJ111 DET262 PONCT21 NOM231 PPR262 DET201 NOM261 PONCT23'
    p[0] = " ".join(p[1:])
    print(f"Ligne 26 analysée : {p[0]}")

# Règle pour la ligne 27
def p_line27(p):
    'line27 : PREP271 D111 NOM271 CONJ111 D111 NOM272 PONCT41'
    p[0] = " ".join(p[1:])
    print(f"Ligne 27 analysée : {p[0]}")

# Règle pour la ligne 28
def p_line28(p):
    'line28 : CONJ281 ADV281 CONJ92 PONCT21 D52 NOM281 PONCT23 ADV282 ADV283 PONCT151 ADJ281 NOM282 PONCT151'
    p[0] = " ".join(p[1:])
    print(f"Ligne 28 analysée : {p[0]}")

# Règle pour la ligne 29
def p_line29(p):
    'line29 : DET291 ADJ41 VERBE132 PRO291 PONCT21 PREP142 VERBE21 PP291 PONCT151'
    p[0] = " ".join(p[1:])
    print(f"Ligne 29 analysée : {p[0]}")

# Règle pour la ligne 30
def p_line30(p):
    'line30 : INTERJECTION301 PRONOM11 AUX301 CONJ301 PP301 DET201 NOM301 ADJ301 PONCT23'
    p[0] = " ".join(p[1:])
    print(f"Ligne 30 analysée : {p[0]}")

# Règle pour la ligne 31
def p_line31(p):
    'line31 : CONJ31 DET311 NOM311 PRO291 PONCT21 VERBE21 PP311 PONCT151'
    p[0] = " ".join(p[1:])
    print(f"Ligne 31 analysée : {p[0]}")

    

def p_vers1(p):
      'vers1 :   DELIMITER line1 '
      if(p[2]=='1'): 
            print('1 Oh ! vous aurez trop dit au pauvre petit ange')
      else:
            print('erreur au niveau du delimiter de vers1,il faut mettre le delimiter 1')
              
def p_vers2(p):
      'vers2 :   DELIMITER line2 '
      if(p[2]=='2'): 
          print('2 Qu\'il est d\'autres anges là-haut,')
      else:
              print('erreur au niveau du delimiter de vers2,il faut mettre le delimiter 2')
def p_vers3(p):
      'vers3 :   DELIMITER line3 '
      if(p[2]=='3'): 
            print('3 Que rien ne souffre au ciel, que jamais rien n\'y change,')
      else:
              print('erreur au niveau du delimiter de vers3,il faut mettre le delimiter 3')
def p_vers4(p):
      'vers4 :   DELIMITER line4 '
      if(p[2]=='4'): 
            print('4 Qu\'il est doux d\'y rentrer bientôt ;')
      else:
              print('erreur au niveau du delimiter de vers4,il faut mettre le delimiter 4')
def p_vers5(p):
      'vers5 :   DELIMITER line5 '
      if(p[2]=='5'): 
            print(' 5 Que le ciel est un dôme aux merveilleux pilastres,')
      else:
              print('erreur au niveau du delimiter de vers5,il faut mettre le delimiter 5')
def p_vers6(p):
      'vers6 :   DELIMITER line6'
      if(p[2]=='6'): 
            print('6 Une tente aux riches couleurs,')
      else:
              print('erreur au niveau du delimiter de vers6,il faut mettre le delimiter 6')
        
def p_vers7(p):
      'vers7 :   DELIMITER line7'
      if(p[2]=='7'): 
            print('7 Un jardin bleu rempli de lis qui sont des astres,')
      else:
              print('erreur au niveau du delimiter de vers7,il faut mettre le delimiter 7')

def p_vers8(p):
      'vers8 :   DELIMITER line8'
      if(p[2]=='8'): 
            print('8 Et d\'étoiles qui sont des fleurs ;')
      else:
              print('erreur au niveau du delimiter de vers8,il faut mettre le delimiter 8')


def p_vers9(p):
      'vers9 :   DELIMITER line9'
      if(p[2]=='9'): 
            print(' 9 Que c\'est un lieu joyeux plus qu\'on ne saurait dire,')
      else:
              print('erreur au niveau du delimiter de vers9,il faut mettre le delimiter 9')



def p_vers10(p):
      'vers10 :   DELIMITER line10'
      if(p[2]=='10'): 
            print(' 10 Où toujours, se laissant charmer,')
      else:
              print('erreur au niveau du delimiter de vers10,il faut mettre le delimiter 10')


def p_vers11(p):
      'vers11 :   DELIMITER line11 '
      if(p[2]=='11'): 
            print('11 On a les chérubins pour jouer et pour rire,')
      else:
              print('erreur au niveau du delimiter de vers11,il faut mettre le delimiter 1')
def p_vers12(p):
      'vers12 :   DELIMITER line12 '
      if(p[2]=='12'): 
            print('12 Dans une si belle maison !')
      else:
              print('erreur au niveau du delimiter de vers12,il faut mettre le delimiter 1') 
def p_vers13(p):
      'vers13 :   DELIMITER line13 '
      if(p[2]=='13'): 
            print('Qu\'il est doux d\'être un coeur qui brûle comme un cierge,')
      else:
              print('erreur au niveau du delimiter de vers13,il faut mettre le delimiter 2')
def p_vers14(p):
      'vers14 :   DELIMITER line14 '
      if(p[2]=='14'): 
            print('Et de vivre, en toute saison,')
      else:
              print('erreur au niveau du delimiter de vers14,il faut mettre le delimiter 3')
def p_vers15(p):
      'vers15 :   DELIMITER line15 '
      if(p[2]=='15'): 
            print(' 15 Dans une si belle maison !')
      else:
              print('erreur au niveau du delimiter de vers15,il faut mettre le delimiter 4')
def p_vers16(p):
      'vers16 :   DELIMITER line16 '
      if(p[2]=='16'): 
            print(' 16 Et puis vous n\'aurez pas assez dit, pauvre mère,')
      else:
              print('erreur au niveau du delimiter de vers16,il faut mettre le delimiter 16')
def p_vers17(p):
      'vers17 :   DELIMITER line17'
      if(p[2]=='17'): 
            print(' 17 A ce fils si frêle et si doux,')
      else:
              print('erreur au niveau du delimiter de vers17,il faut mettre le delimiter 17')
        
def p_vers18(p):
      'vers18 :   DELIMITER line18'
      if(p[2]=='18'): 
            print(' 18 Que vous étiez à lui dans cette vie amère,')
      else:
              print('erreur au niveau du delimiter de vers18,il faut mettre le delimiter 18')

def p_vers19(p):
      'vers19 :   DELIMITER line19'
      if(p[2]=='19'): 
            print('19 Mais aussi qu\'il était à vous ;')
      else:
              print('erreur au niveau du delimiter de vers19,il faut mettre le delimiter 19')


def p_vers20(p):
      'vers20 :   DELIMITER line20'
      if(p[2]=='20'): 
            print(' 20 Que, tant qu\'on est petit, la mère sur nous veille,')
      else:
              print('erreur au niveau du delimiter de vers20,il faut mettre le delimiter 20')



def p_vers21(p):
      'vers21 :   DELIMITER line21'
      if(p[2]=='21'): 
            print('21 Mais que plus tard on la défend ;')
      else:
              print('erreur au niveau du delimiter de vers21,il faut mettre le delimiter 21')


def p_vers22(p):
      'vers22 :   DELIMITER line22 '
      if(p[2]=='22'): 
            print('22 Et qu\'elle aura besoin, quand elle sera vieille,')
      else:
              print('erreur au niveau du delimiter de vers22,il faut mettre le delimiter 22')
              
def p_vers23(p):
      'vers23 :   DELIMITER line23 '
      if(p[2]=='23'): 
            print('23 D\'un homme qui soit son enfant ;')
      else:
              print('erreur au niveau du delimiter de vers23,il faut mettre le delimiter 23')
def p_vers24(p):
      'vers24 :   DELIMITER line24'
      if(p[2]=='24'): 
            print('24 Vous n\'aurez point assez dit à cette jeune âme')
      else:
              print('erreur au niveau du delimiter de vers24,il faut mettre le delimiter 24')
def p_vers25(p):
      'vers25 :   DELIMITER line25 '
      if(p[2]=='25'): 
            print('25 Que Dieu veut qu\'on reste ici-bas,')
      else:
              print('erreur au niveau du delimiter de vers25,il faut mettre le delimiter 25')
def p_vers26(p):
      'vers26 :   DELIMITER line26 '
      if(p[2]=='26'): 
            print(' 26 La femme guidant l\'homme et l\'homme aidant la femme,')
      else:
              print('erreur au niveau du delimiter de vers5,il faut mettre le delimiter 26')
def p_vers27(p):
      'vers27 :   DELIMITER line27'
      if(p[2]=='27'): 
            print(' 27 Pour les douleurs et les combats ;')
      else:
              print('erreur au niveau du delimiter de vers27,il faut mettre le delimiter 27')
        
def p_vers28(p):
      'vers28 :   DELIMITER line28'
      if(p[2]=='28'): 
            print('28 Si bien qu\'un jour, ô deuil ! irréparable perte !')
      else:
              print('erreur au niveau du delimiter de vers28,il faut mettre le delimiter 28')

def p_vers29(p):
      'vers29 :   DELIMITER line29'
      if(p[2]=='29'): 
            print('29 Le doux être s\'en est allé !... -')
      else:
              print('erreur au niveau du delimiter de vers29,il faut mettre le delimiter 29')


def p_vers30(p):
      'vers30 :   DELIMITER line30'
      if(p[2]=='30'): 
            print('30 Hélas ! vous avez donc laissé la cage ouverte,')
      else:
              print('erreur au niveau du delimiter de vers30,il faut mettre le delimiter 30')



def p_vers31(p):
      'vers31 :   DELIMITER line31'
      if(p[2]=='31'): 
            print('31 Que votre oiseau s\'est envolé !')
      else:
              print('erreur au niveau du delimiter de vers31,il faut mettre le delimiter 31')


#This code integrates speech recognition and parsing to validate a spoken line of poem
def get_proverb_from_voice(parser):
    #Part of the speech_recognition library, used for converting speech to text
    recognizer = sr.Recognizer()

    # Utilise le microphone comme source audio
    #Opens the microphone as the audio source
    with sr.Microphone() as source:
        print("Dis un vers :")
        #Records audio from the microphone
        audio = recognizer.listen(source)

    try:
        # Convertit la parole en texte
        #Converts the recorded audio into text using Google's speech
        #The language='fr' parameter specifies that the speech is in French.
        text = recognizer.recognize_google(audio, language='fr')
        
        text = text.capitalize()

        text = text + ','
        
        # Utilise le texte pour vérifier si le vers est dans la liste existante
        #Validates the recognized text against the predefined grammar rules.
        result = parser.parse(text)
        if result:
            print("Bravo! vers trouvé :", text)
        else:
            print("vers incorrect :", text)

     #Handling Exceptions
    except sr.UnknownValueError:
        print("Impossible de comprendre l'audio")
    except sr.RequestError as e:
        print("Erreur lors de la requête :", e)

#Error Handling in Parsing
def p_error(p):
    global resultParser
    global positionParserError
    if p:
        print(f"Erreur détectée : {p.value} à la position {p.lexpos}")
        positionParserError = {
            "ligne": p.lineno,
            "index": p.lexpos,
            "value": p.value,
            "length": len(p.value)
        }
    else:
        positionParserError = {
            "ligne": "Unknown",
            "index": "Unknown",
            "value": "Unknown",
            "length": "Unknown"
        }
    print("this is a wrong proverb")
    print("positionParserError = ", positionParserError)

# Build the parser
parser = yacc.yacc(debug=True)
# Build the parser
parser = yacc.yacc()

# Example usage of the parser pour verifier syntaxiquemnt 
 
data ="Oh! vous aurez trop dit au pauvre petit ange"
result = parser.parse(data)
print(result)    

get_proverb_from_voice(parser)