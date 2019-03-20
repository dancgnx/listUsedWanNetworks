import cgxinit
import cloudgenix
import json
import sys

# create CGX object and authenticate
cgx = cgxinit.go()

# shortcut to jd function
jd = cloudgenix.jd


wannetworks={}
# itirate through the list of sites
for site in cgx.get.sites().cgx_content["items"]:

    # itirate through waninterfaces
    for waninterface in cgx.get.waninterfaces(site["id"]).cgx_content["items"]:
        wannetworks[waninterface["network_id"]] = "HELLO"


#itirate through wannetworks and check if they exist in "wannetworks" dict
for wannetwork in cgx.get.wannetworks().cgx_content["items"]:
    # check if wannetwork is a key inside "wannetworks" dict
    if wannetwork["id"] not in wannetworks:
        print (wannetwork["name"])
#        cgx.delete.wannetworks(wannetwork["id"])
