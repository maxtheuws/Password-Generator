import string
import random

def genereer():
    teller = 0
    wachtwoord = ""
    ww1 = ""
    ww2 = ""
    ww3 = ""
    ww4 = ""
    aantaltrue = 0
    mogelijkheid = 0
    lengte = int(input("Wat moet de lengte van het wachtwoord worden?"))
    hoofdletter = input("Wil je hoofdletters in je wachtwoord? (Antwoord met ja of nee)")
    if hoofdletter == "ja":
        hoofdletter = True
    elif hoofdletter == "nee":
        hoofdletter = False
    else:
        print("Voer ja of nee in")
        exit()
    cijfers = input("Wil je cijfers in je wachtwoord?(Antwoord met ja of nee)")
    if cijfers == "ja":
        cijfers = True
    elif cijfers == "nee":
        cijfers = False
    else:
        print("Voer ja of nee in")
        exit()
    symbolen = input("Wil je speciale tekens in je wachtwoord?(Antwoord met ja of nee)")
    if symbolen == "ja":
        symbolen = True
    elif symbolen == "nee":
        symbolen = False
    else:
        print("Voer ja of nee in")
        exit()
    if hoofdletter == True and cijfers == True and symbolen == True:
        mogelijkheid = 1
        aantaltrue = 3
    if hoofdletter == True and cijfers == True and symbolen == False:
        mogelijkheid = 2
        aantaltrue = 2
    if hoofdletter == True and cijfers == False and symbolen == True:
        mogelijkheid = 3
        aantaltrue = 2
    if hoofdletter == False and cijfers == True and symbolen == True:
        mogelijkheid = 4
        aantaltrue = 2
    if hoofdletter == False and cijfers == True and symbolen == False:
        mogelijkheid = 5
        aantaltrue = 1
    if hoofdletter == False and cijfers == False and symbolen == True:
        mogelijkheid = 6
        aantaltrue = 1
    if hoofdletter == False and cijfers == False and symbolen == False:
        mogelijkheid = 7
        aantaltrue = 0
    if hoofdletter == True and cijfers == False and symbolen == False:
        mogelijkheid = 8
        aantaltrue = 1
    teller = lengte - aantaltrue
    if mogelijkheid == 1:
        ww1 = str(random.choice(string.ascii_uppercase))
        ww2 = str(random.choice(string.digits))
        ww3 = str(random.choice(string.punctuation))
        for i in range (0, teller):
            ww4 = ww4 + str(random.choice(string.ascii_letters))
        wachtwoord = ww1 + ww2 + ww3 + ww4
    if mogelijkheid == 2:
        ww1 = random.choice(string.ascii_uppercase)
        ww2 = random.choice(string.digits)
        for i in range (aantaltrue, lengte):
            ww3 = ww3 + str(random.choice(string.ascii_letters))
        wachtwoord = ww1 + ww2 + ww3
    if mogelijkheid == 3:
        ww1 = random.choice(string.ascii_uppercase)
        ww2 = random.choice(string.punctuation)
        for i in range (aantaltrue, lengte):
            ww3 = ww3 + str(random.choice(string.printable))
        wachtwoord = ww1 + ww2 + ww3
    if mogelijkheid == 4:
        ww1 = random.choice(string.digits)
        ww2 = random.choice(string.punctuation)
        for i in range (aantaltrue, lengte):
            ww3 = ww3 + str(random.choice(string.ascii_lowercase))
        wachtwoord = ww1 + ww2 + ww3
    if mogelijkheid == 5:
        ww1 = random.choice(string.digits)
        for i in range (aantaltrue, lengte):
            ww2 = ww2 + str(random.choice(string.ascii_lowercase))
        wachtwoord = ww1 + ww2
    if mogelijkheid == 6:
        ww1 = random.choice(string.punctuation)
        for i in range (aantaltrue, lengte):
           ww2 = ww2 + str(random.choice(string.ascii_lowercase))
        wachtwoord = ww1 + ww2
    if mogelijkheid == 7:
        for i in range (aantaltrue, lengte):
            wachtwoord = wachtwoord + str(random.choice(string.ascii_lowercase))
    if mogelijkheid == 8:
        ww1 = random.choice(string.ascii_uppercase)
        for i in range (aantaltrue, lengte):
           ww2 = ww2 + str(random.choice(string.ascii_letters))
        wachtwoord = ww1 + ww2
    print(wachtwoord)
genereer();
