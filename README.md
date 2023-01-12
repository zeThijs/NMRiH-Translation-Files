# [NMRiH] Translation files for use with sm-map-translator.
https://github.com/dysphie/sm-map-translator


### Automatic MyMemory Translations dump :shipit:

Some translations may be a bit inaccurate.
Took a while to make, with over a million characters translated
Please feel free to leave improvements, additions with a pull request or message.

I'm curious how accurate the translations are in general, leave a message ! ( I don't speak most of the translated languages )


### Translation files Usage:

Make sure to have @Dysphie 's map translator installed. 
Copy The translation files from translated to the sourcemod/translations/_maps.


### autotranslate.py info:
A python cli script that will automatically translate translation files you feed it, based on language codes. 
Uses MyMemory to dump translations with unknown accuracy') 
You can use it to add your map's translations


**Script Usage:**

- Open a command line interface (cmd.exe, terminal, etc)
- Execute python autotranslate.py -f <map_translation_file> OR -p <directory to translate>
- [optional parameter] -mail <yourmail>

A map translation file can be acquired using sm-map-translator (https://github.com/dysphie/sm-map-translator#usage)
It is recommended to supply a mail address, as the MyMemory's daily allowed characters is pretty low without one 

<pre>
 Script Requires python 3.5+, and the translate library:
       https://pypi.org/project/translate/
       pip install translate
</pre>
