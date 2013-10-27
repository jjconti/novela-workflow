def getContentInALine(fileName):
    if fileName.startswith('!') or fileName.startswith('foto_'):
        return ''
    fileName = fileName.strip('?#')
    fileContent = open(fileName + '.txt', 'r').readlines()
    for line in fileContent:
        if not line.startswith('\\') and len(line) > 1:
            words = countWords(fileContent)
            return words + (4 - len(words)) * ' ' + line

def countWords(content):
    words = []
    for line in content:
        if not line.startswith('\\') and line:
            words += line.split()
    return str(len(words))

content = ''
for line in open('xolopes.index').readlines():
    f = line.split()[0]
    firstLine = getContentInALine(f)
    content += f + (20 - len(f)) * ' ' + (firstLine if firstLine else '\n')

final = open('xolopes.index', 'w+')
final.write(content)
