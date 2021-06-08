import random as r
import math
from PIL import Image
import base64

#Mostrem a l'usuari el circuit amb el que es realitza l'exercici
img = Image.open('Passa_alta_ordre2.PNG')
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
    tipusex=''
    print("Benvingut o benvinguda al generador d'exercicis de filtres passa alta d'ordre 2.\n\nSi vol un problema de determinar el tipus de filtre, premi 0.\n\nSi vol un problema de determinar la funció de transferència del filtre , premi 1\n\nSi vol un problema de determinar el coeficient d'amortiment, premi 2\n\nSi vol un problema de trobar la freqüència angular natural, premi 3.\n")
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
        tipusex="Amortiment"
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
    with open("Passa_alta_ordre2.PNG", "rb") as imageFile:
        foto = base64.b64encode(imageFile.read())
        fotostr=foto.decode("utf-8")

    #Creació del fitxer XML
    if numrep==0:
        with open("Passa_alta_ordre2.xml","a") as file:
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
            file.write("<text>$course$/top/PythonQuiz/Analogic/Filtres/Passa alta ordre 2</text>\n")
            file.write("</category>\n")
            file.write("</question>\n")

    for i in range (permutacions):
        #Generació dels valors de les resistències
        C1=r.randrange(2,7,1)

        #Càlcul de la freqüencia angular natural ,el mòdul del guany i la funcio de transferencia
        freqangular="1/"+str(round(math.sqrt(C1),3))+"RC"
        amortiment='('+str(C1+2)+'-A)/'+str(round(math.sqrt(C1)*2,3))
        funciobona='H(s)='+str(C1)+'A(srC)^2'+'/'+'('+str(C1)+'(sRC)^2+('+str(C1+2)+'-A)sRC+1)'

        #Generació de les respostes errònies
        freqangulardolenta1="1/(RC)"
        freqangulardolenta2="1/"+str(round(math.sqrt(C1)/2,3))+"RC"
        freqangulardolenta3="1/"+str(C1)+"RC"
        freqangulardolenta4="0.5/(RC)"
        amortimentdolent1='('+str(C1+1)+'-A)/'+str(round(math.sqrt(C1)*2,3))
        amortimentdolent2='('+str(2*C1+1)+'-A)/'+str(round(math.sqrt(C1)*2,3))
        amortimentdolent3='('+str(C1+2)+'-A)/'+str(round(math.sqrt(C1),3))
        amortimentdolent4='('+str(C1)+'-A)/'+str(round(math.sqrt(C1)*2,3))
        
        funciodolenta1='H(s)=A(srC)^2'+'/'+'('+str(C1)+'(sRC)^2+('+str(C1+2)+'-A)sRC+1)'
        funciodolenta2='H(s)='+str(C1)+'A(srC)^2'+'/'+'('+str(C1)+'(sRC)^2+('+str(2*C1+2)+'-A)sRC+1)'
        funciodolenta3='H(s)='+str(C1)+'A(srC)^2'+'/'+'('+str(C1)+'(sRC)^2+('+str(C1+1)+'-A)sRC+1)'
        funciodolenta4='H(s)='+str(C1)+'A(srC)^2'+'/'+'('+str(C1/2)+'(sRC)^2+('+str(C1+2)+'-A)sRC+1)'

        #Generació dels tipus de filtres
        tipusfiltrebo="Passa alta d'ordre 2"
        tipusfiltredolent1="Passa baixa d'ordre 1"
        tipusfiltredolent2="Passa alta d'ordre 1"
        tipusfiltredolent3="Passa banda d'ordre 2"
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
            respostabona=str(amortiment)
            respostadolenta1=str(amortimentdolent1)
            respostadolenta2=str(amortimentdolent2)
            respostadolenta3=str(amortimentdolent3)
            respostadolenta4=str(amortimentdolent4)

        else:
            respostabona=str(freqangular)
            respostadolenta1=str(freqangulardolenta1)
            respostadolenta2=str(freqangulardolenta2)
            respostadolenta3=str(freqangulardolenta3)
            respostadolenta4=str(freqangulardolenta4)

        #Es crea l'enunciat del fitxer XML
        enunciat_xml="El circuit de la figura és un filtre actiu amb arquitectura de Sallen-Key simplificada, que presenta una funció de transferencia H(s) com la indicada al costat de la figura. Les admitàncies Y1 i Y3 corresponen a dos condensadors de capacitats "+str(C1)+"C i C respectivament. Les admitàncies Y2 i Y4 corresponen a dues resistències de valor R. El valor del guany de l'amplificador és A." 
        if tipus==3:
            enunciat_xml+=" Calcula la freqüència angular natural"
        elif tipus==2:
            enunciat_xml+=" Calcula el coeficient d'amortiment"
        elif tipus==0:
            enunciat_xml+=" Determina el tipus de filtre."
        else:
            enunciat_xml+=" Determina la funció de transferència del filtre."

        #Es mostren per pantalla els valors aleatoris generats i les respostes
        enunciat_py="El valor del condensador és C1: "+str(C1)+"C\n"
        if tipus==3:
            enunciat_py+="La freqüència angular natural del filtre és "+respostabona
        elif tipus==2:
            enunciat_py+="El coeficient d'amortiment del filtre és "+respostabona
        elif tipus==0:
            enunciat_py+="El tipus de filtre és "+respostabona
        else:
            enunciat_py+="La funció de transferència del filtre és "+respostabona
        print("\n"+enunciat_py+"\n")

        #Es creen les preguntes dins dels fitxers XML
        with open("Passa_alta_ordre2.xml","a") as file:
            file.write("<question type=\"multichoice\">\n")
            file.write("<name>\n")
            file.write("<text>"+tipusex+" Permutació "+str(i)+"</text>\n") #i indica la permutació#
            file.write("</name>\n")
            file.write("<questiontext format=\"html\">\n")
            file.write("<file name=\"Passa_alta_ordre2.PNG\" path=\"/\" encoding=\"base64\">"+str(fotostr)+"\n"+"</file>\n")
            file.write("<text><![CDATA["+enunciat_xml+".<br><br><img src=\"@@PLUGINFILE@@/Passa_alta_ordre2.PNG\" alt="" width=\"284\" height=\"425\" role=\"presentation\" class=\"img-responsive atto_image_button_text-bottom\"><br>]]></text>\n")
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
    print("Si vol generar un altre exercici de filtres passa alta d'ordre 2, premi 0. En cas contrari, premi 1\n")
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
                print("\nGràcies per haver utilitzat el generador d'exercicis de filtres passa alta d'ordre 2!")
                with open("Passa_alta_ordre2.xml","a") as file:
                    file.write("</quiz>")
            else:
                print("\n")
    numrep+=1

