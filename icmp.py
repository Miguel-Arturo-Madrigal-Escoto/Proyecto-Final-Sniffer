from abc import ABC, abstractmethod

class ICMP(ABC):
    def __init__(self, file):
        self._type = 0
        self._code = 0
        self._checksum = 0x0
        self._file = open("Paquetes Redes/" + file, "rb")
    
    @abstractmethod
    def _getType(self):
        pass

    @abstractmethod
    def _getCode(self):
        pass

    def _getChecksum(self):
        bytes_str = self._file.read(2)
        aux = ''
        
        for byte in bytes_str:
            aux += f'{byte:02x}'.upper()
        
        self._checksum = aux

        return self._checksum
        
    def __str__(self):
        return (
            "\nTipo: " + str(self._getType()) + 
            "\n\nCodigo " + str(self._getCode()) + 
            "\n\nChecksum: " + str(self._getChecksum()) 
        )