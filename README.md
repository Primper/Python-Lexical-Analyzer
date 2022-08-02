# Python Lexical Analyzer
This Python program is a lexical analyzer of a custom programming language.
The program interface is implemented through PyQT.

How the program works:
The user enters a program code into the input field of the interface. After clicking on the "Start analysis" button, the entire contents of the line is transferred to the "tempo" txt file. The program takes data from a file and processes it by performing lexical analysis.

###The Backus-Naur formulas are listed below:

+ <character>::= A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z
+ <number>::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
+ <integer>::= <binary> | <octal> | <decimal> | <hexadecimal>
+ <binary>::= {/ 0 | 1 /} (B | b)
+ <octal>::= {/ 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 /} (O | o)
+ <decimal>::= {/ <number> /} [D | d]
+ <hexadecimal>::= <number> {<number> | A | B | C | D | E | F | a | b | c | d | e | f} (H | h)
+ <real>::= <numeric_string> <index> | [<numeric_string>] . <numeric_string> [index]
+ <numeric_string>::= {/ <number> /}
+ <index>::= ( E | e ) [ + | - ] <numeric_string>
+ <program>::= «{» {/ (<description> | <operator>) ; /} «}»
+ <description>::= {<identifier> {, <identifier> } : <type> ;}
+ <type>::= % | ! | $
+ <compound>::= begin <operator> { ; <operator> } end
+ <assignment>::= <identifier> := <expression>
+ <conditional>::= if  «(»<expression> «)» <operator> [else <operator>]
+ <fixed_cycle>::= for <assignment>  to <expression> [step <expression>] <operator> next
+ <conditional_loop>::= while «(»<expression> «)» <operator>
+ <input>::= readln identifier {, <identifier> }
+ <output>::= writeln <expression> {, <expression> }
+ <comment_start>::= «/*»
+ <comment_end>::= «*/»
+ <relation_group_operations>::= NE | EQ | LT | LE | GT | GE
+ <addition_group_operations>:: = plus | min | or
+ <multiplication_group_operations>::= mult | div | and
+ <unary_operation>::= ~
+ <expression>::= <operand> {<relation_group_operations> <operand>}
+ <operand>::= <term> {<addition_group_operations> <term>}
+ <term>::= <multiplier> {<multiplication_group_operations> <multiplier>}
+ <multiplier>::= <identifier> | <number> | <boolean_constant> | <unary_operation>  <multiplier> | «(»<expression>«)»
+ <number>::= <integer> | <real>
+ <boolean_constant>::= true | false
+ <identifier>::= <character> {<character> | <number>}
