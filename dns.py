class DNS:
    def __init__(self, file, byte):
        self.__id = 0x0
        self.__qr = 0
        self.__opcode = 0
        self.__aa = 0
        self.__tc = 0
        self.__rd = 0
        self.__ra = 0
        self.__z = 0
        self.__ad = 0
        self.__cd = 0
        self.__rcode = 0

        self.__qdcount = 0
        self.__qdname = ''
        self.__qdtype = 0
        self.__qdclass = 0

        self.__ancount = 0
        self.__anname = ''
        self.__antype = 0
        self.__anclass = 0
        self.__anttl = 0
        self.__andatalength = 0
        self.__anrdata = 0
        
        self.__nscount = 0
        self.__arcount = 0

        self.__positions = []
        self.__sizes = []
        self.__valid_chars = [chr(k) for k in range(97, 123)] + [chr(w) for w in range(65,91)] + [str(i) for i in range(0,10)] \
                + ['-', '/', '.', '_', '~', '!', '$', '&', '(',')','*', '+',',',';','=',':','@']
        self.__band = True
        self.__nocname = False

        self._file = open("Paquetes Redes/" + file, "rb")
        self._file.seek(byte)

    def _get_id(self):
        read = self._file.read(2)
        aux = ''

        for byte in read:
            aux += f'{byte:02x}'.upper()

        self.__id = aux

        self._get_flags()  # obtener las banderas después del id

        return self.__id

    def _get_flags(self):
        bytes_str = self._file.read(2)
        aux = ''

        for byte in bytes_str:
            aux += '{:08b}'.format(byte)

        self.__qr = int(aux[:1], 2)
        self.__opcode = int(aux[1:5], 2)
        self.__aa = int(aux[5:6], 2)
        self.__tc = int(aux[6:7], 2)
        self.__rd = int(aux[7:8], 2)
        self.__ra = int(aux[8:9], 2)
        self.__z = int(aux[9:10], 2)
        self.__ad = int(aux[10:11], 2)
        self.__cd = int(aux[11:12], 2)
        self.__rcode = int(aux[12:], 2)

    def _get_qr_flag(self):
        qr = ''

        if self.__qr == 0:
            qr = f'{self.__qr} - (Consulta)'
        elif self.__qr == 1:
            qr = f'{self.__qr} - (Respuesta)'

        return qr

    def _get_opcode_flag(self):
        opcode = ''

        if self.__opcode == 0:
            opcode = f'{self.__opcode} - Consulta estandar (QUERY)'
        elif self.__opcode == 1:
            opcode = f'{self.__opcode} - Consulta inversa (IQUERY)'
        elif self.__opcode == 2:
            opcode = f'{self.__opcode} - Solicitud del estado del servidor (STATUS)'
        else:
            opcode = f'{self.__opcode}: Reservado para el futuro'

        return opcode

    def _get_aa_flag(self):
        return self.__aa

    def _get_tc_flag(self):
        return self.__tc

    def _get_rd_flag(self):
        return self.__rd

    def _get_ra_flag(self):
        return self.__ra

    def _get_z_flag(self):
        return self.__z

    def _get_ad_flag(self):
        return self.__ad

    def _get_cd_flag(self):
        return self.__cd

    def _get_rcode_flag(self):
        if self.__rcode == 0:
            return f'{self.__rcode} - Ningún error'
        elif self.__rcode == 1:
            return f'{self.__rcode} - Error de formato. El servidor fue incapaz de \
                    interpretar el mensaje'
        elif self.__rcode == 2:
            return f'{self.__rcode} - Fallo en el servidor. El mensaje no fue procesado \
                    debido a un problema con el servidor'
        elif self.__rcode == 3:
            return f'{self.__rcode} - Error en nombre. El nombre de dominio de la consulta \
                    no existe'
        elif self.__rcode == 4:
            return f'{self.__rcode} - No implementado. El tipo de consulta no está \
                    implementado en el servidor de nombres'
        elif self.__rcode == 5:
            return f'{self.__rcode} - Rechazado. El servidor rechaza responder \
                    por razones políticas'
        return ''
            
    def _get_qdcount(self):
        bytes_str = self._file.read(2)
        aux = ''

        for byte in bytes_str:
            aux += '{:08b}'.format(byte)

        self.__qdcount = int(aux, 2)

        return self.__qdcount

    def _get_qdname(self):
        j = 0
        self.__positions.append(self._file.tell())
        while n := ord(self._file.read(1)):
            j = 0
            while j < n:
                self.__qdname += chr(ord(self._file.read(1)))
                j += 1
            self.__qdname += '.'
        self.__qdnamecpy = self.__qdname[:-1]

        return self.__qdname[:-1]
    
    def _get_qdtype(self):
        bytes_str = self._file.read(2)
        aux = ''

        for byte in bytes_str:
            aux += '{:08b}'.format(byte)

        self.__qdtype = int(aux, 2)

        if self.__qdtype == 1:
            return f'{self.__qdtype} - A'
        elif self.__qdtype == 5:
            return f'{self.__qdtype} - CNAME'
        elif self.__qdtype == 13:
            return f'{self.__qdtype} - HINFO'
        elif self.__qdtype == 15:
            return f'{self.__qdtype} - MX'
        elif self.__qdtype == 22 or self.__qdtype == 23:
            return f'{self.__qdtype} - NS'
        return ''
    
    def _get_qdclass(self):
        bytes_str = self._file.read(2)
        aux = ''

        for byte in bytes_str:
            aux += '{:08b}'.format(byte)

        self.__qdclass = int(aux, 2)

        if self.__qdclass == 1:
            return f'{self.__qdclass} - IN'
        elif self.__qdclass == 3:
            return f'{self.__qdclass} - CH'
        return ''

    def _get_ancount(self):
        bytes_str = self._file.read(2)
        aux = ''

        for byte in bytes_str:
            aux += '{:08b}'.format(byte)

        self.__ancount = int(aux, 2)

        return self.__ancount

    def _get_anname(self):
        bytes_str = self._file.read(2)
        curr = self._file.tell()
        aux = self.__anname
        self.__anname = ''

        if self.__nocname:
            self.__anname = self.__qdname[:-1]
            return self.__anname
        else:
            if self.__band:
                try:
                    self._file.seek(self.__positions.pop())
                    while n := ord(self._file.read(1)):
                        j = 0
                        while j < n:
                            self.__anname += chr(ord(self._file.read(1)))
                            j += 1
                        self.__anname += '.'
                    
                    self._file.seek(curr)
                    return self.__anname[:-1]
                except:
                    return self.__qdname[:-1]
            else:
                self._file.seek(self.__positions[-1])
                j = self.__sizes[-1]
                cont = 0
                
                while cont < j:
                    c = chr(ord(self._file.read(1)))
                    self.__anname += str(c) if c in self.__valid_chars else '.'
                    cont += 1

                self.__anname = self.__anname.replace('..', '')
                
                if self.__anname [0] == '.':
                    self.__anname  = self.__anname .replace(self.__anname [0], '', 1)
                if self.__anname [-1] == '.':
                    self.__anname  = self.__anname[:-1]
                
                if j < 5:
                    p = aux.index('.')
                    aux = aux[p:]
                    self.__anname = aux[1:]

                self._file.seek(curr)

                return self.__anname
    
    def _get_antype(self):
        bytes_str = self._file.read(2)
        aux = ''

        for byte in bytes_str:
            aux += '{:08b}'.format(byte)

        self.__antype = int(aux, 2)

        if self.__antype == 1:
            return f'{self.__antype} - A'
        elif self.__antype == 5:
            return f'{self.__antype} - CNAME'
        elif self.__antype == 13:
            return f'{self.__antype} - HINFO'
        elif self.__antype == 15:
            return f'{self.__antype} - MX'
        elif self.__antype == 22 or self.__antype == 23:
            return f'{self.__antype} - NS'
        return ''
    
    def _get_anclass(self):
        bytes_str = self._file.read(2)
        aux = ''

        for byte in bytes_str:
            aux += '{:08b}'.format(byte)

        self.__anclass = int(aux, 2)

        if self.__anclass == 1:
            return f'{self.__anclass} - IN'
        elif self.__anclass == 3:
            return f'{self.__anclass} - CH'
        return ''

    def _get_anttl(self):
        bytes_str = self._file.read(4)
        aux = ''
        for byte in bytes_str:
            aux += '{:08b}'.format(byte)
             
        try:
            self.__anttl = int(aux, 2)
        except ValueError:
            self.__anttl = -1

        return self.__anttl if self.__anttl != -1 else ''

    def _get_andatalength(self):
        bytes_str = self._file.read(2)
        aux = ''
        for byte in bytes_str:
            aux += '{:08b}'.format(byte)
             
        try:
            self.__andatalength = int(aux, 2)
        except ValueError:
            self.__andatalength = -1

        return self.__andatalength if self.__andatalength != -1 else ''

    def _get_anrdata(self):
        aux = ''
        if self.__antype == 1: #A
            ipv4 = ''
            bytes_str = self._file.read(self.__andatalength)
            for line in bytes_str:
                aux = str(int(line))
                ipv4 += aux + '.'
            
            self.__nocname = True
            ipv4 = ipv4[:-1]
            return '\t\t-> Address: ' + ipv4

        elif self.__antype == 5: #CNAME
            cname = ''
            
            if not self.__nocname:
                if self.__andatalength > 0:
                    try:
                        curr = self._file.tell()
                        j = 0
                        while j < self.__andatalength:
                            c = chr(ord(self._file.read(1)))
                            cname += str(c) if c in self.__valid_chars else '.'
                            j += 1

                        cname = cname.replace('..', '')

                        if cname[0] == '.':
                            cname = cname.replace(cname[0], '', 1)
                        if cname[-1] == '.':
                            cname = cname[:-1]

                        if self.__andatalength < 5:
                            p = self.__anname.index('.')
                            cname = self.__anname[p+1:]

                        self.__band = False
                        self.__positions.append(curr)
                        self.__sizes.append(self.__andatalength)
                    except:
                        cname = self.__anname
          
            else:
                cname = self.__qdname[:-1]

            return '\t\t-> Name: ' + cname

            
        elif self.__antype == 15: #MX
            mx = ''
            bytes_str = self._file.read(self.__andatalength)
            for i in bytes_str:
                mx += chr(ord(i))
            return '\t\t-> Mail Exchange: ' + mx

        elif self.__antype == 22 or self.__antype == 23: #NS PTR y SOA
            oname = ''
            bytes_str = self._file.read(self.__andatalength)
            for i in bytes_str:
                oname += chr(ord(i))
            return '\t\t-> Domain Name Server: ' + oname

        return '\t\t'
  
    def _get_nscount(self):
        bytes_str = self._file.read(2)
        aux = ''

        for byte in bytes_str:
            aux += '{:08b}'.format(byte)

        self.__nscount = int(aux, 2)

        return self.__nscount
    
    def _get_arcount(self):
        bytes_str = self._file.read(2)
        aux = ''

        for byte in bytes_str:
            aux += '{:08b}'.format(byte)

        self.__arcount = int(aux, 2)

        return self.__arcount

    def __str__(self):
        cadena = \
            "\n\n\t======================== DNS ============================" +\
            "\n\nID: " + self._get_id() +\
            "\n\nFlags:\n\tQR: " + self._get_qr_flag() +\
            "\n\tOP code: " + self._get_opcode_flag() +\
            "\n\tAA: " + str(self._get_aa_flag()) +\
            "\n\tTC: " + str(self._get_tc_flag()) +\
            "\n\tRD: " + str(self._get_rd_flag()) +\
            "\n\tRA: " + str(self._get_ra_flag()) +\
            "\n\t Z: " + str(self._get_z_flag()) +\
            "\n\tAD: " + str(self._get_ad_flag()) +\
            "\n\tCD: " + str(self._get_cd_flag()) +\
            "\n\tRCode: " + self._get_rcode_flag() +\
            "\n\nQDCount: " + str(self._get_qdcount()) +\
            "\n\nANCount: " + str(self._get_ancount()) +\
            "\n\nNSCount: " + str(self._get_nscount()) +\
            "\n\nARCount: " + str(self._get_arcount())

        #por si hay mas de una pregunta     
        query = '\n\nDNS Question:' if self.__qdcount > 0 else '\n\nDNS question:\n\t No question'
        for i in range (0,self.__qdcount):
            query += "\n\tName: " + self._get_qdname()
            query += "\n\tType: " + self._get_qdtype()
            query += "\n\tClass: " + self._get_qdclass()

        #por si hay mas de una respuesta
        answer = '\n\nDNS Answer:' if self.__ancount > 0 else '\n\nDNS Answer:\n\t No answer'
        for i in range (0,self.__ancount):
            answer += f"\n\tName: " + str(self._get_anname())
            answer += "\n\tType: " + str(self._get_antype()) 
            answer += "\n\tClass: " + str(self._get_anclass()) 
            answer += "\n\tTTL: " + str(self._get_anttl()) 
            answer += "\n\tData Length: " + str(self._get_andatalength()) 
            answer += "\n\tRData:\n"  + str(self._get_anrdata()) + '\n'

        return cadena + query + answer
        
    def __del__(self):
        try:
            self._file.close()
        except:
            print("No se pudo cerrar el archivo")


if __name__ == "__main__":
    try:
        packet = DNS("ethernet_ipv4_udp_dns.bin", byte=42)
        print(packet)
    except:
        print("Ha ocurrido un error en la creacion del paquete")

