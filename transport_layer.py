from abc import ABC, abstractmethod

class TransportLayer(ABC):
    def __init__(self, file, byte):
        self._source_port = ''
        self._destination_port = '' #puerto destino (str)
        self._destination_service = 0 #puerto destino (int)
        self._source_service = 0
        self._length = 0
        self._reserved = 0
        self._flag_ns = 0
        self._flag_cwr = 0
        self._flag_ece = 0
        self._flag_urg = 0
        self._flag_ack = 0
        self._flag_psh = 0
        self._flag_rst = 0
        self._flag_syn = 0
        self._flag_fin = 0
        self._checksum = 0x0
        self._data = ''
        self._file = open("Paquetes Redes/" + file, "rb")
        self._file.seek(byte)
    
    @abstractmethod
    def _getSourcePort(self):
        pass

    @abstractmethod
    def _getDestinationPort(self):
        pass
    
    @abstractmethod
    def _getLength(self):
        pass

    @property
    def destination_service(self):
        return self._destination_service

    @property
    def source_service(self):
        return self._source_service

    def _getChecksum(self):
        bytes_str = self._file.read(2)
        aux = ''
        
        for byte in bytes_str:
            aux += f'{byte:02x}'.upper()
        
        self._checksum = aux

        return self._checksum
    
    def _getData(self):
        read = self._file.read()
        for line in read:
            self._data += '{:02x}'.format(line).upper() + ' '

        return self._data

    def __str__(self):
        return (
            "\n\nPuerto origen: " + self._getSourcePort() + 
            "\n\nPuerto destino: " + self._getDestinationPort()
        )