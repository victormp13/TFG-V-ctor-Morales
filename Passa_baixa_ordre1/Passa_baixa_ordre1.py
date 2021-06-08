import random as r
from PIL import Image
import base64

#Mostrem a l'usuari el circuit amb el que es realitza l'exercici
img = Image.open('Passa_baixa_ordre1.PNG')
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
    print("Benvingut o benvinguda al generador d'exercicis de filtres passa baixa d'ordre 1.\n\nSi vol un problema de determinar el tipus de filtre, premi 0.\n\nSi vol un problema de determinar la funció de transferència del filtre , premi 1\n\nSi vol un problema de determinar el tipus de filtre i la seva expressió, premi 2\n\nSi vol un problema de trobar la freqüència angular natural, premi 3.\n")
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
        tipusex="Tipus de filtre i expressió"
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
    with open("Passa_baixa_ordre1.PNG", "rb") as imageFile:
        foto = base64.b64encode(imageFile.read())
        fotostr=foto.decode("utf-8")

    #Creació del fitxer XML
    if numrep==0:
        with open("Passa_baixa_ordre1.xml","a") as file:
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
            file.write("<text>$course$/top/PythonQuiz/Analogic/Filtres/Passa baixa ordre 1</text>\n")
            file.write("</category>\n")
            file.write("</question>\n")

    for i in range (permutacions):
        #Generació dels valors de les admitàncies
        R1=r.randint(1,4)
        R2=r.randint(5,10)
        C=r.randint(1,6)

        #Generació de les funcions de transferència correctes i errònies
        funciobona='H(s)='+str(round(-R2/R1,3))+'/'+'(1+'+str(int(R2*C))+'sRC)'
        funciodolenta1='H(s)='+str(round(-R2/R1,3))+'/'+'(1+'+str(int(R1*C))+'sRC)'
        funciodolenta2='H(s)='+str(round(-R2/R1,3))+'s/'+'(1+'+str(round(1/(R1*C),3))+'sRC)'
        funciodolenta3='H(s)='+str(round(R2/R1,3))+'/'+'(1+'+str(int(R1*C))+'sRC)'
        funciodolenta4='H(s)='+str(round(R1/R2,3))+'s/'+'(1+'+str(round(1/(R1*C),3))+'sRC)'

        #Generació dels tipus de filtres
        tipusfiltrebo="Passa baixa d'ordre 1"
        tipusfiltredolent1="Passa alta d'ordre 1"
        tipusfiltredolent2="Passa baixa d'ordre 2"
        tipusfiltredolent3="Passa banda d'ordre 2"
        tipusfiltredolent4="Passa alta d'ordre 2"

        #Càlcul de la freqüència angular natural i generació de les freqüències errònies
        frequenciabona=str(round(1/(R2*C),3))+'/RC'
        frequenciadolenta1=str(round(R1/(R2*C),3))+'/RC'
        frequenciadolenta2=str(round(1/(R1*C),3))+'/RC'
        frequenciadolenta3=str(round(R2/(R1*C),3))+'/RC'
        frequenciadolenta4=str(round(-1/(R2*C),3))+'/RC'
        
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
            respostabona=tipusfiltrebo+', '+funciobona
            respostadolenta1=tipusfiltrebo+', '+funciodolenta1
            respostadolenta2=tipusfiltrebo+', '+funciodolenta2
            respostadolenta3=tipusfiltredolent1+', '+funciobona
            respostadolenta4=tipusfiltredolent1+', '+funciodolenta1

        else:
            respostabona=frequenciabona
            respostadolenta1=frequenciadolenta1
            respostadolenta2=frequenciadolenta2
            respostadolenta3=frequenciadolenta3
            respostadolenta4=frequenciadolenta4
            
        #Es crea l'enunciat del fitxer XML
        enunciat_xml="El circuit de la figura és un filtre basat en un amplificador operacional ideal. Els valors de les resistències R1 i R2 són de "+str(R1)+'R i '+str(R2)+'R respectivament i el valor del condensador és de '+str(C)+'C.'
        if tipus==0:
            enunciat_xml+=" De quin tipus de filtre es tracta?"
        elif tipus==1:
            enunciat_xml+=" Troba la seva funció de transferència"
        elif tipus==2:
            enunciat_xml+=" Indica el tipus de filtre i troba la seva funció de transferència"
        else:
            enunciat_xml+=" Calcula la freqüència angular natural del filtre"

        #Es mostren per pantalla els valors aleatoris generats i les respostes
        enunciat_py="Els valors de les resistències R1 i R2 són de "+str(R1)+'R i '+str(R2)+'R respectivament. El valor del condensador és de '+str(C)+'C.\n'
        if tipus==3:
            enunciat_py+="La freqüència angular natural del filtre és "+respostabona
        elif tipus==2:
            enunciat_py+="El tipus de filtre i la funció de transferència són "+respostabona
        elif tipus==1:
            enunciat_py+="La funció de transferència del filtre és "+respostabona
        else:
            enunciat_py+="El tipus de filtre és "+respostabona
        print("\n"+enunciat_py+"\n")

        #Es creen les preguntes dins dels fitxers XML
        with open("Passa_baixa_ordre1.xml","a") as file:
            file.write("<question type=\"multichoice\">\n")
            file.write("<name>\n")
            file.write("<text>"+tipusex+" Permutació "+str(i)+"</text>\n") #i indica la permutació#
            file.write("</name>\n")
            file.write("<questiontext format=\"html\">\n")
            file.write("<file name=\"Passa_baixa_ordre1.PNG\" path=\"/\" encoding=\"base64\">"+str(fotostr)+"\n"+"</file>\n")
            file.write("<text><![CDATA["+enunciat_xml+".<br><br><img src=\"@@PLUGINFILE@@/Passa_baixa_ordre1.PNG\" alt="" width=\"284\" height=\"425\" role=\"presentation\" class=\"img-responsive atto_image_button_text-bottom\"><br>]]></text>\n")
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
    print("Si vol generar un altre exercici de filtres passa baixa d'ordre 1, premi 0. En cas contrari, premi 1\n")
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
                print("\nGràcies per haver utilitzat el generador d'exercicis de filtres passa baixa d'ordre 1!")
                with open("Passa_baixa_ordre1.xml","a") as file:
                    file.write("</quiz>")
            else:
                print("\n")
    numrep+=1
