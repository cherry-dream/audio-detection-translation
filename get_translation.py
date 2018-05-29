# -*- coding:ascii -*-
import codecs

from googletrans import Translator


def main():
    _, input = sys.argv
    translator = Translator()
    
    with open(input, 'r') as f:
        input=f.readlines()
    
    out=''
    for line in translator.translate(input, dest='zh-CN'):
        out = out + line.text 
    
    out.encode('utf8')
    
    
    filename = input.split('.')[0]
    with codecs.open("output_{0}.txt".format(filename), "w", encoding="utf-8") as f:
    f.write(out)
    print "Finished translating and write the translation to {0}.txt".format(filename)

if __name__ == "__main__":
    main()


