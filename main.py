#from _typeshed import WriteableBuffer
import threading
import multiprocessing
from concurrent.futures import ThreadPoolExecutor

import timeit

from Raport import Raport
from RaportGenerator import RaportGenerator


# Todos :


# returns list of values
def readingValuesFromFile(fileName):
    values = 0
    with open(fileName, "r") as file:
        data = file.readlines()
        # removing '\n' from list of strings
        String = [x.strip()for x in data ]
        # Creating string with values
        valuesString = ""
        for element in String:
            valuesString += element
        valuesString = valuesString.replace(" ", "")
        valueStringSplitted = valuesString.split(",")
        # Converting stringValues to int list
        values = [int(x) for x in valueStringSplitted]
    return values


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


# Main function
def main():

    Values = readingValuesFromFile("task2.txt") 
    print(Values)
    
    c = input("spacja kontynuacja")
    
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

