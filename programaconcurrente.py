#A continuación, ambos subprocesos intentan cambiar el valor de la variable compartida.
#Y corren para ver qué subproceso escribe un valor a la variable en último lugar.
#El valor del subproceso que escribe en la última variable compartida se conserva porque sobrescribe 
#el valor que escribió el subproceso anterior.
#En este programa, ambos subprocesos intentan modificar el valor de la variable al mismo tiempo. El valor de la variable depende del subproceso que se complete en último lugar.countercounter
#Si el subproceso se completa antes que el subproceso, verá el siguiente resultado:t1t2

#Primero, importe la clase desde el módulo y la función desde el módulo:
from threading import Thread
from time import sleep

#En segundo lugar, defina una variable global llamada cuyo valor es cero
counter = 0

#En tercer lugar, defina una función que aumente el valor de la variable en un número:
def increase(by):
    global counter

    local_counter = counter
    local_counter += by

    sleep(0.1)

    counter = local_counter
    print(f'counter={counter}')


# Cuarto, cree dos hilos. El primer hilo aumenta el en 10 mientras que el segundo hilo aumenta el en 20, etc.
t1 = Thread(target=increase, args=(10,))
t2 = Thread(target=increase, args=(20,))
t3 = Thread(target=increase, args=(30,))
t4 = Thread(target=increase, args=(40,))

# Quinto, inicie los hilos:
t1.start()
t2.start()
t3.start()
t4.start()

#Sexto, desde el hilo principal, espere a que se completen los hilos t1,t2,t3,t4:
t1.join()
t2.join()
t3.join()
t4.join()

#Finalmente, muestra el valor final de la variable:
print(f'The final counter is {counter}')


#Se puede ejecutar varias veces y vemos como va cambiando de valor.