import ply.lex as lex

import re

global resultLexer;global positionLexerError



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
#t_PONCT151=r'!'
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