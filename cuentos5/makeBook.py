import sys

PAPER = 'a5'

def getContent(name):
    return '\input{' + name + '.title} \input{' + name + '.txt}\n'

mainTex = open('cuentos.template', 'r').read()
data = open(sys.argv[1]).read().splitlines()
fileNameBase = data[0]
title = data[1]
content = ''
for name in data[2:]:
    if name and not name.startswith('#'):
        content += getContent(name)

final = open(fileNameBase + '.tex', 'w+')
final.write(mainTex.replace('##CONTENT##', content).replace('##TITLE##', title).replace('##PAPER##', PAPER))  
final.close()
