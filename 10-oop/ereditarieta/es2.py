from abc import ABC, abstractmethod

class ContoBancario(ABC):
    @abstractmethod
    def deposita(self, importo) : pass
    
    @abstractmethod
    def preleva(self, importo) : pass
    
    @abstractmethod
    def saldo(self) : pass
    

class ContoCorrente(ContoBancario):
    def __init__(self, saldo):
        self.saldo = saldo
    
    def deposita(self, importo):
        self.saldo += importo
    
    def preleva(self, importo):
        self.saldo -= importo
    
    def saldo(self):
        return self.saldo
    
class ContoDiRisparmio(ContoBancario):
    def __init__(self, saldo, limite):
        self.saldo = saldo
        self.limite = limite
    
    def deposita(self, importo):
        self.saldo += importo
    
    def preleva(self, importo):
        if not self.limite:
            self.saldo -= importo
    
    def saldo(self):
        return self.saldo