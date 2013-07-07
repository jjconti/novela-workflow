import os

def getAsTexContent(fileName):
    fileContent = open(fileName + '.txt', 'r').read()
    return '''
\\vspace{1.5cm}
##CONTENT##
'''.replace('##CONTENT##', fileContent)

content = ''
for f in open('xolopes.index').read().splitlines():
    content += getAsTexContent(f)

mainTex = open('xolopesBase.tex', 'r').read()
final = open('xolopes.tex', 'w+')
final.write(mainTex.replace('##CONTENT##', content))
