def getContentInALine(fileName):
    if fileName.startswith('foto_'):
        return 'F' * 100
    fileContent = open(fileName + '.txt', 'r').readlines()
    words = countWords(fileContent)
    return (words / 9) * '+'

def countWords(content):
    words = []
    for line in content:
        if not line.startswith('\\h') and line:
            words += line.split()
    return len(words)

content = ''
for line in open('xolopes.index').readlines():
    f = line.split()[0]
    if f.startswith('#') or f.startswith('!') or f.endswith('?'):
        continue
    line = getContentInALine(f)
    content += line + '\n'

final = open('xolopesGraph.txt', 'w+')
final.write(content)
