import multiprocessing
from concurrent.futures import ThreadPoolExecutor
import timeit 
from Report import Report
from ReportGenerator import ReportGenerator


# ToDo:
# kod programu jest zgodny z dokumentem PEP8 (programpycodestyle nie wypisuje komunikatów o błędach),
# Wygenerowac raport na interpreterach : CPython,
# Wygenerowac raport na interpreterach : PyPy,
# Wygenerowac raport na interpreterach : Stackless Python,
# Ogolny clean up kodu w poszczegolnych klasach - uwaga niektore obiekty maja nieuzywane metody


# returns list of values 
def reading_values_from_file(file_name):
    values = 0
    with open(file_name, "r") as file:
        data = file.readlines()
        # removing '\n' from list of strings
        string = [x.strip() for x in data]
        # Creating string with values
        values_string = ""
        for element in string:
            values_string += element
        values_string = values_string.replace(" ", "")
        value_string_splitted = values_string.split(",")
        # Converting stringValues to int list
        values = [int(x) for x in value_string_splitted]
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
def perform_multiprocess_test(values, processes):
    with multiprocessing.Pool(processes=processes) as pool:
        pool.map(calculation, values)


# Multithreading Test
# values - list of data for calculation
# processes - number of threadings to perform calculations 
def perform_multithreading_test(values, threads):
    with ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(calculation, values)


# Main function
def main():

    values = reading_values_from_file("task3.txt")
    print("Test probe values : ")
    print(values)

    # Creating raporting objects  
    raport_1x_multi_threading = Report()
    raport_4x_multi_threading = Report()
    raport_4x_multi_processing = Report()
    raport_cpus_multi_processing = Report()
    
    # Setting test description
    raport_1x_multi_threading.set_test_description("1 thread (s)")
    raport_4x_multi_threading.set_test_description("4 threads (s)")
    raport_4x_multi_processing.set_test_description("4 processes (s)")
    raport_cpus_multi_processing.set_test_description("process based on number of CPUs (s)")

    # Setting system, interpreter and processor information
    raport_1x_multi_threading.set_system_interpreter_and_processor_info()
    raport_4x_multi_threading.set_system_interpreter_and_processor_info()
    raport_4x_multi_processing.set_system_interpreter_and_processor_info()
    raport_cpus_multi_processing.set_system_interpreter_and_processor_info()

    print("Performing test...")
    for test in range(4):
        for recurrence in range(5):
            start = timeit.default_timer()
            message = ""

            if test == 0:  # 1x multithreading test
                perform_multithreading_test(values, 1)
                message = "Test 1x multithreading"
                end = timeit.default_timer()
                result = end - start
                raport_1x_multi_threading.add_probe(result) # adding result to report

            if test == 1:  # 4x multithreating test
                perform_multithreading_test(values, 4)
                message = "Test 4x multithreading"
                end = timeit.default_timer()
                result = end - start
                raport_4x_multi_threading.add_probe(result) # adding result to report

            if test == 2:  # 4x multiprocessing test
                perform_multiprocess_test(values, 4)
                message = "Test 4x multiprocessing" 
                end = timeit.default_timer()
                result = end - start
                raport_4x_multi_processing.add_probe(result) # adding result to report

            if test == 3:  # multiprocessing test according to CPUs available
                cpus = raport_cpus_multi_processing.get_cpus_quantity()
                perform_multiprocess_test(values, cpus)
                message = f"Test multiprocess according to number of CPUs ({cpus}):" 
                end = timeit.default_timer()
                result = end - start
                raport_cpus_multi_processing.add_probe(result) # adding result to report
            print(f"{message} {round(result, 3)} seconds")
    print("test DONE.")
    # Adding finished reports to list of reports
    raports_list = []
    raports_list.append(raport_1x_multi_threading)
    raports_list.append(raport_4x_multi_threading)
    raports_list.append(raport_4x_multi_processing)
    raports_list.append(raport_cpus_multi_processing)

    # Generating report and saving to HTML file
    raport_generator = ReportGenerator(raports_list)
    raport_generator.save_to_html()
    

if __name__ == "__main__":
    main()

