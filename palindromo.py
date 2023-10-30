frase = str(input('Digite um nome'))
frase = frase.upper().replace(" ","") 

invertido = frase.upper() [::-1] 
invertido = invertido.replace(" ", "")  

if frase == invertido:
    print("palíndromo")
else:
    print("não é palíndromo")