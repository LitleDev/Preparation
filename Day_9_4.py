# Interface Segregation Priciple
# clinet should not be forced to depend on methods that they dont use

# example 

class Machine:
    def print(self):
        pass
    
    def scan(self):
        pass

    def fax(self):
        pass
    
class Old_printer(Machine):
    def print(self):
        print("Printing ")
    
    def scan(self):
        raise NotImplementedError
    
    def fax(self):
        raise NotImplementedError
        
# correct implementation

class Printer:
    def print(self):
        pass
    
class Scanner:
    def scan(self):
        pass
    
class Faxing:
    def fax(self):
        pass
    
class HP_printer(Printer , Scanner):
    def print(self):
        # some print methods
        return 
    
    def scan(self):
        # some sacing document 
        return
    

class Cisco_printer(Printer , Faxing):
    def print(self):
        # some print methods
        return
    def fax(self):
        # some print methods
        return


hp = HP_printer()

hp.print()
hp.scan()


cisco = Cisco_printer()
cisco.print()
cisco.fax()
    
