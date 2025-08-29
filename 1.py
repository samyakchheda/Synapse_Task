from itertools import combinations

Pokedex = {
"Pikachu": ("Electric",),
"Charizard": ("Fire", "Flying"),
"Lapras": ("Water", "Ice"),
"Machamp": ("Fighting",),
"Mewtwo": ("Psychic", "Fighting"),
"Hoopa": ("Psychic", "Ghost", "Dark"),
"Lugia": ("Psychic", "Flying", "Water"),
"Squirtle": ("Water",),
"Gengar": ("Ghost", "Poison"),
"Onix": ("Rock", "Ground")
}
k=int(input("Enter the number of Pokemon you want in your squad: "))
combo=list(combinations(Pokedex.keys(),k))
max_types=0
squad=[]

for c in combo:
    type=set()
    for pokemon in c:
        type.update(Pokedex[pokemon])
        if len(type)>max_types:
            max_types=len(type)
            squad=c
    type.clear()
print(f"Best squad: {squad} with {max_types} unique types")

