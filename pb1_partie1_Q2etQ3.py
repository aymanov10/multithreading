###### Probleme ######

###### Partie 2 : version multi-thread #######
import threading



import queue
import random
import time




class Calcul(threading.Thread):
	
    def __init__(self, liste,queue):
    
        threading.Thread.__init__(self)

        self.liste = liste
        self.queue = queue
        
        
                       
    def run(self):
        while not self.queue.empty():
            item = self.queue.get()
			#print('item:',item)
            if item is None:
                break
            #print(item)
            try:
                s = eval(liste[item])
                print(threading.current_thread().name,  ' item:', item ,    s)
                self.queue.task_done()
            except Exception as exc:
                print(threading.current_thread().name,  ' item:', item ,    exc.__class__ )
        
if __name__ == '__main__':    
	#help(threading.current_thread().getName

	n = int(input("Entrez un nombre de processeur :"))
	nom_fichier = str(input('Entrez le nom du fichier svp ! '))
	myQueue = queue.Queue()
	liste = []
	with open(f"C:/Users/ua/Desktop/{nom_fichier}","r") as f :
		for line in f :
			liste.append(line)
				
	#liste = ['3**1 + 3**2+3**3+3**4+3**5','3**4+3**5','3**1', '3**2','3**3','3**4+3**5','3**4','3**5','3**1 +3**2+3**3+3**4+3**5','3**4+3**5','3**1']
	for i in range(len(liste)) :
		myQueue.put(i)
	print("Queue Populated")
	tasks = []
	for i in range(n):
		thread = Calcul( liste,myQueue)
		thread.start()
		tasks.append(thread)
	for thread in tasks:
		thread.join()
