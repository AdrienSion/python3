from operator import truediv
# Commentait ctrl shift :
# shift alt T = ouvrir terminal

nombre = 123
print(nombre)
# type permet de savoir de quel type de données il s'agit
print(type(nombre))


# On peut écrire un entier avec .0 pour dire que c'est un float
nombre = 3.14
print(nombre)
print(type(nombre))

nombre = "123"
print(nombre)
print(type(nombre))
# exit() permet de mettre fin à la requette

text = "lorem ipsum"
print(text)

is_day = True
print(is_day)
print(type(is_day))

has_sugar = False
print(has_sugar)

has_accepted_ula = None
print(has_accepted_ula)

html_code = '<h1>Titre de mon blog</h1>'
print(html_code)

nickname = "John \"doeuf\" doe"
nickname = "John O\"Connor"
print(nickname)

multiline_text = "foo\nbar\nbaz"
print(multiline_text)

multiline_text = """foo
bar
baz"""
print(multiline_text)

# Fonctions = code qui effectue des opérations 

# type()

nombre = "2.71"
print(nombre)
print(type(nombre))

nombre = float(nombre)
print(nombre)
print(type(nombre))

nombre = 3.14
print(nombre)
print(type(nombre))

nombre = int(nombre)
print(nombre)
print(type(nombre))

texte = str(nombre)
print(texte)
print(type(texte))

my_var = 0
my_var = bool(my_var)
print(my_var)

my_var = 1
my_var = bool(my_var)
print(my_var)

my_var = -123
my_var = bool(my_var)
print(my_var)

my_var = "0"
my_var = bool(my_var)
print(my_var)

my_var = ""
my_var = bool(my_var)
print(my_var)

my_var = " "
my_var = bool(my_var)
print(my_var)

my_var = "123"
my_var = bool(my_var)
print(my_var)

my_var = "-123"
my_var = bool(my_var)
print(my_var)

my_var = [123, "abc", False]
my_var = bool(my_var)
print(my_var)

my_var = [False]
my_var = bool(my_var)
print(my_var)

my_var = [None]
my_var = bool(my_var)
print(my_var)

my_var = None
my_var = bool(my_var)
print(my_var)