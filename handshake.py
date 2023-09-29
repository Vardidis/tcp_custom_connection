class Handshake:

    status = True
    connected = False

    def __init__(self, type:str):
        if type == 'SYN':
            if self.status:
                self.connected = True
                return ['SYN', 'ACK']
        return 'RST'

class packet:

    source_port:int
    dest_port:int = 443
    seq_number:int = 0
    ack_number:int = 64
    offset:int = 0
    reserved:int
    tcp_flags:dict[int] = {'NS': 0, 'CWR': 0, 'ECE': 0, 'URG': 0, 'ACK': 0, 'PSH': 0, 'RST': 0, 'SYN': 0, 'FIN': 0}
    window:None
    checksum:int
    urgent_point:int
    tcp_options:int

    def __init__(self, sp, flg):
        self.source_port = sp
        self.tcp_flags = flg