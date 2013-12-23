import os
import sys

def getAsTexContent(fileName, i):
    if fileName.startswith('#') or fileName.startswith('!'):
        return ''
    fileName = fileName.strip('?')
    fileContent = open(fileName + '.txt', 'r').read()
    if fileName.startswith('foto_'):
        draft = "[draft]" if len(sys.argv) > 1 and sys.argv[1] == 'draft' else ""
        return "\\afterpage{\\includepdf" + draft + "{" + fileContent.strip() + "}}"
    else:
        return '''
\\hrulefill \\hspace{0.1cm}\\decofourleft\\hspace{0.2cm} ##INDEX## \\hspace{0.2cm}\\decofourright \\hspace{0.1cm}\\hrulefill

\\nopagebreak

\\vspace{0.5cm}

\\nopagebreak

##CONTENT##
\\vspace{0.5cm}
'''.replace('##CONTENT##', fileContent).replace('##INDEX##', str(i))

content = ''
i = 1
for line in open('xolopes.index').readlines():
    f = line.split()[0]
    content += getAsTexContent(f, i)
    if not f.startswith('foto_'):
        i += 1

mainTex = open('xolopesBase.tex', 'r').read()
final = open('draft.tex' if len(sys.argv) > 1 and sys.argv[1] == 'draft' else 'xolopes.tex', 'w+')
final.write(mainTex.replace('##CONTENT##', content))
