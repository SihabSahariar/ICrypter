def encrypt(text):
    new_text = ""
    for i in text:
        if i == 'a':new_text+='p'
        elif i == 'b':new_text+='q'
        elif i == 'c':new_text+='r'
        elif i == 'd':new_text+='s'
        elif i == 'e':new_text+='t'
        elif i == 'f':new_text+='u'
        elif i == 'g':new_text+='v'
        elif i == 'h':new_text+='w'
        elif i == 'i':new_text+='x'
        elif i == 'j':new_text+='y'
        elif i == 'k':new_text+='z'
        elif i == 'l':new_text+='a'
        elif i == 'm':new_text+='b'
        elif i == 'n':new_text+='c'
        elif i == 'o':new_text+='d'
        elif i == 'p':new_text+='e'
        elif i == 'q':new_text+='f'
        elif i == 'r':new_text+='g'
        elif i == 's':new_text+='h'
        elif i == 't':new_text+='i'
        elif i == 'u':new_text+='j'
        elif i == 'v':new_text+='k'
        elif i == 'w':new_text+='l'
        elif i == 'x':new_text+='m'
        elif i == 'y':new_text+='n'
        elif i == 'z':new_text+='o'

        elif i == 'A':new_text+='Q'
        elif i == 'B':new_text+='R'
        elif i == 'D':new_text+='S'
        elif i == 'C':new_text+='T'
        elif i == 'E':new_text+='U'
        elif i == 'F':new_text+='V'
        elif i == 'G':new_text+='W'
        elif i == 'H':new_text+='X'
        elif i == 'I':new_text+='Y'
        elif i == 'J':new_text+='Z'
        elif i == 'K':new_text+='A'
        elif i == 'L':new_text+='B'
        elif i == 'M':new_text+='C'
        elif i == 'N':new_text+='D'
        elif i == 'O':new_text+='E'
        elif i == 'P':new_text+='F'
        elif i == 'Q':new_text+='G'
        elif i == 'R':new_text+='H'
        elif i == 'S':new_text+='I'
        elif i == 'T':new_text+='J'
        elif i == 'U':new_text+='K'
        elif i == 'V':new_text+='L'
        elif i == 'W':new_text+='M'
        elif i == 'X':new_text+='N'
        elif i == 'Y':new_text+='O'
        elif i == 'Z':new_text+='P'
        else: new_text+=i
    return new_text


def decrypt(text):
    new_text = ""
    for i in text:
        if i == 'p':new_text+='a'
        elif i == 'q':new_text+='b'
        elif i == 'r':new_text+='c'
        elif i == 's':new_text+='d'
        elif i == 't':new_text+='e'
        elif i == 'u':new_text+='f'
        elif i == 'v':new_text+='g'
        elif i == 'w':new_text+='h'
        elif i == 'x':new_text+='i'
        elif i == 'y':new_text+='j'
        elif i == 'z':new_text+='k'
        elif i == 'a':new_text+='l'
        elif i == 'b':new_text+='m'
        elif i == 'c':new_text+='n'
        elif i == 'd':new_text+='o'
        elif i == 'e':new_text+='p'
        elif i == 'f':new_text+='q'
        elif i == 'g':new_text+='r'
        elif i == 'h':new_text+='s'
        elif i == 'i':new_text+='t'
        elif i == 'j':new_text+='u'
        elif i == 'k':new_text+='v'
        elif i == 'l':new_text+='w'
        elif i == 'm':new_text+='x'
        elif i == 'n':new_text+='y'
        elif i == 'o':new_text+='z'

        elif i == 'Q':new_text+='A'
        elif i == 'R':new_text+='B'
        elif i == 'S':new_text+='C'
        elif i == 'T':new_text+='D'
        elif i == 'U':new_text+='E'
        elif i == 'V':new_text+='F'
        elif i == 'W':new_text+='G'
        elif i == 'X':new_text+='H'
        elif i == 'Y':new_text+='I'
        elif i == 'Z':new_text+='J'
        elif i == 'A':new_text+='K'
        elif i == 'B':new_text+='L'
        elif i == 'C':new_text+='M'
        elif i == 'D':new_text+='N'
        elif i == 'E':new_text+='O'
        elif i == 'F':new_text+='P'
        elif i == 'G':new_text+='Q'
        elif i == 'H':new_text+='R'
        elif i == 'I':new_text+='S'
        elif i == 'J':new_text+='T'
        elif i == 'K':new_text+='U'
        elif i == 'L':new_text+='V'
        elif i == 'M':new_text+='W'
        elif i == 'N':new_text+='X'
        elif i == 'O':new_text+='Y'
        elif i == 'P':new_text+='Z'
        else: new_text+=i
    return new_text