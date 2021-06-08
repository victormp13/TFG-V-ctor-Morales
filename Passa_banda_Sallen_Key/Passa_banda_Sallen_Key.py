import random as r
import math
from PIL import Image
import base64

#Mostrem a l'usuari el circuit amb el que es realitza l'exercici
img = Image.open('Passa_banda_Sallen_Key.PNG')
img.show()

#Definim la variable que controla si es vol tornar a generar un altre problema
repetir=True
numrep=0

#Preguntem a l'usuari quantes permutacions vol generar
while(repetir==True):
    tipus=-1
    permutacions=-1
    repeticio=-1
    tipus0=-1
    permutacions0=-1
    repeticio0=-1
    print("Benvingut o benvinguda al generador d'exercicis de filtres passa banda amb arquitectura de Sallen-Key.\n\nSi vol un problema de determinar el tipus de filtre, premi 0.\n\nSi vol un problema de determinar la funció de transferència del filtre , premi 1\n\nSi vol un problema de determinar el guany a la freqüència natural, premi 2\n\nSi vol un problema de trobar la freqüència angular natural, premi 3.\n")
    while(tipus<0 or tipus>3):
        tipus0=str(input())
        if tipus0.isdigit()==False:
            print("\n")
            print("Valor no vàlid. Torni a introduir un valor vàl·lid.\n")
        else:
            tipus=int(tipus0)
            if tipus<0 or tipus>3:
                print("\n")
                print("Valor no vàlid. Torni a introduir un valor vàl·lid.\n")

    if tipus==0:
        tipusex="Tipus de filtre"
    elif tipus==1:
        tipusex="Funció de transferència"
    elif tipus==2:
        tipusex="Guany"
    else:
        tipusex="Freqüència angular"

    print("\n\nQuants permutacions diferents voldrà crear?\n")
    while(permutacions<=0):
        permutacions0=str(input())
        if permutacions0.isdigit()==False:
            print("\n")
            print("Valor no vàlid. Torni a introduir un valor vàl·lid.\n")
        else:
            permutacions=int(permutacions0)

    #Convertim la foto a decodificació utf-8
    with open("Passa_banda_Sallen_Key.PNG", "rb") as imageFile:
        foto = base64.b64encode(imageFile.read())
        fotostr=foto.decode("utf-8")

    #Creació del fitxer XML
    if numrep==0:
        with open("Passa_banda_Sallen_Key.xml","a") as file:
            file.write("<?xml version=\"1.0\" encoding=\"iso-8859-1\"?>\n")
            file.write("<quiz>\n")
            file.write("<question type=\"category\">\n")
            file.write("<category>\n")
            file.write("<text>$course$/top</text>\n")
            file.write("</category>\n")
            file.write("</question>\n")
            file.write("<question type=\"category\">\n")
            file.write("<category>\n")
            file.write("<text>$course$/top/PythonQuiz</text>\n")
            file.write("</category>\n")
            file.write("</question>\n")
            file.write("<question type=\"category\">\n")
            file.write("<category>\n")
            file.write("<text>$course$/top/PythonQuiz/Analogic</text>\n")
            file.write("</category>\n")
            file.write("</question>\n")
            file.write("<question type=\"category\">\n")
            file.write("<category>\n")
            file.write("<text>$course$/top/PythonQuiz/Analogic/Filtres</text>\n")
            file.write("</category>\n")
            file.write("</question>\n")
            file.write("<question type=\"category\">\n")
            file.write("<category>\n")
            file.write("<text>$course$/top/PythonQuiz/Analogic/Filtres/Passa banda Sallen-Key</text>\n")
            file.write("</category>\n")
            file.write("</question>\n")

    for i in range (permutacions):
        #Generació dels valors de les resistències
        R1=r.randrange(1,6,1)
        R2=R1*r.randrange(1,6,1)/2
        A=round(1+R2/R1,3)

        #Càlcul de la freqüencia angular natural ,el mòdul del guany i la funcio de transferencia
        freqangular=str(round(math.sqrt(2),3))+"/(RC)"
        guany=round(A/(4-A),3)
        funciobona='H(s)='+str(round(A/2,3))+'sRC'+' / '+'(0.5(sRC)^2+'+str(round((4-A)/2,3))+'sRC+1)'
            

        #Generació de les respostes errònies
        freqangulardolenta1=str(2)+"/(RC)"
        freqangulardolenta2=str(4)+"/(RC)"
        freqangulardolenta3=str(round(math.sqrt(2)/2,3))+"/(RC)"
        freqangulardolenta4=str(round(math.sqrt(2)*2,3))+"/(RC)"
        guanydolent1=round(guany/2,3)
        guanydolent2=round(guany*2,3)
        guanydolent3=round(guany*math.sqrt(2),3)
        guanydolent4=round(guany*3,3)
        funciodolenta1='H(s)='+str(round(A,3))+'sRC'+'/'+'((sRC)^2+'+str(round((4-A),3))+'sRC+1)'
        funciodolenta2='H(s)='+str(round(A/2,3))+'sRC'+'/'+'((sRC)^2+'+str(round((4-A)/2,3))+'sRC+1)'
        funciodolenta3='H(s)='+str(round(A/2,3))+'sRC'+'/'+'(0.5(sRC)^2'+str(round((A-4)/2,3))+'sRC+1)'
        funciodolenta4='H(s)='+str(round(A,3))+'sRC'+'/'+'(0.5(sRC)^2+'+str(round((4-A)/2,3))+'sRC+1)'

        #Generació dels tipus de filtres
        tipusfiltrebo="Passa banda d'ordre 2"
        tipusfiltredolent1="Passa alta d'ordre 1"
        tipusfiltredolent2="Passa baixa d'ordre 1"
        tipusfiltredolent3="Passa alta d'ordre 2"
        tipusfiltredolent4="Passa baixa d'ordre 2"

        #Definim les respostes en funció de la opció triada
        if tipus==0:
            respostabona=tipusfiltrebo
            respostadolenta1=tipusfiltredolent1
            respostadolenta2=tipusfiltredolent2
            respostadolenta3=tipusfiltredolent3
            respostadolenta4=tipusfiltredolent4

        elif tipus==1:
            respostabona=funciobona
            respostadolenta1=funciodolenta1
            respostadolenta2=funciodolenta2
            respostadolenta3=funciodolenta3
            respostadolenta4=funciodolenta4

        elif tipus==2:
            respostabona=str(guany)
            respostadolenta1=str(guanydolent1)
            respostadolenta2=str(guanydolent2)
            respostadolenta3=str(guanydolent3)
            respostadolenta4=str(guanydolent4)

        else:
            respostabona=str(freqangular)
            respostadolenta1=str(freqangulardolenta1)
            respostadolenta2=str(freqangulardolenta2)
            respostadolenta3=str(freqangulardolenta3)
            respostadolenta4=str(freqangulardolenta4)

        #Es crea l'enunciat del fitxer XML
        enunciat_xml="El circuit de la figura és un filtre actiu amb arquitectura de Sallen-Key, que presenta una funció de transferencia H(s) com la indicada al costat de la figura. Les admitàncies Y3 i Y5 corresponen a dos condensadors de capacitat C. Les admitàncies Y1, Y2 i Y5 corresponen a tres resistències de valor R. L'amplificador té un guany A que es calcula amb la fórmula indicada al costat de la figura i els valors de les resistències R1 i R2 són de "+str(R1)+"k i "+str(R2)+"k respectivament." 
        if tipus==3:
            enunciat_xml+=" Calcula la freqüència angular natural"
        elif tipus==2:
            enunciat_xml+=" Calcula el mòdul del guany a la freqüència natural del filtre"
        elif tipus==0:
            enunciat_xml+=" Determina el tipus de filtre."
        else:
            enunciat_xml+=" Determina la funció de transferència del filtre."

        #Es mostren per pantalla els valors aleatoris generats i les respostes
        enunciat_py="Els valors de les resistències són R1: "+str(R1)+"k i R2: "+str(R2)+"k.\n"
        if tipus==3:
            enunciat_py+="La freqüència angular natural del filtre és "+respostabona
        elif tipus==2:
            enunciat_py+="El mòdul del guany a la freqüència natural del filtre és "+respostabona
        elif tipus==0:
            enunciat_py+="El tipus de filtre és "+respostabona
        else:
            enunciat_py+="La funció de transferència del filtre és "+respostabona
        print("\n"+enunciat_py+"\n")

        #Es creen les preguntes dins dels fitxers XML
        with open("Passa_banda_Sallen_Key.xml","a") as file:
            file.write("<question type=\"multichoice\">\n")
            file.write("<name>\n")
            file.write("<text>"+tipusex+" Permutació "+str(i)+"</text>\n") #i indica la permutació#
            file.write("</name>\n")
            file.write("<questiontext format=\"html\">\n")
            file.write("<file name=\"Passa_banda_Sallen_Key.PNG\" path=\"/\" encoding=\"base64\">"+str(fotostr)+"\n"+"</file>\n")
            file.write("<text><![CDATA["+enunciat_xml+".<br><br><img src=\"@@PLUGINFILE@@/Passa_banda_Sallen_Key.PNG\" alt="" width=\"284\" height=\"425\" role=\"presentation\" class=\"img-responsive atto_image_button_text-bottom\"><br>]]></text>\n")
            file.write("</questiontext>\n")
            file.write("<generalfeedback format=\"html\">\n")
            file.write("<text></text>\n")
            file.write("</generalfeedback>\n")
            file.write("<hidden>0</hidden>\n")
            file.write("<single>true</single>\n")
            file.write("<shuffleanswers>true</shuffleanswers>\n")
            file.write("<answernumbering>none</answernumbering>\n")
            file.write("<correctfeedback format=\"html\">\n")
            file.write("<text>La teva resposta és correcta.</text>\n")
            file.write("</correctfeedback>\n")
            file.write("<incorrectfeedback format=\"html\">\n")
            file.write("<text>La teva resposta és incorrecta.</text>\n")
            file.write("</incorrectfeedback>\n")
            file.write("<shownumcorrect/>\n")
            file.write("<answer fraction=\"100\" format=\"html\">\n")
            file.write("<text>"+"<![CDATA["+str(respostabona)+"]]></text>\n")
            file.write("<feedback format=\"html\">\n")
            file.write("<text></text>\n")
            file.write("</feedback>\n")
            file.write("</answer>\n")
            file.write("<answer fraction=\"-25\" format=\"html\">\n")
            file.write("<text><![CDATA["+str(respostadolenta1)+"]]></text>\n")
            file.write("<feedback format=\"html\">\n")
            file.write("<text></text>\n")
            file.write("</feedback>\n")
            file.write("</answer>\n")
            file.write("<answer fraction=\"-25\" format=\"html\">\n")
            file.write("<text><![CDATA["+str(respostadolenta2)+"]]></text>\n")
            file.write("<feedback format=\"html\">\n")
            file.write("<text></text>\n")
            file.write("</feedback>\n")
            file.write("</answer>\n")
            file.write("<answer fraction=\"-25\" format=\"html\">\n")
            file.write("<text><![CDATA["+str(respostadolenta3)+"]]></text>\n")
            file.write("<feedback format=\"html\">\n")
            file.write("<text></text>\n")
            file.write("</feedback>\n")
            file.write("</answer>\n")
            file.write("<answer fraction=\"-25\" format=\"html\">\n")
            file.write("<text><![CDATA["+str(respostadolenta4)+"]]></text>\n")
            file.write("<feedback format=\"html\">\n")
            file.write("<text></text>\n")
            file.write("</feedback>\n")
            file.write("</answer>\n")
            file.write("<answer fraction=\"0\" format=\"html\">\n")
            file.write("<text><![CDATA[Deixa en blanc]]></text>\n")
            file.write("<feedback format=\"html\">\n")
            file.write("<text></text>\n")
            file.write("</feedback>\n")
            file.write("</answer>\n")
            file.write("</question>\n")

    #Preguntem a l'usuari si vol generar un altre exercici 
    print("Si vol generar un altre exercici de filtres passa banda amb arquitectura de Sallen-Key, premi 0. En cas contrari, premi 1\n")
    while(repeticio<0 or repeticio>1):
        repeticio0=str(input())
        if repeticio0.isdigit()==False:
            print("\n")
            print("Valor no vàlid. Torni a introduir un valor vàl·lid.\n")
        else:
            repeticio=int(repeticio0)
            if repeticio<0 or repeticio>1:
                print("\n")
                print("Valor no vàlid. Torni a introduir un valor vàl·lid.\n")
            elif repeticio==1:
                repetir=False
                print("\nGràcies per haver utilitzat el generador d'exercicis de filtres passa banda amb arquitectura de Sallen-Key!")
                with open("Passa_banda_Sallen_Key.xml","a") as file:
                    file.write("</quiz>")
            else:
                print("\n")
    numrep+=1

