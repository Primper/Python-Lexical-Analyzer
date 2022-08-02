from cmath import e

class LexicalAnalyzer: # Lexical analyzer class
    def __init__(self, program_filename):
        self.ch = ''  # Variable for the character being read
        self.buf = ''  # buffer variable
        self.state = ['H', 'ID', 'NUM', 'COM', 'ASGN', 'DLM', 'FIN', 'ER', 'COMM', 'ERCOM'] # State variable
        self.TW = ['begin', 'end', 'if', 'else', 'for', 'to', 'step', 'next', 'while', 'readln', 'writeln',  # Array of keywords
                    'true', 'false', 'plus', 'min', 'or', 'mult', 'div', 'and', 'NE', 'EQ', 'LT', 'LE', 'GT', 'GE'] 
        self.TD = ['(', ')', ',', ':', ':=', ';', '=', '{', '}', '[', ']', '+', '-',  # Delimiter array
                   '<', '>', '!', '&', '|', '«', '»', '$', '%', '/*', '*/', '/', '*']  
        self.TNUM = []  # Array of identifiers
        self.TID = []  # Array of constants
        self.dt = 0  # Variable required to form the numerical value of the constant
        self.current_state = 'H'  # INITIAL state
        self.program_filename = program_filename  # Program name - file path
        self.file = None  # Variable to store the file descriptor
        self.lexeme_list = []  # List of tokens
        self.status = ''

    # Method that reads a character from a file
    def get_next(self):
        self.ch = self.file.read(1)  # Reading ONE character

    # Method that clears the buffer
    def clear(self):
        self.buf = ''  # assignment to an empty string

    # Method that adds the next character to the buffer
    def add(self):
        self.buf += self.ch  # adding a new character to the buffer list

    # A method that looks up tokens in a table.
    #   Determines whether a token from the buffer is in the list of tokens with index "cls"
    #   i.e. lookup in a "specific" table
    def look(self, cls):
        if self.buf in cls:
            return cls.index(self.buf)  # return list index
            # if the buffer is found, then its index is returned
        else:
            return -1

    # Method that adds an element to the table if it does not exist
    #    and returns its index
    def put(self, cls):
        if self.buf not in cls:
            cls.append(self.buf)
        return cls.index(self.buf)

    # Method to add a number to a table if it doesn't exist
    #    and returns the index
    def putnum(self, cls):
        if self.dt not in cls:
            cls.append(self.dt)
        return cls.index(self.dt)

    # Method that adds a token to a list of tokens
    def make_lex(self, cls, num):
        self.lexeme_list.append([cls, num])

    # Method that analyzes a program into states
    def run_analysis(self):
        self.file = open(self.program_filename, 'r') # opening a file for analysis
        self.get_next()  # get next character into buffer
        while True:
            if self.current_state == 'H':  # If the current state is "H"
                if self.ch == ' ' or self.ch == '\n' or self.ch == '\t':  # and the character is: " ", "\n", "\t", then
                    self.get_next() # get the next character
                elif self.ch.isalpha():  # If the symbol is a number, then the work is either with an IDENTIFIER or with a VARIABLE
                    self.clear()
                    self.add()
                    self.get_next()
                    self.current_state = 'ID'  # pre-set as IDENTIFIER
                elif self.ch.isdigit():  # If character is a number
                    self.dt = int(self.ch)
                    self.get_next()
                    self.current_state = 'NUM'  # NUMBER identifier
                elif self.ch == '/':  # comment processing
                    self.get_next()
                    if(self.ch == '*'):
                        self.current_state = 'COM'  # COMMENT identifier
                elif self.ch == ':':  # assignment processing
                    self.get_next()
                    self.current_state = 'ASGN'  # ASSIGNMENT ID
                elif self.ch == '}':  # end of program processing
                    self.make_lex(2, 8)
                    self.current_state = 'FIN'  # end-of-program identifier
                else:
                    self.current_state = 'DLM'  # delimiter identifier
            elif self.current_state == 'ID':
                if self.ch.isalpha() or self.ch.isdigit():
                    self.add()
                    self.get_next()
                else:
                    j = self.look(self.TW)
                    if j != -1:
                        self.make_lex(1, j)
                    else:
                        j = self.put(self.TID)
                        self.make_lex(4, j)
                    self.current_state = 'H'
            elif self.current_state == 'NUM':
                if self.ch.isdigit():
                    self.dt = self.dt * 10 + int(self.ch)
                    self.get_next()
                    if self.ch == 'b':  # Transfer to binary system
                        self.ch = ''
                        a = self.dt
                        b=0
                        k = 0
                        c=0
                        for i in range (len(str(a))):
                            b=a%10
                            a=int(a/10)
                            c = c + (b*(2**k))
                            k = k+1
                        print(c)
                        self.dt = c
                        self.get_next()
                    elif self.ch == 'd':  # Convert to octal system
                        self.ch = ''
                        a = self.dt
                        b=0
                        k = 0
                        c=0
                        for i in range (len(str(a))):
                            b=a%10
                            a=int(a/10)
                            c = c + (b*(8**k))
                            k = k+1
                        print(c)
                        self.dt = c
                        self.get_next()
                    elif (self.ch == 'h'):  # Convert to hexadecimal system
                        self.ch = ''
                        a = self.dt
                        b=0
                        k = 0
                        c=0
                        for i in range (len(str(a))):
                            b=a%10
                            a=int(a/10)
                            c = c + (b*(16**k))
                            k = k+1
                        print(c)
                        self.dt = c
                        self.get_next()
                    elif (self.ch == 'e'):  # Transfer to exponent
                        self.ch = ''
                        a = self.dt
                        c=0
                        ex = 0
                        self.get_next()
                        if self.ch.isdigit():  # If character is a number
                            self.dt = int(self.ch)
                            ex = self.dt
                            c = a * (10 ** ex)
                            self.dt = c
                            self.get_next()
                else:
                    j = self.putnum(self.TNUM)
                    self.make_lex(3, j)
                    self.current_state = 'H'
            elif self.current_state == 'COM':
                while self.current_state == 'COM':
                    self.get_next()
                    if self.ch == '*':
                        self.clear()
                        self.get_next()
                        if self.ch == '/':
                            self.clear()
                            self.current_state = 'H'
                        else:
                            self.clear()
                            self.current_state = 'ERCOM'
                    if self.ch == '\n':
                        self.current_state = 'ERCOM'

            elif self.current_state == 'DLM':
                self.clear()
                self.add()
                j = self.look(self.TD)
                if j != -1:
                    self.get_next()
                    self.make_lex(2, j)
                    self.current_state = 'H'
                else:
                    if(self.current_state != 'ER'):
                        self.current_state = 'ER'
                    else:
                        self.current_state = 'ER'
            elif self.current_state == 'ASGN':
                if self.ch == '=':
                    self.make_lex(2, 4)
                else:
                    self.make_lex(2, 3)
                self.get_next()
                self.current_state = 'H'
            if self.current_state == 'FIN' or self.current_state == 'ER' or self.current_state == 'ERCOM':
                break
        # Analysis results
        if self.current_state == 'ER':
            self.status = 'LEXICAL | ERROR: Please check program for errors!'
        if self.current_state == 'ERCOM':
            self.status = 'LEXICAL | ERROR: Please check comments!'
        if self.current_state == 'FIN':
            self.status = 'LEXICAL | Analysis completed successfully!'
        self.file.close()
        return self.lexeme_list

