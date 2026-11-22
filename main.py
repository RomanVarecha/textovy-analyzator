"""Projekt 1:Textový analyzátor"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

line = "-" * 40

# znaky, které se odstraní ze začátku a konce slov
PUNCTUATION = ".,:;!?()[]{}\"'-"

# přihlášení uživatele
username = input("username:").strip()
password = input("password:").strip()

if username in users and users[username] == password:
    print(line)
    print(f"Welcome to the app, {username}")
    print(f"We have {len(TEXTS)} texts to be analyzed.")
    print(line)
else:
    print("unregistered user, terminating the program..")
    exit()

# výběr textu
choice = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ").strip()

if not choice.isdigit():
    print("You have to enter a number, terminating the program..")
    exit()

choice = int(choice)

if choice < 1 or choice > len(TEXTS):
    print("There is no text with this number, terminating the program..")
    exit()

text = TEXTS[choice - 1]

# rozdělení textu na slova a odstranění interpunkce
words = []
for word in text.split():
    word = word.strip(PUNCTUATION)
    if word:    # samotná interpunkce by po očištění zůstala prázdná
        words.append(word)

# počítání slov
titlecase = 0
uppercase = 0
lowercase = 0
numbers_count = 0
numbers_sum = 0

for word in words:
    if word.isdigit():
        numbers_count += 1
        numbers_sum += int(word)
    elif word.istitle():
        titlecase += 1
    elif word.isupper():
        uppercase += 1
    elif word.islower():
        lowercase += 1

print(line)
print(f"There are {len(words)} words in the selected text.")
print(f"There are {titlecase} titlecase words.")
print(f"There are {uppercase} uppercase words.")
print(f"There are {lowercase} lowercase words.")
print(f"There are {numbers_count} numeric strings.")
print(f"The sum of all the numbers {numbers_sum}")

# četnost délek slov: klíč = délka slova, hodnota = kolikrát se vyskytla
lengths = {}
for word in words:
    length = len(word)
    if length in lengths:
        lengths[length] += 1
    else:
        lengths[length] = 1

# sloupcový graf - šířka sloupce podle nejdelší řady hvězdiček
width = len("OCCURRENCES") + 5    # záhlaví s mezerami kolem
for count in lengths.values():
    if count > width:
        width = count

print(line)
print("LEN|" + "OCCURRENCES".center(width) + "|NR.")
print(line)

for length in sorted(lengths):
    count = lengths[length]
    length_text = str(length).rjust(3)    # délka zarovnaná doprava na 3 znaky
    stars = "*" * count
    stars_text = stars.ljust(width)       # hvězdičky doplněné mezerami
    print(f"{length_text}|{stars_text}|{count}")
