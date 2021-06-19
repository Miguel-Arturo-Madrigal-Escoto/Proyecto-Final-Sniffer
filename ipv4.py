from ip import IP

class IPv4(IP):
    def __init__(self, file):
        super().__init__(file)
        self.__header_length = 0
        self.__id = 0
        self.__flags = ""
        self.__fragments = ""
        self.__total_length = 0
        self.__checksum = ""      

    def __getVersion(self):
        self._file.seek(14)
        read = self._file.read(1)
        aux = '{0:08b}'.format(ord(read))
        self._version = str(int(aux[:4], 2))
        self.__header_length = int(aux[4:], 2)

        return self._version
    
    def __getHeaderLength(self):
        return str(self.__header_length * 32 // 8) + " bytes"

    def __getDS(self):
        read = self._file.read(1)
        aux = '{0:08b}'.format(ord(read))
        aux_priority = aux[:3]
        aux_service = aux[3:]
        self._setPriority(aux_priority) 
        self._setService(aux_service)
        
        return self._getPriority() + '\n' + self._getService()
        
    def __getID(self):
        read = self._file.read(2)
        aux = ''
        for byte in read:
            aux += "{:08b}".format(byte)

        self.__id = int(aux, 2)

        return str(self.__id)

    def __getFlags(self):
        self._file.seek(20)
        read = self._file.read(2)
        aux = ''
        for byte in read:
            aux += "{:08b}".format(byte)
        self.__flags += "Banderas ({}): \n\tNo usado ({}): reservado\n".format(aux[:3], aux[0])
        
        if(aux[1].__eq__("0")):
            self.__flags += "\t¿DF? ({}): falso(divisible)\n".format(aux[1])
            if(aux[2].__eq__("0")):
                self.__flags += "\t¿MF? ({}): falso(último fragmento)\n".format(aux[2])
            else:
                self.__flags += "\t¿MF? ({}): verdadero(más fragmentos)\n".format(aux[2])
        else:
            self.__flags += "\t¿DF? ({}): verdadero(indivisible)\n\t¿MF? ({}): falso(último fragmento)\n".format(aux[1], aux[2])

        self.__fragments += "Desplazamiento de Fragmentos: {} \n\t".format(int(aux[3:], 2))
        
        return self.__flags

    def __getFragments(self):
        return self.__fragments

    def __getChecksum(self):
        read = self._file.read(2)

        for line in read:
            aux = hex(line)
            self.__checksum += '{:02x}'.format(line).upper()

        return self.__checksum

    def getNextHeader(self):
        return self._IP__next_header

    def __getSourceIp(self):
        read = self._file.read(4)
        for line in read:
            aux = str(int(line))
            self._source += aux + '.'

        self._source = self._source[:-1]
        
        return self._source

    def __getDestinationIp(self):
        read = self._file.read(4)
        
        for line in read:
            aux = str(int(line))
            self._destination += aux + '.'

        self._destination = self._destination[:-1]
        
        return self._destination
    
    def __del__(self):
        try:
            self._file.close()
        except:
            print("No se pudo cerrar el archivo")

    def __str__(self):
        return "\n\n\t======================== IPv4 ============================" + \
            "\n\nVersion: "  + self.__getVersion() + "\n\nLongitud encabezado: " + self.__getHeaderLength() + \
            "\n\nTipo de servicio:\t\n" + self.__getDS() + "\n\nLongitud total:\n\t" + self._getLength() + \
            "\n\nIdentificador:\n\t" + self.__getID() + "\n\n" + self.__getFlags() + "\n" + self.__getFragments() + \
            "\nTTL: " + self._getHopCount() + "\n\nProtocolo: "  + self._getNext() + "\n\nSuma de verificacion: " + \
            self.__getChecksum() + "\n\nDireccion IP origen: " + self.__getSourceIp() + \
            "\n\nDireccion IP destino: " + self.__getDestinationIp() + "\n" + "\nDatos: " + self._getData() 

if __name__ == "__main__":
    try:
        packet = IPv4("ethernet_ipv4_icmp_host_unreachable.bin")
        print(packet)
    except:
        print("Ha ocurrido un error en la creacion del paquete")

