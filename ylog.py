import os, inspect
import logging
import logging.handlers
import pandas as pd


# formatter & file logging
FORMAT = "[%(levelname)-8s][%(filename)s:#%(lineno)4s] %(funcName)s() > %(message)s"
logging.basicConfig(level=logging.DEBUG,
                    format=FORMAT,
                    datefmt='%m-%d %H:%M',
                    filename='log.log',
                    filemode='w')
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter(FORMAT)
console.setFormatter(formatter)
__logger = logging.getLogger('')
__logger.addHandler(console)

d = logging.debug
i = logging.info
w = logging.warning
e = logging.error
c = logging.critical



def k(value):
    caller = inspect.getframeinfo(inspect.stack()[1][0])
    levelname = 'DEBUG'
    filename = os.path.basename(caller.filename)
    lineno = caller.lineno
    funcName = caller.function
    message = f'{type(value)} - {value}'
    print(f'[{levelname:8}][{filename}:#{lineno:4}] {funcName}() > {message}')

def p(message):
    caller = inspect.getframeinfo(inspect.stack()[1][0])
    levelname = 'DEBUG'
    filename = os.path.basename(caller.filename)
    lineno = caller.lineno
    funcName = caller.function
    print(f'[{levelname:8}][{filename}:#{lineno:4}] {funcName}() > ...')
    print(message)

# class log:

#     __logger = logging.getLogger('')
#     tag = ''

#     @classmethod
#     def tag_by_main_script(cls, script_file):
#         cls.tag = os.path.splitext(os.path.basename(script_file))[0]
    
#     my_format = '[{levelname:8}][{filename}:#{lineno:4}] {funcName}() > {message}'

#     @classmethod
#     def k(cls, value):
#         caller = inspect.getframeinfo(inspect.stack()[1][0])
#         levelname = 'DEBUG'
#         filename = os.path.basename(caller.filename)
#         lineno = caller.lineno
#         funcName = caller.function
#         # FORMAT = "[%(levelname)-8s][%(filename)s:#%(lineno)4s] %(funcName)s() > %(message)s"
#         message = f'{type(value)} - {value}'
#         print(f'[{levelname:8}][{filename}:#{lineno:4}] {funcName}() > {message}')

#     @classmethod
#     def d(cls, message):
#         cls.__logger.debug(f'[{cls.tag}] {message}')

#     @classmethod
#     def i(cls, message):
#         # caller = inspect.getframeinfo(inspect.stack()[1][0])
#         # levelname = 'DEBUG'
#         # filename = os.path.basename(caller.filename)
#         # lineno = caller.lineno
#         # funcName = caller.function
#         cls.__logger.info('[' + cls.tag + '] ' + message)

#     @classmethod
#     def w(cls, message):
#         cls.__logger.warning('[' + cls.tag + '] ' + message)

#     @classmethod
#     def e(cls, message):
#         cls__logger.error('[' + cls.tag + '] ' + message)

#     @classmethod
#     def c(cls, message):
#         cls.__logger.critical('[' + cls.tag + '] ' + message)
