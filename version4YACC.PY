import ply.yacc as yacc
from lex4 import tokens
import ply.lex as lex

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
    print("this is a wrong line")
    print("positionParserError = ", positionParserError)

# Build the parser
parser = yacc.yacc(debug=True)



# Example usage of the parser pour verifier syntaxiquemnt 
 
data ="Si bien qu'un jour , ô deuil ! irréparable perte !"
result = parser.parse(data)
print(result)    

