from ip import IP

class IPv6(IP):
    def __init__(self, file):
        super().__init__(file)
        self.__flow_label = 0
    
    def __getVersion(self):
        self._file.seek(14)
        bytes_str = self._file.read(4)
        aux = ''
        for byte in bytes_str:
            aux += '{:08b}'.format(byte)
        
        self._version = int(aux[:4], 2)
        self._setPriority(aux[4:7])
        self._setService(aux[7:12])
        self.__setFlowLabel(aux[12:])

        return self._version

    def __setFlowLabel(self, flow):
        self.__flow_label = int(flow, 2) 

    def __getFlowLabel(self):
        return str(self.__flow_label)

    def getNextHeader(self):
        return self._IP__next_header
      
    def __getSourceAddress(self):
        self._file.seek(22)
        read = self._file.read(16)

        cont = 0
        for line in read:
            aux = hex(line)

            self._source += '{:02x}'.format(line).upper()

            if cont % 2 == 1:
                self._source += ":"
            cont += 1

        return self._source[:-1]

    def __getDestinationAddress(self):
        read = self._file.read(16)

        cont = 0
        for line in read:
            aux = hex(line)

            self._destination += '{:02x}'.format(line).upper()

            if cont % 2 == 1:
                self._destination += ":"
            cont += 1

        return self._destination[:-1]

    def __str__(self):
        return (
            "\n\n\t======================== IPv6 ============================" +
            "\n\nVersion: " + str(self.__getVersion()) + 
            "\n\nClase de trafico: " + '\n' + self._getPriority() + '\n' + self._getService() +
            "\n\nEtiqueta de flujo: " + self.__getFlowLabel() +
            "\n\nTamaño de datos: " + self._getLength() +
            "\n\nEncabezado siguiente: " + self._getNext() +
            "\n\nLimite de salto: " + self._getHopCount() +
            "\n\nDireccion MAC origen: " + self.__getSourceAddress() +
            "\n\nDireccion MAC destino: " + self.__getDestinationAddress()+
            "\n\nDatos: " + self._getData()
        )
    
    def __del__(self):
        try:
            self._file.close()
        except:
            print("No se pudo cerrar el archivo")


if __name__ == "__main__":
    try:
        packet = IPv6("ipv6_icmpv6_hop_limit.bin")
        print(packet)   
    except:
       print("Ha ocurrido un error en la creacion del paquete")
