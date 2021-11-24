#from _typeshed import WriteableBuffer
import threading
import multiprocessing
from concurrent.futures import ThreadPoolExecutor

import timeit

from Raport import Raport
from RaportGenerator import RaportGenerator



# Todos :
# InProgress - Dodac obliczanie na cztery procesy
# Dodac obliczenia na procesach, ktorych liczba zalezy od liczby dostepnych procesow w systemie
# Pobrac dane z pliku
# done - Pobawic sie raport generatorem i wstepnie wygenerowac raport podmieniajac wartosci 


# Glowne zadanie !!
"""
Values = [15972490, 80247910, 92031257, 75940266,
            97986012, 87599664, 75231321, 11138524,
            68870499, 11872796, 79132533, 40649382,
            63886074, 53146293, 36914087, 62770938]
 """


Values = [10, 20, 30, 40,
            50, 60, 70, 80,
            90, 100, 110, 120,
            130, 140, 150, 160]


# Main calculation  
def calculation(values, start, end):
    for j in range(start, end):
        i = 1
        result = 0
        for n in range(1, values[j]): 
            result = result + (n-i) * i
            i += 1


# Main calculation  
def calculation_X(value):
    start = 1
    end = value
    i = 1
    result = 0
    for n in range(1, end): 
        result = result + (n-i) * i
        i += 1


# 1x threading test
def perform1xThreadingTest(values):   
    t1 = threading.Thread(target = calculation, args = (Values, 0, 15),)
    t1.start()
    t1.join()


# 4x threadings test
def perform4xThreadingsTest(values):
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


# 4x multiprocess test
def perform4xMultiprocessTest(values):
    p1 = multiprocessing.Process(target=calculation, args=(Values,0,3),)
    p2 = multiprocessing.Process(target=calculation, args=(Values,4,7),)
    p3 = multiprocessing.Process(target=calculation, args=(Values,8,11),)
    p4 = multiprocessing.Process(target=calculation, args=(Values,12,15),)

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()


def performMultiprocessTest(values, processes):
    with multiprocessing.Pool(processes=processes) as pool:
        pool.map(calculation_X, values)

def performMultithreadingTest(values, threads):
    with ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(calculation_X, values)



""""
# Run threads
# values - list with values for calculations
# thread - number of threads to perform calculations 
def performThreadingTest(values, thread):
    threadRun = []
    for i in thread:
        threadRun[i] = threading.Thread(target = calculation, args = (values,0,3),)
"""

def main():


    ListaRaportow = []

    # !! SYMULACJA TESTOW I ZBIERANIA DANYCH DO RAPORTOW !!
    """"
    # 1x thread
    Raport2 = Raport()
    Raport2.setTestDescription("1 thread")
    Raport2.setSystemInterpreterAndProcessorInfo()

    Raport2.addProbe(35.5411)
    Raport2.addProbe(33.5422)
    Raport2.addProbe(37.5433)
    Raport2.addProbe(33.5444)
    Raport2.addProbe(35.5455)
    
    # 4x threads
    Raport1 = Raport()
    Raport1.setTestDescription("4 threads")
    Raport1.setSystemInterpreterAndProcessorInfo()

    Raport1.addProbe(25.5411)
    Raport1.addProbe(23.5422)
    Raport1.addProbe(27.5433)
    Raport1.addProbe(23.5444)
    Raport1.addProbe(25.5455)

    # 4x processes
    Raport3 = Raport()
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

    a = input("Stop ! Przejscie do generowania raportu! ")

    # Generator raportu - testy
    Generator = RaportGenerator(ListaRaportow)
    htmlPart = Generator.showHtml()
    print(htmlPart)

    a = input("Stop ! Przejscie do save raportu do HTML! ")

    # SAVE raportow

    Generator.saveHtml()

    #print(timeit.timeit(funkcja(Values), 1))

"""

    # tutaj chilowo zablokowane

    """
    # jeden watek
    start = timeit.default_timer()
    t1 = threading.Thread(target = calculation, args = (Values, 0, 15),)
    t1.start()
    t1.join()
    end = timeit.default_timer()
    result = end - start
    print(f"1x watek {result} sekund")


    # cztery watki
    start = timeit.default_timer()
    t1 = threading.Thread(target = calculation, args = (Values, 0, 15),)
    t1.start()
    t1.join()
    end = timeit.default_timer()
    result = end - start
    print(f"4x watek {result} sekund")



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
"""

    # Testy 1x threating
    print("Test 1x threating")
    start = timeit.default_timer()
    perform1xThreadingTest(Values)
    end = timeit.default_timer()
    result = end - start
    print(f"1x threating {result} sekund")

    # Testy 4x threating
    print("Testy 4x threatings")
    start = timeit.default_timer()
    perform4xThreadingsTest(Values)
    end = timeit.default_timer()
    result = end - start
    print(f"4x threating {result} sekund")

    # Testy 4x multiprocessing
    print("Test 4x multiprocess")
    start = timeit.default_timer()
    perform4xMultiprocessTest(Values)
    end = timeit.default_timer()
    result = end - start
    print(f"4x multiprocess {result} sekund")
    
    print("")
    print ("**** Testy skroconej formy ****" )

    # Testy 1x multiprocessing by pool
    print("Test 1x multithreading POOL")
    start = timeit.default_timer()
    performMultithreadingTest(Values, 1)
    end = timeit.default_timer()
    result = end - start
    print(f"1x multithreading POOL {result} sekund")

    # Testy 4x multithreating by pool
    print("Test 4x multithreating by POOL")
    start = timeit.default_timer()
    performMultithreadingTest(Values, 4)
    end = timeit.default_timer()
    result = end - start
    print(f"4x multithreating POOL {result} sekund")

    # Testy 4x multiprocessing by pool
    print("Test 4x multiprocess POOL")
    start = timeit.default_timer()
    performMultiprocessTest(Values, 4)
    end = timeit.default_timer()
    result = end - start
    print(f"4x multiprocess POOL {result} sekund")


if __name__ == "__main__":
    main()
