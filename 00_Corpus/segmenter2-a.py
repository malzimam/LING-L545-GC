import sys

line = sys.stdin.readline()
while line != '':
    for token in line.split (' '):
        if token.strip() == '':
            continue
        elif token[-1] in '؟!':
            sys.stdout.write(token + '\n')
        elif token[-1] in '،':
            sys.stdout.write(token + '\n')
        elif token[-1] == '.':
            if token in ['ق.م.','ق.م','ج.ه','ف.م','أ.م','ك.س','ك.ش','و.ف','ض.ج','س.ب','ف.س','ن.س.ب.','ر.ب','ر.ج','ب.ج.','د.ب.','ت.ج.م.','أ.','د.','م.','غ.','ة.','ف.','ب.','ن.','ض.ج.','س.ب.','ف.س.','ك.س.','ك.ش.']:
                sys.stdout.write(token + ' ')
            else:
                sys.stdout.write(token + '\n')
        else:
            sys.stdout.write(token + ' ')
    line = sys . stdin . readline ()
