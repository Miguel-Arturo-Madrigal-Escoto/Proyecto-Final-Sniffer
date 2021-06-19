class Ethernet:
    def __init__(self, file):
        self.__sourceMac = ""
        self.__destinationMac = ""
        self.__type = ""
        self.__data = ""
        self.__protocol = ""
        self.__file = open("Paquetes Redes/" + file, "rb")

    def __getSourceMac(self):
        read = self.__file.read(6)
        for line in read:
            self.__sourceMac += '{:02x}'.format(line).upper() + ":"

        self.__sourceMac = self.__sourceMac[:-1]

        return self.__sourceMac

    def __getDestinationMac(self):
        read = self.__file.read(6)
        for line in read:
            self.__destinationMac += '{:02x}'.format(line).upper() + ":"

        self.__destinationMac = self.__destinationMac[:-1]

        return self.__destinationMac

    def __getType(self):
        read = self.__file.read(2)
        for line in read:
            self.__type += '{:02x}'.format(line).upper()

        if(self.__type.__eq__("0800")):
            self.__protocol = 'IPv4'
            self.__type = "{} -> IPv4".format(self.__type)

        elif(self.__type.__eq__("0806")):
            self.__protocol = 'ARP'
            self.__type = "{} -> ARP".format(self.__type)

        elif(self.__type.__eq__("8035")):
            self.__protocol = 'RARP'
            self.__type = "{} -> RARP".format(self.__type)

        elif(self.__type.__eq__("86DD")):
            self.__protocol = 'IPv6'
            self.__type = "{} -> IPv6".format(self.__type)

        return self.__type

    def __getData(self):
        read = self.__file.read()
        for line in read:
            self.__data += '{:02x}'.format(line).upper() + ' '

        return self.__data

    def getProtocol(self):
        return self.__protocol

    def __str__(self):
        return "\n\t======================== Ethernet ========================" + \
            "\n\nDireccion Mac origen: " + self.__getSourceMac() + "\n\nDireccion Mac destino: " + \
            self.__getDestinationMac() + "\n\nTipo de codigo: " + self.__getType()  
            #"\n\nDatos: " + self.__getData()

    def __del__(self):
        try:
            self.__file.close()
        except:
            print("No se pudo cerrar el archivo")


if __name__ == "__main__":
    try:
        frame = Ethernet("ethernet_arp_reply.bin")
        print(frame)
    except:
        print("Ha ocurrido un error en la creacion del paquete")