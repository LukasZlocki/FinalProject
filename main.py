#from _typeshed import WriteableBuffer
import threading
import timeit

import Raport



# Todos :
# Pobawic sie raport generatorem i wstepnie wygenerowac raport podmieniajac wartosci 
# Dodac cztery procesy
# Pobrac dane z pliku

# Glowne zadanie !!
# """
Values = [15972490, 80247910, 92031257, 75940266,
            97986012, 87599664, 75231321, 11138524,
            68870499, 11872796, 79132533, 40649382,
            63886074, 53146293, 36914087, 62770938]
# """

#Values = [15972490, 80247910, 92031257,  75940266]

#Values = [20, 40, 50, 20]


# Main calculation  
def calculation(values, start, end):
    for j in range(start, end):
        i = 1
        result = 0
        for n in range(1, values[j]): 
            result = result + (n-i) * i
            i += 1

# Run threads
# values - list with values for calculations
# thread - number of threads to perform calculations 
def performThreadingTest(values, thread):
    threadRun = []
    for i in thread:
        threadRun[i] = threading.Thread(target = calculation, args = (values,0,3),)


def main():

    ListaRaportow = []

    # !! SYMULACJA TESTOW I ZBIERANIA DANYCH DO RAPORTOW !!
    
    # 1x thread
    Raport2 = Raport.Raport()
    Raport2.setTestDescription("1 thread")
    Raport2.setSystemInterpreterAndProcessorInfo()

    Raport2.addProbe(35.5411)
    Raport2.addProbe(33.5422)
    Raport2.addProbe(37.5433)
    Raport2.addProbe(33.5444)
    Raport2.addProbe(35.5455)
    
    # 4x threads
    Raport1 = Raport.Raport()
    Raport1.setTestDescription("4 threads")
    Raport1.setSystemInterpreterAndProcessorInfo()

    Raport1.addProbe(25.5411)
    Raport1.addProbe(23.5422)
    Raport1.addProbe(27.5433)
    Raport1.addProbe(23.5444)
    Raport1.addProbe(25.5455)

    # 4x processes
    Raport3 = Raport.Raport()
    Raport3.setTestDescription("4 processes")
    Raport3.setSystemInterpreterAndProcessorInfo()

    Raport3.addProbe(15.5411)
    Raport3.addProbe(13.5422)
    Raport3.addProbe(17.5433)
    Raport3.addProbe(13.5444)
    Raport3.addProbe(15.5455)

    # Dodanie raportow
    ListaRaportow.append(Raport1)
    ListaRaportow.append(Raport2)
    ListaRaportow.append(Raport3)


    a = input("Stop ! Rapoty zebrane wcisnij enter by wydrukowac dane! ")

    # Wydruki raportow : 
    print("Dostepne raporty : ")
    for e in ListaRaportow:
        print(" ", e.getTestDescription())
        print(" ", e.getMedianOfAllProbes())

    a = input("Stop ! Nic nie wciskaj! ")

    #print(timeit.timeit(funkcja(Values), 1))



    # tutaj chilowo zablokowane
'''

    # jeden watek
    start = timeit.default_timer()
    t1 = threading.Thread(target = calculation, args = (Values, 0, 15),)
    t1.start()
    t1.join()
    end = timeit.default_timer()
    result = end - start
    print(f"Jeden watek {result} sekund")


    # cztery watki
    start = timeit.default_timer()
    t1 = threading.Thread(target = calculation, args = (Values,0,3),)
    t2 = threading.Thread(target = calculation, args = (Values,4,7),)
    t3 = threading.Thread(target = calculation, args = (Values,8,11),)
    t4 = threading.Thread(target = calculation, args = (Values,12,15),)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    end = timeit.default_timer()
    result = end - start
    print(f"4x watek {result} sekund") 

'''

if __name__ == "__main__":
    main()
