#calculate avarage note (notes range: 1-6)
oceny=[]
while True:
    print("Podaj ocenę od 1 do 6 lub naciśnij enter aby zakończyć")
    ocena=input()
    if ocena=='':
        break
    elif str(ocena).isalpha():
#   elif not str(ocena).isnumeric():       
        print("Nieprawidłowa wartość")
    else:
        if float(ocena)<1.0 or float(ocena)>6.0:
            print("Nieprawidłowa ocena")
        else:       
            oceny.append(ocena)

if oceny==[]:
    print("Nie podałeś żadnej oceny")
else:     
    print('Podane oceny to: ' +str(oceny))
    suma=0
    for i in range(len(oceny)):
         suma=suma + float(oceny[i])  
    print('Suma podanych ocen to: ' + str(suma))
    srednia=suma/len(oceny)
    srednia=round(srednia,2)
    print('Srednia podanych ocen to: ' + str(srednia))    
  


