# Raport data 

import os, platform, sys
import statistics # median calculation

class Raport:
    def __init__(self):
        self.probesMediana = []
        self.testDescription = ""
        self.pythonVersion =""
        self.interpreterName = ""
        self.interpreterVersion = ""
        self.operatingSystem = ""
        self.operatingSysVersion = ""
        self.processor = ""
        self.cpus = ""


    # SETTERS
    def setSystemInterpreterAndProcessorInfo(self):
        self.pythonVersion = platform.python_version()
        self.interpreterName = platform.python_implementation()
        self.interpreterVersion = sys.version
        self.operatingSys = platform.system()    
        self.operatingSysVersion = platform.release()
        self.processor = platform.processor()
        self.cpus = os.cpu_count()
    

    def setTestDescription(self, testDescr):
        self.testDescription = testDescr

    # adding probe to 
    def addProbeMediana(self, probe):
        self.probesMediana.append(probe)


    # GETTERS
    def getListOfAllProbes(self):
        return self.probes

    def getMedianOfAllProbes(self):
        #medianValue = statistics.median(self.probes)
        return self.probesMediana[0]

    def getTestDescription(self):
        return self.testDescription

    def printSystemInterpreterAndProcessorInfo(self):
        print(f"{self.pythonVersion}")
        print(f"{self.interpreterName}")
        print(f"{self.interpreterVersion}")
        print(f"{self.operatingSys}")
        print(f"{self.operatingSysVersion}")
        print(f"{self.processor}")
        print(f"{self.cpus}")