###### Probleme ######

###### Partie 1 : version mono-tache #######


def evaluer1():
    liste =  ['(65535/2 ) *(-1+1) - 32768','a+ b','(65535/2 ) *(1+1) - 32768','int(-32767.5)','int(557.5)','65535 /2']
    for i in liste:
        s = eval(i)
        yield (f"{i } = {s}" )
        

def evaluer():
	with open(f"C:/Users/ua/Desktop/{nom_fichier}" ,'r') as f:
		for line in f:
			if (line[0] == '\n'): 
				pass
			else: 
				try:		
					s = eval(str(line))
					yield (f"{line }        =       {s}" )
				except Exception as exc :
					
					yield (f"{line }        =       {exc.__class__}" )
			"""else :
				code = compile(line, '<string>', 'exec')
				s = eval(code) 
				
				yield (f"{line :-<10} = {s}" )
			"""




if __name__ == '__main__':
	#e1 = evaluer1()
	#print(next(e))
	while True:
		try:
			nom_fichier = str(input('Entrez le nom du fichier svp ! '))
			e = evaluer()
			print(next(e))
			print(next(e))
			print(next(e))
			print(next(e))
			break
		except  FileNotFoundError :
			print("Oups!! Fichier introuvable , Veuillez entrer le bon fichier")
	
	
