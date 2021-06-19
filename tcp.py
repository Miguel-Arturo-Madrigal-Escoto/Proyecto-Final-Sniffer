from transport_layer import TransportLayer

class TCP(TransportLayer):
    # ? se le pasa el byte de donde lee porque tambien va en IPv6
    def __init__(self, file, byte):
        super().__init__(file, byte)
        self.__sequence_number = 0
        self.__acknoledgement_number = 0

    def _getSourcePort(self):
        bytes_str = self._file.read(2)
        aux = ''
        for byte in bytes_str:
            aux += '{:08b}'.format(byte)
        aux = int(aux, 2)

        self._source_port = aux #puerto origen (int)

        if aux >= 0 and aux <= 1023:
            if aux == 20 or aux == 21:
                self._source_port = '\n\tPuerto bien conocido: {}\n\tServicio: FTP'.format(
                    aux)
            elif aux == 22:
                self._source_port = '\n\tPuerto bien conocido: {}\n\tServicio: SSH'.format(
                    aux)
            elif aux == 23:
                self._source_port = '\n\tPuerto bien conocido: {}\n\tServicio: TELNET'.format(
                    aux)
            elif aux == 25:
                self._source_port = '\n\tPuerto bien conocido: {}\n\tServicio: SMTP'.format(
                    aux)
            elif aux == 53:
                self._source_port = '\n\tPuerto bien conocido: {}\n\tServicio: DNS'.format(
                    aux)
            elif aux == 80:
                self._source_port = '\n\tPuerto bien conocido: {}\n\tServicio: HTTP'.format(
                    aux)
            elif aux == 110:
                self._source_port = '\n\tPuerto bien conocido: {}\n\tServicio: POP3'.format(
                    aux)
            elif aux == 143:
                self._source_port = '\n\tPuerto bien conocido: {}\n\tServicio: IMAP'.format(
                    aux)
            elif aux == 443:
                self._source_port = '\n\tPuerto bien conocido: {}\n\tServicio: HTTPS'.format(
                    aux)
            elif aux == 993:
                self._source_port = '\n\tPuerto bien conocido: {}\n\tServicio: IMAP SSL'.format(
                    aux)
            elif aux == 995:
                self._source_port = '\n\tPuerto bien conocido: {}\n\tServicio: POP SSL'.format(
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
            if aux == 20 or aux == 21:
                self._destination_port = '\n\tPuerto bien conocido: {}\n\tServicio: FTP'.format(
                    aux)
            elif aux == 22:
                self._destination_port = '\n\tPuerto bien conocido: {}\n\tServicio: SSH'.format(
                    aux)
            elif aux == 23:
                self._destination_port = '\n\tPuerto bien conocido: {}\n\tServicio: TELNET'.format(
                    aux)
            elif aux == 25:
                self._destination_port = '\n\tPuerto bien conocido: {}\n\tServicio: SMTP'.format(
                    aux)
            elif aux == 53:
                self._destination_port = '\n\tPuerto bien conocido: {}\n\tServicio: DNS'.format(
                    aux)
            elif aux == 80:
                self._destination_port = '\n\tPuerto bien conocido: {}\n\tServicio: HTTP'.format(
                    aux)
            elif aux == 110:
                self._destination_port = '\n\tPuerto bien conocido: {}\n\tServicio: POP3'.format(
                    aux)
            elif aux == 143:
                self._destination_port = '\n\tPuerto bien conocido: {}\n\tServicio: IMAP'.format(
                    aux)
            elif aux == 443:
                self._destination_port = '\n\tPuerto bien conocido: {}\n\tServicio: HTTPS'.format(
                    aux)
            elif aux == 993:
                self._destination_port = '\n\tPuerto bien conocido: {}\n\tServicio: IMAP SSL'.format(
                    aux)
            elif aux == 995:
                self._destination_port = '\n\tPuerto bien conocido: {}\n\tServicio: POP SSL'.format(
                    aux)
            else:
                self._destination_port = '\n\tPuerto bien conocido: {}\n\tServicio: Desconocido'.format(
                    aux)

        elif aux >= 1024 and aux <= 49151:
            self._destination_port = 'Puerto registrado -> {}'.format(aux)
        elif aux >= 49152 and aux <= 65535:
            self._destination_port = 'Puerto dinamico/privado -> {}'.format(
                aux)
        else:
            self._destination_port = 'Puerto desconocido -> {}'.format(aux)

        return self._destination_port

    def __getSequenceNumber(self):
        bytes_str = self._file.read(4)
        aux = ''
        for byte in bytes_str:
            aux += '{:08b}'.format(byte)
        self.__sequence_number = int(aux, 2)

        return self.__sequence_number

    def __getAcknowledgementNumber(self):
        bytes_str = self._file.read(4)
        aux = ''

        for byte in bytes_str:
            aux += '{:08b}'.format(byte)
        self.__acknoledgement_number = int(aux, 2)

        return self.__acknoledgement_number

    def _getLength(self):
        bytes_str = self._file.read(2)
        aux = ''

        for byte in bytes_str:
            aux += '{:08b}'.format(byte)

        self._length = int(aux[:4], 2)
        self._reserved = int(aux[5:7], 2)
        self._flag_ns = int(aux[7:8], 2)
        self._flag_cwr = int(aux[8:9], 2)
        self._flag_ece = int(aux[9:10], 2)
        self._flag_urg = int(aux[10:11], 2)
        self._flag_ack = int(aux[11:12], 2)
        self._flag_psh = int(aux[12:13], 2)
        self._flag_rst = int(aux[13:14], 2)
        self._flag_syn = int(aux[14:15], 2)
        self._flag_fin = int(aux[15:16], 2)

        return self._length

    def _getReserved(self):
        return self._reserved

    def _getFlagNs(self):
        return self._flag_ns

    def _getFlagCwr(self):
        return self._flag_cwr

    def _getFlagEce(self):
        return self._flag_ece

    def _getFlagUrg(self):
        return self._flag_urg

    def _getFlagAck(self):
        return self._flag_ack

    def _getFlagPsh(self):
        return self._flag_psh

    def _getFlagRst(self):
        return self._flag_rst

    def _getFlagSyn(self):
        return self._flag_syn

    def _getFlagFin(self):
        return self._flag_fin

    def _getWindowSize(self):
        bytes_str = self._file.read(2)
        aux = ''

        for byte in bytes_str:
            aux += '{:08b}'.format(byte)

        self.__window_size = int(aux, 2)
        
        return self.__window_size

    def _getUrgentPointer(self):
        bytes_str = self._file.read(2)
        aux = ''

        for byte in bytes_str:
            aux += '{:b}'.format(byte)

        self.__urgent_pointer = int(aux, 2)
        
        return self.__urgent_pointer

    def __str__(self):
        return (
            "\n\n\t======================== TCP ============================" +
            str(super().__str__()) +
            "\n\nNumero de secuencia: " + str(self.__getSequenceNumber()) +
            "\n\nNumero de acuse de recibo: " + str(self.__getAcknowledgementNumber()) +
            "\n\nLongitud de cabecera: " + str(self._getLength()) +
            "\n\nReservado: " + str(self._getReserved()) +
            "\n\nFlags:\n\tNS: " + str(self._getFlagNs()) +
            "\n\tCWR: " + str(self._getFlagCwr()) +
            "\n\tECE: " + str(self._getFlagEce()) +
            "\n\tURG: " + str(self._getFlagUrg()) +
            "\n\tACK: " + str(self._getFlagAck()) +
            "\n\tPSH: " + str(self._getFlagPsh()) +
            "\n\tRST: " + str(self._getFlagRst()) +
            "\n\tSYN: " + str(self._getFlagSyn()) +
            "\n\tFIN: " + str(self._getFlagFin()) +
            "\n\nTamaño de ventana: " + str(self._getWindowSize()) +
            "\n\nSuma de verificación: " + self._getChecksum() +
            "\n\nPuntero urgente: " + str(self._getUrgentPointer()) +
            "\n\nDatos: " + str(self._getData())
        )

    def __del__(self):
        try:
            self._file.close()
        except:
            print("No se pudo cerrar el archivo")


if __name__ == "__main__":
    try:
        segment = TCP("ethernet_ipv4_tcp_syn.bin", byte=34)
        print(segment)
    except:
        print("Ha ocurrido un error en la creacion del paquete")
