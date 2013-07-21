import os

def getAsTexContent(fileName):
    if fileName.startswith('#'):
        return ''
    fileName = fileName.strip('?')
    fileContent = open(fileName + '.txt', 'r').read()
    return '''
\\vspace{0.5cm}
\\hrulefill\\hspace{0.2cm} \\decofourleft\\decofourright \\hspace{0.2cm} \\hrulefill
\\vspace{0.5cm}

##CONTENT##
'''.replace('##CONTENT##', fileContent)

content = ''
for f in open('xolopes.index').read().splitlines():
    content += getAsTexContent(f)

mainTex = open('xolopesBase.tex', 'r').read()
final = open('xolopes.tex', 'w+')
final.write(mainTex.replace('##CONTENT##', content))
