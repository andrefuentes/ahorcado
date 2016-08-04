import random
from error import mu
lista=["amar","apoyar","aprender","ayudar","bailar","beber","caer","cambiar","cantar","cerrar","cocinar","comenzar","comer","comparar","comprar","conducir","contar","continuar","correr","cortar","costar","creer","dar","decidir","decir","descansar","describir","destruir","doler","dormir","elegir","empezar","empujar","encontrar","encontrarse","enseñar","entender","esconder","escribir","escuchar","esperar","estudiar","explicar","ganar","gritar","hablar","hacer","intentar","ir","jugar","lanzar","lavar","leer","limpiar","llamar","llegar","llenar","llorar","luchar","mandar","mejorar","mentir","mirar","morir","mostrar","mover","necesitar","ocurrir","odiar","ofrecer","olvidar","oir","pagar","pensar","perder","perdonar","permitir","poder","poner","preferir","preguntar","preparar","prometer","pulsar","quedarse","quemar","querer","recibir","reconocer","recordar","repetir","responder","reir","saber","sacar","salir","saltar","sentar","sentir","ser","sonreir","tener","terminar","tirar","tocar","trabajar"]
v=0
print("bienvenido")
print("_________________")
print("|")
print("|")
print("|")
print("|")
print("|")		
gano=False
opc="si"

palabra=random.choice(lista)
numero=len(palabra)
guiones="_ "*numero
letras= list(palabra)
guiones2=guiones.strip(" ")
guiones3=guiones2.split(" ")
while gano!="si" and gano!="no":	
	 
	print(guiones3)
	s=input("letra?:")
	for i in range(numero):
		if palabra[i]==s:
			guiones3[i]=s		
	
	if s in palabra:
		gano=True
	else:
		gano=False	
	
	if gano == False:
		v=v+1
		print (mu(v))
		if v == 7:
			gano = "no"
	if " _"	not in guiones:
		gano ="si"	
