#!/usr/bin/env python3
import pandas
import os
import numpy as np
"""
THIS IS A TEST IN A TWO ROWS SUBSET OF THE DATAFRAME

!!!!! ÇA MARCHE :)))))))) !!!!!!!!!!

Code pour generer dictionnaire. Au prealable, avec
cat 1335.vdb.tab | cut -f 2 | cut -d ";" -f 1 | uniq
OTUConTaxonomy
"Bacteria(100)  => on a confirmé que ce sont toutes Bacteria

--
for joha: set interpreter venv: #!/home/johanna/.local/venv/bin/python3

"""
tb = pandas.read_csv("1335.vdb.tab", sep='\t', lineterminator='\r' )
minitb = tb[:3]  # subset
print(minitb.shape)

def getcountsfromrow(row):
    l_l = [ row['door_in_1'],
            row['door_in_2'],
            row['faucet_handle_1'],
            row['faucet_handle_2'],
            row['sink_floor_1'],
            row['sink_floor_2'],
            row['soap_dispenser_1'],
            row['stall_in_1'],
            row['toilet_floor_1'],
            row['toilet_floor_2'],
            row['toilet_flush_handle_1'],
            row['toilet_flush_handle_2'],
            row['toilet_seat_1'],
            row['toilet_seat_2'] ]
    return l_l

dicotaxo = { "name" : "Bacteria", "count" : [0 for i in range(14)], "children" : []}
for index,row in minitb.iterrows():
    leveltax = row["OTUConTaxonomy"].split(";")  # uniquement indexes >=1 m'interessent 
    COUNTS = getcountsfromrow(row)
    tmp5 = {}
    tmp4 = {}
    tmp3 = {}
    tmp2 = {}
    tmp1 = {}
    tmp5["name"] = leveltax[5]
    tmp4["name"] = leveltax[4]
    tmp3["name"] = leveltax[3]
    tmp2["name"] = leveltax[2]
    tmp1["name"] = leveltax[1]      
    tmp5["count"] =  getcountsfromrow(row)
    tmp5["children"] = []  # lowest level
    tmp4["count"] =  getcountsfromrow(row)
    tmp4["children"] = [tmp5]
    tmp3["count"] =  getcountsfromrow(row)
    tmp3["children"] = [tmp4]
    tmp2["count"] =  getcountsfromrow(row)
    tmp2["children"] = [tmp3]
    tmp1["count"] = getcountsfromrow(row)
    tmp1["children"] = [tmp2]
    tmpcounts = dicotaxo["count"]
    dicotaxo["count"] = np.add(tmpcounts, COUNTS)
    if leveltax[1] not in [m["name"] for m in dicotaxo["children"]] :
        dicotaxo["children"].append(tmp1)
    else:
        for m in dicotaxo["children"]:
            if m["name"] == leveltax[1]:
                tmpc = m["count"]
                m["count"] = np.add(tmpc, COUNTS)
                if leveltax[2] not in [n["name"] for n in m["children"]] :
                    m["children"].append(tmp2)
                else:
                    for n in m["children"]:
                        if n["name"] == leveltax[2]:
                            tmpc = n["count"]
                            n["count"] = np.add(tmpc, COUNTS)
                            if leveltax[3] not in [o["name"] for o in n["children"]]:
                                n["children"].append(tmp3)
                            else: 
                                for o in n["children"]:
                                    if o["name"] == leveltax[3]:
                                        tmpc = o["count"]
                                        o["count"] = np.add(tmpc,COUNTS)
                                        if leveltax[4] not in [p["name"] for p in o["children"]]:
                                            o["children"].append(tmp4)
                                        else:
                                            for p in o["children"]:
                                                if p["name"] == leveltax[4]:
                                                    tmpc = p["count"]
                                                    p["count"] = np.add(tmpc, COUNTS)
                                                    if leveltax[5] not in [q["name"] for q in p["children"]]:
                                                        p["children"].append(tmp5)
                                                    else:
                                                        for q in p["children"]:
                                                            if q["name"] == leveltax[5]:
                                                                tmpc = q["count"]
                                                                q["count"] = np.add(tmpc, COUNTS)
                                                                q["children"] = []
                                                                # this is the lowest level                                        
    

print(dicotaxo)



#### EVOLUTION
# without conditionnal loops:
"""{'name': 'Actinobacteria(100)', 'count': [1381.0, 1032.0, 335.0, 577.0, 38.0, 36.0, 1115.0, 598.0, 45.0, 87.0, 13.0, 329.0, 76.0, 156.0], 'children': [{'name': 'Actinobacteria(100)', 'count': [1381.0, 1032.0, 335.0, 577.0, 38.0, 36.0, 1115.0, 598.0, 45.0, 87.0, 13.0, 329.0, 76.0, 156.0], 'children': [{'name': 'Actinomycetales(100)', 'count': [1381.0, 1032.0, 335.0, 577.0, 38.0, 36.0, 1115.0, 598.0, 45.0, 87.0, 13.0, 329.0, 76.0, 156.0], 'children': []}]}]}
{'name': 'Proteobacteria(100)', 'count': [20.0, 17.0, 1686.0, 3.0, 411.0, 564.0, 128.0, 9.0, 430.0, 707.0, 0.0, 25.0, 258.0, 0.0], 'children': [{'name': 'Gammaproteobacteria(100)', 'count': [20.0, 17.0, 1686.0, 3.0, 411.0, 564.0, 128.0, 9.0, 430.0, 707.0, 0.0, 25.0, 258.0, 0.0], 'children': [{'name': 'Pseudomonadales(100)', 'count': [20.0, 17.0, 1686.0, 3.0, 411.0, 564.0, 128.0, 9.0, 430.0, 707.0, 0.0, 25.0, 258.0, 0.0], 'children': []}]}]}
{'name': 'Actinobacteria(100)', 'count': [8.0, 47.0, 6.0, 418.0, 15.0, 8.0, 84.0, 45.0, 6.0, 30.0, 3.0, 283.0, 41.0, 1059.0], 'children': [{'name': 'Actinobacteria(100)', 'count': [8.0, 47.0, 6.0, 418.0, 15.0, 8.0, 84.0, 45.0, 6.0, 30.0, 3.0, 283.0, 41.0, 1059.0], 'children': [{'name': 'Actinomycetales(100)', 'count': [8.0, 47.0, 6.0, 418.0, 15.0, 8.0, 84.0, 45.0, 6.0, 30.0, 3.0, 283.0, 41.0, 1059.0], 'children': []}]}]}
"""
# with conditionnal loops but not summing vectors:
"""
{'name': 'Actinobacteria(100)', 'count': [1381.0, 1032.0, 335.0, 577.0, 38.0, 36.0, 1115.0, 598.0, 45.0, 87.0, 13.0, 329.0, 76.0, 156.0], 'children': [{'name': 'Actinobacteria(100)', 'count': [1381.0, 1032.0, 335.0, 577.0, 38.0, 36.0, 1115.0, 598.0, 45.0, 87.0, 13.0, 329.0, 76.0, 156.0], 'children': [{'name': 'Actinomycetales(100)', 'count': array([1389., 1079.,  341.,  995.,   53.,   44., 1199.,  643.,   51.,
        117.,   16.,  612.,  117., 1215.]), 'children': []}]}]}
{'name': 'Proteobacteria(100)', 'count': [20.0, 17.0, 1686.0, 3.0, 411.0, 564.0, 128.0, 9.0, 430.0, 707.0, 0.0, 25.0, 258.0, 0.0], 'children': [{'name': 'Gammaproteobacteria(100)', 'count': [20.0, 17.0, 1686.0, 3.0, 411.0, 564.0, 128.0, 9.0, 430.0, 707.0, 0.0, 25.0, 258.0, 0.0], 'children': [{'name': 'Pseudomonadales(100)', 'count': [20.0, 17.0, 1686.0, 3.0, 411.0, 564.0, 128.0, 9.0, 430.0, 707.0, 0.0, 25.0, 258.0, 0.0], 'children': []}]}]}

"""
## final result:
"""
"""


# old lines:
"""
#dicotaxo["children"].append(tmp1)
    for m in dicotaxo["children"]:
        if m["name"] == leveltax[1]:
            for n in m["children"]:
                if n["name"] == leveltax[2]:
                    for o in n["children"]:
                        if o["name"] == leveltax[3]:
                            tmpc = o["count"] 
                            o["count"] = np.add(tmpc, getcountsfromrow(row))
                            #o["children"] = []
                            pass
                        #elif leveltax[3] not in [o["name"] for o in n["children"]]:
"""