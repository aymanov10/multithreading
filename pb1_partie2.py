import threading
from threading import Thread, Lock
import queue
import random
import time
import sys
import pandas as pd
import numpy as np

def test(u):
    m= 0
    a = random.sample(range(0, 20),u)
     
    while a !=  random.sample(range(0, 20), u) :
        m+=1
        
    return (m,a)



myQueue = queue.Queue()

class Calcul(threading.Thread):

    def __init__(self, liste):
    
        threading.Thread.__init__(self)
        #self.affichage  = affichage 
        self.liste = liste
        #self.queue = queue

    def run(self):
        #global a, name,Item,index
        global index
        while not myQueue.empty():
            item = myQueue.get()
            #print(item)
            if item is None:
                break
            try:
                name1 = (threading.current_thread().name)
                #print( "Thread: {0} start get item from queue[current size = {1}] at time = {2} \n".format(name1, myQueue.qsize(), time.strftime('%H:%M:%S')))
                start[item] = [myQueue.qsize(),time.strftime('%H:%M:%S')]
                name[item]= (threading.current_thread().name)
                a[item]=(eval(liste[item]))
                finish[item] = [myQueue.qsize(),time.strftime('%H:%M:%S')]
                Item.append(item)
            except   Exception as exc:
                name1 = (threading.current_thread().name)
                start[item] = [myQueue.qsize(),time.strftime('%H:%M:%S')]
                name[item]=(threading.current_thread().name)
                a[item]=     exc.__class__ 
                finish[item] = [myQueue.qsize(),time.strftime('%H:%M:%S')]
                Item.append(item)
            #print(threading.current_thread().name,'item:',item,eval(liste[item]))
            myQueue.task_done()
            index+=1
            #print(Item)
            if index == len(self.liste):
                 #print(len(Item))
                 #print(len(liste))
                 print(pd.DataFrame(data={'Nom de la tache ':name,'liste rang':Item,'instruction':liste,'evalation':a,'Nb_Rest_Thread_and_TimeStart':start,'Nb_Rest_Thread_and_TimeFinish':finish})) 
           
       
if __name__ == '__main__':
    #lock = Lock()
    liste = ["isinstance(1, str)",2,'1==1','3**4+3**5',"test(5)","test(3)","time.sleep(1)",'3**1',"time.sleep(2)", '3**2',"1/0",'3**3',"time.sleep(2)",'3**4+3**5','3**4','3**5','3**4+3**5','3**4+3**5','3**1']
    a = [[]]*len(liste) # global variable
    name =[[]]*len(liste)
    Item = []
    index = 0
    start = [[]]*len(liste)
    finish = [[]]*len(liste)
    #liste = [str(2**i) for i in range(10)]
    for i in range(len(liste)):
        myQueue.put(i)
    

    tasks = []
    for i in range(4):
        thread = Calcul(liste ) #target=Calcul, args=(myQueue,liste)
        thread.start()
        tasks.append(thread)
    for thread in tasks:
        thread.join()
    myQueue.join()