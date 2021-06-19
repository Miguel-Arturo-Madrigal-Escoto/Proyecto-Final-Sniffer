from transport_layer import TransportLayer

class UDP(TransportLayer):
    def __init__(self, file, byte):
        super().__init__(file, byte)
    
    def _getSourcePort(self):
        bytes_str = self._file.read(2)
        aux = ''
        for byte in bytes_str:
            aux += '{:08b}'.format(byte)
        aux = int(aux, 2)

        self._source_service = aux #puerto origen(int)

        if aux >= 0 and aux <= 1023:
            if aux == 53:
                self._source_port = '\n\tPuerto bien conocido: {}\n\tServicio: DNS'.format(
                    aux)
            elif aux == 67 or aux == 68:
                self._source_port = '\n\tPuerto bien conocido: {}\n\tServicio: DHCP'.format(
                    aux)
            elif aux == 69:
                self._source_port = '\n\tPuerto bien conocido: {}\n\tServicio: TFTP'.format(
                    aux)
            elif aux == 443:
                self._source_port = '\n\tPuerto bien conocido: {}\n\tServicio: HTTPS'.format(
                    aux)
            else:
                self._source_port = '\n\tPuerto bien conocido: {}\n\tServicio: Desconocido'.format(
                    aux)

        elif aux >= 1024 and aux <= 49151:
            self._source_port = 'Puerto registrado -> {}'.format(aux)
        elif aux >= 49152 and aux <= 65535:
            self._source_port = 'Puerto dinamico/privado -> {}'.format(aux)
        else:
            self._source_port = 'Puerto desconocido -> {}'.format(aux)

        return self._source_port
    
    def _getDestinationPort(self):
        bytes_str = self._file.read(2)
        aux = ''
        for byte in bytes_str:
            aux += '{:08b}'.format(byte)
        aux = int(aux, 2)

        self._destination_service = aux #puerto destino (int)

        if aux >= 0 and aux <= 1023:
            if aux == 53:
                self._destination_port = '\n\tPuerto bien conocido: {}\n\tServicio: DNS'.format(
                    aux)
            elif aux == 67 or aux == 68:
                self._destination_port = '\n\tPuerto bien conocido: {}\n\tServicio: DHCP'.format(
                    aux)
            elif aux == 69:
                self._destination_port = '\n\tPuerto bien conocido: {}\n\tServicio: TFTP'.format(
                    aux)
            elif aux == 443:
                self._destination_port = '\n\tPuerto bien conocido: {}\n\tServicio: HTTPS'.format(
                    aux)
            else:
                self._destination_port = '\n\tPuerto bien conocido: {}\n\tServicio: Desconocido'.format(
                    aux)

        elif aux >= 1024 and aux <= 49151:
            self._destination_port = 'Puerto registrado -> {}'.format(aux)
        elif aux >= 49152 and aux <= 65535:
            self._destination_port = 'Puerto dinamico/privado -> {}'.format(aux)
        else:
            self._destination_port = 'Puerto desconocido -> {}'.format(aux)

        return self._destination_port
    
    def _getLength(self):
        bytes_str = self._file.read(2)

        aux = ''
        for byte in bytes_str:
            aux += '{:08b}'.format(byte)

        self._length = int(aux, 2)

        return self._length
    
    
    def __str__(self):
        return (
            "\n\n\t======================== UDP ============================" +
            str(super().__str__()) +
            "\n\nLongitud total: " + str(self._getLength()) + " bytes" +
            "\n\nChecksum: " + self._getChecksum() +
            "\n\nDatos: " + self._getData()
        )

    def __del__(self):
        try:
            self._file.close()
        except:
            print("No se pudo cerrar el archivo")

if __name__ == "__main__":
    try:
        datagram = UDP("ethernet_ipv4_udp_dns.bin", byte=34)
        print(datagram)
    except:
        print("Ha ocurrido un error en la creacion del paquete")