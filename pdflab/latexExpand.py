import sys
def expandCommand(inText,cmdName,appendSuffix):
    """
    takes a text and returns (recurvsively) all of the latex code involved)
    """
    spLines = inText.split('\\'+cmdName+'{')
    if(len(spLines)>1):
        restArgs = map(lambda s: s.partition('}'),spLines[1:])
        completeFile = [expandLatex(fName+appendSuffix)+' '+fLines for (fName,junk,fLines) in restArgs]
        return ' '.join([spLines[0]]+completeFile)
    else:
        return inText

def expandLatex(inFileName,debug=False):
    """
    takes a file and returns (recurvsively) all of the latex code involved)
    """
    if (debug): print 'Parsing latex file:'+inFileName
    fullFile = open(inFileName,'r').readlines()
    allText=''.join(fullFile)
    allText=expandCommand(allText,'input', '')
    allText=expandCommand(allText,'include','')
    return allText

def expandLatexFile(inFile,outFile):
    exText = expandLatex(inFile,True)
    out=open(outFile,'w')
    out.write(exText)
    out.flush()
    out.close()

if __name__ == "__main__":
    latexFile=sys.argv[1]
    if(len(sys.argv)>2):
        outFile=sys.argv[2]
        expandLatexFile(latexFile,outFile)
    else:
        print expandLatex(latexFile)
