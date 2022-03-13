rain = input("Is it raining? (yes/no) : ")

if rain.lower() == "yes" :
    wind = input("Is it windy? (yes/no) : ")
    if wind.lower() == "yes" :
        print("It is too windy for an umbrella")
    else :
        print("Take an umbrella")
else :
    print("Enjoy your day")