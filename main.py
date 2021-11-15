#from _typeshed import WriteableBuffer
import threading
import timeit

import Raport



# Todos :
# DONE -> Stworzyc obiekt do raportowania
# DONE -> W obiekcie do raportowania wyliczac mediane dla poszczegolnych wynikow
# DOBE -> powtoryzc wielokrotnie probe
# stworzyc generator do formatu Html
# Dodac wiele procesow, ktore realizuja zadanie
# InProgress -> zorganizowac glowny kod wykonujacy threadingsy w jakas zgrabna petle, funkcje czy tez obiekt

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

    c = Raport()
    c.setTestDescription("4 watki testowe")
    c.setSystemInterpreterAndProcessorInfo()

    c.addProbe(25.541)
    c.addProbe(23.542)
    c.addProbe(27.543)
    c.addProbe(23.544)
    c.addProbe(25.545)
    c.addProbe(22.546)

    testy = c.getListOfAllProbes()
    mediana = c.getMedianOfAllProbes()

    print(f"Baza testow: {testy}")
    print(f"Mediana testow: {mediana}")
    c.printSystemInterpreterAndProcessorInfo()

    a = input("Stop ! Nic nie wciskaj ! ")



    #print(timeit.timeit(funkcja(Values), 1))



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

if __name__ == "__main__":
    main()
