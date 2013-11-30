# -*- coding: utf-8 -*-

S = 4
R = 3
content = '''
digraph mapa {
    nodesep="0.1";
    node [penwidth=8 fontsize=64 shape = circle];
    edge [penwidth=8]
'''
files = [x.split()[0] for x in open('xolopes.index').readlines() if not x.startswith('foto_')]
rels = {
    'todos': ['revolucion8'],
    'mozzano': ['mudarse'],
    'dudasHostel1': ['testigoJeova'],
    'noticiaRobo': ['robo'],
    'destino': ['escalas', 'narcoAvion1'],
    'narcoAvion5': ['billetera1'],
    'escalas': ['playaDelCarmen', 'cancun'],
    'girls': ['yankees'],
    'xolopes': ['timados'],
    'elixir': ['brujo0'],
    'excursiones': ['todos', 'chichenWiki', 'tulumWiki', 'villadolid', 'cenotes', 'ucraniana6', 'maya1', 'islaMujeres', 'cozumel0'],
    'saer': ['saccomanno', 'comoUnLibro', 'enLaPlaya', 'escritor', 'intro', 'señaladores', 'todos'],
    'chancho1': ['leyenda1'],
    'tulumWiki': ['israeli', 'carretera', 'turcas', 'camara'],
    'pescadorYEmpresario': ['conGaspar'],
    'animacion3': ['todos'],
    'escritor': ['todos'],
    'enLaPlaya': ['todos'],
    'ucraniana5': ['todos'],
    'hacker1': ['todos'],
    'despegue': ['todos'],
    'mochileros': ['todos'],
    'ucraniana6': ['todos'],
    'fheinz': ['todos'],
    'cozumel4': ['todos'],
    'chichen4Obsidiana': ['todos'],
    'argentino': ['todos', 'resto1'],
    'playaDelCarmen': ['todos'],
    'hanselYGretel': ['todos'],
    'animacion1': ['todos'],
    'monica2': ['todos'],
    'dudasHostel2': ['todos'],
    'mail3': ['todos'],
    'turcas': ['todos'],
    'billetera5': ['todos'],
    'conGaspar': ['robo'],
    'hackerNoticia': ['robo'],
    'brujo0': ['robo'],
    'animacion2': ['robo']
}
ffrom = None
newffrom = None
while files:
    if newffrom == ffrom:
        ffrom = files.pop(0)
    else:
        ffrom = newffrom
    for f in files:
        if f.startswith('#') or f.startswith('!') or f.endswith('?'):
            files.pop(files.index(f))
            continue
        if f[0:S] == ffrom[0:S]:
            if ffrom not in rels:
                rels[ffrom] = []
            rels[ffrom].append(f)
            newffrom = files.pop(files.index(f))
            break

files = [x.split()[0] for x in open('xolopes.index').readlines() if not x.startswith('foto_')]
numbers = {x[1]:str(x[0] + 1) for x in enumerate(files)}
for r in rels:
    content += numbers[r] + ' -> ' + '{' + " ".join([numbers[i] for i in rels[r]]) + '}\n'


content += '{rank=same;' + numbers[files.pop(0)] + ';}\n'
lastContent = '{rank=same;' + numbers[files.pop()] + ';}\n'
for chunk in [files[x:x+R] for x in xrange(0, len(files), R)]:
    content += '{rank=same;' + " ".join([numbers[i] for i in chunk]) + ';}\n'
content += lastContent
content += '\n}'
final = open('chunks.txt', 'w+')
final.write(content)
