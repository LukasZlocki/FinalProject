import os
import platform
import statistics  # median calculation
import sys


class Report:
    def __init__(self):
        self.probes = []
        self.testDescription = ""
        self.pythonVersion = ""
        self.interpreterName = ""
        self.interpreterVersion = ""
        self.operatingSystem = ""
        self.operatingSysVersion = ""
        self.processor = ""
        self.cpus = ""

    # SETTERS
    def set_system_interpreter_and_processor_info(self):
        self.pythonVersion = platform.python_version()
        self.interpreterName = platform.python_implementation()
        self.interpreterVersion = sys.version
        self.operatingSystem = platform.system()
        self.operatingSysVersion = platform.release()
        self.processor = platform.processor()
        self.cpus = os.cpu_count()

    def set_test_description(self, test_description):
        self.testDescription = test_description

    # adding probe to 
    def add_probe(self, probe):
        probe = round(probe, 3)
        self.probes.append(probe)

    # GETTERS
    def get_list_of_all_probes(self):
        return self.probes

    def get_median_of_all_probes(self):
        medianValue = statistics.median(self.probes)
        return medianValue 

    def get_test_description(self):
        return self.testDescription

    # return number of CPUs of the tested system
    def get_cpus_quantity(self):
        return self.cpus

    def print_system_interpreter_and_processor_info(self):
        print(f"{self.pythonVersion}")
        print(f"{self.interpreterName}")
        print(f"{self.interpreterVersion}")
        print(f"{self.operatingSystem}")
        print(f"{self.operatingSysVersion}")
        print(f"{self.processor}")
        print(f"{self.cpus}")