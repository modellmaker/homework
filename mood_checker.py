print("How are You feeling today?")
mood = input()
mood = mood.lower()

if mood == "happy":
    print("It is great, to see You happy!")
elif mood == "nervous":
    print("Take a few deep breath.")
elif mood == "sad":
    print("Smile, it'll become better soon. :) ")
elif mood == "excited":
    print("Why are You excited?")
elif mood == "relaxed":
    print("Good to hear that.")
else:
    print("I don't recognize this mood.")
