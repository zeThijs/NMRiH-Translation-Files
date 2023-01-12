# [NMRiH] NMRiH Diffmoder fork     
**Translation files for use with sm-map-translator.**
https://github.com/dysphie/sm-map-translator

**This is a dump of translations, automagically retrieved using MyMemory API. Some translations may be a bit inaccurate.**
Took a while to make, with over a million characters translated
Please feel free to leave improvements, additions with a pull request or message.
I'm curious how accurate the translations are in general, leave a message ! ( I don't speak most of the translated languages )

**Translation files Usage:**
Make sure to have Dysphie's map translator installed. 
Copy The translation files from translated to the sourcemod/translations/_maps.

**autotranslate.py info:**
A python cli script that will automatically translate translation files you feed it, based on language codes. 
Uses MyMemory to dump translations with unknown accuracy') 
You can use it to add your map's translations

**Script Usage:**
Open a command line interface (cmd.exe, terminal, etc)
Execute python autotranslate.py -f <map_translation_file> OR -p <directory to translate>]'
A map translation file can be acquired using sm-map-translator (https://github.com/dysphie/sm-map-translator#usage)
It is recommended to supply a mail address with -mail <yourmail>,
as the MyMemory's maximum daily characters is pretty low without one 

 Requires python 3.5+, and translate library:
       https://pypi.org/project/translate/
       pip install translate
