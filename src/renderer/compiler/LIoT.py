from sys import * 
import sys
import serial
import time
from rply import LexerGenerator
from parser import Parser

#ser = serial.Serial('/dev/cu.usbmodem1411', 9600)

tokens = []
port = argv[2]
def get_lines(filename):
    data = open(filename, 'r').readlines()
    return data
def open_file(filename):
    data = open(filename, "r").readlines()
    return data
class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # PrintToLCD
        self.lexer.add('PRINTTOLCD', r'printtolcd')
        # Sleep
        self.lexer.add('SLEEP', r'sleep')
        # Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        # Semi Colon
        self.lexer.add('SEMI_COLON', r'\;')
        # Strings
        self.lexer.add("STRING", r'"[^"]*"')
        # Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        # Number
        self.lexer.add('NUMBER', r'\d+')
        # letters
        self.lexer.add('VARNAME', r'\$[^\)^\s]*')
        # Ignore spaces
        self.lexer.ignore('\s+')
        # Ignore br
        self.lexer.ignore('\n')
        # Ignore comments
        self.lexer.ignore('^//\w*')
        # Ignore empty line
        self.lexer.ignore('(^(\r\n|\n|\r)$)|(^(\r\n|\n|\r))|^\s*$')
        # OUTPUT
        self.lexer.add('OUTPUT', r'output')
        # Pinon
        self.lexer.add('PINON', r'pinon')  
        # Pinoff
        self.lexer.add('PINOFF', r'pinoff')  
        # Variable
        self.lexer.add('VAR', r'var')
        # IF
        self.lexer.add('IF', r'if')
        # ENDIF
        self.lexer.add('ENDIF', r'endif')
        # THEN
        self.lexer.add('THEN', r'then')
        # Variable
        #self.lexer.add('GETVAR', r'\$[^\)]*')
        # Equals
        self.lexer.add('EQUAL', r'\=')          
    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()



def run():
    sys.tracebacklimit = 0
    time.sleep(1)
    try:
        data = open_file(argv[1])
    except:
        raise Exception("Bitte oeffne eine Datei!")
    lexer = Lexer().get_lexer()
    lines = len(get_lines(argv[1]))
    script = open(argv[1])
    i = 0
    
    for line in script:
        line = line.strip()
        if not line: 
            i+=1  # line is blank
            continue
        else:
            tokens = lexer.lex(data[i])
            pg = Parser()
            pg.parse()
            parser = pg.get_parser()
            parser.parse(tokens).eval()
            time.sleep(0.01)
            i+=1
run()
print("\nDone!")
