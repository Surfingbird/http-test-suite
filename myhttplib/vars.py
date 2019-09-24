DEFAULT_FILE = 'index.html'

CONFIG_PATH = '/etc/httpd.conf'

CHUNCK_SIZE = 1024

cpu_limit_field = 'cpu_limit'
document_root_field = 'document_root'

class Congif():
    def __init__(self):
        with open(CONFIG_PATH, 'rb') as file:
            contents = file.read().decode('UTF-8')
            lines = contents.split('\n')
            data = {}
            for line in lines:
                if line:
                    key, value = line.split(' ')
                    data[key] = value
            self.data = data
    def build(self):
        self._ROOT_DIR = self.data[document_root_field]
        self._CPU_LIMIT = self.data[cpu_limit_field]

    @property
    def ROOT_DIR(self):
        return self._ROOT_DIR

    @property
    def CPU_LIMIT(self):
        return self._CPU_LIMIT

config = Congif()
config.build()
