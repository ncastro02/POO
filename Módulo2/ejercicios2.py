#Cadenas
#Ejemplo conteo de caracteres
word = 'by'
print(len(word)) #len cuenta el no. de caracteres(2)

empty = ''
print(len(empty)) #(0)

i_am = 'I\'m'
print(len(i_am)) #(3)

multiline = '''Línea #1 
Línea #2''' #El caracter invisible es el espacio en blanco (\n)
print(len(multiline)) #(17)

#Ejemplo operaciones con cadenas
str1 = 'a'
str2 = 'b'
print(str1 + str2) #ab
print(str2 + str1) #ba
print(5 * 'a') #aaaaa
print('b' * 4) #bbbb

# La función ord ().
char_1 = 'a'
char_2 = ' '  # space
print(ord(char_1))
print(ord(char_2))

# Demostración de la función chr.
print(chr(97)) 
print(chr(945))

# Indexando cadenas.
the_string = 'silly walks'
for ix in range(len(the_string)):
    print(the_string[ix], end=' ')
print()

# Iterando a través de una cadena.
the_string = 'silly walks'
for character in the_string:
    print(character, end=' ')
print()

# Rebanadas
alpha = "abdefg"
print(alpha[1:3]) #bd
print(alpha[3:]) #efg
print(alpha[:3]) #abd
print(alpha[3:-2]) #e
print(alpha[-3:4]) #e
print(alpha[::2]) #adf
print(alpha[1::2]) #beg

alphabet = "bcdefghijklmnopqrstuvwxy"
alphabet = "a" + alphabet
alphabet = alphabet + "z"
print(alphabet) 

# Demonstrando min() - Ejemplo 1:
print(min("aAbByYzZ"))
# Demonstrando min() - Ejemplo 2 y 3:
t = 'Los Caballeros Que Dicen "¡Ni!"'
print('[' + min(t) + ']')
t = [0, 1, 2]
print(min(t))

# Demostración de max() - Ejemplo 1:
print(max("aAbByYzZ"))
# Demostración de max() - Ejemplo 2 & 3:
t = 'Los Caballeros Que Dicen "¡Ni!"'
print('[' + max(t) + ']')
t = [0, 1, 2]
print(max(t))

# Demonstrando el método index():
print("aAbByYzZaA".index("b")) #Busca la secuencia desde el principio
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

# Demostración de la función list():
print(list("abcabc"))
# Demostración de la función list():
print("abcabc".count("b"))
print('abcabc'.count("d"))

#Los operadores in y not in
alphabet = "abcdefghijklmnopqrstuvwxyz"
print("f" in alphabet) #True
print("F" in alphabet) #False
print("1" in alphabet) #False
print("ghi" in alphabet) #True
print("Xyz" in alphabet) #False

# Demostración del método capitalize():
print('aBcD'.capitalize()) #Abcd
# Demostración del método center():
print('[' + 'alpha'.center(10) + ']')
# Demostración del método endswith():
if "epsilon".endswith("on"):
    print("si")
else:
    print("no")
# Demostración del método find():
print("Eta".find("ta"))
print("Eta".find("mma"))

# Demostración del método the isalnum():
print('lambda30'.isalnum()) #True
print('lambda'.isalnum()) #True
print('30'.isalnum()) #True
print('@'.isalnum()) #False
print('lambda_30'.isalnum()) #False








