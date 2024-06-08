from BambuFTP import BambuFTP

class Printer():
    def __init__(self, name, enabled):
        self.name = name
        self.enabled = enabled
        self.connected = False

class BambooPrinter(Printer):
    def __init__(self, name, ip, pw, enabled):
        super().__init__(name, enabled)
        self.ip = ip
        self.pw = pw

        self.ftp = BambuFTP()
        #self.ftp.set_debuglevel(2)
        self.ftp.set_pasv(True)

    def connect(self):
        try:
            self.ftp.connect(host=self.ip, port=990, timeout=10, source_address=None)
            self.ftp.login('bblp', self.pw)
            self.ftp.prot_p()
            self.connected = True
        except:
            return False

    def upload(self, filename, file):
        self.ftp.storbinary(f'STOR {filename}', file)

    def disconnect(self):
        try:
            self.ftp.quit()
            self.connected = False
        except:
            return False