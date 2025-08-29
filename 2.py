
str=input("Enter the string: ").upper()
word="LUMOS"
runes=0
result=""
for i in range(len(str)):
    if str[i] in word and not str[i] in result:
        result+=str[i]
    runes+=1
    if result==word:
        break

if result==word:
    print(f"Found the spell in {runes} runes")
else:
    print(-1)

