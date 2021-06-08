import random as r
import math
from PIL import Image
import base64
import cmath

#Mostrem a l'usuari el circuit amb el que es realitza l'exercici
img = Image.open('Passa_banda_Rauch.PNG')
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
    print("Benvingut o benvinguda al generador d'exercicis de filtres passa banda amb arquitectura de Rauch.\n\nSi vol un problema de trobar la freqüència angular natural, premi 0.\n\nSi vol un problema de trobar el mòdul del guany a la freqüència natural, premi 1\n\nSi vol un problema de trobar el desfasament del circuit a la freqüència natural, premi 2\n")
    while(tipus<0 or tipus>2):
        tipus0=str(input())
        if tipus0.isdigit()==False:
            print("\n")
            print("Valor no vàlid. Torni a introduir un valor vàl·lid.\n")
        else:
            tipus=int(tipus0)
            if tipus<0 or tipus>2:
                print("\n")
                print("Valor no vàlid. Torni a introduir un valor vàl·lid.\n")

    if tipus==0:
        tipusex="Freqüència angular"
    elif tipus==1:
        tipusex="Mòdul del guany"
    else:
        tipusex="Desfasament"

    print("\n\nQuants permutacions diferents voldrà crear?\n")
    while(permutacions<=0):
        permutacions0=str(input())
        if permutacions0.isdigit()==False:
            print("\n")
            print("Valor no vàlid. Torni a introduir un valor vàl·lid.\n")
        else:
            permutacions=int(permutacions0)

    #Convertim la foto a decodificació utf-8
    with open("Passa_banda_Rauch.PNG", "rb") as imageFile:
        foto = base64.b64encode(imageFile.read())
        fotostr=foto.decode("utf-8")

    #Creació del fitxer XML
    if numrep==0:
        with open("Passa_banda_Rauch.xml","a") as file:
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
            file.write("<text>$course$/top/PythonQuiz/Analogic/Filtres/Passa banda Rauch</text>\n")
            file.write("</category>\n")
            file.write("</question>\n")

    for i in range (permutacions):
        #Generació dels valors de les admitàncies
        y1=1
        y2=r.randrange(1,6,1)
        r3=r.randrange(50,300,50)
        y3=1/r3
        y4=1
        y5=1

        #Càlcul de la freqüencia angular natural i el mòdul del guany 
        freqangular=math.sqrt(1/(y4*y5/y3))
        freqangular0=complex(0,freqangular)
        guany=round(abs(-y1*y5/y3*freqangular0/(y4*y5/y3*freqangular0*freqangular0+y1+y2*freqangular0+y4*freqangular0+y5*freqangular0)),3)
        guanycom=-y1*y5/y3*freqangular0/(y4*y5/y3*freqangular0*freqangular0+y1+y2*freqangular0+y4*freqangular0+y5*freqangular0)
        if guanycom.imag<0.1:
            guanycom=complex(guanycom.real,0)
        fase=cmath.phase(guanycom)
        fase=round(math.degrees(fase),3)

        #Generació de les respostes errònies
        freqangulardolenta1=round(freqangular/10,4)
        freqangulardolenta2=round(freqangular*2,4)
        freqangulardolenta3=round(freqangular/3,4)
        freqangulardolenta4=round(freqangular/5,4)
        freqangulardolenta5=round(freqangular/10,4)
        freqangulardolenta6=round(freqangular,4)
        freqangulardolenta7=round(freqangular,4)
        freqangulardolenta8=round(freqangular/10,4)
        guanydolent1=round(guany*10,4)
        guanydolent2=round(guany/10,4)
        guanydolent3=round(guany/3,4)
        guanydolent4=round(guany*3,4)
        guanydolent5=round(guany,4)
        guanydolent6=round(guany/10,4)
        guanydolent7=round(guany/3,4)
        guanydolent8=round(guany/3,4)

        #Definim les respostes en funció de la opció triada
        if tipus==0:
            respostabona=str(freqangular)+"/(RC)"
            respostadolenta1=str(freqangulardolenta1)+"/(RC)"
            respostadolenta2=str(freqangulardolenta2)+"/(RC)"
            respostadolenta3=str(freqangulardolenta3)+"/(RC)"
            respostadolenta4=str(freqangulardolenta4)+"/(RC)"

        elif tipus==1:
            respostabona=str(guany)
            respostadolenta1=str(guanydolent1)
            respostadolenta2=str(guanydolent2)
            respostadolenta3=str(guanydolent3)
            respostadolenta4=str(guanydolent4)

        else:
            respostabona=str(fase)+'º'
            respostadolenta1=str(fase-45)+'º'
            respostadolenta2=str(fase-90)+'º'
            respostadolenta3=str(fase-180)+'º'
            respostadolenta4=str(fase-135)+'º'

        #Es crea l'enunciat del fitxer XML
        enunciat_xml="El circuit de la figura és un filtre actiu amb arquitectura de Rauch, que presenta una funció de transferencia H(s) com la indicada al costat de la figura. L'admitància Y2 correspon a un condensador de capacitat "+str(y2)+"C. Les admitàncies Y4 i Y5 corresponen a dos condensadors idèntics de capacitat C. Les admitàncies Y1 i Y3 corresponen, respectivament, a resistències de valors R i "+str(int(r3))+"R."
        if tipus==0:
            enunciat_xml+=" Calcula la freqüència angular natural"
        elif tipus==1:
            enunciat_xml+=" Calcula el mòdul del guany a la freqüència natural del filtre"
        else:
            enunciat_xml+=" Calcula el desfasament del circuit a la freqüència natural del filtre"

        #Es mostren per pantalla els valors aleatoris generats i les respostes
        enunciat_py="Els valors de les admitàncies són Y1: "+str(y1)+"/R, Y2: "+str(y2)+"sC, Y3: "+str(round(y3,4))+"/R, Y4: "+str(y4)+"sC, Y5: "+str(y5)+"sC.\n"
        if tipus==0:
            enunciat_py+="La freqüència angular natural del filtre és "+respostabona
        elif tipus==1:
            enunciat_py+="El mòdul del guany a la freqüència natural del filtre és "+respostabona
        else:
            enunciat_py+="El desfassament del circuit a la freqüència natural és "+respostabona
        print("\n"+enunciat_py+"\n")
        
        #Es creen les preguntes dins dels fitxers XML
        with open("Passa_banda_Rauch.xml","a") as file:
            file.write("<question type=\"multichoice\">\n")
            file.write("<name>\n")
            file.write("<text>"+tipusex+" Permutació "+str(i)+"</text>\n") #i indica la permutació#
            file.write("</name>\n")
            file.write("<questiontext format=\"html\">\n")
            file.write("<file name=\"Passa_banda_Rauch.PNG\" path=\"/\" encoding=\"base64\">"+str(fotostr)+"\n"+"</file>\n")
            file.write("<text><![CDATA["+enunciat_xml+".<br><br><img src=\"@@PLUGINFILE@@/Passa_banda_Rauch.PNG\" alt="" width=\"284\" height=\"425\" role=\"presentation\" class=\"img-responsive atto_image_button_text-bottom\"><br>]]></text>\n")
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
    print("Si vol generar un altre exercici de filtres passa banda amb arquitectura de Rauch, premi 0. En cas contrari, premi 1\n")
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
                print("\nGràcies per haver utilitzat el generador d'exercicis de filtres passa banda amb arquitectura de Rauch!")
                with open("Passa_banda_Rauch.xml","a") as file:
                    file.write("</quiz>")
            else:
                print("\n")
    numrep+=1
            
        
