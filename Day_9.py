# single only responsibility 
# violates the Single only responsibility priciple
class Node:
    def __init__(self,data):
        self.data = data
        
    def generate():
        return f"Report: {self.data}"
        
    def save_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(self.generate())
            
# Corrected method and class  

class Report: 
    def __init__(self , data ):
        self.data = data 
    
    def generate(self):
        return f" Report : {self.data}"
    
class Save_Report:
    def add_to_file(self, report ,filename):
        with open(filename, "w") as f:
            f.write(self.generate())
            
            
if __name__ == "__main__":
    report = Report("Report Data Here !")
    s_report = Save_Report()
    s_report.add_to_file(report.generate() , "path/filename")
    
