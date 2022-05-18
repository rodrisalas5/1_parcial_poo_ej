array = []
array3 = []
array5 = []
array7 = []

while(True):
    while (True):
        palabra = input("Ingrese una palabra: ")
        if palabra.isdigit():
            print("La palabra debe de ser solo alfabetica, reintentar.")
        else:
            break
    if (palabra[(len(palabra)-1)] == "." ):
        break
    else:
        array.append(palabra)

print(" ".join(array))

for i in range(len(array)):
  if ( len(array[i]) == 3):
    array3.append(array[i])
  elif ( len(array[i]) == 5):
    array5.append(array[i])
  elif ( len(array[i]) == 7):
    array7.append(array[i])

print(f"Hay {len(array3)} palabras con 3 letras {array3}")
print(f"Hay {len(array5)} palabras con 5 letras {array5}")
print(f"Hay {len(array7)} palabras con 7 letras {array7}")