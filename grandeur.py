a = int(input("Quel est votre nombre a ?"))
b = int(input("Quel est votre nombre b ?"))
c = int(input("Quel est votre nombre c ?"))

if a > b and a > c :
    print(f"a est le plus grand")
elif b > a and b > c :
    print(f"b est le plus grand")
elif c > a and c > b :
    print(f"c est le plus grand")
