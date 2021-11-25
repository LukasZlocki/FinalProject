#from _typeshed import WriteableBuffer
import threading
import multiprocessing
from concurrent.futures import ThreadPoolExecutor

import timeit

from Raport import Raport
from RaportGenerator import RaportGenerator



# Todos :
# Dodac obliczenia na procesach, ktorych liczba zalezy od liczby dostepnych procesorow w systemie
# Pobrac dane z pliku
# done - Pobawic sie raport generatorem i wstepnie wygenerowac raport podmieniajac wartosci 
# done - Dodac obliczanie na cztery procesy


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
def calculation(value):
    end = value
    i = 1
    result = 0
    for n in range(1, end): 
        result = result + (n-i) * i
        i += 1


# Multiprocess Test
# values - list of data for calculation
# processes - number of processes to perform calculations 
def performMultiprocessTest(values, processes):
    with multiprocessing.Pool(processes=processes) as pool:
        pool.map(calculation, values)


# Multithreading Test
# values - list of data for calculation
# processes - number of threadings to perform calculations 
def performMultithreadingTest(values, threads):
    with ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(calculation, values)


def main():

    raport_1xMultiThreading = Raport()
    raport_4xMultiThreading = Raport()
    raport_4xMultiProcessing = Raport()
    raport_CpusMultiProcessing = Raport()
    
    # Setting test description
    raport_1xMultiThreading.setTestDescription("1 thread (s)")
    raport_4xMultiThreading.setTestDescription("4 threads (s)")
    raport_4xMultiProcessing.setTestDescription("4 processes (s)")
    raport_CpusMultiProcessing.setTestDescription("process based on number of CPUs (s)")

    # Setting system, interpreter and processor information
    raport_1xMultiThreading.setSystemInterpreterAndProcessorInfo()
    raport_4xMultiThreading.setSystemInterpreterAndProcessorInfo()
    raport_4xMultiProcessing.setSystemInterpreterAndProcessorInfo()
    raport_CpusMultiProcessing.setSystemInterpreterAndProcessorInfo()

    print("Performing test")
    for test in range(4):

        for recurrence in range(5):
            start = timeit.default_timer()
            end = 0
            message = ""

            if (test == 0 ): # 1x multithreading test
                performMultithreadingTest(Values, 1)
                message = "Test 1x multithreading"
                end = timeit.default_timer()
                result = end - start
                raport_1xMultiThreading.addProbe(result) # adding result to raport

            if (test == 1): # 4x multithreating test
                performMultithreadingTest(Values, 4)
                message = "Test 4x multithreading"
                end = timeit.default_timer()
                result = end - start
                raport_4xMultiThreading.addProbe(result) # adding result to raport  

            if (test == 2): # 4x multiprocessing test 
                performMultiprocessTest(Values, 4)
                message = "Test 4x multiprocessing" 
                end = timeit.default_timer()
                result = end - start
                raport_4xMultiProcessing.addProbe(result) # adding result to raport

            if (test == 3): # multiprocessing test accoring to CPUs available
                cpus = raport_CpusMultiProcessing.getCpusNumber()
                performMultiprocessTest(Values, cpus)
                message = f"Test multiprocess according to number of CPUs ({cpus}):" 
                end = timeit.default_timer()
                result = end - start
                raport_CpusMultiProcessing.addProbe(result) # adding result to raport
            print(f"{message} {round(result, 3)} seconds")

    # Adding finished raports to list of raports
    raportsList = []
    raportsList.append(raport_1xMultiThreading)
    raportsList.append(raport_4xMultiThreading)
    raportsList.append(raport_4xMultiProcessing)
    raportsList.append(raport_CpusMultiProcessing)

    # Generating raport and saving to HTML file
    raportGenerator = RaportGenerator(raportsList)
    raportGenerator.saveToHtml()
    


if __name__ == "__main__":
    main()



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


    """
    # 1x multithreading 
    print("Test 1x multithreading")
    start = timeit.default_timer()
    performMultithreadingTest(Values, 1)
    end = timeit.default_timer()
    result = end - start
    print(f"1x multithreading: {round(result, 3)} sekund")
    raport_1xMultiThreading.addProbe(result) # adding result to raport

    # 4x multithreating 
    print("Test 4x multithreating")
    start = timeit.default_timer()
    performMultithreadingTest(Values, 4)
    end = timeit.default_timer()
    result = end - start
    print(f"4x multithreating: {round(result, 3)} sekund")
    raport_4xMultiThreading.addProbe(result) # adding result to raport

    # 4x multiprocessing 
    print("Test 4x multiprocess")
    start = timeit.default_timer()
    performMultiprocessTest(Values, 4)
    end = timeit.default_timer()
    result = end - start
    print(f"4x multiprocess: {round(result, 3)} sekund")
    raport_4xMultiProcessing.addProbe(result) # adding result to raport

    # multiprocessing according to CPUs
    cpus = raport_CpusMultiProcessing.getCpusNumber()
    print("Test multiprocess according to number of CPUs: ")
    for _ in range(5):
        start = timeit.default_timer()
        performMultiprocessTest(Values, cpus)
        end = timeit.default_timer()
        result = end - start
        print(f"multiprocess by {cpus} CPUs: {round(result, 3)} sekund")
        raport_CpusMultiProcessing.addProbe(result) # adding result to raport
    """