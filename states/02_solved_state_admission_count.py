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

# TASK: Print out the admission year and the admission count when admission count was greater than one 

"""
    step 1 -> extract the admission years from admissions dictionary
    
    step 2 -> create a dictionary of key,value pairs where key is year and value is year count
    
    step 3 -> sort the resulting dict by count > 1

"""
admission_years = [year for _,year in admissions.items()]
print(reprlib.repr(admission_years)) # [1819, 1959, 1912, 1836, 1850, 1876, ...]

admission_count_dict = {year: admission_years.count(year) for year in admission_years }
print(reprlib.repr(admission_count_dict)) # {1787: 3, 1788: 8, 1789: 1, 1790: 1, ...}

final_count_dict = {k:v for k,v in sorted(admission_count_dict.items(), key= lambda x: x[1], reverse = True) if v > 1 }
print(final_count_dict) # {1788: 8, 1889: 4, 1787: 3, 1959: 2, 1912: 2, 1845: 2, 1890: 2, 1864: 2}
