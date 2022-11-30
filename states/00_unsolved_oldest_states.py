# from states_data import state_list,abbreviations, populations, capitals, admissions


# import reprlib module to limit print output
import reprlib

admissions = {'al':1819, 'ak':1959, 'az':1912, 'ar':1836, 'ca':1850, 
         'co':1876, 'ct':1788, 'de':1787, 'fl':1845, 'ga':1788, 'hi':1959, 
         'id':1890, 'il':1818, 'in':1816, 'ia':1846, 'ks':1861, 'ky':1792, 
         'la':1812, 'me':1820, 'md':1788, 'ma':1788, 'mi':1837, 'mn':1858, 
         'ms':1817, 'mo':1821, 'mt':1889, 'ne':1864, 'nv':1864, 'nh':1788, 
         'nj':1787, 'nm':1912, 'ny':1788, 'nc':1789, 'nd':1889, 'oh':1803, 
         'ok':1907, 'or':1859, 'pa':1787, 'ri':1790, 'sc':1788, 'sd':1889, 
         'tn':1796, 'tx':1845, 'ut':1896, 'vt':1791, 'va':1788, 'wa':1889, 
         'wv':1863, 'wi':1848, 'wy':1890}


abbreviations = {'Alabama':'al', 'Alaska':'ak', 'Arizona':'az', 'Arkansas':'ar',
         'California':'ca', 'Colorado':'co', 'Connecticut':'ct', 
         'Delaware':'de', 'Florida':'fl', 'Georgia':'ga', 'Hawaii':'hi', 
         'Idaho':'id', 'Illinois':'il', 'Indiana':'in', 'Iowa':'ia', 
         'Kansas':'ks', 'Kentucky':'ky', 'Louisiana':'la', 'Maine':'me', 
         'Maryland':'md', 'Massachusetts':'ma', 'Michigan':'mi', 
         'Minnesota':'mn', 'Mississippi':'ms', 'Missouri':'mo',
         'Montana':'mt', 'Nebraska':'ne', 'Nevada':'nv', 'New Hampshire':'nh', 
         'New Jersey':'nj', 'New Mexico':'nm', 'New York':'ny', 
         'North Carolina':'nc', 'North Dakota':'nd', 'Ohio':'oh',
         'Oklahoma':'ok', 'Oregon':'or', 'Pennsylvania':'pa', 
         'Rhode Island':'ri', 'South Carolina':'sc', 'South Dakota':'sd',
         'Tennessee':'tn', 'Texas':'tx', 'Utah':'ut', 'Vermont':'vt', 
         'Virginia':'va', 'Washington':'wa', 'West Virginia':'wv', 
         'Wisconsin':'wi', 'Wyoming':'wy'}

# TASK: Print out the full name of the oldest state(s)

# sample print
print(reprlib.repr(admissions)) # {'ak': 1959, 'al': 1819, 'ar': 1836, 'az': 1912, ...}