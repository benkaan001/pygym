# from states_data import populations, capitals

# import reprlib module to limit print output
import reprlib

# TASK print out the capitals of the most populous 3 states


populations = {'al':4833722, 'ak':735132, 'az':6626624, 'ar':2959373, 'ca':38332521,
         'co':5268367, 'ct':3596080, 'de':925749, 'fl':19552860, 'ga':9992167,
         'hi':1404054, 'id':1612136, 'il':12882135, 'in':6570902, 'ia':3090416,
         'ks':2893957, 'ky':4395295, 'la':4625470, 'me':1328302, 'md':5928814,
         'ma':6692824, 'mi':9895622, 'mn':5420380, 'ms':2991207, 'mo':6021988,
         'mt':1015165, 'ne':1868516, 'nv':2790136, 'nh':1323459, 'nj':8899339,
         'nm':2085287, 'ny':19651127, 'nc':9848060, 'nd':723393, 'oh':11570808,
         'ok':3850568, 'or':3930065, 'pa':12773801, 'ri':1051511, 'sc':4774839,
         'sd':844877, 'tn':6495978, 'tx':26448193, 'ut':2900872, 'vt':626630,
         'va':8260405, 'wa':6971406, 'wv':1854304, 'wi':5742713, 'wy':582658}

capitals = {'al':'Montgomery', 'ak':'Juneau', 'az':'Phoenix',
           'ar':'Little Rock', 'ca':'Sacramento', 'co':'Denver',
           'ct':'Hartford', 'de':'Dover', 'fl':'Tallahassee', 'ga':'Atlanta',
           'hi':'Honolulu', 'id':'Boise', 'il':'Springfield',
           'in':'Indianapolis', 'ia':'Des Moines', 'ks':'Topeka',
           'ky':'Frankfort', 'la':'Baton Rouge', 'me':'Augusta',
           'md':'Annapolis', 'ma':'Boston', 'mi':'Lansing', 'mn':'St. Paul',
           'ms':'Jackson', 'mo':'Jefferson City', 'mt':'Helena',
           'ne':'Lincoln', 'nv':'Carson City', 'nh':'Concord', 'nj':'Trenton',
           'nm':'Santa Fe', 'ny':'Albany', 'nc':'Raleigh', 'nd':'Bismarck',
           'oh':'Columbus', 'ok':'Oklahoma City', 'or':'Salem',
           'pa':'Harrisburg', 'ri':'Providence', 'sc':'Columbia',
           'sd':'Pierre', 'tn':'Nashville', 'tx':'Austin',
           'ut':'Salt Lake City', 'vt':'Montpelier', 'va':'Richmond',
           'wa':'Olympia', 'wv':'Charleston', 'wi':'Madison', 'wy':'Cheyenne'}

# sample print
print(reprlib.repr(capitals)) 
# {'ak': 'Juneau', 'al': 'Montgomery', 'ar': 'Little Rock', 'az': 'Phoenix', ...}

