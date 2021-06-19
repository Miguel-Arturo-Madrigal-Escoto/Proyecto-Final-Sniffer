from icmp import ICMP

class ICMPv6(ICMP):
    def __init__(self, file):
        super().__init__(file)
    
    # ? implementa el @abstractmethod
    def _getType(self):
        self._file.seek(54)
        self._type = ord(self._file.read(1))
        self.__setCode()

        if self._type == 1:
            self._type = "{} Mensaje de destino inalcanzable".format(self._type)
        elif self._type == 2:
            self._type = "{} Mensaje de paquete demasiado grande".format(self._type)
        elif self._type == 3:
            self._type = "{} Time Exceeded Message".format(self._type)
        elif self._type == 4:
            self._type = "{} Mensaje de problema de parámetro".format(self._type)
        elif self._type == 128:
            self._type = "{} Mensaje del pedido de eco".format(self._type)
        elif self._type == 129:
            self._type = "{} Mensaje de respuesta de eco".format(self._type)
        elif self._type == 133:
            self._type = "{} Mensaje de solicitud de router".format(self._type)
        elif self._type == 134:
            self._type = "{} Mensaje de anuncio de router".format(self._type)
        elif self._type == 135:
            self._type = "{} Mensaje de solicitud vecino".format(self._type)
        elif self._type == 136:
            self._type = "{} Mensaje de anuncio de vecino".format(self._type)
        elif self._type == 137:
            self._type = "{} Reoriente el mensaje".format(self._type)
        else:
            self._type = "{} Mensaje desconocido".format(self._type)

        return self._type

    def __setCode(self):
        self._code = ord(self._file.read(1))

    # ? se implementa el @abstractmethod
    def _getCode(self):
        if self._type == "1 Mensaje de destino inalcanzable" and self._code == 0:
            self._code = "{} No existe ruta destino".format(self._code)
        elif self._type == "1 Mensaje de destino inalcanzable" and self._code == 1:
            self._code = "{} Comunicacion con el destino administrativamente prohibida".format(self._code)
        elif self._type == "1 Mensaje de destino inalcanzable" and self._code == 2:
            self._code = "{} No asignado".format(self._code)
        elif self._type == "1 Mensaje de destino inalcanzable" and self._code == 3:
            self._code = "{} Direccion inalcanzable".format(self._code)
        elif self._type == "2 Mensaje de paquete demasiado grande" and self._code == 0:
            self._code = '{}'.format(self._code)
        elif self._type == "3 Time Exceeded Message" and self._code == 0:
            self._code = "{} El limite de salto excedido".format(self._code)
        elif self._type == "3 Time Exceeded Message" and self._code == 1:
            self._code = "{} Tiempo de reensamble de fragmento excedido".format(self._code)
        elif self._type == "4 Mensaje de problema de parámetro" and self._code == 0:
            self._code = "{} Campo de encabezado erroneo".format(self._code)
        elif self._type == "4 Mensaje de problema de parámetro" and self._code == 1:
            self._code = "{} Tipo de encabezado siguiente desconocido".format(self._code)
        elif self._type == "4 Mensaje de problema de parámetro" and self._code == 2:
            self._code = "{} Opcion desconocida de IPv6 encontrada".format(self._code)
        else:
            self._code = '{}'.format(self._code)    
        
        return self._code
    
    def __str__(self):
        return (
            "\n\n\t======================== ICMPv6 ============================" +
            "\n\n" + super().__str__()
        )

    def __del__(self):
        try:
            self._file.close()
        except:
            print("No se pudo cerrar el archivo")
            
if __name__ == "__main__":
    try:
        packet = ICMPv6("ipv6_icmpv6_hop_limit.bin")
        print(packet)
    except:
        print("Ha ocurrido un error en la creacion del paquete")