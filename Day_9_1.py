# single only responsibility 
# advance level for single only with abstraction

class Report: 
    def __init__(self , data ):
        self.data = data 
    
    def generate(self):
        return f" Report : {self.data}"

from abc import ABC , abstractmethod 

# contarct or abstract method from 
class Report_Saver(ADC):
    @abstractmethod
    def add_to_file(self, report ,filename):
        pass


class FileReport(Report_Saver):
    def add_to_file(self, report ,filename):
        with open(filename, "w") as f:
            f.write(self.generate())
            
            
if __name__ == "__main__":
    report = Report("Report Data Here !")
    s_report = FileReport()
    s_report.add_to_file(report.generate() , "path/filename")
    
