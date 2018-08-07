from rply import ParserGenerator
from ast import Number, Sum, Sub, Print, Sleep, String, Output, PinOn, PinOff,setVar,getVar,Letter, Empty, Loop, IfStatement

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'PRINTTOLCD', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SEMI_COLON', 'SUM', 'SUB', 'STRING', 'SLEEP', 'OUTPUT', 'PINON', 'PINOFF', 'EQUAL', 'VAR','VARNAME','GETVAR','IF','ENDIF','THEN','EQUAL']
        )

    def parse(self):
        
        @self.pg.production('program : PRINTTOLCD OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def program(p):
            return Print(p[2])
        @self.pg.production('program : SLEEP OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def sleep(p):
            return Sleep(p[2])
        @self.pg.production('program : OUTPUT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def output(p):
            return Output(p[2])
        @self.pg.production('program : PINON OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def pinon(p):
            return PinOn(p[2])
        @self.pg.production('program : PINOFF OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def pinoff(p):
            return PinOff(p[2])
        @self.pg.production('program : VAR expression EQUAL expression SEMI_COLON')
        def var(p):
            return setVar(p[1],p[3])
        @self.pg.production('program : IF expression EQUAL expression THEN program ENDIF')
        def ifstatement(p):
            return IfStatement(p[1],p[3],p[5])
        
        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return Sum(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)
        
        @self.pg.production('expression : STRING')
        def string(p):
            return String(p[0].value)
        @self.pg.production('expression : VARNAME')
        def varname(p):
            s = p[0].value
            return Letter(s)
        # @self.pg.production('expression : GETVAR')
        # def getvar(p):
        #     s = p[0].value
        #     return getVar(s)

        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(p[0].value)
        
        @self.pg.error
        def error_handle(token):
            raise ValueError("Ran into a %s where it wasn't expected" + token.gettokentype)

        
    def get_parser(self):
        return self.pg.build()