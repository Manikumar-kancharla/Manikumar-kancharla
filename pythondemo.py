#find vowels and consonents from user input and integer given print invalid 




mam=input("eneter a alphabets  :")
mam.lower()

if mam in ("a","e","i","o","u"):
    print("vowels")

elif mam >="a" and mam<="z":
    print("consonent")
else:
    print("invalid")
