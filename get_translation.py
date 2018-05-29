# -*- coding:ascii -*-
import codecs
import sys

from googletrans import Translator


def main():
    _, input_file = sys.argv
    translator = Translator()

    with open(input_file, 'r') as f:
        input=f.readlines()

    out=''
    for line in translator.translate(input, dest='zh-CN'):
        out = out + line.text

    out.encode('utf8')


    filename = input_file.split('_output_')[1].split('.')[0]
    with codecs.open("translation_output_{0}.txt".format(filename), "w", encoding="utf-8") as f:
        f.write(out)
    print "Finished translating and write the translation to translation_output_{0}.txt".format(filename)

if __name__ == "__main__":
    main()
