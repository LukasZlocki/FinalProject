# Class for generating raport to html 

class RaportGenerator:
    def __init__(self):
        self.raports = []
        self.HtmlPart1 = ""
        self.HtmlExecutionEnvironment = ""
        self.HtmlTestResults = ""
        self.HtmlSummary = ""
        self.HtmlFooter = ""

    # static data for html 
    author = "Lukasz Zlocki"

    htmlPart1 = f'''
        <!DOCTYPE html>
        <html>
        <head>
        <title>Multithreading/Multiprocessing benchmark results</title>
        <style>
        '''
    HtmlExecutionEnvironment = f'''
        <h2>Execution environment</h2>
        <p>
        Python version: 3.8.5<br/>
        Interpreter: CPython<br/>
        Interpreter version: 3.8.5 (default, Jul 28 2020, 12:59:40) 
        [GCC 9.3.0]<br/>
        Operating system: Linux<br/>
        Operating system version: 5.4.0-48-generic<br/>
        Processor: x86_64<br/>
        CPUs: 8
        </p>   
        '''

    HtmlTestResults = f'''
        <h2>Test results</h2>
        <p>The following table shows detailed test results:</p>
        <table>
        <tr>
            <th>Execution:</th>
            <th>1&nbsp;thread (s)</th>
            <th>4&nbsp;threads (s)</th>
            <th>4&nbsp;processes (s)</th>
            <th>processes based on number of CPUs (s)</th>
        </tr>

        <tr>
            <td>1</td>
            <td>13.774</td>
            <td>13.678</td>
            <td>3.942</td>
            <td>4.038</td>
        </tr>

        <tr>
            <td>2</td>
            <td>13.366</td>
            <td>13.735</td>
            <td>4.048</td>
            <td>3.760</td>
        </tr>

        <tr>
            <td>3</td>
            <td>13.579</td>
            <td>13.636</td>
            <td>4.006</td>
            <td>3.902</td>
        </tr>

        <tr>
            <td>4</td>
            <td>13.491</td>
            <td>13.654</td>
            <td>4.144</td>
            <td>3.786</td>
        </tr>

        <tr>
            <td>5</td>
            <td>13.573</td>
            <td>13.753</td>
            <td>4.162</td>
            <td>4.266</td>
        </tr>

        </table>  
        '''

    HtmlSummary = f'''
        <h2>Summary</h2>
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
            <td>13.573</td>
            <td>13.678</td>
            <td>4.048</td>
            <td>3.902</td>
        </tr>

        </table>
        '''

    HtmlFooter = f'''
        <p>App author: {author}</p>

        </body>
        </html>
        '''

    def addRaport(self, raport):
        self.raports.append(raport)
    
    def showHtml(self):
        return self.htmlPart1

