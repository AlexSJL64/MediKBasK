def main():
    print()

#Ask When? 
moment=input("Is it the morning?")
if moment == "yes":
    print("Egun on!")
    print()
else:
    print("Arratsalde on!")
    print()

#who is the user? User Dictionnary 
users={"service agent":"langilea", 
"nursing assistant":"artatzaile-laguntzailea",
 "nurse":"erizaina",
 "physiotherapist":"kinesiterapeuta",
 "doctor":"medikua", 
 "psychologist":"psikologoa"}
user=input("Who are you? Nursing assistant? Nurse? Physiotherapist?Doctor?Psychologist?... Tell me, I will help to translate!").strip().lower()
print(f"In Basque:{users[user]} naiz!")
print()

#Patient presentation
print("What is your name? Where do you come from? How old are you?")
print("Follow this translation below...")
print("Nola deitzen zara? Nongoa Zara? Zenbat urte dituze?")

#stop if not easy to understand 
print ()
professional= input("Too hard to understand?")
if professional=="yes":
    print("You can say: Ez dut ulertzen! it means I don't understand!")
else:
    print("Let's go! GOAZEN!!")

#Ask for symptoms 
print("Now we ask: how are you? Nola zara?")
symptoms={"I am hungry": "Gose naiz",
"I am cold": "Hoztua naiz", "I am hot":"Berotua naiz", 
"I am thirsty":"Egarri naiz", 
"I feel bad":" Gaizki naiz", 
"I am tired":"Aketua naiz","I am fine":"Ongi naiz"}
print("What is the patient choice in this list? I will help to translate!")
for symptom in symptoms:
    print("-", symptom)
choice= input("Patient choice?")
if choice in symptoms:
    print("In Basque:", symptoms[choice])
else:
    print("I can't help, I don't have it in my dictionnary!")




if __name__ == "__main__":
    main()