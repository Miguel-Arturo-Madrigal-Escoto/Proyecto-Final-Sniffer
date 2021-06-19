class IP:
    def __init__(self, file):
        self._version = 0
        self._priority = ""
        self._service = ""
        self._length = 0
        self._hop_count = 0
        self._next = ""
        self._source = ""
        self._destination = ""
        self._data = ""
        self._file = open("Paquetes Redes/" + file, "rb")

    def _setPriority(self, priority):
        self._priority += '\n\tPrioridad ' + priority + ': '

        if(priority.__eq__("000")):
            self._priority += "Rutina"
        
        elif(priority.__eq__("001")):
            self._priority += "Prioritario"

        elif(priority.__eq__("010")):
            self._priority += "Inmediato"

        elif(priority.__eq__("011")):
            self._priority += "Relámpago"

        elif(priority.__eq__("100")):
            self._priority += "Invalidación relámpago"

        elif(priority.__eq__("101")):
            self._priority += "Procesando llamada crítica y de emergencia"

        elif(priority.__eq__("110")):
            self._priority += "Control de trabajo de internet"
        
        elif(priority.__eq__("111")):
            self._priority += "Control de red"

    def _getPriority(self):
        return self._priority

    def _setService(self, service):
        self._service += '\n\tServicio ' + service + ': '

        if(service[0].__eq__('0')):
            self._service += "\n\tRetardo (" + '0' + "): normal"
        else:
            self._service += "\n\tRetardo (" + '1' + "): bajo"

        if(service[1].__eq__('0')):
            self._service += "\n\tRendimiento (" + '0' + "): normal"
        else:
            self._service += "\n\tRendimiento (" + '1' + "): alto"

        if(service[2].__eq__('0')):
            self._service += "\n\tFiabilidad (" + '0' + "): normal"
        else:
            self._service += "\n\tFiabilidad (" + '1' + "): alta"

        self._service += "\n\tNo usados (" + "00" + "): reservados para el futuro" 
    
    def _getService(self):
        return self._service

    def _getLength(self):
        bytes_str = self._file.read(2)
        aux = ''
        for byte in bytes_str:
            aux += '{:08b}'.format(byte)

        self._length = int(aux, 2)

        return str(self._length) + " octetos"
    
    def _getNext(self):
        read = self._file.read(1)
        for line in read:
            aux = str(int(line))

        self._next = ""

        if aux.__eq__('1'):
            self._next += "ICMPv4"
        elif aux.__eq__('6'):
            self._next += "TCP"
        elif aux.__eq__("17"):
            self._next += "UDP"
        elif aux.__eq__("58"):
            self._next += "ICMPv6"
        elif aux.__eq__("118"):
            self._next += "STP"
        elif aux.__eq__("121"):
            self._next += "SMP"
        else:
            self._next += "Desconocido"   
        self.__next_header = self._next

        return self._next

    def _getHopCount(self):
        read = self._file.read(1)
        aux = ord(read)
        self._hop_count = aux

        return str(self._hop_count)
    
    def _getData(self):
        read = self._file.read()
        for line in read:
            self._data += '{:02x}'.format(line).upper() + ' '

        return self._data