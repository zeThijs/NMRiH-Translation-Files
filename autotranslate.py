
# Requires python 3.5+, and translate library:
#       https://pypi.org/project/translate/
#       pip install translate

# Uncle Tio's nice chart for language codes:
# https://github.com/Uncle-Tio/nmrih-maps-translation-files#language-code-table-and-status
# Note: You can see the full list of language codes at addons/sourcemod/configs/languages.cfg
# if you are getting translation rate limited, change ip and continue

import sys
from translate import Translator
from pyparsing import *
import argparse
import os
print("Using python version:" + sys.version)
print("------------------------------------------------------------------------")
print("     ZeThijs sm-map-translator autotranslate")
print("     Uses MyMemory api to dump translations\n")
print("     Input example: -f path/nmo_mansion_v1.txt OR -p <dirtotranslate>")
print("     For more information: ")
print("         https://github.com/dysphie/sm-map-translator")
print("         https://github.com/zeThijs/NMRiH-Translation-Files.git")
print("------------------------------------------------------------------------")


lcodes = ["en", "ar", "pt", "bg", "cze", "da", "nl", "fi", "fr", "de", "el", "he", "hu", "it", "jp", "ko", "ko", "lv", "lt", "no", "pl", "pt_p", "ro", "ru", "chi", "sk", "es", "sv", "th", "tr", "ua", "vi"]

#some codes are different in sourcemod than international langcodes apparently ¯\_(ツ)_/¯
langcode_fix = {
"ua"    : "uk",
"jp"    : "ja",
"pt_p"  : "pt"
# "zho"   : "zh" #redundant
}



parser = argparse.ArgumentParser(prog='sm-map-translator autotranslate',
                usage='%(prog)s -f <map_translation_file> OR -p <directory to translate> (recommended) -mail <yourmail]',
                description='Uses MyMemory to dump translations with unknown acuracy to sm-map-translator files')
parser.add_argument('-file',    type=str,           help='sm-map-translator file to translate')
parser.add_argument('-path',    type=str,           help='directory containing txts to translate')
parser.add_argument('-mail',    type=str,           help='Providing a valid email to MyMemory increases your daily translation limit')
args = parser.parse_args()


if args.file is not None:
    if not os.path.exists(args.file): 
        print("-f given map_translation_file does not exist. ")
        sys.exit(1)
    else:
        print("Translating:" + args.file)        
elif args.path is not None:
    if not os.path.exists(args.path): 
        print("-p directory does not exist.")
        sys.exit(1)
    else:
        print("Translating:" + args.path)
else:
    print("No valid file or directoy given, exiting..")
    



translators={}
def init_translators():
    #initialize translators
    for lcode in lcodes:
        #fix broken langcodes
        if lcode in langcode_fix:
            lcode = langcode_fix[lcode]
        
        if args.mail is not None:
            translators[lcode] = Translator(to_lang=lcode, email=args.mail)
        else: 
            translators[lcode] = Translator(to_lang=lcode)

# teststring = "banana is good"

def translate_element(lcode, message):
    #fix broken langcodes
    if lcode in langcode_fix:
        lcode = langcode_fix[lcode]

    translation = translators[lcode].translate(message)
    if (translation == "" or translation == None):
       return message   #no translation, return original string
    else:
        return translation
    

def translate_file(file):
    print("Attempting translation of: " + file)
    filename = file

    LBRACE, RBRACE = map(Suppress, '{}')
    key = dblQuotedString | Word(printables, excludeChars='{}/')
    value = Forward()
    node = Group(key + value)
    dblQuotedString.setParseAction(removeQuotes)
    section = Group(LBRACE + ZeroOrMore(node) + RBRACE)
    value << (key | section)
    results = OneOrMore(node).parseFile(filename).asList()

    failures = 0

    # There this is terrible, and i will make a better keyvalue parser, next time. For this script, this works i gues lol
    for entry in results:
        if isinstance(entry, list):
            for entry1 in entry:
                if isinstance(entry1, list):
                    for entry2 in entry1:
                        if isinstance(entry2, list):
                            for entry3 in entry2:
                                if isinstance(entry3, list):
                                    for entry4 in entry3:
                                        try:
                                            # if '/' in entry4[1]:#some objectives use / for two languages. This confuses the translator
                                            #     entry4[1] = translate_element(entry4[0], entry4[1].split("/")[-1])
                                            # else:
                                            entry4[1] =  translate_element(entry4[0], entry4[1])

                                            if entry4[1].find("WARNING") != -1:
                                                print("----Error detected in remote translator!----") 
                                                print("\n Error message from remote:")
                                                print(entry4[1] + "\n")
                                                
                                                if entry4[1].find("FREE") != -1:
                                                    print("You were probably ratelimited, try changing your ip.")
                                                    
                                                print("Exiting.. (try again)")
                                                sys.exit(1)

                                        except Exception as exception:
                                            print("An error occuring while translating a message, skipping..")
                                            failures += 1
                                            
                                else:
                                    print("Translating message id: " + entry3)
            
    f = open(filename, "w", encoding="utf-8")

    f.write("Phrases\n{")
    for entry in results:
        if isinstance(entry, list):
            for entry1 in entry:
                if isinstance(entry1, list):
                    for entry2 in entry1:
                        if isinstance(entry2, list):
                            for entry3 in entry2:
                                if isinstance(entry3, list):
                                    for entry4 in entry3:
                                        f.write("\t\t\"" + entry4[0] + "\"\t\t\"" + entry4[1] + "\"\n")
                                    f.write("\t}")
                                else:
                                    f.write("\n\t\"" + entry3 + "\""+"\n\t{\n")
    f.write("\n}")
    f.close()

    print("Finished translating: " + filename)
    if (failures>0):
        print("Failed to translate: " + str(failures) + " messages.")
    print("--------------------------------------------------------\n\n")
    
    
def translate_folder(folderpath):
    with os.scandir(folderpath) as it:
        for entry in it:
            if entry.name.endswith(".txt") and entry.is_file():
                translate_file(entry.path)


#main
init_translators()

if args.file is not None:
    translate_file(args.file)
elif args.path is not None:
    translate_folder(args.path)