Readme!
1.	Individual work
2.	Work is done with python 3
3.	Instruction on running projects:

For two python files (BMC.py & DPLL.py):
1)	Run them in terminal;
2)	The program will first ask the user how many sentences should be read as knowledge base, please type a number;
3)	Follow the instruction showed on screen and type knowledge base (one sentence per line);
4)	The screen will then show a sentence to ask user to type sentences which should be checked. One sentence per line and the program will give the answer immediately. When the check is done, please type ¡°END¡±.

Input format:
Since program is sensitive to the format of the input, here is the input for four questions.

Basic model checking:
Q1:
2
P
( P => Q )

Q
END

Q2: 
5
( ! P11 )
( B11 <=> ( P12 | P21 ) )
( B21 <=> ( P11 | P22 | P31 ) )
( ! B11 )
B21

P12
END

Q3: 
4
( MY => IM )
( ( ! MY ) => ( ( ! IM ) & MA ) )
( ( IM | MA ) => HO )
( HO => MA )

MY
MA
HO
END

Q4:
(1)
3
( A <=> ( C & A ) )
( B <=> ( ! C ) )
( C <=> ( B | ( ! A ) ) )

A
B
C
END

(2)
3
( A <=> ( ! C ) )
( B <=> ( A & C ) )
( C <=> B )

A
B
C
END

Q5:
12
( A <=> ( H & I ) )
( B <=> ( A & L ) )
( C <=> ( B & G ) )
( D <=> ( E & L ) )
( E <=> ( C & H ) )
( F <=> ( D & I ) )
( G <=> ( ( ! E ) & ( ! J ) ) )
( H <=> ( ( ! F ) & ( ! K ) ) )
( I <=> ( ( ! G ) & ( ! K ) ) )
( J <=> ( ( ! A ) & ( ! C ) ) )
( K <=> ( ( ! D ) & ( ! F ) ) )
( L <=> ( ( ! B ) & ( ! J ) ) )

A
B
C
D
E
F
G
H
I
J
K
L
END

DPLL:
Q1:
2
P
( ( ! P ) | Q )

Q
END


Q2:
10
( ! P11 )
( ( ! B11 ) | P12 | P21 )
( ( ! P12 ) | B11 )
( ( ! P21 ) | B11 )
( ( ! B21 ) | P11 | P22 | P31 )
( ( ! P11 ) | B21 )
( ( ! P22 ) | B21 )
( ( ! P31 ) | B21 )
( ! B11 )
B21

P12
END

Q3:
6
( ( ! MY ) | IM )
( ( ! HO ) | MA )
( MY | ( ! IM ) )
( MY | MA )
( ( ! IM ) | HO )
( ( ! MA ) | HO )

MY
MA
HO
END


Q4:
(1)
6
( ( ! A ) | C )
( ( ! B ) | ( ! C ) )
( C | B )
( ( ( ! C ) | ( ! A ) ) | B )
( ( ! B ) | C )
( A | C )

A
B
C
END


(2)
7
( ( ! A ) | ( ! C ) )
( C | A )
( ( ! B ) | A )
( ( ! B ) | C )
( ( ( ! A ) | ( ! C ) ) | B )
( ( ! C ) | B )
( ( ! B ) | C )

A
B
C
END

