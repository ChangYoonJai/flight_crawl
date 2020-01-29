import logging

class ylog(logging.Logger):

    def __init__(self, name='default', level=logging.DEBUG):
        super().__init__(name, level)
        self.d = self.debug
        FORMAT =  "[%(levelname)-8s][%(filename)15s:%(lineno)-4s][%(funcName)20s()] %(message)s"
        logging.basicConfig(level=logging.DEBUG,
                            format=FORMAT,
                            datefmt='%m-%d %H:%M',
                            filename=f'{name}.log',
                            filemode='w')
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        formatter = logging.Formatter(FORMAT)
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)
    
