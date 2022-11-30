# from states_data import state_list,abbreviations, populations, capitals, admissions


# import reprlib module to limit print output
import reprlib

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

admissions = {'al':1819, 'ak':1959, 'az':1912, 'ar':1836, 'ca':1850, 
         'co':1876, 'ct':1788, 'de':1787, 'fl':1845, 'ga':1788, 'hi':1959, 
         'id':1890, 'il':1818, 'in':1816, 'ia':1846, 'ks':1861, 'ky':1792, 
         'la':1812, 'me':1820, 'md':1788, 'ma':1788, 'mi':1837, 'mn':1858, 
         'ms':1817, 'mo':1821, 'mt':1889, 'ne':1864, 'nv':1864, 'nh':1788, 
         'nj':1787, 'nm':1912, 'ny':1788, 'nc':1789, 'nd':1889, 'oh':1803, 
         'ok':1907, 'or':1859, 'pa':1787, 'ri':1790, 'sc':1788, 'sd':1889, 
         'tn':1796, 'tx':1845, 'ut':1896, 'vt':1791, 'va':1788, 'wa':1889, 
         'wv':1863, 'wi':1848, 'wy':1890}

# sample print
print(reprlib.repr(populations)) # {'ak': 735132, 'al': 4833722, 'ar': 2959373, 'az': 6626624, ...}


"""
    TASK -> Calculate the population difference between the oldest and youngest state
    
    EXPECTED OUTPUT -> 478305
            
"""

