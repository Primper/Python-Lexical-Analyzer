# Python Lexical Analyzer
This Python program is a lexical analyzer of a custom programming language.
The program interface is implemented through PyQT.

## How the program works:
The user enters a program code into the input field of the interface. After clicking on the "Start" button, the entire contents of the line is transferred to the "tempo" txt file. The program takes data from a file and processes it by performing lexical analysis.

### Sample input code for analysis:

`
{    
a := 9;
b := 33;
/* Comment */
c := a plus b;
}
`

### The Backus-Naur forms are listed below:

+ ___character___ ::= A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z
+ ___number___ ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
+ ___integer___ ::= ___binary___ | ___octal___ | ___decimal___ | ___hexadecimal___
+ ___binary___ ::= {/ 0 | 1 /} (B | b)
+ ___octal___ ::= {/ 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 /} (O | o)
+ ___decimal___ ::= {/ ___number___ /} [D | d]
+ ___hexadecimal___ ::= ___number___ {___number___ | A | B | C | D | E | F | a | b | c | d | e | f} (H | h)
+ ___real___ ::= ___numeric_string___ ___index___ | [___numeric_string___] . ___numeric_string___ [___index___]
+ ___numeric_string___ ::= {/ ___number___ /}
+ ___index___ ::= ( E | e ) [ + | - ] ___numeric_string___
+ ___program___ ::= «{» {/ (___description___ | ___operator___) ; /} «}»
+ ___description___ ::= {___identifier___ {, ___identifier___ } : ___type___ ;}
+ ___type___ ::= % | ! | $
+ ___compound___ ::= begin ___operator___ { ; ___operator___ } end
+ ___assignment___ ::= ___identifier___ := ___expression___
+ ___conditional___ ::= if  «(»___expression___ «)» ___operator___ [else ___operator___]
+ ___fixed_cycle___ ::= for ___assignment___  to ___expression___ [step ___expression___] ___operator___ next
+ ___conditional_loop___ ::= while «(»___expression___ «)» ___operator___
+ ___input___ ::= readln ___identifier___ {, ___identifier___ }
+ ___output___ ::= writeln ___expression___ {, ___expression___ }
+ ___comment_start___ ::= «/*»
+ ___comment_end___ ::= «*/»
+ ___relation_group_operations___ ::= NE | EQ | LT | LE | GT | GE
+ ___addition_group_operations___ :: = plus | min | or
+ ___multiplication_group_operations___ ::= mult | div | and
+ ___unary_operation___ ::= ~
+ ___expression___ ::= ___operand___ {___relation_group_operations___ ___operand___}
+ ___operand___ ::= ___term___ {___addition_group_operations___ ___term___}
+ ___term___ ::= ___multiplier___ {___multiplication_group_operations___ ___multiplier___}
+ ___multiplier___ ::= ___identifier___ | ___number___ | ___boolean_constant___ | ___unary_operation___  ___multiplier___ | «(»___expression___«)»
+ ___number___ ::= ___integer___ | ___real___
+ ___boolean_constant___ ::= true | false
+ ___identifier___ ::= ___character___ {___character___ | ___number___}
