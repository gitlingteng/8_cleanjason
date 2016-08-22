# -*- coding: utf-8 -*-
from urllib.request import urlopen
import json

class Parsefile(object):
    #read in from urlsite,use decode('utf-8') to tell special charaters
    file=open('messydata.json',encoding='utf-8')
    def readinput(self):
        return self.file.read(1024)
    #Parse file using JSONDecoder
    def parse_by_chunk(self):
        decoder = json.JSONDecoder(strict=False)
        buffer = ''
        for chunk in iter(self.readinput, ''):
            buffer += chunk
            while buffer:
                try:
                    result, index = decoder.raw_decode(buffer)
                    yield result
                    buffer = buffer[index:]
                #catch error
                except ValueError as e:
                    print("??",e)
                    #Read more
                    break

def main():
    imputd=Parsefile().parse_by_chunk()
    #write JSON object to file in neat style
    output = open('neatdata.json', 'w', encoding='utf8')
    n=0
    for objs in imputd:
        if n>0:
            output.write("\n")
        output.write(json.dumps(objs,indent = 4,ensure_ascii=False))
        n=n+1
main()
