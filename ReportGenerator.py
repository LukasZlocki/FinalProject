# Class for generating report to html

class ReportGenerator:
    def __init__(self, raportsList):
        self.report = raportsList
        self.author = "Lukasz Zlocki"

    def html_header(self):
        html_part1 = '''<!DOCTYPE html>
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
        <h1>Multithreading/Multiprocessing benchmark results</h1>
        <p>
        </p>'''
        return html_part1

    def html_environment(self):
        HtmlExecutionEnvironment = f'''<h2>Execution environment</h2>
            <p>
            Python version: {self.report[0].pythonVersion}<br/>
            Interpreter: {self.report[0].interpreterName}<br/>
            Interpreter version: {self.report[0].interpreterVersion}<br/>
            Operating system: {self.report[0].operatingSystem}<br/>
            Operating system version: {self.report[0].operatingSysVersion}<br/>
            Processor: {self.report[0].processor}<br/>
            CPUs: {self.report[0].cpus}
            </p>'''
        return HtmlExecutionEnvironment

    def html_test_results(self):
        html_test_results = f'''<h2>Test results</h2>
            <p>The following table shows detailed test results:</p>
            <table>
            <tr>
                <th>Execution:</th>
                <th>{self.report[0].get_test_description()}</th>
                <th>{self.report[1].get_test_description()}</th>
                <th>{self.report[2].get_test_description()}</th>
                <th>{self.report[3].get_test_description()}</th>
            </tr>

            <tr>
                <td>1</td>
                <td>{'{:.3f}'.format(self.report[0].probes[0])}</td>
                <td>{'{:.3f}'.format(self.report[1].probes[0])}</td>
                <td>{'{:.3f}'.format(self.report[2].probes[0])}</td>
                <td>{'{:.3f}'.format(self.report[3].probes[0])}</td>
            </tr>

            <tr>
                <td>2</td>
                <td>{'{:.3f}'.format(self.report[0].probes[1])}</td>
                <td>{'{:.3f}'.format(self.report[1].probes[1])}</td>
                <td>{'{:.3f}'.format(self.report[2].probes[1])}</td>
                <td>{'{:.3f}'.format(self.report[3].probes[1])}</td>
            </tr>

            <tr>
                <td>3</td>
                <td>{'{:.3f}'.format(self.report[0].probes[2])}</td>
                <td>{'{:.3f}'.format(self.report[1].probes[2])}</td>
                <td>{'{:.3f}'.format(self.report[2].probes[2])}</td>
                <td>{'{:.3f}'.format(self.report[3].probes[2])}</td>
            </tr>

            <tr>
                <td>4</td>
                <td>{'{:.3f}'.format(self.report[0].probes[3])}</td>
                <td>{'{:.3f}'.format(self.report[1].probes[3])}</td>
                <td>{'{:.3f}'.format(self.report[2].probes[3])}</td>
                <td>{'{:.3f}'.format(self.report[3].probes[3])}</td>
            </tr>

            <tr>
                <td>5</td>
                <td>{'{:.3f}'.format(self.report[0].probes[4])}</td>
                <td>{'{:.3f}'.format(self.report[1].probes[4])}</td>
                <td>{'{:.3f}'.format(self.report[2].probes[4])}</td>
                <td>{'{:.3f}'.format(self.report[3].probes[4])}</td>
            </tr>

            </table>'''
        return html_test_results

    def html_summary(self):
        html_summary = f'''<h2>Summary</h2>
            <p>The following table shows the median of all results:</p>
            <table>
            <tr>
                <th>Execution:</th>
                <th>{self.report[0].get_test_description()}</th>
                <th>{self.report[1].get_test_description()}</th>
                <th>{self.report[2].get_test_description()}</th>
                <th>{self.report[3].get_test_description()}</th>
            </tr>

            <tr>
                <td>Median:</td>
                <td>{'{:.3f}'.format(self.report[0].get_median_of_all_probes())}</td>
                <td>{'{:.3f}'.format(self.report[1].get_median_of_all_probes())}</td>
                <td>{'{:.3f}'.format(self.report[2].get_median_of_all_probes())}</td>
                <td>{'{:.3f}'.format(self.report[3].get_median_of_all_probes())}</td>
            </tr>

            </table>'''
        return html_summary

    def html_footer(self):
        html_footer = f'''<p>App author: {self.author}</p>

            </body>
            </html>'''
        return html_footer

    def show_html(self):
        return self.html_environment()

    def assembly_all_html(self):
        html = "" + self.html_header() + "" \
            + self.html_environment() + "" \
            + self.html_test_results() + "" \
            + self.html_summary() + "" \
            + self.html_footer()
        return html

    def save_to_html(self):
        html = self.assembly_all_html()
        user_name = input("Give a name of generated report: ")
        file_name = user_name + ".html"
        with open(file_name, 'w') as file:
            file.write(html)
