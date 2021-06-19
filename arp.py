class ARP:
    def __init__(self, file):
        self.__hardware = ""
        self.__protocol = ""
        self.__hwLengthDirection = 0
        self.__protocolLengthDirection = 0
        self.__operationCode = ""
        self.__sourceHW = ""
        self.__sourceIP = ""
        self.__destinationHW = ""
        self.__destinationIP = ""
        self.__file = open("Paquetes Redes/" + file, "rb")

    def __getHardware(self):
        self.__file.seek(14)
        bytes_str = self.__file.read(2)
        aux = ''

        for byte in bytes_str:
            aux += '{:08b}'.format(byte)
        aux = int(aux, 2)
        
        if(aux == 0):
            self.__hardware = "{} Reserved".format(aux)
        elif(aux == 1):
            self.__hardware = "{} Ethernet (10Mb)".format(aux)
        elif(aux == 2):
            self.__hardware = "{} Experimental Ethernet (3Mb)".format(aux)
        elif(aux == 3):
            self.__hardware = "{} Amateur Radio AX.25".format(aux)
        elif(aux == 4):
            self.__hardware = "{} Proteon ProNET Token Ring".format(aux)
        elif(aux == 5):
            self.__hardware = "{} Chaos".format(aux)
        elif(aux == 6):
            self.__hardware = "{} IEEE 802 Networks".format(aux)
        elif(aux == 7):
            self.__hardware = "{} ARCNET".format(aux)
        elif(aux == 8):
            self.__hardware = "{} Hyperchannel".format(aux)
        elif(aux == 9):
            self.__hardware = "{} Lanstar".format(aux)
        elif(aux == 10):
            self.__hardware = "{} Autonet Short Address".format(aux)
        elif(aux == 11):
            self.__hardware = "{} LocalTalk".format(aux)
        elif(aux == 12):
            self.__hardware = "{} LocalNet (IBM PCNet or SYTEK LocalNET)".format(aux)
        elif(aux == 13):
            self.__hardware = "{} Ultra link".format(aux)
        elif(aux == 14):
            self.__hardware = "{} SMDS".format(aux)
        elif(aux == 15):
            self.__hardware = "{} Frame Relay".format(aux)
        elif(aux == 16):
            self.__hardware = "{} Asynchronous Transmission Mode (ATM)".format(aux)
        elif(aux == 17):
            self.__hardware = "{} HDLC".format(aux)
        elif(aux == 18):
            self.__hardware = "{} Fibre Channel".format(aux)
        elif(aux == 19):
            self.__hardware = "{} Asynchronous Transmission Mode (ATM)".format(aux)
        elif(aux == 20):
            self.__hardware = "{} Serial Line".format(aux)
        elif(aux == 21):
            self.__hardware = "{} Asynchronous Transmission Mode (ATM)".format(aux)
        elif(aux == 22):
            self.__hardware = "{} MIL-STD-188-220".format(aux)
        elif(aux == 23):
            self.__hardware = "{} Metricom".format(aux)
        elif(aux == 24):
            self.__hardware = "{} IEEE 1394.1995".format(aux)
        elif(aux == 25):
            self.__hardware = "{} MAPOS".format(aux)
        elif(aux == 26):
            self.__hardware = "{} Twinaxial".format(aux)
        elif(aux == 27):
            self.__hardware = "{} EUI-64".format(aux)
        elif(aux == 28):
            self.__hardware = "{} HIPARP".format(aux)
        elif(aux == 29):
            self.__hardware = "{} IP and ARP over ISO 7816-3".format(aux)
        elif(aux == 30):
            self.__hardware = "{} ARPSec".format(aux)
        elif(aux == 31):
            self.__hardware = "{} IPsec tunnel".format(aux)
        elif(aux == 32):
            self.__hardware = "{} InfiniBand (TM)".format(aux)
        elif(aux == 33):
            self.__hardware = "{} TIA-102 Project 25 Common Air Interface (CAI)".format(aux)
        elif(aux == 34):
            self.__hardware = "{} Wiegand Interface".format(aux)
        elif(aux == 35):
            self.__hardware = "{} Pure IP".format(aux)
        elif(aux == 36):
            self.__hardware = "{} HW_EXP1".format(aux)
        elif(aux == 37):
            self.__hardware = "{} HFI".format(aux)
        elif(aux >= 38 and aux <= 255):
            self.__hardware = "{} Unassigned".format(aux)
        elif(aux == 256):
            self.__hardware = "{} HW_EXP2".format(aux)
        elif(aux == 257):
            self.__hardware = "{} AEthernet".format(aux)
        elif(aux >= 258 and aux <= 65534):
            self.__hardware = "{} Unassigned".format(aux)
        elif(aux == 65535):
            self.__hardware = "{} Reserved".format(aux)
        else:
            self.__hardware = "{} Unknown".format(aux)
            
        return self.__hardware

    def __getProtocol(self):
        byte_str = self.__file.read(2)
        for byte in byte_str:
            self.__protocol += '{:02x}'.format(byte).upper()

        if(self.__protocol.__eq__("0800")):
            self.__protocol = "{} -> IPv4".format(self.__protocol)
        elif(self.__protocol.__eq__("0806")):
            self.__protocol = "{} -> ARP".format(self.__protocol)
        elif(self.__protocol.__eq__("8035")):
            self.__protocol = "{} -> RARP".format(self.__protocol)
        elif(self.__protocol.__eq__("86DD")):
            self.__protocol = "{} -> IPv6".format(self.__protocol)
        else:
            self.__protocol = "{} -> Desconocido".format(self.__protocol)
        
        return self.__protocol

    def __getHWLengthDirection(self):
        byte = self.__file.read(1)
        self.__hwLengthDirection = ord(byte)

        return self.__hwLengthDirection

    def __getProtocolLengthDirection(self):
        byte = self.__file.read(1)
        self.__protocolLengthDirection = ord(byte)
        
        return self.__protocolLengthDirection

    def __getOperationCode(self):
        byte_str = self.__file.read(2)
        for byte in byte_str:
            self.__operationCode += '{}'.format(byte).upper()

        if self.__operationCode.__eq__("01") :
            self.__operationCode = "{} Solicitud ARP".format(self.__operationCode)
        elif self.__operationCode.__eq__("02"):
            self.__operationCode = "{} Respuesta ARP".format(self.__operationCode)
        elif self.__operationCode.__eq__("03"):
            self.__operationCode = "{} Solicitud RARP".format(self.__operationCode)
        elif self.__operationCode.__eq__("04"):
            self.__operationCode = "{} Respuesta RARP".format(self.__operationCode)
        
        return self.__operationCode

    def __getSourceHW(self):
        bytes_str = self.__file.read(self.__hwLengthDirection)

        for byte in bytes_str:
            self.__sourceHW += '{:02x}'.format(byte).upper() + ":"

        self.__sourceHW = self.__sourceHW[:-1]

        return self.__sourceHW

    def __getSourceIP(self):
        bytes_str = self.__file.read(self.__protocolLengthDirection)

        for byte in bytes_str:
            self.__sourceIP += str(int(byte)) + '.'

        self.__sourceIP = self.__sourceIP[:-1]

        return self.__sourceIP

    def __getDestinationHW(self):
        bytes_str = self.__file.read(self.__hwLengthDirection)

        for byte in bytes_str:
            self.__destinationHW += '{:02x}'.format(byte).upper() + ":"

        self.__destinationHW = self.__destinationHW[:-1]

        return self.__destinationHW

    def __getDestinationIP(self):
        bytes_str = self.__file.read(self.__protocolLengthDirection)

        for byte in bytes_str:
            self.__destinationIP += str(byte) + '.'

        self.__destinationIP = self.__destinationIP[:-1]

        return self.__destinationIP

    def __str__(self):
        return (
            "\n\n\t======================== ARP/RARP ============================" +
            "\n\nTipo de hardware: "   + self.__getHardware() +
            "\n\nTipo de protocolo: "   + self.__getProtocol() +
            "\n\nLongitud direccion de hardware: "   + str(self.__getHWLengthDirection()) + " bytes"  +
            "\n\nLongitud direccion de protocolo: " + str(self.__getProtocolLengthDirection()) + " bytes" +
            "\n\nCodigo de operacion: " + self.__getOperationCode() +
            "\n\nDireccion MAC de origen: " + self.__getSourceHW() + 
            "\n\nDireccion IP de origen: " + self.__getSourceIP() + 
            "\n\nDireccion MAC de destino: " + self.__getDestinationHW() +
            "\n\nDireccion IP de destino: " + self.__getDestinationIP()
        )

    def __del__(self):
        try:
            self.__file.close()
        except:
            print("No se pudo cerrar el archivo")

if __name__ == "__main__":
    try:
        packet = ARP("ethernet_arp_reply.bin")
        print(packet)
    except:
        print("Ha ocurrido un error en la creacion del paquete")