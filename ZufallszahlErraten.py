from random import randint
Zufallszahl = randint(0,100)                                                                    #Erstellen der Zufallszahl.
Eingabe = int(101)                                                                              #Eingabe wird definiert.
while Eingabe < 0 or Eingabe > 100:                                                             #Anfordern einer Eingabe und Überprüfung, ob die angegebene Zahl den Anforderungen Entspricht.
    Eingabe = input('Geben Sie eine Zahl von 0 - 100 an: ')
    try:                                                                                        #Umwandeln der Eingabe in das "int" Format und überprüfen, ob eine gültige Eingabe gemacht wurde.
        Eingabe = int(Eingabe)
    except:                                                                                     #bei einer ungültigen Eingabe wird eine Eingabe außerhalb des Anforderungsbereichen Angegeben, sodass der Benutzer wieder Angefragt wird.
        Eingabe = 101
while not Eingabe == Zufallszahl:                                                               #Überprüfung, ob die Zufallszahl erraten wurde. Andernfalls wird dem Nutzer die Information gegeben,
    if Eingabe > Zufallszahl:                                                                   #ob sich der angegebene Wert unter oder über dem gesuchten Wert befindet und ein neuer Versuch gefordert.
        print('Die von Ihnen Eingegebene Zahl ist Groesser als die gesuchte Zahl')
    else:
        print('Die von Ihnen Eingegebene Zahl ist kleiner als die gesuchte Zahl')
    Eingabe = int(101)
    while Eingabe < 0 or Eingabe > 100:
        Eingabe = input('Versuchen Sie es erneut mit einer Zahl von 0 - 100: ')
        try:
            Eingabe = int(Eingabe)
        except:
            Eingabe = 101
print('Herzlichten Glückwunsch, Sie haben die gesuchte Zahl erraten')                           #Sobald die Zufallszahl Erraten wurde, wird dem Nutzer beglückwünscht.
temp = input('Geben Sie etwas beliebiges an, um das Programm zu beenden: ')                     #Zuletzt kann der Nutzer durch das Angeben von etwas beliebigem oder dem einfachen betätigen der Entertaste das Programm beenden.
