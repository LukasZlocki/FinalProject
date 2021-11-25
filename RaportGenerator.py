# Class for generating raport to html 

from Raport import Raport

# TODO:
# done setRaport : send Raport class to RaportGenerator
# done generateRaport : base on Raport class generate Html  ex. "{raport.probe1}""
# saveRaport : write method to save html to file with asking about file name
# 




class RaportGenerator:
    def __init__(self, raportsList):
        self.raport = raportsList
        self.author = "Lukasz Zlocki"


    def Html_Header(self):
        htmlPart1 = '''<!DOCTYPE html>
        <html>
        <head>
        <title>Multithreading/Multiprocessing benchmark results</title>
        <style>
        body {
        font-size: 10pt;
        }

        h2 {
        padding-top: 10pt;
        }

        table {
        font-family: arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
        table-layout: fixed ;
        }

        td, th {
        border: 2px solid #b9b9b9;
        padding: 10px;
        text-align: center;
        width: 25% ;
        }

        th {
        background-color: #d5d5d5;
        }

        td {
        }

        tr:nth-child(odd) {
        background-color: #eeeeee;
        }
        </style>
        </head>
        <body>
        '''      
        return htmlPart1


    def Html_Environment(self):
        HtmlExecutionEnvironment = f'''<h2>Execution environment</h2>
            <p>
            Python version: {self.raport[0].pythonVersion}<br/>
            Interpreter: {self.raport[0].interpreterName}<br/>
            Interpreter version: {self.raport[0].interpreterVersion}<br/>
            Operating system: {self.raport[0].operatingSys}<br/>
            Operating system version: {self.raport[0].operatingSysVersion}<br/>
            Processor: {self.raport[0].processor}<br/>
            CPUs: {self.raport[0].cpus}
            </p>'''       
        return HtmlExecutionEnvironment


    def Html_TestResults(self):
        HtmlTestResults = f'''<h2>Test results</h2>
            <p>The following table shows detailed test results:</p>
            <table>
            <tr>
                <th>Execution:</th>
                <th>{self.raport[0].testDescription} (s)</th>
                <th>{self.raport[1].testDescription} (s)</th>
                <th>{self.raport[2].testDescription} (s)</th>
                <th>processes based on number of CPUs (s)</th>
            </tr>

            <tr>
                <td>1</td>
                <td>{self.raport[0].probes[0]}</td>
                <td>{self.raport[1].probes[0]}</td>
                <td>{self.raport[2].probes[0]}</td>
                <td>4.038</td>
            </tr>

            <tr>
                <td>2</td>
                <td>{self.raport[0].probes[1]}</td>
                <td>{self.raport[1].probes[1]}</td>
                <td>{self.raport[2].probes[1]}</td>
                <td>3.760</td>
            </tr>

            <tr>
                <td>3</td>
                <td>{self.raport[0].probes[2]}</td>
                <td>{self.raport[1].probes[2]}</td>
                <td>{self.raport[2].probes[2]}</td>
                <td>3.902</td>
            </tr>

            <tr>
                <td>4</td>
                <td>{self.raport[0].probes[3]}</td>
                <td>{self.raport[1].probes[3]}</td>
                <td>{self.raport[2].probes[3]}</td>
                <td>3.786</td>
            </tr>

            <tr>
                <td>5</td>
                <td>{self.raport[0].probes[4]}</td>
                <td>{self.raport[1].probes[4]}</td>
                <td>{self.raport[2].probes[4]}</td>
                <td>4.266</td>
            </tr>

            </table>'''           
        return HtmlTestResults


    def Html_Summary(self):
        HtmlSummary = f'''<h2>Summary</h2>
            <p>The following table shows the median of all results:</p>
            <table>
            <tr>
                <th>Execution:</th>
                <th>1&nbsp;thread (s)</th>
                <th>4&nbsp;threads (s)</th>
                <th>4&nbsp;processes (s)</th>
                <th>processes based on number of CPUs (s)</th>
            </tr>

            <tr>
                <td>Median:</td>
                <td>{self.raport[0].getMedianOfAllProbes()}</td>
                <td>{self.raport[1].getMedianOfAllProbes()}</td>
                <td>{self.raport[2].getMedianOfAllProbes()}</td>
                <td>3.902</td>
            </tr>

            </table>'''   
        return HtmlSummary


    def Html_Footer(self):
        HtmlFooter = f'''<p>App author: {self.author}</p>

            </body>
            </html>'''           
        return HtmlFooter


    """
    def setRaport(self, raport):
        self.raport = raport
    """


    def showHtml(self):
        return self.Html_Environment()

    def assemblyAllHtmls(self):
        html = "" + self.Html_Header() + "" + self.Html_Environment() + "" + self.Html_TestResults() + "" + self.Html_Summary() + "" + self.Html_Footer()
        return html

    def saveToHtml(self):
        html = self.assemblyAllHtmls()
        userName = input("Give a name of generated raport: ")
        fileName = userName + ".html"
        with open(fileName, 'w') as file:
            file.write(html)


