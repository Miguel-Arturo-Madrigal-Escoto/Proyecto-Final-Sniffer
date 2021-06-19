from icmp import ICMP

class ICMPv4(ICMP):
    def __init__(self, file):
        super().__init__(file)
        
    def _getType(self):
        self._file.seek(34)
        byte = self._file.read(1)
        self._type = ord(byte)
        msg = ""

        if self._type == 0:
            msg = "{}: Echo reply (respuesta de eco)".format(self._type)
        elif self._type == 3:
            msg = "{}: Destination Unreachable (destino inaccesible)".format(self._type)
        elif self._type == 4:
            msg = "{}: Source Quench (disminución del tráfico desde el origen)".format(self._type)   
        elif self._type == 5:
            msg = "{}: Redirect (redireccionar - cambio de ruta)".format(self._type)
        elif self._type == 8:
            msg = "{}: Echo (solicitud de eco)".format(self._type)
        elif self._type == 11:
            msg = "{}: Time Exceeded (tiempo excedido para un datagrama)".format(self._type)
        elif self._type == 12:
            msg = "{}: Parameter problem (problema de parámetros)".format(self._type)
        elif self._type == 13:
            msg = "{}: Timestamp (solicitud de marca de tiempo)".format(self._type)
        elif self._type == 14:
            msg = "{}: Timestamp reply (respuesta de marca de tiempo)".format(self._type)
        elif self._type == 15:
            msg = "{}: Information request (solicitud de información)".format(self._type)
        elif self._type == 16:
            msg = "{}: Information reply (respuesta de información)".format(self._type)
        elif self._type == 17:
            msg = "{}: Addressmask (solicitud de máscara de dirección)".format(self._type)
        elif self._type == 18:
            msg = "{}: Addressmask reply (respuestas de máscara de dirección)".format(self._type)
        else:
            msg = "{}: Tipo de mensaje desconocido".format(self._type)
        
        return msg

    def _getCode(self):
        byte = self._file.read(1)
        self._code = ord(byte)
        msg = ""

        if self._code == 0:
            msg = "{}: No se puede llegar a la red".format(self._code)
        elif self._code == 1:
            msg = "{}: No se puede llegar al host o aplicacion de destino".format(self._code)
        elif self._code == 2:
            msg = "{}: El destino no dispone del protocolo solicitado".format(self._code)
        elif self._code == 3:
            msg = "{}: No se puede llegar al puerto destino o la aplicacion destino no esta libre".format(self._code)
        elif self._code == 4:
            msg = "{}: Se necesita aplicar fragmentacion, pero el flag correspondiente indica lo contrario".format(self._code)
        elif self._code == 5:
            msg = "{}: La ruta de origen no es correcta".format(self._code)
        elif self._code == 6:
            msg = "{}: No se conoce la red destino".format(self._code)
        elif self._code == 7:
            msg = "{}: No se conoce el host destino".format(self._code)
        elif self._code == 8:
            msg = "{}: El host origen esta aislado".format(self._code)
        elif self._code == 9:
            msg = "{}: La comunicacion con la red destino esta prohibida por razones administrativas".format(self._code)
        elif self._code == 10:
            msg = "{}: La comunicacion con el host destino esta prohibida por razones administrativas".format(self._code)
        elif self._code == 11:
            msg = "{}: No se puede llegar a la red destino debido al tipo de servicio".format(self._code)
        elif self._code == 12:
            msg = "{}: No se puede llegar al host destino debido al tipo de servicio".format(self._code)
        else:
            msg = "{}: Codigo de error desconocido".format(self._code)

        return msg

    def __str__(self):
        return (
            "\n\n\t======================== ICMPv4 ============================" +
            "\n\n" + super().__str__()
        )

    def __del__(self):
        try:
            self._file.close()
        except:
            print("No se pudo cerrar el archivo")

if __name__ == "__main__":
    try:
        packet = ICMPv4("ethernet_ipv4_icmp_host_unreachable.bin")
        print(packet)
    except:
        print("Ha ocurrido un error en la creacion del paquete")

