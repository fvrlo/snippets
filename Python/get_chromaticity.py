import colour

keyz = [ "Name",
    "2° (x)y",     # Chromaticity coordinates of the illuminants.
    "2° x(y)",     # Chromaticity coordinates of the illuminants.
    "10° (x)y",    # Chromaticity coordinates of the illuminants.
    "10° x(y)",    # Chromaticity coordinates of the illuminants.
    "2° (x)yz",     # CIE XYZ tristimulus values of the illuminants.
    "2° x(y)z",     # CIE XYZ tristimulus values of the illuminants.
    "2° xy(z)",     # CIE XYZ tristimulus values of the illuminants.
    "10° (x)yz",    # CIE XYZ tristimulus values of the illuminants.
    "10° x(y)z",    # CIE XYZ tristimulus values of the illuminants.
    "10° xy(z)",    # CIE XYZ tristimulus values of the illuminants.
    "HunterLab 2° x",  # CIE XYZ tristimulus values of the HunterLab illuminants.
    "HunterLab 2° y",  # CIE XYZ tristimulus values of the HunterLab illuminants.
    "HunterLab 2° z",  # CIE XYZ tristimulus values of the HunterLab illuminants.
    "HunterLab 2° a",  # CIE XYZ tristimulus values of the HunterLab illuminants.
    "HunterLab 2° b",  # CIE XYZ tristimulus values of the HunterLab illuminants.
    "HunterLab 10° x", # CIE XYZ tristimulus values of the HunterLab illuminants.
    "HunterLab 10° y", # CIE XYZ tristimulus values of the HunterLab illuminants.
    "HunterLab 10° z", # CIE XYZ tristimulus values of the HunterLab illuminants.
    "HunterLab 10° a", # CIE XYZ tristimulus values of the HunterLab illuminants.
    "HunterLab 10° b"  # CIE XYZ tristimulus values of the HunterLab illuminants.
    ]

masterdict = {}
for cie in ["cie_2_1931", "cie_10_1964"]:
    for sets in [colour.CCS_ILLUMINANTS, colour.TVS_ILLUMINANTS, colour.TVS_ILLUMINANTS_HUNTERLAB]:
        for x in dict(sets)[cie]:
            if x not in masterdict.keys():
                masterdict[x] = {}

for x in dict(colour.CCS_ILLUMINANTS)["cie_2_1931"]:
    masterdict[x][keyz[1]] = dict(colour.CCS_ILLUMINANTS)["cie_2_1931"][x][0]
    masterdict[x][keyz[2]] = dict(colour.CCS_ILLUMINANTS)["cie_2_1931"][x][1]

for x in dict(colour.CCS_ILLUMINANTS)["cie_10_1964"]:
    masterdict[x][keyz[3]] = dict(colour.CCS_ILLUMINANTS)["cie_10_1964"][x][0]
    masterdict[x][keyz[4]] = dict(colour.CCS_ILLUMINANTS)["cie_10_1964"][x][1]

for x in dict(colour.TVS_ILLUMINANTS)["cie_2_1931"]:
    masterdict[x][keyz[5]] = dict(colour.TVS_ILLUMINANTS)["cie_2_1931"][x][0]
    masterdict[x][keyz[6]] = dict(colour.TVS_ILLUMINANTS)["cie_2_1931"][x][1]
    masterdict[x][keyz[7]] = dict(colour.TVS_ILLUMINANTS)["cie_2_1931"][x][2]

for x in dict(colour.TVS_ILLUMINANTS)["cie_10_1964"]:
    masterdict[x][keyz[8]] = dict(colour.TVS_ILLUMINANTS)["cie_10_1964"][x][0]
    masterdict[x][keyz[9]] = dict(colour.TVS_ILLUMINANTS)["cie_10_1964"][x][1]
    masterdict[x][keyz[10]] = dict(colour.TVS_ILLUMINANTS)["cie_10_1964"][x][2]

for x in dict(colour.TVS_ILLUMINANTS_HUNTERLAB["cie_2_1931"]):
    masterdict[x][keyz[11]] = dict(colour.TVS_ILLUMINANTS_HUNTERLAB["cie_2_1931"])[x][1][0]
    masterdict[x][keyz[12]] = dict(colour.TVS_ILLUMINANTS_HUNTERLAB["cie_2_1931"])[x][1][1]
    masterdict[x][keyz[13]] = dict(colour.TVS_ILLUMINANTS_HUNTERLAB["cie_2_1931"])[x][1][2]
    masterdict[x][keyz[14]] = dict(colour.TVS_ILLUMINANTS_HUNTERLAB["cie_2_1931"])[x][2][0]
    masterdict[x][keyz[15]] = dict(colour.TVS_ILLUMINANTS_HUNTERLAB["cie_2_1931"])[x][2][1]

for x in dict(colour.TVS_ILLUMINANTS_HUNTERLAB["cie_10_1964"]):
    masterdict[x][keyz[16]] = dict(colour.TVS_ILLUMINANTS_HUNTERLAB["cie_10_1964"])[x][1][0]
    masterdict[x][keyz[17]] = dict(colour.TVS_ILLUMINANTS_HUNTERLAB["cie_10_1964"])[x][1][1]
    masterdict[x][keyz[18]] = dict(colour.TVS_ILLUMINANTS_HUNTERLAB["cie_10_1964"])[x][1][2]
    masterdict[x][keyz[19]] = dict(colour.TVS_ILLUMINANTS_HUNTERLAB["cie_10_1964"])[x][2][0]
    masterdict[x][keyz[20]] = dict(colour.TVS_ILLUMINANTS_HUNTERLAB["cie_10_1964"])[x][2][1]

out_title = ""
for item in keyz:
    out_title = out_title + item + ","

print(out_title)
for x in masterdict.keys():
    outbound = "" + x + ","
    for z in keyz:
        try:
            if z == keyz[0]:
                outbound = x + ","
            else:
                outbound = outbound + str(masterdict[x][z]) + ","
        except KeyError:
            outbound = outbound + "" + ","
    print(outbound)
print()
print()



ls_keys = [ "Name",
    "2° X CCS LS",  # Chromaticity coordinates of the light sources.
    "2° Y CCS LS",  # Chromaticity coordinates of the light sources.
    "10° X CCS LS", # Chromaticity coordinates of the light sources.
    "10° Y CCS LS"  # Chromaticity coordinates of the light sources.
    ]

light_sources = {}
for cie in ["cie_2_1931", "cie_10_1964"]:
    for x in dict(colour.CCS_LIGHT_SOURCES)[cie]:
        if x not in light_sources.keys():
            light_sources[x] = {}



for x in dict(colour.CCS_LIGHT_SOURCES)["cie_2_1931"]:
    light_sources[x][ls_keys[1]] = dict(colour.CCS_LIGHT_SOURCES)["cie_2_1931"][x][0] or ""
    light_sources[x][ls_keys[2]] = dict(colour.CCS_LIGHT_SOURCES)["cie_2_1931"][x][1] or ""

for x in dict(colour.CCS_LIGHT_SOURCES)["cie_10_1964"]:
    light_sources[x][ls_keys[3]] = dict(colour.CCS_LIGHT_SOURCES)["cie_10_1964"][x][0] or ""
    light_sources[x][ls_keys[4]] = dict(colour.CCS_LIGHT_SOURCES)["cie_10_1964"][x][1] or ""


out_title = ""
for item in ls_keys:
    out_title = out_title + item + ","
print(out_title)
for x in light_sources.keys():
    outbound = "" + x + ","
    for z in ls_keys:
        try:
            if z == ls_keys[0]:
                outbound = x + ","
            else:
                outbound = outbound + str(light_sources[x][z]) + ","
        except KeyError:
            outbound = outbound + "" + ","
    print(outbound)