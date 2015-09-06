DIVISION = [
    (0, 'Puerto Rico'),
    (1, 'New England (Northeast region)'),
    (2, 'Middle Atlantic (Northeast region)'),
    (3, 'East North Central (Midwest region)'),
    (4, 'West North Central (Midwest region)'),
    (5, 'South Atlantic (South region)'),
    (6, 'East South Central (South region)'),
    (7, 'West South Central (South Region)'),
    (8, 'Mountain (West region)'),
    (9, 'Pacific (West region)'),
]

REGION = [
    (1, 'Northeast'),
    (2, 'Midwest'),
    (3, 'South'),
    (4, 'West'),
    (9, 'Puerto Rico'),
]

ST = [
    (1, 'Alabama/AL'),
    (2, 'Alaska/AK'),
    (4, 'Arizona/AZ'),
    (5, 'Arkansas/AR'),
    (6, 'California/CA'),
    (8, 'Colorado/CO'),
    (9, 'Connecticut/CT'),
    (10, 'Delaware/DE'),
    (11, 'District of Columbia/DC'),
    (12, 'Florida/FL'),
    (13, 'Georgia/GA'),
    (15, 'Hawaii/HI'),
    (16, 'Idaho/ID'),
    (17, 'Illinois/IL'),
    (18, 'Indiana/IN'),
    (19, 'Iowa/IA'),
    (20, 'Kansas/KS'),
    (21, 'Kentucky/KY'),
    (22, 'Louisiana/LA'),
    (23, 'Maine/ME'),
    (24, 'Maryland/MD'),
    (25, 'Massachusetts/MA'),
    (26, 'Michigan/MI'),
    (27, 'Minnesota/MN'),
    (28, 'Mississippi/MS'),
    (29, 'Missouri/MO'),
    (30, 'Montana/MT'),
    (31, 'Nebraska/NE'),
    (32, 'Nevada/NV'),
    (33, 'New Hampshire/NH'),
    (34, 'New Jersey/NJ'),
    (35, 'New Mexico/NM'),
    (36, 'New York/NY'),
    (37, 'North Carolina/NC'),
    (38, 'North Dakota/ND'),
    (39, 'Ohio/OH'),
    (40, 'Oklahoma/OK'),
    (41, 'Oregon/OR'),
    (42, 'Pennsylvania/PA'),
    (44, 'Rhode Island/RI'),
    (45, 'South Carolina/SC'),
    (46, 'South Dakota/SD'),
    (47, 'Tennessee/TN'),
    (48, 'Texas/TX'),
    (49, 'Utah/UT'),
    (50, 'Vermont/VT'),
    (51, 'Virginia/VA'),
    (53, 'Washington/WA'),
    (54, 'West Virginia/WV'),
    (55, 'Wisconsin/WI'),
    (56, 'Wyoming/WY'),
    (72, 'Puerto Rico/PR'),
]

ADJUST = [
    (1015675, '2006 factor (1.015675)'),
]

WGTP = [
    (0001..9999, 'Integer weight of housing unit'),
]

NP = [
    (00, 'Vacant unit'),
    (01, 'One person record (one person in household or any person in group quarters)'),
    (02..20, 'Number of person records (number of persons in household)'),
]

TYPE = [
    (1, 'Housing unit'),
    (2, 'Institutional group quarters'),
    (3, 'Noninstitutional group quarters'),
]

ACR = [
    (b, 'N/A (GQ/not a one-family house or mobile home)'),
    (1, 'House on less than one acre'),
    (2, 'House on one to less than ten acres'),
    (3, 'House on ten or more acres'),
]

AGS = [
    (b, 'N/A (less than 1 acre/GQ/vacant/ 2 or more units in structure)'),
    (1, 'None'),
    (2, '$ 1 - $ 999'),
    (3, '$ 1000 - $ 2499'),
    (4, '$ 2500 - $ 4999'),
    (5, '$ 5000 - $ 9999'),
    (6, '$10000+'),
]

BDS = [
    (b, 'N/A (GQ)'),
    (0, 'No bedrooms'),
    (1, '1 Bedroom'),
    (2, '2 Bedrooms'),
    (3, '3 Bedrooms'),
    (4, '4 Bedrooms'),
    (5, '5 or more bedrooms'),
]

BLD = [
    (bb, 'N/A (GQ)'),
    (01, 'Mobile home or trailer'),
    (02, 'One-family house detached'),
    (03, 'One-family house attached'),
    (04, '2 Apartments'),
    (05, '3-4 Apartments'),
    (06, '5-9 Apartments'),
    (07, '10-19 Apartments'),
    (08, '20-49 Apartments'),
    (09, '50 or more apartments'),
    (10, 'Boat, RV, van, etc.'),
]

BUS = [
    (b, 'N/A (GQ/not a one-family house or mobile home)'),
    (1, 'Yes'),
    (2, 'No'),
]

CONP = [
    (bbbb, 'N/A (not owned or being bought/not condo/GQ/vacant/no condo fee)'),
    (0001..9999, '$1 - $9999 (Rounded and top-coded)'),
]

ELEP = [
    (bbb, 'N/A (GQ/vacant)'),
    (001, 'Included in rent or in condo fee'),
    (002, 'No charge or electricity not used'),
    (003..999, '$3 to $999 (Rounded and top-coded)'),
]

FS = [
    (bbbbb, 'N/A (vacant)'),
    (0, 'None'),
    (1..99999, '$1 to $99999'),
]

FULP = [
    (bbbb, 'N/A (GQ/vacant)'),
    (0001, 'Included in rent or in condo fee'),
    (0002, 'No charge or these fuels not used'),
    (0003..9999, '$3 to $9999 (Rounded and top-coded)'),
]

GASP = [
    (bbb, 'N/A (GQ/vacant)'),
    (001, 'Included in rent or in condo fee'),
    (002, 'Included in electricity payment'),
    (003, 'No charge or gas not used'),
    (004..999, '$4 to $999 (Rounded and top-coded)'),
]

HFL = [
    (b, 'N/A (GQ/vacant)'),
    (1, 'Utility gas'),
    (2, 'Bottled, tank, or LP gas'),
    (3, 'Electricity'),
    (4, 'Fuel oil, kerosene, etc.'),
    (5, 'Coal or coke'),
    (6, 'Wood'),
    (7, 'Solar energy'),
    (8, 'Other fuel'),
    (9, 'No fuel used'),
]

INSP = [
    (bbbb, 'N/A (not owned or being bought/not a one family house, mobile home, or condo/GQ/vacant)'),
    (0000, 'None'),
    (0001..9999, '$1 to $9999 (Rounded and top-coded)'),
]

KIT = [
    (b, 'N/A (GQ)'),
    (1, 'Yes, has all three facilities'),
    (2, 'No'),
]

MHP = [
    (bbbbb, 'N/A (GQ/vacant/not owned or being bought/ not mobile home/no costs)'),
    (00000..99999, '$0 to $99999 (Rounded and top-coded)'),
]

MRGI = [
    (b, 'N/A (GQ/vacant/not owned or being bought/ Not a one family house, MHT or condo/not mortgaged/no regular mortgage payment)'),
    (1, 'Yes, insurance included in payment'),
    (2, 'No, insurance paid separately or no insurance'),
]

MRGP = [
    (bbbbb, 'N/A (not owned or being bought/not a one family house, mobile home, or condo/GQ/vacant)'),
    (00001..99999, '$1 to $99999 (Rounded and top-coded)'),
]

MRGT = [
    (b, 'N/A (GQ/vacant/not owned or being bought/not a one family house or condo/not mortgaged/ No regular mortgage payment)'),
    (1, 'Yes, taxes included in payment'),
    (2, 'No, taxes paid separately or taxes not required'),
]

MRGX = [
    (b, 'N/A (not owned or being bought/not a one family house, mobile home, or condo/GQ/vacant)'),
    (1, 'Mortgage deed of trust, or similar debt'),
    (2, 'Contract to purchase'),
    (3, 'None'),
]

PLM = [
    (b, 'N/A (GQ)'),
    (1, 'Yes, has all three facilities'),
    (2, 'No'),
]

RMS = [
    (b, 'N/A (GQ)'),
    (1, '1 Room'),
    (2, '2 Rooms'),
    (3, '3 Rooms'),
    (4, '4 Rooms'),
    (5, '5 Rooms'),
    (6, '6 Rooms'),
    (7, '7 Rooms'),
    (8, '8 Rooms'),
    (9, '9 or more rooms'),
]

RNTM = [
    (b, 'N/A (GQ/not a rental unit/rental-NCR)'),
    (1, 'Yes'),
    (2, 'No'),
]

RNTP = [
    (bbbbb, 'N/A (GQ/not a rental unit)'),
    (00001..99999, '$1 to $99999 (Rounded and top-coded)'),
]

SMP = [
    (bbbbb, 'N/A (GQ/vacant/condo/not owned or being bought/not a one family house/not mortgaged/ no second mortgage)'),
    (00001..99999, '$1 to $99999 (Rounded and top-coded)'),
]

TEL = [
    (b, 'N/A (GQ/vacant)'),
    (1, 'Yes'),
    (2, 'No'),
]

TEN = [
    (b, 'N/A (GQ/vacant)'),
    (1, 'Owned with mortgage or loan'),
    (2, 'Owned free and clear'),
    (3, 'Rented for cash rent'),
    (4, 'No cash rent'),
]

VACS = [
    (b, 'N/A (occupied/GQ)'),
    (1, 'For rent'),
    (2, 'Rented, not occupied'),
    (3, 'For sale only'),
    (4, 'Sold, not occupied'),
    (5, 'For seasonal/recreational/occasional use'),
    (6, 'For migratory workers'),
    (7, 'Other vacant'),
]

VAL = [
    (bb, 'N/A (GQ/rental unit/vacant, not for sale only)'),
    (01, 'Less than $ 10000'),
    (02, '$ 10000 - $ 14999'),
    (03, '$ 15000 - $ 19999'),
    (04, '$ 20000 - $ 24999'),
    (05, '$ 25000 - $ 29999'),
    (06, '$ 30000 - $ 34999'),
    (07, '$ 35000 - $ 39999'),
    (08, '$ 40000 - $ 49999'),
    (09, '$ 50000 - $ 59999'),
    (10, '$ 60000 - $ 69999'),
    (11, '$ 70000 - $ 79999'),
    (12, '$ 80000 - $ 89999'),
    (13, '$ 90000 - $ 99999'),
    (14, '$100000 - $124999'),
    (15, '$125000 - $149999'),
    (16, '$150000 - $174999'),
    (17, '$175000 - $199999'),
    (18, '$200000 - $249999'),
    (19, '$250000 - $299999'),
    (20, '$300000 - $399999'),
    (21, '$400000 - $499999'),
    (22, '$500000 - $749999'),
    (23, '$750000 - $999999'),
    (24, '$1000000+'),
]

VEH = [
    (b, 'N/A (GQ/vacant)'),
    (0, 'No vehicles'),
    (1, '1 vehicle'),
    (2, '2 vehicles'),
    (3, '3 vehicles'),
    (4, '4 vehicles'),
    (5, '5 vehicles'),
    (6, '6 or more vehicles'),
]

WATP = [
    (bbbb, 'N/A (GQ/vacant)'),
    (0001, 'Included in rent or in condo fee'),
    (0002, 'No charge'),
    (0003..9999, '$3 to $9999 (Rounded and top-coded)'),
]

YBL = [
    (b, 'N/A (GQ)'),
    (1, '2005 or later'),
    (2, '2000 to 2004'),
    (3, '1990 to 1999'),
    (4, '1980 to 1989'),
    (5, '1970 to 1979'),
    (6, '1960 to 1969'),
    (7, '1950 to 1959'),
    (8, '1940 to 1949'),
    (9, '1939 or earlier'),
]

FES = [
    (b, 'N/A (GQ/vacant/not a family)'),
    (1, 'Married-couple family: Husband and wife in LF'),
    (2, 'Married-couple family: Husband in labor force, wife not in LF'),
    (3, 'Married-couple family: Husband not in LF, wife in LF'),
    (4, 'Married-couple family: Neither husband nor wife in LF'),
    (5, 'Other family: Male householder, no wife present, in LF'),
    (6, 'Other family: Male householder, no wife present, not in LF'),
    (7, 'Other family: Female householder, no husband present, in LF'),
    (8, 'Other family: Female householder, no husband present, not in LF'),
]

FINCP = [
    (bbbbbbbb, 'N/A(GQ/vacant)'),
    (00000000, 'No family income'),
    (-59999..99999999, 'Total family income in dollars'),
]

FPARC = [
    (b, 'N/A (GQ/vacant/not a family)'),
    (1, 'With related children under 5 years only'),
    (2, 'With related children 5 to 17 years only'),
    (3, 'With related children under 5 years and 5 to 17 years'),
    (4, 'No related children'),
]

GRNTP = [
    (bbbb, 'N/A (GQ/vacant, not rented for cash rent)'),
    (0001..9999, '$1 - $9999'),
]

GRPIP = [
    (bbb, 'N/A (GQ/vacant/not rented for cash rent/owner occupied/no household income)'),
    (001..100, '1% to 100%'),
    (101, '101% or more'),
]

HHL = [
    (b, 'N/A (GQ/vacant)'),
    (1, 'English only'),
    (2, 'Spanish'),
    (3, 'Other Indo-European language'),
    (4, 'Asian or Pacific Island language'),
    (5, 'Other language'),
]

HHT = [
    (b, 'N/A (GQ/vacant)'),
    (1, 'Married-couple family household Other family household:'),
    (2, 'Male householder, no wife present'),
    (3, 'Female householder, no husband present Nonfamily household: Male householder:'),
    (4, 'Living alone'),
    (5, 'Not living alone Female householder:'),
    (6, 'Living alone'),
    (7, 'Not living alone'),
]

HINCP = [
    (bbbbbbbb, 'N/A(GQ/vacant)'),
    (00000000, 'No household income'),
    (-59999..99999999, 'Total household income in dollars'),
]

HUGCL = [
    (b, 'N/A (GQ/vacant)'),
    (0, 'HU does not contain grandchildren'),
    (1, 'HU does contain grandchildren'),
]

HUPAC = [
    (b, 'N/A (GQ/vacant)'),
    (1, 'With children under 6 years only'),
    (2, 'With children 6 to 17 years only'),
    (3, 'With children under 6 years and 6 to 17 years'),
    (4, 'No children'),
]

HUPAOC = [
    (b, 'N/A (GQ/vacant)'),
    (1, 'Presence of own children under 6 years only'),
    (2, 'Presence of own children 6 to 17 years only'),
    (3, 'Presence of own children under 6 years and 6 to 17 years'),
    (4, 'No own children present'),
]

HUPARC = [
    (b, 'N/A (GQ/vacant)'),
    (1, 'Presence of related children under 6 years only'),
    (2, 'Presence of related children 6 to 17 years only'),
    (3, 'Presence of related children under 6 years and 6 to 17 years'),
    (4, 'No related children present'),
]

LNGI = [
    (b, 'N/A (GQ/vacant)'),
    (1, 'Not linguistically isolated'),
    (2, 'Linguistically isolated'),
]

MV = [
    (b, 'N/A (GQ/vacant)'),
    (1, '12 months or less'),
    (2, '13 to 23 months'),
    (3, '2 to 4 years'),
    (4, '5 to 9 years'),
    (5, '10 to 19 years'),
    (6, '20 to 29 years'),
    (7, '30 years or more'),
]

NOC = [
    (bb, 'N/A(GQ/vacant)'),
    (00, 'No own children'),
    (01..19, 'Number of own children in household'),
]

NPF = [
    (bb, 'N/A (GQ/vacant/non-family household)'),
    (02..20, 'Number of persons in family'),
]

NPP = [
    (b, 'N/A (GQ/vacant)'),
    (0, 'Not a grandparent headed household with no parent present'),
    (1, 'Grandparent headed household with no parent present'),
]

NR = [
    (b, 'N/A (GQ/vacant)'),
    (0, 'None'),
    (1, '1 or more nonrelatives'),
]

NRC = [
    (bb, 'N/A (GQ/vacant)'),
    (00, 'No related children'),
    (01..19, 'Number of related children in household'),
]

OCPIP = [
    (bbb, 'N/A (not owned or being bought/not a one family house, mobile home, or condo/GQ/vacant/no HH income)'),
    (001..100, '1% to 100%'),
    (101, '101% or more'),
]

PARTNER = [
    (b, 'N/A (GQ/vacant)'),
    (0, 'No unmarried partner in household'),
    (1, 'Male householder, male partner'),
    (2, 'Male householder, female partner'),
    (3, 'Female householder, male partner'),
    (4, 'Female householder, female partner'),
]

PSF = [
    (b, 'N/A (GQ/vacant)'),
    (0, 'No subfamilies'),
    (1, '1 or more subfamilies'),
]

R18 = [
    (b, 'N/A (GQ/vacant)'),
    (0, 'No person under 18 in household'),
    (1, '1 or more persons under 18 in household'),
]

R60 = [
    (b, 'N/A (GQ/vacant)'),
    (0, 'No person 60 and over'),
    (1, '1 person 60 and over'),
    (2, '2 or more persons 60 and over'),
]

R65 = [
    (b, 'N/A (GQ/vacant)'),
    (0, 'No person 65 and over'),
    (1, '1 person 65 and over'),
    (2, '2 or more persons 65 and over'),
]

RESMODE = [
    (b, 'N/A (GQ)'),
    (1, 'Mail'),
    (2, 'CATI/CAPI'),
]

SMOCP = [
    (bbbbb, 'N/A (not owned or being bought/not a one family house, mobile home, or condo/GQ/vacant/no costs )'),
    (00000, 'No costs'),
    (00001..99999, '$1 - $99999'),
]

SMX = [
    (b, 'N/A (GQ/vacant/not owned or being bought/ not a one family house, mobile home, trailer or condo/not mortgaged/no second mortgage)'),
    (1, 'Yes, a second mortgage'),
    (2, 'Yes, a home equity loan'),
    (3, 'No'),
    (4, 'Both a second mortgage and a home equity loan'),
]

SRNT = [
    (0, 'Not specified rent unit'),
    (1, 'Specified rent unit'),
]

SVAL = [
    (0, 'Not specified owner unit'),
    (1, 'Specified value unit'),
]

TAXP = [
    (bb, 'N/A (GQ/vacant/not owned or being bought/not a one-family house, mobile home or trailer or condo)'),
    (01, 'None'),
    (02, '$ 1 - $ 49'),
    (03, '$ 50 - $ 99'),
    (04, '$ 100 - $ 149'),
    (05, '$ 150 - $ 199'),
    (06, '$ 200 - $ 249'),
    (07, '$ 250 - $ 299'),
    (08, '$ 300 - $ 349'),
    (09, '$ 350 - $ 399'),
    (10, '$ 400 - $ 449'),
    (11, '$ 450 - $ 499'),
    (12, '$ 500 - $ 549'),
    (13, '$ 550 - $ 599'),
    (14, '$ 600 - $ 649'),
    (15, '$ 650 - $ 699'),
    (16, '$ 700 - $ 749'),
    (17, '$ 750 - $ 799'),
    (18, '$ 800 - $ 849'),
    (19, '$ 850 - $ 899'),
    (20, '$ 900 - $ 949'),
    (21, '$ 950 - $ 999'),
    (22, '$1000 - $1099'),
    (23, '$1100 - $1199'),
    (24, '$1200 - $1299'),
    (25, '$1300 - $1399'),
    (26, '$1400 - $1499'),
    (27, '$1500 - $1599'),
    (28, '$1600 - $1699'),
    (29, '$1700 - $1799'),
    (30, '$1800 - $1899'),
    (31, '$1900 - $1999'),
    (32, '$2000 - $2099'),
    (33, '$2100 - $2199'),
    (34, '$2200 - $2299'),
    (35, '$2300 - $2399'),
    (36, '$2400 - $2499'),
    (37, '$2500 - $2599'),
    (38, '$2600 - $2699'),
    (39, '$2700 - $2799'),
    (40, '$2800 - $2899'),
    (41, '$2900 - $2999'),
    (42, '$3000 - $3099'),
    (43, '$3100 - $3199'),
    (44, '$3200 - $3299'),
    (45, '$3300 - $3399'),
    (46, '$3400 - $3499'),
    (47, '$3500 - $3599'),
    (48, '$3600 - $3699'),
    (49, '$3700 - $3799'),
    (50, '$3800 - $3899'),
    (51, '$3900 - $3999'),
    (52, '$4000 - $4099'),
    (53, '$4100 - $4199'),
    (54, '$4200 - $4299'),
    (55, '$4300 - $4399'),
    (56, '$4400 - $4499'),
    (57, '$4500 - $4599'),
    (58, '$4600 - $4699'),
    (59, '$4700 - $4799'),
    (60, '$4800 - $4899'),
    (61, '$4900 - $4999'),
    (62, '$5000 - $5499'),
    (63, '$5500 - $5999'),
    (64, '$6000 - $6999'),
    (65, '$7000 - $7999'),
    (66, '$8000 - $8999'),
    (67, '$9000 - $9999'),
    (68, '$10000+'),
]

WIF = [
    (b, 'N/A (GQ/vacant/non-family household)'),
    (0, 'No workers'),
    (1, '1 worker'),
    (2, '2 workers'),
    (3, '3 or more workers in family'),
]

WKEXREL = [
    (b, 'N/A (GQ/vacant/not a family)'),
    (1, 'Householder and spouse worked FT'),
    (2, 'Householder worked FT; spouse worked < FT'),
    (3, 'Householder worked FT; spouse did not work'),
    (4, 'Householder worked < FT; spouse worked FT'),
    (5, 'Householder worked < FT; spouse worked < FT'),
    (6, 'Householder worked < FT; spouse did not work'),
    (7, 'Householder did not work; spouse worked FT'),
    (8, 'Householder did not work; spouse worked < FT'),
    (9, 'Householder did not work; spouse did not work'),
    (10, 'Male householder worked FT; no spouse present'),
    (11, 'Male householder worked < FT; no spouse present'),
    (12, 'Male householder did not work; no spouse present'),
    (13, 'Female householder worked FT; no spouse present'),
    (14, 'Female householder worked < FT; no spouse present'),
    (15, 'Female householder did not work; no spouse present'),
]

WORKSTAT = [
    (bb, 'N/A (GQ/not a family household)'),
    (1, 'Husband and wife both in labor force, both employed or in Armed Forces'),
    (2, 'Husband and wife both in labor force, husband employed or in Armed Forces, wife unemployed'),
    (3, 'Husband in labor force and wife not in labor force, husband employed or in Armed Forces'),
    (4, 'Husband and wife both in labor force, husband unemployed, wife employed or in Armed Forces'),
    (5, 'Husband and wife both in labor force, husband unemployed, wife unemployed'),
    (6, 'Husband in labor force, husband unemployed, wife not in labor force'),
    (7, 'Husband not in labor force, wife in labor force, wife employed or in Armed Forces'),
    (8, 'Husband not in labor force, wife in labor force, wife unemployed'),
    (9, 'Neither husband nor wife in labor force'),
    (10, 'Male householder with no wife present, householder in labor force, employed or in Armed Forces'),
    (11, 'Male householder with no wife present, householder in labor force and unemployed'),
    (12, 'Male householder with no wife present, householder not in labor force'),
    (13, 'Female householder with no husband present, householder in labor force, employed or in Armed Forces'),
    (14, 'Female householder with no husband present, householder in labor force and unemployed'),
    (15, 'Female householder with no husband present, householder not in labor force'),
]

FACRP = [
    (0, 'No'),
    (1, 'Yes'),
]

FAGSP = [
    (0, 'No'),
    (1, 'Yes'),
]

FBDSP = [
    (0, 'No'),
    (1, 'Yes'),
]

FBLDP = [
    (0, 'No'),
    (1, 'Yes'),
]

FBUSP = [
    (0, 'No'),
    (1, 'Yes'),
]

FCONP = [
    (0, 'No'),
    (1, 'Yes'),
]

FELEP = [
    (0, 'No'),
    (1, 'Yes'),
]

FFSP = [
    (0, 'No'),
    (1, 'Yes'),
]

FFULP = [
    (0, 'No'),
    (1, 'Yes'),
]

FGASP = [
    (0, 'No'),
    (1, 'Yes'),
]

FHFLP = [
    (0, 'No'),
    (1, 'Yes'),
]

FINSP = [
    (0, 'No'),
    (1, 'Yes'),
]

FKITP = [
    (0, 'No'),
    (1, 'Yes'),
]

FMHP = [
    (0, 'No'),
    (1, 'Yes'),
]

FMRGIP = [
    (0, 'No'),
    (1, 'Yes'),
]

FMRGP = [
    (0, 'No'),
    (1, 'Yes'),
]

FMRGTP = [
    (0, 'No'),
    (1, 'Yes'),
]

FMRGXP = [
    (0, 'No'),
    (1, 'Yes'),
]

FMVYP = [
    (0, 'No'),
    (1, 'Yes'),
]

FPLMP = [
    (0, 'No'),
    (1, 'Yes'),
]

FRMSP = [
    (0, 'No'),
    (1, 'Yes'),
]

FRNTMP = [
    (0, 'No'),
    (1, 'Yes'),
]

FRNTP = [
    (0, 'No'),
    (1, 'Yes'),
]

FSMP = [
    (0, 'No'),
    (1, 'Yes'),
]

FSMXHP = [
    (0, 'No'),
    (1, 'Yes'),
]

FSMXSP = [
    (0, 'No'),
    (1, 'Yes'),
]

FTAXP = [
    (0, 'No'),
    (1, 'Yes'),
]

FTELP = [
    (0, 'No'),
    (1, 'Yes'),
]

FTENP = [
    (0, 'No'),
    (1, 'Yes'),
]

FVACSP = [
    (0, 'No'),
    (1, 'Yes'),
]

FVALP = [
    (0, 'No'),
    (1, 'Yes'),
]

FVEHP = [
    (0, 'No'),
    (1, 'Yes'),
]

FWATP = [
    (0, 'No'),
    (1, 'Yes'),
]

FYBLP = [
    (0, 'No'),
    (1, 'Yes'),
]

WGTP1 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP2 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP3 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP4 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP5 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP6 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP7 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP8 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP9 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP10 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP11 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP12 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP13 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP14 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP15 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP16 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP17 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP18 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP19 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP20 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP21 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP22 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP23 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP24 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP25 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP26 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP27 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP28 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP29 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP30 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP31 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP32 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP33 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP34 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP35 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP36 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP37 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP38 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP39 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP40 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP41 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP42 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP43 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP44 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP45 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP46 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP47 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP48 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP49 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP50 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP51 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP52 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP53 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP54 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP55 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP56 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP57 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP58 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP59 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP60 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP61 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP62 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP63 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP64 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP65 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP66 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP67 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP68 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP69 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP70 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP71 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP72 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP73 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP74 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP75 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP76 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP77 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP78 = [
    (0001..9999, 'Integer weight of housing unit'),
]

WGTP79 = [
    (0001..9999, 'Integer weight of housing unit'),
]

RT = [
    (P, 'Person Record'),
]

SERIALNO = [
    (0000001..9999999, 'Unique identifier assigned within state'),
]

SPORDER = [
    (01..20, 'Person number'),
]

PUMA = [
    (77777, 'combination of 01801, 01802, and 01905 in Louisiana'),
]

ST = [
    (01, 'Alabama/AL'),
    (02, 'Alaska/AK'),
    (04, 'Arizona/AZ'),
    (05, 'Arkansas/AR'),
    (06, 'California/CA'),
    (08, 'Colorado/CO'),
    (09, 'Connecticut/CT'),
    (10, 'Delaware/DE'),
    (11, 'District of Columbia/DC'),
    (12, 'Florida/FL'),
    (13, 'Georgia/GA'),
    (15, 'Hawaii/HI'),
    (16, 'Idaho/ID'),
    (17, 'Illinois/IL'),
    (18, 'Indiana/IN'),
    (19, 'Iowa/IA'),
    (20, 'Kansas/KS'),
    (21, 'Kentucky/KY'),
    (22, 'Louisiana/LA'),
    (23, 'Maine/ME'),
    (24, 'Maryland/MD'),
    (25, 'Massachusetts/MA'),
    (26, 'Michigan/MI'),
    (27, 'Minnesota/MN'),
    (28, 'Mississippi/MS'),
    (29, 'Missouri/MO'),
    (30, 'Montana/MT'),
    (31, 'Nebraska/NE'),
    (32, 'Nevada/NV'),
    (33, 'New Hampshire/NH'),
    (34, 'New Jersey/NJ'),
    (35, 'New Mexico/NM'),
    (36, 'New York/NY'),
    (37, 'North Carolina/NC'),
    (38, 'North Dakota/ND'),
    (39, 'Ohio/OH'),
    (40, 'Oklahoma/OK'),
    (41, 'Oregon/OR'),
    (42, 'Pennsylvania/PA'),
    (44, 'Rhode Island/RI'),
    (45, 'South Carolina/SC'),
    (46, 'South Dakota/SD'),
    (47, 'Tennessee/TN'),
    (48, 'Texas/TX'),
    (49, 'Utah/UT'),
    (50, 'Vermont/VT'),
    (51, 'Virginia/VA'),
    (53, 'Washington/WA'),
    (54, 'West Virginia/WV'),
    (55, 'Wisconsin/WI'),
    (56, 'Wyoming/WY'),
    (72, 'Puerto Rico/PR'),
]

ADJUST = [
    (1015675, '2006 factor (1.015675)'),
]

PWGTP = [
    (0001..9999, 'Integer weight of person'),
]

AGEP = [
    (00, 'Under 1 year'),
    (01..99, '1 to 99 years (Top-coded***)'),
]

CIT = [
    (1, 'Born in the U.S. Born in the U.S., Guam, the U.S. Virgin Islands, or the Northern Marianas if current residence is Puerto Rico'),
    (2, 'Born in Puerto Rico, Guam, the U.S. Virgin Islands, or the Northern Marianas Born in Puerto Rico if current residence is Puerto Rico'),
    (3, 'Born abroad of American parents'),
    (4, 'U.S. citizen by naturalization'),
    (5, 'Not a citizen of the U.S.'),
]

COW = [
    (b, 'N/A (less than 16 years old/unemployed who never worked/NILF who last worked more than 5 years ago)'),
    (1, 'Employee of a private for profit company or business or of an individual, for wages, salary, or commissions'),
    (2, 'Employee of a private not-for-profit, tax-exempt, or charitable organization'),
    (3, 'Local government employee (city, county, etc.)'),
    (4, 'State government employee'),
    (5, 'Federal government employee'),
    (6, 'Self-employed in own not incorporated business, professional practice, or farm'),
    (7, 'Self-employed in own incorporated business, professional practice or farm'),
    (8, 'Working without pay in family business or farm'),
    (9, 'Unemployed'),
]

DDRS = [
    (b, 'N/A (Less than 5 years old)'),
    (1, 'Yes'),
    (2, 'No'),
]

DEYE = [
    (b, 'N/A (Less than 5 years old)'),
    (1, 'Yes'),
    (2, 'No'),
]

DOUT = [
    (b, 'N/A (Less than 16 years old)'),
    (1, 'Yes'),
    (2, 'No'),
]

DPHY = [
    (b, 'N/A (Less than 5 years old)'),
    (1, 'Yes'),
    (2, 'No'),
]

DREM = [
    (b, 'N/A (Less than 5 years old)'),
    (1, 'Yes'),
    (2, 'No'),
]

DWRK = [
    (b, 'N/A (Less than 16 years old)'),
    (1, 'Yes'),
    (2, 'No'),
]

ENG = [
    (b, 'N/A (less than 5 years old/speaks only English)'),
    (1, 'Very well'),
    (2, 'Well'),
    (3, 'Not well'),
    (4, 'Not at all'),
]

FER = [
    (b, 'N/A (less than 15 years/greater than 50 years/ male)'),
    (1, 'Yes'),
    (2, 'No'),
]

GCL = [
    (b, 'N/A (less than 30 years/institutional GQ)'),
    (1, 'Yes'),
    (2, 'No'),
]

GCM = [
    (b, 'N/A (less than 30 years/grandparent not responsible for grandchild/institutional GQ)'),
    (1, 'Less than 6 months'),
    (2, '6 to 11 months'),
    (3, '1 to 2 years'),
    (4, '3 to 4 years'),
    (5, '5 or more years'),
]

GCR = [
    (b, 'N/A (less than 30 years/grandchild not living in'),
    (1, 'Yes'),
    (2, 'No'),
]

INTP = [
    (bbbbbb, 'N/A (less than 15 years old)'),
    (000000, 'None'),
    (-09999, 'Loss of $9999 or more'),
    (-00001..-09998, 'Loss $1 to $9998'),
    (000001, '$1 or breakeven'),
    (000002..999999, '$2 to $999999 (Rounded and top-coded)'),
]

JWMNP = [
    (bbb, 'N/A (not a worker or worker who worked at home)'),
    (001..200, '1 to 200 minutes to get to work (Top-coded)'),
]

JWRIP = [
    (bb, 'N/A (not a worker or worker whose means of transportation to work was not car, truck, or van)'),
    (01, 'Drove alone'),
    (02, 'In 2-person carpool'),
    (03, 'In 3-person carpool'),
    (04, 'In 4-person carpool'),
    (05, 'In 5-person carpool'),
    (06, 'In 6-person carpool'),
    (07, 'In 7-person carpool'),
    (08, 'In 8-person carpool'),
    (09, 'In 9-person carpool'),
    (10, 'In 10-person or more carpool'),
]

JWTR = [
    (bb, 'N/A (not a worker--not in the labor force, including persons under 16 years; unemployed; employed, with a job but not at work; Armed Forces, with a job but not at work)'),
    (01, 'Car, truck, or van'),
    (02, 'Bus or trolley bus'),
    (03, 'Streetcar or trolley car (carro publico in Puerto Rico)'),
    (04, 'Subway or elevated'),
    (05, 'Railroad'),
    (06, 'Ferryboat'),
    (07, 'Taxicab'),
    (08, 'Motorcycle'),
    (09, 'Bicycle'),
    (10, 'Walked'),
    (11, 'Worked at home'),
    (12, 'Other method'),
]

LANX = [
    (b, 'N/A (less than 5 years old)'),
    (1, 'Yes, speaks another language'),
    (2, 'No, speaks only English'),
]

MAR = [
    (1, 'Married'),
    (2, 'Widowed'),
    (3, 'Divorced'),
    (4, 'Separated'),
    (5, 'Never married or under 15 years old'),
]

MIG = [
    (b, 'N/A(less than 1 year old)'),
    (1, 'Yes, same house (nonmovers)'),
    (2, 'No, outside US if current residence is US; No, outside Puerto Rico and US if current residence is Puerto Rico'),
    (3, 'No, different house in US if current residence is US; No, different house in Puerto Rico is current residence is Puerto Rico'),
]

MIL = [
    (b, 'N/A (less than 17 years old)'),
    (1, 'Yes, now on active duty'),
    (2, 'Yes, on active duty during the last 12 months, but not now'),
    (3, 'Yes, on active duty in the past, but not during the last 12 months'),
    (4, 'No, training for Reserves/National Guard only'),
    (5, 'No, never served in the military'),
]

MILY = [
    (b, 'N/A (less than 17 years/no active duty military service)'),
    (1, 'Less than 2 years of service'),
    (2, '2 years or more of service'),
]

MLPA = [
    (b, 'N/A (Less than 17 years old/no active duty)'),
    (0, 'Did not serve this period'),
    (1, 'Served this period'),
]

MLPB = [
    (b, 'N/A (Less than 17 years old/no active duty)'),
    (0, 'Did not serve this period'),
    (1, 'Served this period'),
]

MLPC = [
    (b, 'N/A (Less than 17 years old/no active duty)'),
    (0, 'Did not serve this period'),
    (1, 'Served this period'),
]

MLPD = [
    (b, 'N/A (Less than 17 years old/no active duty)'),
    (0, 'Did not serve this period'),
    (1, 'Served this period'),
]

MLPE = [
    (b, 'N/A (Less than 17 years old/no active duty)'),
    (0, 'Did not serve this period'),
    (1, 'Served this period'),
]

MLPF = [
    (b, 'N/A (Less than 17 years old/no active duty)'),
    (0, 'Did not serve this period'),
    (1, 'Served this period'),
]

MLPG = [
    (b, 'N/A (Less than 17 years old/no active duty)'),
    (0, 'Did not serve this period'),
    (1, 'Served this period'),
]

MLPH = [
    (b, 'N/A (Less than 17 years old/no active duty)'),
    (0, 'Did not serve this period'),
    (1, 'Served this period'),
]

MLPI = [
    (b, 'N/A (Less than 17 years old/no active duty)'),
    (0, 'Did not serve this period'),
    (1, 'Served this period'),
]

MLPJ = [
    (b, 'N/A (Less than 17 years old/no active duty)'),
    (0, 'Did not serve this period'),
    (1, 'Served this period'),
]

MLPK = [
    (b, 'N/A (Less than 17 years old/no active duty)'),
    (0, 'Did not serve this period'),
    (1, 'Served this period'),
]

NWAB = [
    (b, 'N/A (less than 16 years old/at work/on layoff)'),
    (1, 'Yes'),
    (2, 'No'),
    (3, 'Did not report'),
]

NWAV = [
    (b, 'N/A (less than 16 years/at work/not looking)'),
    (1, 'Yes'),
    (2, 'No, temporarily ill'),
    (3, 'No, other reasons'),
    (4, 'No, unspecified'),
    (5, 'Did not report'),
]

NWLA = [
    (b, 'N/A (less than 16 years old/at work)'),
    (1, 'Yes'),
    (2, 'No'),
    (3, 'Did not report'),
]

NWLK = [
    (b, 'N/A (less than 16 years old/at work/temporarily absent/informed of recall)'),
    (1, 'Yes'),
    (2, 'No'),
    (3, 'Did not report'),
]

NWRE = [
    (b, 'N/A (less than 16 years old/at work/not on layoff)'),
    (1, 'Yes'),
    (2, 'No'),
    (3, 'Did not report'),
]

OIP = [
    (bbbbbb, 'N/A (less than 15 years old)'),
    (000000, 'None'),
    (000001..999999, '$1 to $999999 (Rounded and top-coded)'),
]

PAP = [
    (bbbbb, 'N/A (less than 15 years old)'),
    (00000, 'None'),
    (00001..99999, '$1 to $99999 (Rounded)'),
]

REL = [
    (00, 'Reference person'),
    (01, 'Husband/wife'),
    (02, 'Son/daughter'),
    (03, 'Brother/sister'),
    (04, 'Father/mother'),
    (05, 'Grandchild'),
    (06, 'Inlaw'),
    (07, 'Other relative'),
    (08, 'Roomer/boarder'),
    (09, 'Housemate/roommate'),
    (10, 'Unmarried partner'),
    (11, 'Foster child'),
    (12, 'Other nonrelative'),
    (13, 'Institutionalized group quarters population'),
    (14, 'Noninstitutionalized group quarters population'),
]

RETP = [
    (bbbbbb, 'N/A (less than 15 years old)'),
    (000000, 'None'),
    (000001..999999, '$1 to $999999 (Rounded and top-coded)'),
]

SCH = [
    (b, 'N/A (less than 3 years old)'),
    (1, 'No, has not attended in the last 3 months'),
    (2, 'Yes, public school or public college'),
    (3, 'Yes, private school or private college'),
]

SCHG = [
    (b, 'N/A (not attending school)'),
    (1, 'Nursery school/preschool'),
    (2, 'Kindergarten'),
    (3, 'Grade 1 to grade 4'),
    (4, 'Grade 5 to grade 8'),
    (5, 'Grade 9 to grade 12'),
    (6, 'College undergraduate'),
    (7, 'Graduate or professional school'),
]

SCHL = [
    (bb, 'N/A (less than 3 years old)'),
    (01, 'No school completed'),
    (02, 'Nursery school to grade 4'),
    (03, 'Grade 5 or grade 6'),
    (04, 'Grade 7 or grade 8'),
    (05, 'Grade 9'),
    (06, 'Grade 10'),
    (07, 'Grade 11'),
    (08, 'Grade 12 no diploma'),
    (09, 'High school graduate'),
    (10, 'Some college, but less than 1 year'),
    (11, 'One or more years of college, no degree'),
    (12, 'Associate's degree'),
    (13, 'Bachelor's degree'),
    (14, 'Master's degree'),
    (15, 'Professional school degree'),
    (16, 'Doctorate degree'),
]

SEMP = [
    (bbbbbb, 'N/A (less than 15 years old)'),
    (000000, 'None'),
    (-09999, 'Loss of $9999 or more'),
    (-00001..-09998, 'Loss $1 to $9998'),
    (000001, '$1 or breakeven'),
    (000002..999999, '$2 to $999999 (Rounded and top-coded)'),
]

SEX = [
    (1, 'Male'),
    (2, 'Female'),
]

SSIP = [
    (bbbbb, 'N/A (less than 15 years old)'),
    (00000, 'None'),
    (00001..99999, '$1 to $99999 (Rounded)'),
]

SSP = [
    (bbbbb, 'N/A (less than 15 years old)'),
    (00000, 'None'),
    (00001..99999, '$1 to $99999 (Rounded)'),
]

WAGP = [
    (bbbbbb, 'N/A (less than 15 years old)'),
    (000000, 'None'),
    (000001..999999, '$1 to 999999 (Rounded and top-coded)'),
]

WKHP = [
    (bb, 'N/A (less than 16 years old/did not work during the past 12 months)'),
    (01..98, '1 to 98 usual hours'),
    (99, '99 or more usual hours'),
]

WKL = [
    (b, 'N/A (less than 16 years old)'),
    (1, 'Within the past 12 months'),
    (2, '1-5 years ago'),
    (3, 'Over 5 years ago or never worked'),
]

WKW = [
    (bb, 'N/A (less than 16 years old/did not work during the past 12 months)'),
    (01..52, '1 to 52 weeks worked past 12 months'),
]

YOEP = [
    (bbbb, 'Born in the US'),
    (1919, '1919 or earlier'),
    (1920, '1920'),
    (1921, '1921'),
    (1922, '1922'),
    (1923, '1923'),
    (1924, '1924'),
    (1925, '1925'),
    (1926, '1926'),
    (1927, '1927'),
    (1928, '1928'),
    (1929, '1929'),
    (1930, '1930'),
    (1931, '1931 or 1932'),
    (1933, '1933 or 1934'),
    (1935, '1935'),
    (1936, '1936'),
    (1937, '1937'),
    (1938, '1938'),
    (1939, '1939'),
    (1940, '1940'),
    (1941, '1941'),
    (1942, '1942'),
    (1943, '1943'),
    (1944, '1944'),
    (1945, '1945'),
    (1946, '1946'),
    (1947, '1947'),
    (1948, '1948'),
    (1949, '1949'),
    (1950, '1950'),
    (1951, '1951'),
    (1952, '1952'),
    (1953, '1953'),
    (1954, '1954'),
    (1955, '1955'),
    (1956, '1956'),
    (1957, '1957'),
    (1958, '1958'),
    (1959, '1959'),
    (1960, '1960'),
    (1961, '1961'),
    (1962, '1962'),
    (1963, '1963'),
    (1964, '1964'),
    (1965, '1965'),
    (1966, '1966'),
    (1967, '1967'),
    (1968, '1968'),
    (1969, '1969'),
    (1970, '1970'),
    (1971, '1971'),
    (1972, '1972'),
    (1973, '1973'),
    (1974, '1974'),
    (1975, '1975'),
    (1976, '1976'),
    (1977, '1977'),
    (1978, '1978'),
    (1979, '1979'),
    (1980, '1980'),
    (1981, '1981'),
    (1982, '1982'),
    (1983, '1983'),
    (1984, '1984'),
    (1985, '1985'),
    (1986, '1986'),
    (1987, '1987'),
    (1988, '1988'),
    (1989, '1989'),
    (1990, '1990'),
    (1991, '1991'),
    (1992, '1992'),
    (1993, '1993'),
    (1994, '1994'),
    (1995, '1995'),
    (1996, '1996'),
    (1997, '1997'),
    (1998, '1998'),
    (1999, '1999'),
    (2000, '2000'),
    (2001, '2001'),
    (2002, '2002'),
    (2003, '2003'),
    (2004, '2004'),
    (2005, '2005'),
    (2006, '2006'),
]

UWRK = [
    (b, 'N/A (less than 16 years/not reported)'),
    (1, 'Worked'),
    (2, 'Did not work'),
]

ANC = [
    (1, 'Single'),
    (2, 'Multiple'),
    (3, 'Unclassified'),
    (4, 'Not reported'),
]

ANC1P = [
    (001, 'Alsatian'),
    (003, 'Austrian'),
    (005, 'Basque'),
    (008, 'Belgian'),
    (009, 'Flemish'),
    (011, 'British'),
    (012, 'British Isles'),
    (020, 'Danish'),
    (021, 'Dutch'),
    (022, 'English'),
    (024, 'Finnish'),
    (026, 'French'),
    (032, 'German'),
    (040, 'Prussian'),
    (046, 'Greek'),
    (049, 'Icelander'),
    (050, 'Irish'),
    (051, 'Italian'),
    (068, 'Sicilian'),
    (077, 'Luxemburger'),
    (078, 'Maltese'),
    (082, 'Norwegian'),
    (084, 'Portuguese'),
    (087, 'Scotch Irish'),
    (088, 'Scottish'),
    (089, 'Swedish'),
    (091, 'Swiss'),
    (097, 'Welsh'),
    (098, 'Scandinavian'),
    (099, 'Celtic'),
    (100, 'Albanian'),
    (102, 'Belorussian'),
    (103, 'Bulgarian'),
    (109, 'Croatian'),
    (111, 'Czech'),
    (112, 'Bohemian'),
    (114, 'Czechoslovakian'),
    (115, 'Estonian'),
    (122, 'German Russian'),
    (124, 'Rom'),
    (125, 'Hungarian'),
    (128, 'Latvian'),
    (129, 'Lithuanian'),
    (130, 'Macedonian'),
    (142, 'Polish'),
    (144, 'Romanian'),
    (148, 'Russian'),
    (152, 'Serbian'),
    (153, 'Slovak'),
    (154, 'Slovene'),
    (170, 'Georgia CIS'),
    (171, 'Ukrainian'),
    (176, 'Yugoslavian'),
    (177, 'Herzegovinian'),
    (178, 'Slavic'),
    (179, 'Slavonian'),
    (183, 'Northern European'),
    (187, 'Western European'),
    (190, 'Eastern European'),
    (195, 'European'),
    (200, 'Spaniard'),
    (210, 'Mexican'),
    (211, 'Mexican American'),
    (212, 'Mexicano'),
    (213, 'Chicano'),
    (215, 'Mexican American Indian'),
    (218, 'Mexican State'),
    (221, 'Costa Rican'),
    (222, 'Guatemalan'),
    (223, 'Honduran'),
    (224, 'Nicaraguan'),
    (225, 'Panamanian'),
    (226, 'Salvadoran'),
    (227, 'Central American'),
    (231, 'Argentinean'),
    (232, 'Bolivian'),
    (233, 'Chilean'),
    (234, 'Colombian'),
    (235, 'Ecuadorian'),
    (236, 'Paraguayan'),
    (237, 'Peruvian'),
    (238, 'Uruguayan'),
    (239, 'Venezuelan'),
    (249, 'South American'),
    (250, 'Latin American'),
    (251, 'Latin'),
    (252, 'Latino'),
    (261, 'Puerto Rican'),
    (271, 'Cuban'),
    (275, 'Dominican'),
    (290, 'Hispanic'),
    (291, 'Spanish'),
    (295, 'Spanish American'),
    (300, 'Bahamian'),
    (301, 'Barbadian'),
    (302, 'Belizean'),
    (308, 'Jamaican'),
    (310, 'Dutch West Indian'),
    (314, 'Trinidadian Tobagonian'),
    (322, 'British West Indian'),
    (325, 'Antigua and Barbuda'),
    (329, 'Grenadian'),
    (330, 'Vincent-Grenadine Islander'),
    (331, 'St Lucia Islander'),
    (335, 'West Indian'),
    (336, 'Haitian'),
    (359, 'Other West Indian'),
    (360, 'Brazilian'),
    (370, 'Guyanese'),
    (400, 'Algerian'),
    (402, 'Egyptian'),
    (406, 'Moroccan'),
    (416, 'Iranian'),
    (417, 'Iraqi'),
    (419, 'Israeli'),
    (421, 'Jordanian'),
    (425, 'Lebanese'),
    (429, 'Syrian'),
    (431, 'Armenian'),
    (434, 'Turkish'),
    (435, 'Yemeni'),
    (442, 'Kurdish'),
    (465, 'Palestinian'),
    (483, 'Assyrian'),
    (484, 'Chaldean'),
    (490, 'Mideast'),
    (495, 'Arab'),
    (496, 'Arabic'),
    (499, 'Other Arab'),
    (508, 'Cameroon'),
    (510, 'Cape Verdean'),
    (522, 'Ethiopian'),
    (523, 'Eritrean'),
    (529, 'Ghanian'),
    (534, 'Kenyan'),
    (541, 'Liberian'),
    (553, 'Nigerian'),
    (564, 'Senegalese'),
    (566, 'Sierra Leonean'),
    (568, 'Somalian'),
    (570, 'South African'),
    (576, 'Sudanese'),
    (587, 'Other Subsaharan African'),
    (598, 'Western African'),
    (599, 'African'),
    (600, 'Afghan'),
    (603, 'Bangladeshi'),
    (609, 'Nepali'),
    (615, 'Asian Indian'),
    (618, 'Bengali'),
    (620, 'East Indian'),
    (650, 'Punjab'),
    (680, 'Pakistani'),
    (690, 'Sri Lankan'),
    (700, 'Burmese'),
    (703, 'Cambodian'),
    (706, 'Chinese'),
    (707, 'Cantonese'),
    (712, 'Mongolian'),
    (720, 'Filipino'),
    (730, 'Indonesian'),
    (740, 'Japanese'),
    (748, 'Okinawan'),
    (750, 'Korean'),
    (765, 'Laotian'),
    (768, 'Hmong'),
    (770, 'Malaysian'),
    (776, 'Thai'),
    (782, 'Taiwanese'),
    (785, 'Vietnamese'),
    (793, 'Eurasian'),
    (794, 'Amerasian'),
    (795, 'Asian'),
    (799, 'Other Asian'),
    (800, 'Austrailian'),
    (803, 'New Zealander'),
    (808, 'Polynesian'),
    (811, 'Hawaiian'),
    (814, 'Samoan'),
    (815, 'Tongan'),
    (820, 'Micronesian'),
    (821, 'Guamanian'),
    (822, 'Chamorro Islander'),
    (841, 'Fijian'),
    (850, 'Pacific Islander'),
    (899, 'Other Pacific'),
    (900, 'Afro American'),
    (901, 'Afro'),
    (902, 'African American'),
    (903, 'Black'),
    (904, 'Negro'),
    (907, 'Creole'),
    (913, 'Central American Indian'),
    (914, 'South American Indian'),
    (917, 'Native American'),
    (918, 'Indian'),
    (919, 'Cherokee'),
    (920, 'American Indian'),
    (921, 'Aleut'),
    (922, 'Eskimo'),
    (924, 'White'),
    (925, 'Anglo'),
    (927, 'Appalachian'),
    (929, 'Pennsylvania German'),
    (931, 'Canadian'),
    (935, 'French Canadian'),
    (936, 'Acadian'),
    (937, 'Cajun'),
    (939, 'American or United States'),
    (983, 'Texas'),
    (994, 'North American'),
    (995, 'Mixture'),
    (996, 'Uncodable entries'),
    (997, 'Other groups'),
    (998, 'Other responses'),
    (999, 'Not reported'),
]

ANC2P = [
    (001, 'Alsatian'),
    (003, 'Austrian'),
    (005, 'Basque'),
    (008, 'Belgian'),
    (009, 'Flemish'),
    (011, 'British'),
    (012, 'British Isles'),
    (020, 'Danish'),
    (021, 'Dutch'),
    (022, 'English'),
    (024, 'Finnish'),
    (026, 'French'),
    (032, 'German'),
    (040, 'Prussian'),
    (046, 'Greek'),
    (049, 'Icelander'),
    (050, 'Irish'),
    (051, 'Italian'),
    (068, 'Sicilian'),
    (077, 'Luxemburger'),
    (078, 'Maltese'),
    (082, 'Norwegian'),
    (084, 'Portuguese'),
    (087, 'Scotch Irish'),
    (088, 'Scottish'),
    (089, 'Swedish'),
    (091, 'Swiss'),
    (097, 'Welsh'),
    (098, 'Scandinavian'),
    (099, 'Celtic'),
    (100, 'Albanian'),
    (102, 'Belorussian'),
    (103, 'Bulgarian'),
    (109, 'Croatian'),
    (111, 'Czech'),
    (112, 'Bohemian'),
    (114, 'Czechoslovakian'),
    (115, 'Estonian'),
    (122, 'German Russian'),
    (124, 'Rom'),
    (125, 'Hungarian'),
    (128, 'Latvian'),
    (129, 'Lithuanian'),
    (130, 'Macedonian'),
    (142, 'Polish'),
    (144, 'Romanian'),
    (148, 'Russian'),
    (152, 'Serbian'),
    (153, 'Slovak'),
    (154, 'Slovene'),
    (170, 'Georgia CIS'),
    (171, 'Ukrainian'),
    (176, 'Yugoslavian'),
    (177, 'Herzegovinian'),
    (178, 'Slavic'),
    (179, 'Slavonian'),
    (183, 'Northern European'),
    (187, 'Western European'),
    (190, 'Eastern European'),
    (195, 'European'),
    (200, 'Spaniard'),
    (210, 'Mexican'),
    (211, 'Mexican American'),
    (212, 'Mexicano'),
    (213, 'Chicano'),
    (215, 'Mexican American Indian'),
    (218, 'Mexican State'),
    (221, 'Costa Rican'),
    (222, 'Guatemalan'),
    (223, 'Honduran'),
    (224, 'Nicaraguan'),
    (225, 'Panamanian'),
    (226, 'Salvadoran'),
    (227, 'Central American'),
    (231, 'Argentinean'),
    (232, 'Bolivian'),
    (233, 'Chilean'),
    (234, 'Colombian'),
    (235, 'Ecuadorian'),
    (236, 'Paraguayan'),
    (237, 'Peruvian'),
    (238, 'Uruguayan'),
    (239, 'Venezuelan'),
    (249, 'South American'),
    (250, 'Latin American'),
    (251, 'Latin'),
    (252, 'Latino'),
    (261, 'Puerto Rican'),
    (271, 'Cuban'),
    (275, 'Dominican'),
    (290, 'Hispanic'),
    (291, 'Spanish'),
    (295, 'Spanish American'),
    (300, 'Bahamian'),
    (301, 'Barbadian'),
    (302, 'Belizean'),
    (308, 'Jamaican'),
    (310, 'Dutch West Indian'),
    (314, 'Trinidadian Tobagonian'),
    (322, 'British West Indian'),
    (325, 'Antigua and Barbuda'),
    (329, 'Grenadian'),
    (330, 'Vincent-Grenadine Islander'),
    (331, 'St Lucia Islander'),
    (335, 'West Indian'),
    (336, 'Haitian'),
    (359, 'Other West Indian'),
    (360, 'Brazilian'),
    (370, 'Guyanese'),
    (400, 'Algerian'),
    (402, 'Egyptian'),
    (406, 'Moroccan'),
    (416, 'Iranian'),
    (417, 'Iraqi'),
    (419, 'Israeli'),
    (421, 'Jordanian'),
    (425, 'Lebanese'),
    (429, 'Syrian'),
    (431, 'Armenian'),
    (434, 'Turkish'),
    (435, 'Yemeni'),
    (442, 'Kurdish'),
    (465, 'Palestinian'),
    (483, 'Assyrian'),
    (484, 'Chaldean'),
    (490, 'Mideast'),
    (495, 'Arab'),
    (496, 'Arabic'),
    (499, 'Other Arab'),
    (508, 'Cameroon'),
    (510, 'Cape Verdean'),
    (522, 'Ethiopian'),
    (523, 'Eritrean'),
    (529, 'Ghanian'),
    (534, 'Kenyan'),
    (541, 'Liberian'),
    (553, 'Nigerian'),
    (564, 'Senegalese'),
    (566, 'Sierra Leonean'),
    (568, 'Somalian'),
    (570, 'South African'),
    (576, 'Sudanese'),
    (587, 'Other Subsaharan African'),
    (598, 'Western African'),
    (599, 'African'),
    (600, 'Afghan'),
    (603, 'Bangladeshi'),
    (609, 'Nepali'),
    (615, 'Asian Indian'),
    (618, 'Bengali'),
    (620, 'East Indian'),
    (650, 'Punjab'),
    (680, 'Pakistani'),
    (690, 'Sri Lankan'),
    (700, 'Burmese'),
    (703, 'Cambodian'),
    (706, 'Chinese'),
    (707, 'Cantonese'),
    (712, 'Mongolian'),
    (720, 'Filipino'),
    (730, 'Indonesian'),
    (740, 'Japanese'),
    (748, 'Okinawan'),
    (750, 'Korean'),
    (765, 'Laotian'),
    (768, 'Hmong'),
    (770, 'Malaysian'),
    (776, 'Thai'),
    (782, 'Taiwanese'),
    (785, 'Vietnamese'),
    (793, 'Eurasian'),
    (794, 'Amerasian'),
    (795, 'Asian'),
    (799, 'Other Asian'),
    (800, 'Austrailian'),
    (803, 'New Zealander'),
    (808, 'Polynesian'),
    (811, 'Hawaiian'),
    (814, 'Samoan'),
    (815, 'Tongan'),
    (820, 'Micronesian'),
    (821, 'Guamanian'),
    (822, 'Chamorro Islander'),
    (841, 'Fijian'),
    (850, 'Pacific Islander'),
    (899, 'Other Pacific'),
    (900, 'Afro American'),
    (901, 'Afro'),
    (902, 'African American'),
    (903, 'Black'),
    (904, 'Negro'),
    (907, 'Creole'),
    (913, 'Central American Indian'),
    (914, 'South American Indian'),
    (917, 'Native American'),
    (918, 'Indian'),
    (919, 'Cherokee'),
    (920, 'American Indian'),
    (921, 'Aleut'),
    (922, 'Eskimo'),
    (924, 'White'),
    (925, 'Anglo'),
    (927, 'Appalachian'),
    (929, 'Pennsylvania German'),
    (931, 'Canadian'),
    (935, 'French Canadian'),
    (936, 'Acadian'),
    (937, 'Cajun'),
    (939, 'American or United States'),
    (983, 'Texas'),
    (994, 'North American'),
    (995, 'Mixture'),
    (996, 'Uncodable entries'),
    (997, 'Other groups'),
    (998, 'Other responses'),
    (999, 'Not reported'),
]

DECADE = [
    (b, 'N/A (Born in the US)'),
    (1, 'Before 1950'),
    (2, '1950 - 1959'),
    (3, '1960 - 1969'),
    (4, '1970 - 1979'),
    (5, '1980 - 1989'),
    (6, '1990 - 1999'),
    (7, '2000 - 2009'),
]

DRIVESP = [
    (b, 'N/A (Nonworker or worker who does not drive to work)'),
    (1, '1.000 vehicles (Drove alone)'),
    (2, '0.500 vehicles (In a 2-person carpool)'),
    (3, '0.333 vehicles (In a 3-person carpool)'),
    (4, '0.250 vehicles (In a 4-person carpool)'),
    (5, '0.200 vehicles (In a 5- or 6-person carpool)'),
    (6, '0.143 vehicles (In a 7-or-more person carpool)'),
]

DS = [
    (b, 'N/A (Less than 5 years old)'),
    (1, 'With a disability'),
    (2, 'Without a disability'),
]

ESP = [
    (b, 'N/A (not own child of householder, and not child in subfamily) Living with two parents:'),
    (1, 'Both parents in labor force'),
    (2, 'Father only in labor force'),
    (3, 'Mother only in labor force'),
    (4, 'Neither parent in labor force Living with one parent: Living with father:'),
    (5, 'Father in the labor force'),
    (6, 'Father not in labor force Living with mother:'),
    (7, 'Mother in the labor force'),
    (8, 'Mother not in labor force'),
]

ESR = [
    (b, 'N/A (less than 16 years old)'),
    (1, 'Civilian employed, at work'),
    (2, 'Civilian employed, with a job but not at work'),
    (3, 'Unemployed'),
    (4, 'Armed forces, at work'),
    (5, 'Armed forces, with a job but not at work'),
    (6, 'Not in labor force'),
]

HISP = [
    (01, 'Not Spanish/Hispanic/Latino'),
    (02, 'Mexican'),
    (03, 'Puerto Rican'),
    (04, 'Cuban'),
    (05, 'Dominican'),
    (06, 'Costa Rican'),
    (07, 'Guatemalan'),
    (08, 'Honduran'),
    (09, 'Nicaraguan'),
    (10, 'Panamanian'),
    (11, 'Salvadoran'),
    (12, 'Other Central American'),
    (13, 'Argentinean'),
    (14, 'Bolivian'),
    (15, 'Chilean'),
    (16, 'Colombian'),
    (17, 'Ecuadorian'),
    (18, 'Paraguayan'),
    (19, 'Peruvian'),
    (20, 'Uruguayan'),
    (21, 'Venezuelan'),
    (22, 'Other South American'),
    (23, 'Spaniard'),
    (24, 'All Other Spanish/Hispanic/Latino'),
]

INDP = [
    (bbbb, 'N/A (less than 16 years old/unemployed who never worked/NILF who last worked more than 5 years ago)'),
    (0170, 'AGR-CROP PRODUCTION'),
    (0180, 'AGR-ANIMAL PRODUCTION'),
    (0190, 'AGR-FORESTRY EXCEPT LOGGING'),
    (0270, 'AGR-LOGGING'),
    (0280, 'AGR-FISHING, HUNTING, AND TRAPPING'),
    (0290, 'AGR-SUPPORT ACTIVITIES FOR AGRICULTURE AND FORESTRY'),
    (0370, 'EXT-OIL AND GAS EXTRACTION'),
    (0380, 'EXT-COAL MINING'),
    (0390, 'EXT-METAL ORE MINING'),
    (0470, 'EXT-NONMETALLIC MINERAL MINING AND QUARRYING'),
    (0480, 'EXT-NOT SPECIFIED TYPE OF MINING'),
    (0490, 'EXT-SUPPORT ACTIVITIES FOR MINING'),
    (0570, 'UTL-ELECTRIC POWER GENERATION, TRANSMISSION AND DISTRIBUTION'),
    (0580, 'UTL-NATURAL GAS DISTRIBUTION'),
    (0590, 'UTL-ELECTRIC AND GAS, AND OTHER COMBINATIONS'),
    (0670, 'UTL-WATER, STEAM, AIR CONDITIONING, AND IRRIGATION SYSTEMS'),
    (0680, 'UTL-SEWAGE TREATMENT FACILITIES'),
    (0690, 'UTL-NOT SPECIFIED UTILITIES'),
    (0770, 'CON-CONSTRUCTION, INCL CLEANING DURING AND IMM AFTER'),
    (1070, 'MFG-ANIMAL FOOD, GRAIN AND OILSEED MILLING'),
    (1080, 'MFG-SUGAR AND CONFECTIONERY PRODUCTS'),
    (1090, 'MFG-FRUIT AND VEGETABLE PRESERVING AND SPECIALTY FOODS'),
    (1170, 'MFG-DAIRY PRODUCTS'),
    (1180, 'MFG-ANIMAL SLAUGHTERING AND PROCESSING'),
    (1190, 'MFG-RETAIL BAKERIES'),
    (1270, 'MFG-BAKERIES, EXCEPT RETAIL'),
    (1280, 'MFG-SEAFOOD AND OTHER MISCELLANEOUS FOODS, N.E.C.'),
    (1290, 'MFG-NOT SPECIFIED FOOD INDUSTRIES'),
    (1370, 'MFG-BEVERAGE'),
    (1390, 'MFG-TOBACCO'),
    (1470, 'MFG-FIBER, YARN, AND THREAD MILLS'),
    (1480, 'MFG-FABRIC MILLS, EXCEPT KNITTING'),
    (1490, 'MFG-TEXTILE AND FABRIC FINISHING AND COATING MILLS'),
    (1570, 'MFG-CARPET AND RUG MILLS'),
    (1590, 'MFG-TEXTILE PRODUCT MILLS, EXCEPT CARPET AND RUG'),
    (1670, 'MFG-KNITTING MILLS'),
    (1680, 'MFG-CUT AND SEW APPAREL'),
    (1690, 'MFG-APPAREL ACCESSORIES AND OTHER APPAREL'),
    (1770, 'MFG-FOOTWEAR'),
    (1790, 'MFG-LEATHER TANNING AND PRODUCTS, EXCEPT FOOTWEAR'),
    (1870, 'MFG-PULP, PAPER, AND PAPERBOARD MILLS'),
    (1880, 'MFG-PAPERBOARD CONTAINERS AND BOXES'),
    (1890, 'MFG-MISCELLANEOUS PAPER AND PULP PRODUCTS'),
    (1990, 'MFG-PRINTING AND RELATED SUPPORT ACTIVITIES'),
    (2070, 'MFG-PETROLEUM REFINING'),
    (2090, 'MFG-MISCELLANEOUS PETROLEUM AND COAL PRODUCTS'),
    (2170, 'MFG-RESIN, SYNTHETIC RUBBER AND FIBERS, AND FILAMENTS'),
    (2180, 'MFG-AGRICULTURAL CHEMICALS'),
    (2190, 'MFG-PHARMACEUTICALS AND MEDICINES'),
    (2270, 'MFG-PAINT, COATING, AND ADHESIVES'),
    (2280, 'MFG-SOAP, CLEANING COMPOUND, AND COSMETICS'),
    (2290, 'MFG-INDUSTRIAL AND MISCELLANEOUS CHEMICALS'),
    (2370, 'MFG-PLASTICS PRODUCTS'),
    (2380, 'MFG-TIRES'),
    (2390, 'MFG-RUBBER PRODUCTS, EXCEPT TIRES'),
    (2470, 'MFG-POTTERY, CERAMICS, AND RELATED PRODUCTS'),
    (2480, 'MFG-STRUCTURAL CLAY PRODUCTS'),
    (2490, 'MFG-GLASS AND GLASS PRODUCTS'),
    (2570, 'MFG-CEMENT, CONCRETE, LIME, AND GYPSUM PRODUCTS'),
    (2590, 'MFG-MISCELLANEOUS NONMETALLIC MINERAL PRODUCTS'),
    (2670, 'MFG-IRON AND STEEL MILLS AND STEEL PRODUCTS'),
    (2680, 'MFG-ALUMINUM PRODUCTION AND PROCESSING'),
    (2690, 'MFG-NONFERROUS METAL, EXCEPT ALUMINUM, PRODUCTION AND PROCESSING'),
    (2770, 'MFG-FOUNDRIES'),
    (2780, 'MFG-METAL FORGINGS AND STAMPINGS'),
    (2790, 'MFG-CUTLERY AND HAND TOOLS'),
    (2870, 'MFG-STRUCTURAL METALS, AND TANK AND SHIPPING CONTAINERS'),
    (2880, 'MFG-MACHINE SHOPS; TURNED PRODUCTS; SCREWS, NUTS AND BOLTS'),
    (2890, 'MFG-COATING, ENGRAVING, HEAT TREATING AND ALLIED ACTIVITIES'),
    (2970, 'MFG-ORDNANCE'),
    (2980, 'MFG-MISCELLANEOUS FABRICATED METAL PRODUCTS'),
    (2990, 'MFG-NOT SPECIFIED METAL INDUSTRIES'),
    (3070, 'MFG-AGRICULTURAL IMPLEMENTS'),
    (3080, 'MFG-CONSTRUCTION, MINING AND OIL FIELD MACHINERY'),
    (3090, 'MFG-COMMERCIAL AND SERVICE INDUSTRY MACHINERY'),
    (3170, 'MFG-METALWORKING MACHINERY'),
    (3180, 'MFG-ENGINES, TURBINES, AND POWER TRANSMISSION EQUIPMENT'),
    (3190, 'MFG-MACHINERY, N.E.C.'),
    (3290, 'MFG-NOT SPECIFIED MACHINERY'),
    (3360, 'MFG-COMPUTER AND PERIPHERAL EQUIPMENT'),
    (3370, 'MFG-COMMUNICATIONS, AUDIO, AND VIDEO EQUIPMENT'),
    (3380, 'MFG-NAVIGATIONAL, MEASURING, ELECTROMEDICAL, AND CONTROL INSTRUMENTS'),
    (3390, 'MFG-ELECTRONIC COMPONENTS AND PRODUCTS, N.E.C.'),
    (3470, 'MFG-HOUSEHOLD APPLIANCES'),
    (3490, 'MFG-ELECTRICAL LIGHTING, EQUIPMENT, AND SUPPLIES, N.E.C.'),
    (3570, 'MFG-MOTOR VEHICLES AND MOTOR VEHICLE EQUIPMENT'),
    (3580, 'MFG-AIRCRAFT AND PARTS'),
    (3590, 'MFG-AEROSPACE PRODUCTS AND PARTS'),
    (3670, 'MFG-RAILROAD ROLLING STOCK'),
    (3680, 'MFG-SHIP AND BOAT BUILDING'),
    (3690, 'MFG-OTHER TRANSPORTATION EQUIPMENT'),
    (3770, 'MFG-SAWMILLS AND WOOD PRESERVATION'),
    (3780, 'MFG-VENEER, PLYWOOD, AND ENGINEERED WOOD PRODUCTS'),
    (3790, 'MFG-PREFABRICATED WOOD BUILDINGS AND MOBILE HOMES'),
    (3870, 'MFG-MISCELLANEOUS WOOD PRODUCTS'),
    (3890, 'MFG-FURNITURE AND RELATED PRODUCTS'),
    (3960, 'MFG-MEDICAL EQUIPMENT AND SUPPLIES'),
    (3970, 'MFG-TOYS, AMUSEMENT, AND SPORTING GOODS'),
    (3980, 'MFG-MISCELLANEOUS MANUFACTURING, N.E.C.'),
    (3990, 'MFG-NOT SPECIFIED MANUFACTURING INDUSTRIES'),
    (4070, 'WHL-MOTOR VEHICLES PARTS AND SUPPLIES MERCHANT WHOLESALERS'),
    (4080, 'WHL-FURNITURE AND HOME FURNISHING MERCHANT WHOLESALERS'),
    (4090, 'WHL-LUMBER AND OTHER CONSTRUCTION MATERIALS MERCHANT WHOLESALERS'),
    (4170, 'WHL-PROFESSIONAL AND COMMERCIAL EQUIPMENT AND SUPPLIES MERCHANT WHOLESALERS'),
    (4180, 'WHL-METALS AND MINERALS, EXCEPT PETROLEUM, MERCHANT WHOLESALERS'),
    (4190, 'WHL-ELECTRICAL GOODS MERCHANT WHOLESALERS'),
    (4260, 'WHL-HARDWARE, PLUMBING AND HEATING EQUIPMENT, AND SUPPLIES MERCHANT WHOLESALERS'),
    (4270, 'WHL-MACHINERY, EQUIPMENT, AND SUPPLIES MERCHANT WHOLESALERS'),
    (4280, 'WHL-RECYCLABLE MATERIAL MERCHANT WHOLESALERS'),
    (4290, 'WHL-MISCELLANEOUS DURABLE GOODS MERCHANT WHOLESALERS'),
    (4370, 'WHL-PAPER AND PAPER PRODUCTS MERCHANT WHOLESALERS'),
    (4380, 'WHL-DRUGS, SUNDRIES, AND CHEMICAL AND ALLIED PRODUCTS MERCHANT WHOLESALERS'),
    (4390, 'WHL-APPAREL, FABRICS, AND NOTIONS MERCHANT WHOLESALERS'),
    (4470, 'WHL-GROCERIES AND RELATED PRODUCTS MERCHANT WHOLESALERS'),
    (4480, 'WHL-FARM PRODUCT RAW MATERIALS MERCHANT WHOLESALERS'),
    (4490, 'WHL-PETROLEUM AND PETROLEUM PRODUCTS MERCHANT WHOLESALERS'),
    (4560, 'WHL-ALCOHOLIC BEVERAGES MERCHANT WHOLESALERS'),
    (4570, 'WHL-FARM SUPPLIES MERCHANT WHOLESALERS'),
    (4580, 'WHL-MISCELLANEOUS NONDURABLE GOODS MERCHANT WHOLESALERS'),
    (4585, 'WHL-ELECTRONIC MARKETS AGENTS AND BROKERS'),
    (4590, 'WHL-NOT SPECIFIED WHOLESALE TRADE'),
    (4670, 'RET-AUTOMOBILE DEALERS'),
    (4680, 'RET-OTHER MOTOR VEHICLE DEALERS'),
    (4690, 'RET-AUTO PARTS, ACCESSORIES, AND TIRE STORES'),
    (4770, 'RET-FURNITURE AND HOME FURNISHINGS STORES'),
    (4780, 'RET-HOUSEHOLD APPLIANCE STORES'),
    (4790, 'RET-RADIO, TV, AND COMPUTER STORES'),
    (4870, 'RET-BUILDING MATERIAL AND SUPPLIES DEALERS'),
    (4880, 'RET-HARDWARE STORES'),
    (4890, 'RET-LAWN AND GARDEN EQUIPMENT AND SUPPLIES STORES'),
    (4970, 'RET-GROCERY STORES'),
    (4980, 'RET-SPECIALTY FOOD STORES'),
    (4990, 'RET-BEER, WINE, AND LIQUOR STORES'),
    (5070, 'RET-PHARMACIES AND DRUG STORES'),
    (5080, 'RET-HEALTH AND PERSONAL CARE, EXCEPT DRUG, STORES'),
    (5090, 'RET-GASOLINE STATIONS'),
    (5170, 'RET-CLOTHING AND ACCESSORIES, EXCEPT SHOE, STORES'),
    (5180, 'RET-SHOE STORES'),
    (5190, 'RET-JEWELRY, LUGGAGE,AND LEATHER GOODS STORES'),
    (5270, 'RET-SPORTING GOODS, CAMERA, AND HOBBY AND TOY STORES'),
    (5280, 'RET-SEWING, NEEDLEWORK AND PIECE GOODS STORES'),
    (5290, 'RET-MUSIC STORES'),
    (5370, 'RET-BOOK STORES AND NEWS DEALERS'),
    (5380, 'RET-DEPARTMENT AND DISCOUNT STORES'),
    (5390, 'RET-MISCELLANEOUS GENERAL MERCHANDISE STORES'),
    (5470, 'RET-FLORISTS'),
    (5480, 'RET-OFFICE SUPPLIES AND STATIONARY STORES'),
    (5490, 'RET-USED MERCHANDISE STORES'),
    (5570, 'RET-GIFT, NOVELTY, AND SOUVENIR SHOPS'),
    (5580, 'RET-MISCELLANEOUS RETAIL STORES'),
    (5590, 'RET-ELECTRONIC SHOPPING'),
    (5591, 'RET-ELECTRONIC AUCTIONS'),
    (5592, 'RET-MAIL-ORDER HOUSES'),
    (5670, 'RET-VENDING MACHINE OPERATORS'),
    (5680, 'RET-FUEL DEALERS'),
    (5690, 'RET-OTHER DIRECT SELLING ESTABLISHMENTS'),
    (5790, 'RET-NOT SPECIFIED RETAIL TRADE'),
    (6070, 'TRN-AIR TRANSPORTATION'),
    (6080, 'TRN-RAIL TRANSPORTATION'),
    (6090, 'TRN-WATER TRANSPORTATION'),
    (6170, 'TRN-TRUCK TRANSPORTATION'),
    (6180, 'TRN-BUS SERVICE AND URBAN TRANSIT'),
    (6190, 'TRN-TAXI AND LIMOUSINE SERVICE'),
    (6270, 'TRN-PIPELINE TRANSPORTATION'),
    (6280, 'TRN-SCENIC AND SIGHTSEEING TRANSPORTATION'),
    (6290, 'TRN-SERVICES INCIDENTAL TO TRANSPORTATION'),
    (6370, 'TRN-POSTAL SERVICE'),
    (6380, 'TRN-COURIERS AND MESSENGERS'),
    (6390, 'TRN-WAREHOUSING AND STORAGE'),
    (6470, 'INF-NEWSPAPER PUBLISHERS'),
    (6480, 'INF-PUBLISHING, EXCEPT NEWSPAPERS AND SOFTWARE'),
    (6490, 'INF-SOFTWARE PUBLISHING'),
    (6570, 'INF-MOTION PICTURES AND VIDEO INDUSTRIES'),
    (6590, 'INF-SOUND RECORDING INDUSTRIES'),
    (6670, 'INF-RADIO AND TELEVISION BROADCASTING AND CABLE'),
    (6675, 'INF-INTERNET PUBLISHING AND BROADCASTING'),
    (6680, 'INF-WIRED TELECOMMUNICATIONS CARRIERS'),
    (6690, 'INF-OTHER TELECOMMUNICATION SERVICES'),
    (6692, 'INF-INTERNET SERVICE PROVIDERS'),
    (6695, 'INF-DATA PROCESSING, HOSTING, AND RELATED SERVICES'),
    (6770, 'INF-LIBRARIES AND ARCHIVES'),
    (6780, 'INF-OTHER INFORMATION SERVICES'),
    (6870, 'FIN-BANKING AND RELATED ACTIVITIES'),
    (6880, 'FIN-SAVINGS INSTITUTIONS, INCLUDING CREDIT UNIONS'),
    (6890, 'FIN-NON-DEPOSITORY CREDIT AND RELATED ACTIVITIES'),
    (6970, 'FIN-SECURITIES, COMMODITIES, FUNDS, TRUSTS, AND OTHER FINANCIAL INVESTMENTS'),
    (6990, 'FIN-INSURANCE CARRIERS AND RELATED ACTIVITIES'),
    (7070, 'FIN-REAL ESTATE'),
    (7080, 'FIN-AUTOMOTIVE EQUIPMENT RENTAL AND LEASING'),
    (7170, 'FIN-VIDEO TAPE AND DISK RENTAL'),
    (7180, 'FIN-OTHER CONSUMER GOODS RENTAL'),
    (7190, 'FIN-COMMERCIAL, INDUSTRIAL, AND OTHER INTANGIBLE ASSETS RENTAL AND LEASING'),
    (7270, 'PRF-LEGAL SERVICES'),
    (7280, 'PRF-ACCOUNTING, TAX PREPARATION, BOOKKEEPING AND PAYROLL SERVICES'),
    (7290, 'PRF-ARCHITECTURAL, ENGINEERING, AND RELATED SERVICES'),
    (7370, 'PRF-SPECIALIZED DESIGN SERVICES'),
    (7380, 'PRF-COMPUTER SYSTEMS DESIGN AND RELATED SERVICES'),
    (7390, 'PRF-MANAGEMENT, SCIENTIFIC, AND TECHNICAL CONSULTING SERVICES'),
    (7460, 'PRF-SCIENTIFIC RESEARCH AND DEVELOPMENT SERVICES'),
    (7470, 'PRF-ADVERTISING AND RELATED SERVICES'),
    (7480, 'PRF-VETERINARY SERVICES'),
    (7490, 'PRF-OTHER PROFESSIONAL, SCIENTIFIC, AND TECHNICAL SERVICES'),
    (7570, 'PRF-MANAGEMENT OF COMPANIES AND ENTERPRISES'),
    (7580, 'PRF-EMPLOYMENT SERVICES'),
    (7590, 'PRF-BUSINESS SUPPORT SERVICES'),
    (7670, 'PRF-TRAVEL ARRANGEMENTS AND RESERVATION SERVICES'),
    (7680, 'PRF-INVESTIGATION AND SECURITY SERVICES'),
    (7690, 'PRF-SERVICES TO BUILDINGS AND DWELLINGS, EX CONSTR CLN'),
    (7770, 'PRF-LANDSCAPING SERVICES'),
    (7780, 'PRF-OTHER ADMINISTRATIVE, AND OTHER SUPPORT SERVICES'),
    (7790, 'PRF-WASTE MANAGEMENT AND REMEDIATION SERVICES'),
    (7860, 'EDU-ELEMENTARY AND SECONDARY SCHOOLS'),
    (7870, 'EDU-COLLEGES AND UNIVERSITIES, INCLUDING JUNIOR COLLEGES'),
    (7880, 'EDU-BUSINESS, TECHNICAL, AND TRADE SCHOOLS AND TRAINING'),
    (7890, 'EDU-OTHER SCHOOLS, INSTRUCTION, AND EDUCATIONAL SERVICES'),
    (7970, 'MED-OFFICES OF PHYSICIANS'),
    (7980, 'MED-OFFICES OF DENTISTS'),
    (7990, 'MED-OFFICE OF CHIROPRACTORS'),
    (8070, 'MED-OFFICES OF OPTOMETRISTS'),
    (8080, 'MED-OFFICES OF OTHER HEALTH PRACTITIONERS'),
    (8090, 'MED-OUTPATIENT CARE CENTERS'),
    (8170, 'MED-HOME HEALTH CARE SERVICES'),
    (8180, 'MED-OTHER HEALTH CARE SERVICES'),
    (8190, 'MED-HOSPITALS'),
    (8270, 'MED-NURSING CARE FACILITIES'),
    (8290, 'MED-RESIDENTIAL CARE FACILITIES, WITHOUT NURSING'),
    (8370, 'SCA-INDIVIDUAL AND FAMILY SERVICES'),
    (8380, 'SCA-COMMUNITY FOOD AND HOUSING, AND EMERGENCY SERVICES'),
    (8390, 'SCA-VOCATIONAL REHABILITATION SERVICES'),
    (8470, 'SCA-CHILD DAY CARE SERVICES'),
    (8560, 'ENT-INDEPENDENT ARTISTS, PERFORMING ARTS, SPECTATOR SPORTS AND RELATED INDUSTRIES'),
    (8570, 'ENT-MUSEUMS, ART GALLERIES, HISTORICAL SITES, AND SIMILAR INSTITUTIONS'),
    (8580, 'ENT-BOWLING CENTERS'),
    (8590, 'ENT-OTHER AMUSEMENT, GAMBLING, AND RECREATION INDUSTRIES'),
    (8660, 'ENT-TRAVELER ACCOMMODATION'),
    (8670, 'ENT-RECREATIONAL VEHICLE PARKS AND CAMPS, AND ROOMING AND BOARDING HOUSES'),
    (8680, 'ENT-RESTAURANTS AND OTHER FOOD SERVICES'),
    (8690, 'ENT-DRINKING PLACES, ALCOHOLIC BEVERAGES'),
    (8770, 'SRV-AUTOMOTIVE REPAIR AND MAINTENANCE'),
    (8780, 'SRV-CAR WASHES'),
    (8790, 'SRV-ELECTRONIC AND PRECISION EQUIPMENT REPAIR AND MAINTENANCE'),
    (8870, 'SRV-COMMERCIAL AND INDUSTRIAL MACHINERY AND EQUIPMENT REPAIR AND MAINTENANCE'),
    (8880, 'SRV-PERSONAL AND HOUSEHOLD GOODS REPAIR AND MAINTENANCE'),
    (8970, 'SRV-BARBER SHOPS'),
    (8980, 'SRV-BEAUTY SALONS'),
    (8990, 'SRV-NAIL SALONS AND OTHER PERSONAL CARE SERVICES'),
    (9070, 'SRV-DRYCLEANING AND LAUNDRY SERVICES'),
    (9080, 'SRV-FUNERAL HOMES, CEMETERIES AND CREMATORIES'),
    (9090, 'SRV-OTHER PERSONAL SERVICES'),
    (9160, 'SRV-RELIGIOUS ORGANIZATIONS'),
    (9170, 'SRV-CIVIC, SOCIAL, ADVOCACY ORGANIZATIONS, AND GRANTMAKING AND GIVING SERVICES'),
    (9180, 'SRV-LABOR UNIONS'),
    (9190, 'SRV-BUSINESS, PROFESSIONAL, POLITICAL AND SIMILAR ORGANIZATIONS'),
    (9290, 'SRV-PRIVATE HOUSEHOLDS'),
    (9370, 'ADM-EXECUTIVE OFFICES AND LEGISLATIVE BODIES'),
    (9380, 'ADM-PUBLIC FINANCE ACTIVITIES'),
    (9390, 'ADM-OTHER GENERAL GOVERNMENT AND SUPPORT'),
    (9470, 'ADM-JUSTICE, PUBLIC ORDER, AND SAFETY ACTIVITIES'),
    (9480, 'ADM-ADMINISTRATION OF HUMAN RESOURCE PROGRAMS'),
    (9490, 'ADM-ADMINISTRATION OF ENVIRONMENTAL QUALITY AND HOUSING PROGRAMS'),
    (9570, 'ADM-ADMINISTRATION OF ECONOMIC PROGRAMS AND SPACE RESEARCH'),
    (9590, 'ADM-NATIONAL SECURITY AND INTERNATIONAL AFFAIRS'),
    (9670, 'MIL-U.S. ARMY'),
    (9680, 'MIL-U.S. AIR FORCE'),
    (9690, 'MIL-U.S. NAVY'),
    (9770, 'MIL-U.S. MARINES'),
    (9780, 'MIL-U.S. COAST GUARD'),
    (9790, 'MIL-U.S. ARMED FORCES, BRANCH NOT SPECIFIED'),
    (9870, 'MIL-MILITARY RESERVES OR NATIONAL GUARD'),
    (9920, 'UNEMPLOYED, WITH NO WORK EXPERIENCE IN THE LAST 5 YEARS **'),
]

JWAP = [
    (bbb, 'N/A (not a worker; worker who worked at home)'),
    (001, '12:00 a.m. to 12:04 a.m.'),
    (002, '12:05 a.m. to 12:09 a.m.'),
    (003, '12:10 a.m. to 12:14 a.m.'),
    (004, '12:15 a.m. to 12:19 a.m.'),
    (005, '12:20 a.m. to 12:24 a.m.'),
    (006, '12:25 a.m. to 12:29 a.m.'),
    (007, '12:30 a.m. to 12:39 a.m.'),
    (008, '12:40 a.m. to 12:44 a.m.'),
    (009, '12:45 a.m. to 12:49 a.m.'),
    (010, '12:50 a.m. to 12:59 a.m.'),
    (011, '1:00 a.m. to 1:04 a.m.'),
    (012, '1:05 a.m. to 1:09 a.m.'),
    (013, '1:10 a.m. to 1:14 a.m.'),
    (014, '1:15 a.m. to 1:19 a.m.'),
    (015, '1:20 a.m. to 1:24 a.m.'),
    (016, '1:25 a.m. to 1:29 a.m.'),
    (017, '1:30 a.m. to 1:34 a.m.'),
    (018, '1:35 a.m. to 1:39 a.m.'),
    (019, '1:40 a.m. to 1:44 a.m.'),
    (020, '1:45 a.m. to 1:49 a.m.'),
    (021, '1:50 a.m. to 1:59 a.m.'),
    (022, '2:00 a.m. to 2:04 a.m.'),
    (023, '2:05 a.m. to 2:09 a.m.'),
    (024, '2:10 a.m. to 2:14 a.m.'),
    (025, '2:15 a.m. to 2:19 a.m.'),
    (026, '2:20 a.m. to 2:24 a.m.'),
    (027, '2:25 a.m. to 2:29 a.m.'),
    (028, '2:30 a.m. to 2:34 a.m.'),
    (029, '2:35 a.m. to 2:39 a.m.'),
    (030, '2:40 a.m. to 2:44 a.m.'),
    (031, '2:45 a.m. to 2:49 a.m.'),
    (032, '2:50 a.m. to 2:54 a.m.'),
    (033, '2:55 a.m. to 2:59 a.m.'),
    (034, '3:00 a.m. to 3:04 a.m.'),
    (035, '3:05 a.m. to 3:09 a.m.'),
    (036, '3:10 a.m. to 3:14 a.m.'),
    (037, '3:15 a.m. to 3:19 a.m.'),
    (038, '3:20 a.m. to 3:24 a.m.'),
    (039, '3:25 a.m. to 3:29 a.m.'),
    (040, '3:30 a.m. to 3:34 a.m.'),
    (041, '3:35 a.m. to 3:39 a.m.'),
    (042, '3:40 a.m. to 3:44 a.m.'),
    (043, '3:45 a.m. to 3:49 a.m.'),
    (044, '3:50 a.m. to 3:54 a.m.'),
    (045, '3:55 a.m. to 3:59 a.m.'),
    (046, '4:00 a.m. to 4:04 a.m.'),
    (047, '4:05 a.m. to 4:09 a.m.'),
    (048, '4:10 a.m. to 4:14 a.m.'),
    (049, '4:15 a.m. to 4:19 a.m.'),
    (050, '4:20 a.m. to 4:24 a.m.'),
    (051, '4:25 a.m. to 4:29 a.m.'),
    (052, '4:30 a.m. to 4:34 a.m.'),
    (053, '4:35 a.m. to 4:39 a.m.'),
    (054, '4:40 a.m. to 4:44 a.m.'),
    (055, '4:45 a.m. to 4:49 a.m.'),
    (056, '4:50 a.m. to 4:54 a.m.'),
    (057, '4:55 a.m. to 4:59 a.m.'),
    (058, '5:00 a.m. to 5:04 a.m.'),
    (059, '5:05 a.m. to 5:09 a.m.'),
    (060, '5:10 a.m. to 5:14 a.m.'),
    (061, '5:15 a.m. to 5:19 a.m.'),
    (062, '5:20 a.m. to 5:24 a.m.'),
    (063, '5:25 a.m. to 5:29 a.m.'),
    (064, '5:30 a.m. to 5:34 a.m.'),
    (065, '5:35 a.m. to 5:39 a.m.'),
    (066, '5:40 a.m. to 5:44 a.m.'),
    (067, '5:45 a.m. to 5:49 a.m.'),
    (068, '5:50 a.m. to 5:54 a.m.'),
    (069, '5:55 a.m. to 5:59 a.m.'),
    (070, '6:00 a.m. to 6:04 a.m.'),
    (071, '6:05 a.m. to 6:09 a.m.'),
    (072, '6:10 a.m. to 6:14 a.m.'),
    (073, '6:15 a.m. to 6:19 a.m.'),
    (074, '6:20 a.m. to 6:24 a.m.'),
    (075, '6:25 a.m. to 6:29 a.m.'),
    (076, '6:30 a.m. to 6:34 a.m.'),
    (077, '6:35 a.m. to 6:39 a.m.'),
    (078, '6:40 a.m. to 6:44 a.m.'),
    (079, '6:45 a.m. to 6:49 a.m.'),
    (080, '6:50 a.m. to 6:54 a.m.'),
    (081, '6:55 a.m. to 6:59 a.m.'),
    (082, '7:00 a.m. to 7:04 a.m.'),
    (083, '7:05 a.m. to 7:09 a.m.'),
    (084, '7:10 a.m. to 7:14 a.m.'),
    (085, '7:15 a.m. to 7:19 a.m.'),
    (086, '7:20 a.m. to 7:24 a.m.'),
    (087, '7:25 a.m. to 7:29 a.m.'),
    (088, '7:30 a.m. to 7:34 a.m.'),
    (089, '7:35 a.m. to 7:39 a.m.'),
    (090, '7:40 a.m. to 7:44 a.m.'),
    (091, '7:45 a.m. to 7:49 a.m.'),
    (092, '7:50 a.m. to 7:54 a.m.'),
    (093, '7:55 a.m. to 7:59 a.m.'),
    (094, '8:00 a.m. to 8:04 a.m.'),
    (095, '8:05 a.m. to 8:09 a.m.'),
    (096, '8:10 a.m. to 8:14 a.m.'),
    (097, '8:15 a.m. to 8:19 a.m.'),
    (098, '8:20 a.m. to 8:24 a.m.'),
    (099, '8:25 a.m. to 8:29 a.m.'),
    (100, '8:30 a.m. to 8:34 a.m.'),
    (101, '8:35 a.m. to 8:39 a.m.'),
    (102, '8:40 a.m. to 8:44 a.m.'),
    (103, '8:45 a.m. to 8:49 a.m.'),
    (104, '8:50 a.m. to 8:54 a.m.'),
    (105, '8:55 a.m. to 8:59 a.m.'),
    (106, '9:00 a.m. to 9:04 a.m.'),
    (107, '9:05 a.m. to 9:09 a.m.'),
    (108, '9:10 a.m. to 9:14 a.m.'),
    (109, '9:15 a.m. to 9:19 a.m.'),
    (110, '9:20 a.m. to 9:24 a.m.'),
    (111, '9:25 a.m. to 9:29 a.m.'),
    (112, '9:30 a.m. to 9:34 a.m.'),
    (113, '9:35 a.m. to 9:39 a.m.'),
    (114, '9:40 a.m. to 9:44 a.m.'),
    (115, '9:45 a.m. to 9:49 a.m.'),
    (116, '9:50 a.m. to 9:54 a.m.'),
    (117, '9:55 a.m. to 9:59 a.m.'),
    (118, '10:00 a.m. to 10:04 a.m.'),
    (119, '10:05 a.m. to 10:09 a.m.'),
    (120, '10:10 a.m. to 10:14 a.m.'),
    (121, '10:15 a.m. to 10:19 a.m.'),
    (122, '10:20 a.m. to 10:24 a.m.'),
    (123, '10:25 a.m. to 10:29 a.m.'),
    (124, '10:30 a.m. to 10:34 a.m.'),
    (125, '10:35 a.m. to 10:39 a.m.'),
    (126, '10:40 a.m. to 10:44 a.m.'),
    (127, '10:45 a.m. to 10:49 a.m.'),
    (128, '10:50 a.m. to 10:54 a.m.'),
    (129, '10:55 a.m. to 10:59 a.m.'),
    (130, '11:00 a.m. to 11:04 a.m.'),
    (131, '11:05 a.m. to 11:09 a.m.'),
    (132, '11:10 a.m. to 11:14 a.m.'),
    (133, '11:15 a.m. to 11:19 a.m.'),
    (134, '11:20 a.m. to 11:24 a.m.'),
    (135, '11:25 a.m. to 11:29 a.m.'),
    (136, '11:30 a.m. to 11:34 a.m.'),
    (137, '11:35 a.m. to 11:39 a.m.'),
    (138, '11:40 a.m. to 11:44 a.m.'),
    (139, '11:45 a.m. to 11:49 a.m.'),
    (140, '11:50 a.m. to 11:54 a.m.'),
    (141, '11:55 a.m. to 11:59 a.m.'),
    (142, '12:00 p.m. to 12:04 p.m.'),
    (143, '12:05 p.m. to 12:09 p.m.'),
    (144, '12:10 p.m. to 12:14 p.m.'),
    (145, '12:15 p.m. to 12:19 p.m.'),
    (146, '12:20 p.m. to 12:24 p.m.'),
    (147, '12:25 p.m. to 12:29 p.m.'),
    (148, '12:30 p.m. to 12:34 p.m.'),
    (149, '12:35 p.m. to 12:39 p.m.'),
    (150, '12:40 p.m. to 12:44 p.m.'),
    (151, '12:45 p.m. to 12:49 p.m.'),
    (152, '12:50 p.m. to 12:54 p.m.'),
    (153, '12:55 p.m. to 12:59 p.m.'),
    (154, '1:00 p.m. to 1:04 p.m.'),
    (155, '1:05 p.m. to 1:09 p.m.'),
    (156, '1:10 p.m. to 1:14 p.m.'),
    (157, '1:15 p.m. to 1:19 p.m.'),
    (158, '1:20 p.m. to 1:24 p.m.'),
    (159, '1:25 p.m. to 1:29 p.m.'),
    (160, '1:30 p.m. to 1:34 p.m.'),
    (161, '1:35 p.m. to 1:39 p.m.'),
    (162, '1:40 p.m. to 1:44 p.m.'),
    (163, '1:45 p.m. to 1:49 p.m.'),
    (164, '1:50 p.m. to 1:54 p.m.'),
    (165, '1:55 p.m. to 1:59 p.m.'),
    (166, '2:00 p.m. to 2:04 p.m.'),
    (167, '2:05 p.m. to 2:09 p.m.'),
    (168, '2:10 p.m. to 2:14 p.m.'),
    (169, '2:15 p.m. to 2:19 p.m.'),
    (170, '2:20 p.m. to 2:24 p.m.'),
    (171, '2:25 p.m. to 2:29 p.m.'),
    (172, '2:30 p.m. to 2:34 p.m.'),
    (173, '2:35 p.m. to 2:39 p.m.'),
    (174, '2:40 p.m. to 2:44 p.m.'),
    (175, '2:45 p.m. to 2:49 p.m.'),
    (176, '2:50 p.m. to 2:54 p.m.'),
    (177, '2:55 p.m. to 2:59 p.m.'),
    (178, '3:00 p.m. to 3:04 p.m.'),
    (179, '3:05 p.m. to 3:09 p.m.'),
    (180, '3:10 p.m. to 3:14 p.m.'),
    (181, '3:15 p.m. to 3:19 p.m.'),
    (182, '3:20 p.m. to 3:24 p.m.'),
    (183, '3:25 p.m. to 3:29 p.m.'),
    (184, '3:30 p.m. to 3:34 p.m.'),
    (185, '3:35 p.m. to 3:39 p.m.'),
    (186, '3:40 p.m. to 3:44 p.m.'),
    (187, '3:45 p.m. to 3:49 p.m.'),
    (188, '3:50 p.m. to 3:54 p.m.'),
    (189, '3:55 p.m. to 3:59 p.m.'),
    (190, '4:00 p.m. to 4:04 p.m.'),
    (191, '4:05 p.m. to 4:09 p.m.'),
    (192, '4:10 p.m. to 4:14 p.m.'),
    (193, '4:15 p.m. to 4:19 p.m.'),
    (194, '4:20 p.m. to 4:24 p.m.'),
    (195, '4:25 p.m. to 4:29 p.m.'),
    (196, '4:30 p.m. to 4:34 p.m.'),
    (197, '4:35 p.m. to 4:39 p.m.'),
    (198, '4:40 p.m. to 4:44 p.m.'),
    (199, '4:45 p.m. to 4:49 p.m.'),
    (200, '4:50 p.m. to 4:54 p.m.'),
    (201, '4:55 p.m. to 4:59 p.m.'),
    (202, '5:00 p.m. to 5:04 p.m.'),
    (203, '5:05 p.m. to 5:09 p.m.'),
    (204, '5:10 p.m. to 5:14 p.m.'),
    (205, '5:15 p.m. to 5:19 p.m.'),
    (206, '5:20 p.m. to 5:24 p.m.'),
    (207, '5:25 p.m. to 5:29 p.m.'),
    (208, '5:30 p.m. to 5:34 p.m.'),
    (209, '5:35 p.m. to 5:39 p.m.'),
    (210, '5:40 p.m. to 5:44 p.m.'),
    (211, '5:45 p.m. to 5:49 p.m.'),
    (212, '5:50 p.m. to 5:54 p.m.'),
    (213, '5:55 p.m. to 5:59 p.m.'),
    (214, '6:00 p.m. to 6:04 p.m.'),
    (215, '6:05 p.m. to 6:09 p.m.'),
    (216, '6:10 p.m. to 6:14 p.m.'),
    (217, '6:15 p.m. to 6:19 p.m.'),
    (218, '6:20 p.m. to 6:24 p.m.'),
    (219, '6:25 p.m. to 6:29 p.m.'),
    (220, '6:30 p.m. to 6:34 p.m.'),
    (221, '6:35 p.m. to 6:39 p.m.'),
    (222, '6:40 p.m. to 6:44 p.m.'),
    (223, '6:45 p.m. to 6:49 p.m.'),
    (224, '6:50 p.m. to 6:54 p.m.'),
    (225, '6:55 p.m. to 6:59 p.m.'),
    (226, '7:00 p.m. to 7:04 p.m.'),
    (227, '7:05 p.m. to 7:09 p.m.'),
    (228, '7:10 p.m. to 7:14 p.m.'),
    (229, '7:15 p.m. to 7:19 p.m.'),
    (230, '7:20 p.m. to 7:24 p.m.'),
    (231, '7:25 p.m. to 7:29 p.m.'),
    (232, '7:30 p.m. to 7:34 p.m.'),
    (233, '7:35 p.m. to 7:39 p.m.'),
    (234, '7:40 p.m. to 7:44 p.m.'),
    (235, '7:45 p.m. to 7:49 p.m.'),
    (236, '7:50 p.m. to 7:54 p.m.'),
    (237, '7:55 p.m. to 7:59 p.m.'),
    (238, '8:00 p.m. to 8:04 p.m.'),
    (239, '8:05 p.m. to 8:09 p.m.'),
    (240, '8:10 p.m. to 8:14 p.m.'),
    (241, '8:15 p.m. to 8:19 p.m.'),
    (242, '8:20 p.m. to 8:24 p.m.'),
    (243, '8:25 p.m. to 8:29 p.m.'),
    (244, '8:30 p.m. to 8:34 p.m.'),
    (245, '8:35 p.m. to 8:39 p.m.'),
    (246, '8:40 p.m. to 8:44 p.m.'),
    (247, '8:45 p.m. to 8:49 p.m.'),
    (248, '8:50 p.m. to 8:54 p.m.'),
    (249, '8:55 p.m. to 8:59 p.m.'),
    (250, '9:00 p.m. to 9:04 p.m.'),
    (251, '9:05 p.m. to 9:09 p.m.'),
    (252, '9:10 p.m. to 9:14 p.m.'),
    (253, '9:15 p.m. to 9:19 p.m.'),
    (254, '9:20 p.m. to 9:24 p.m.'),
    (255, '9:25 p.m. to 9:29 p.m.'),
    (256, '9:30 p.m. to 9:34 p.m.'),
    (257, '9:35 p.m. to 9:39 p.m.'),
    (258, '9:40 p.m. to 9:44 p.m.'),
    (259, '9:45 p.m. to 9:49 p.m.'),
    (260, '9:50 p.m. to 9:54 p.m.'),
    (261, '9:55 p.m. to 9:59 p.m.'),
    (262, '10:00 p.m. to 10:04 p.m.'),
    (263, '10:05 p.m. to 10:09 p.m.'),
    (264, '10:10 p.m. to 10:14 p.m.'),
    (265, '10:15 p.m. to 10:19 p.m.'),
    (266, '10:20 p.m. to 10:24 p.m.'),
    (267, '10:25 p.m. to 10:29 p.m.'),
    (268, '10:30 p.m. to 10:34 p.m.'),
    (269, '10:35 p.m. to 10:39 p.m.'),
    (270, '10:40 p.m. to 10:44 p.m.'),
    (271, '10:45 p.m. to 10:49 p.m.'),
    (272, '10:50 p.m. to 10:55 p.m.'),
    (273, '10:55 p.m. to 10:59 p.m.'),
    (274, '11:00 p.m. to 11:04 p.m.'),
    (275, '11:05 p.m. to 11:09 p.m.'),
    (276, '11:10 p.m. to 11:14 p.m.'),
    (277, '11:15 p.m. to 11:19 p.m.'),
    (278, '11:20 p.m. to 11:24 p.m.'),
    (279, '11:25 p.m. to 11:29 p.m.'),
    (280, '11:30 p.m. to 11:34 p.m.'),
    (281, '11:35 p.m. to 11:39 p.m.'),
    (282, '11:40 p.m. to 11:44 p.m.'),
    (283, '11:45 p.m. to 11:49 p.m.'),
    (284, '11:50 p.m. to 11:54 p.m.'),
    (285, '11:55 p.m. to 11:59 p.m.'),
]

JWDP = [
    (bbb, 'N/A (not a worker; worker who worked at home)'),
    (001, '12:00 a.m. to 12:29 a.m.'),
    (002, '12:30 a.m. to 12:59 a.m.'),
    (003, '1:00 a.m. to 1:29 a.m.'),
    (004, '1:30 a.m. to 1:59 a.m.'),
    (005, '2:00 a.m. to 2:29 a.m.'),
    (006, '2:30 a.m. to 2:59 a.m.'),
    (007, '3:00 a.m. to 3:09 a.m.'),
    (008, '3:10 a.m. to 3:19 a.m.'),
    (009, '3:20 a.m. to 3:29 a.m.'),
    (010, '3:30 a.m. to 3:39 a.m.'),
    (011, '3:40 a.m. to 3:49 a.m.'),
    (012, '3:50 a.m. to 3:59 a.m.'),
    (013, '4:00 a.m. to 4:09 a.m.'),
    (014, '4:10 a.m. to 4:19 a.m.'),
    (015, '4:20 a.m. to 4:29 a.m.'),
    (016, '4:30 a.m. to 4:39 a.m.'),
    (017, '4:40 a.m. to 4:49 a.m.'),
    (018, '4:50 a.m. to 4:59 a.m.'),
    (019, '5:00 a.m. to 5:04 a.m.'),
    (020, '5:05 a.m. to 5:09 a.m.'),
    (021, '5:10 a.m. to 5:14 a.m.'),
    (022, '5:15 a.m. to 5:19 a.m.'),
    (023, '5:20 a.m. to 5:24 a.m.'),
    (024, '5:25 a.m. to 5:29 a.m.'),
    (025, '5:30 a.m. to 5:34 a.m.'),
    (026, '5:35 a.m. to 5:39 a.m.'),
    (027, '5:40 a.m. to 5:44 a.m.'),
    (028, '5:45 a.m. to 5:49 a.m.'),
    (029, '5:50 a.m. to 5:54 a.m.'),
    (030, '5:55 a.m. to 5:59 a.m.'),
    (031, '6:00 a.m. to 6:04 a.m.'),
    (032, '6:05 a.m. to 6:09 a.m.'),
    (033, '6:10 a.m. to 6:14 a.m.'),
    (034, '6:15 a.m. to 6:19 a.m.'),
    (035, '6:20 a.m. to 6:24 a.m.'),
    (036, '6:25 a.m. to 6:29 a.m.'),
    (037, '6:30 a.m. to 6:34 a.m.'),
    (038, '6:35 a.m. to 6:39 a.m.'),
    (039, '6:40 a.m. to 6:44 a.m.'),
    (040, '6:45 a.m. to 6:49 a.m.'),
    (041, '6:50 a.m. to 6:54 a.m.'),
    (042, '6:55 a.m. to 6:59 a.m.'),
    (043, '7:00 a.m. to 7:04 a.m.'),
    (044, '7:05 a.m. to 7:09 a.m.'),
    (045, '7:10 a.m. to 7:14 a.m.'),
    (046, '7:15 a.m. to 7:19 a.m.'),
    (047, '7:20 a.m. to 7:24 a.m.'),
    (048, '7:25 a.m. to 7:29 a.m.'),
    (049, '7:30 a.m. to 7:34 a.m.'),
    (050, '7:35 a.m. to 7:39 a.m.'),
    (051, '7:40 a.m. to 7:44 a.m.'),
    (052, '7:45 a.m. to 7:49 a.m.'),
    (053, '7:50 a.m. to 7:54 a.m.'),
    (054, '7:55 a.m. to 7:59 a.m.'),
    (055, '8:00 a.m. to 8:04 a.m.'),
    (056, '8:05 a.m. to 8:09 a.m.'),
    (057, '8:10 a.m. to 8:14 a.m.'),
    (058, '8:15 a.m. to 8:19 a.m.'),
    (059, '8:20 a.m. to 8:24 a.m.'),
    (060, '8:25 a.m. to 8:29 a.m.'),
    (061, '8:30 a.m. to 8:34 a.m.'),
    (062, '8:35 a.m. to 8:39 a.m.'),
    (063, '8:40 a.m. to 8:44 a.m.'),
    (064, '8:45 a.m. to 8:49 a.m.'),
    (065, '8:50 a.m. to 8:54 a.m.'),
    (066, '8:55 a.m. to 8:59 a.m.'),
    (067, '9:00 a.m. to 9:04 a.m.'),
    (068, '9:05 a.m. to 9:09 a.m.'),
    (069, '9:10 a.m. to 9:14 a.m.'),
    (070, '9:15 a.m. to 9:19 a.m.'),
    (071, '9:20 a.m. to 9:24 a.m.'),
    (072, '9:25 a.m. to 9:29 a.m.'),
    (073, '9:30 a.m. to 9:34 a.m.'),
    (074, '9:35 a.m. to 9:39 a.m.'),
    (075, '9:40 a.m. to 9:44 a.m.'),
    (076, '9:45 a.m. to 9:49 a.m.'),
    (077, '9:50 a.m. to 9:54 a.m.'),
    (078, '9:55 a.m. to 9:59 a.m.'),
    (079, '10:00 a.m. to 10:09 a.m.'),
    (080, '10:10 a.m. to 10:19 a.m.'),
    (081, '10:20 a.m. to 10:29 a.m.'),
    (082, '10:30 a.m. to 10:39 a.m.'),
    (083, '10:40 a.m. to 10:49 a.m.'),
    (084, '10:50 a.m. to 10:59 a.m.'),
    (085, '11:00 a.m. to 11:09 a.m.'),
    (086, '11:10 a.m. to 11:19 a.m.'),
    (087, '11:20 a.m. to 11:29 a.m.'),
    (088, '11:30 a.m. to 11:39 a.m.'),
    (089, '11:40 a.m. to 11:49 a.m.'),
    (090, '11:50 a.m. to 11:59 a.m.'),
    (091, '12:00 p.m. to 12:09 p.m.'),
    (092, '12:10 p.m. to 12:19 p.m.'),
    (093, '12:20 p.m. to 12:29 p.m.'),
    (094, '12:30 p.m. to 12:39 p.m.'),
    (095, '12:40 p.m. to 12:49 p.m.'),
    (096, '12:50 p.m. to 12:59 p.m.'),
    (097, '1:00 p.m. to 1:09 p.m.'),
    (098, '1:10 p.m. to 1:19 p.m.'),
    (099, '1:20 p.m. to 1:29 p.m.'),
    (100, '1:30 p.m. to 1:39 p.m.'),
    (101, '1:40 p.m. to 1:49 p.m.'),
    (102, '1:50 p.m. to 1:59 p.m.'),
    (103, '2:00 p.m. to 2:09 p.m.'),
    (104, '2:10 p.m. to 2:19 p.m.'),
    (105, '2:20 p.m. to 2:29 p.m.'),
    (106, '2:30 p.m. to 2:39 p.m.'),
    (107, '2:40 p.m. to 2:49 p.m.'),
    (108, '2:50 p.m. to 2:59 p.m.'),
    (109, '3:00 p.m. to 3:09 p.m.'),
    (110, '3:10 p.m. to 3:19 p.m.'),
    (111, '3:20 p.m. to 3:29 p.m.'),
    (112, '3:30 p.m. to 3:39 p.m.'),
    (113, '3:40 p.m. to 3:49 p.m.'),
    (114, '3:50 p.m. to 3:59 p.m.'),
    (115, '4:00 p.m. to 4:09 p.m.'),
    (116, '4:10 p.m. to 4:19 p.m.'),
    (117, '4:20 p.m. to 4:29 p.m.'),
    (118, '4:30 p.m. to 4:39 p.m.'),
    (119, '4:40 p.m. to 4:49 p.m.'),
    (120, '4:50 p.m. to 4:59 p.m.'),
    (121, '5:00 p.m. to 5:09 p.m.'),
    (122, '5:10 p.m. to 5:19 p.m.'),
    (123, '5:20 p.m. to 5:29 p.m.'),
    (124, '5:30 p.m. to 5:39 p.m.'),
    (125, '5:40 p.m. to 5:49 p.m.'),
    (126, '5:50 p.m. to 5:59 p.m.'),
    (127, '6:00 p.m. to 6:09 p.m.'),
    (128, '6:10 p.m. to 6:19 p.m.'),
    (129, '6:20 p.m. to 6:29 p.m.'),
    (130, '6:30 p.m. to 6:39 p.m.'),
    (131, '6:40 p.m. to 6:49 p.m.'),
    (132, '6:50 p.m. to 6:59 p.m.'),
    (133, '7:00 p.m. to 7:29 p.m.'),
    (134, '7:30 p.m. to 7:59 p.m.'),
    (135, '8:00 p.m. to 8:29 p.m.'),
    (136, '8:30 p.m. to 8:59 p.m.'),
    (137, '9:00 p.m. to 9:09 p.m.'),
    (138, '9:10 p.m. to 9:19 p.m.'),
    (139, '9:20 p.m. to 9:29 p.m.'),
    (140, '9:30 p.m. to 9:39 p.m.'),
    (141, '9:40 p.m. to 9:49 p.m.'),
    (142, '9:50 p.m. to 9:59 p.m.'),
    (143, '10:00 p.m. to 10:09 p.m.'),
    (144, '10:10 p.m. to 10:19 p.m.'),
    (145, '10:20 p.m. to 10:29 p.m.'),
    (146, '10:30 p.m. to 10:39 p.m.'),
    (147, '10:40 p.m. to 10:49 p.m.'),
    (148, '10:50 p.m. to 10:59 p.m.'),
    (149, '11:00 p.m. to 11:29 p.m.'),
    (150, '11:30 p.m. to 11:59 p.m.'),
]

LANP = [
    (bbb, 'N/A (less than 5 years old/speaks only English)'),
    (601, 'Jamaican Creole'),
    (607, 'German'),
    (608, 'Pennsylvania Dutch'),
    (609, 'Yiddish'),
    (610, 'Dutch'),
    (611, 'Afrikaans'),
    (614, 'Swedish'),
    (615, 'Danish'),
    (616, 'Norwegian'),
    (619, 'Italian'),
    (620, 'French'),
    (622, 'Patois'),
    (623, 'French Creole'),
    (624, 'Cajun'),
    (625, 'Spanish'),
    (629, 'Portuguese'),
    (631, 'Romanian'),
    (635, 'Irish Gaelic'),
    (637, 'Greek'),
    (638, 'Albanian'),
    (639, 'Russian'),
    (641, 'Ukrainian'),
    (642, 'Czech'),
    (645, 'Polish'),
    (646, 'Slovak'),
    (647, 'Bulgarian'),
    (648, 'Macedonian'),
    (649, 'Serbocroatian'),
    (650, 'Croatian'),
    (651, 'Serbian'),
    (653, 'Lithuanian'),
    (654, 'Lettish'),
    (655, 'Armenian'),
    (656, 'Persian'),
    (657, 'Pashto'),
    (658, 'Kurdish'),
    (662, 'India n.e.c.'),
    (663, 'Hindi'),
    (664, 'Bengali'),
    (665, 'Panjabi'),
    (666, 'Marathi'),
    (667, 'Gujarathi'),
    (671, 'Urdu'),
    (674, 'Nepali'),
    (676, 'Pakistan n.e.c.'),
    (677, 'Sinhalese'),
    (679, 'Finnish'),
    (682, 'Hungarian'),
    (691, 'Turkish'),
    (701, 'Telugu'),
    (702, 'Kannada'),
    (703, 'Malayalam'),
    (704, 'Tamil'),
    (708, 'Chinese'),
    (711, 'Cantonese'),
    (712, 'Mandarin'),
    (714, 'Formosan'),
    (717, 'Burmese'),
    (720, 'Thai'),
    (721, 'Miao-yao, Mien'),
    (722, 'Hmong'),
    (723, 'Japanese'),
    (724, 'Korean'),
    (725, 'Laotian'),
    (726, 'Mon-Khmer, Cambodian'),
    (728, 'Vietnamese'),
    (732, 'Indonesian'),
    (739, 'Malay'),
    (742, 'Tagalog'),
    (743, 'Bisayan'),
    (744, 'Sebuano'),
    (746, 'Ilocano'),
    (752, 'Chamorro'),
    (767, 'Samoan'),
    (768, 'Tongan'),
    (776, 'Hawaiian'),
    (777, 'Arabic'),
    (778, 'Hebrew'),
    (779, 'Syriac'),
    (780, 'Amharic'),
    (783, 'Cushite'),
    (791, 'Swahili'),
    (792, 'Bantu'),
    (793, 'Mande'),
    (794, 'Fulani'),
    (796, 'Kru, Ibo, Yoruba'),
    (799, 'African'),
    (806, 'Other Algonquian languages'),
    (862, 'Apache'),
    (864, 'Navaho'),
    (907, 'Dakota'),
    (924, 'Keres'),
    (933, 'Cherokee'),
    (964, 'Zuni'),
    (966, 'American Indian'),
    (985, 'Other Indo-European languages'),
    (986, 'Other Asian languages'),
    (988, 'Other Pacific Island languages'),
    (989, 'Other specified African languages'),
    (990, 'Aleut-Eskimo languages'),
    (992, 'South/Central American Indian languages'),
    (993, 'Other Specified North American Indian languages'),
    (994, 'Other languages'),
    (996, 'Uncodable'),
]

MIGPUMA = [
    (bbbbb, 'N/A (person less than 1 year old/lived in same house 1 year ago)'),
    (00001, 'Did not live in the United States or in Puerto Rico one year ago'),
    (00002, 'Lived in Puerto Rico one year ago and current residence is in the U.S.'),
    (00100..08200, 'Assigned Migration PUMA. Use with MIGSP.'),
]

MIGSP = [
    (bbb, 'N/A (person less than 1 year old/lived in same house 1 year ago)'),
    (001, 'Alabama/AL'),
    (002, 'Alaska/AK'),
    (004, 'Arizona/AZ'),
    (005, 'Arkansas/AR'),
    (006, 'California/CA'),
    (008, 'Colorado/CO'),
    (009, 'Connecticut/CT'),
    (010, 'Delaware/DE'),
    (011, 'District of Columbia/DC'),
    (012, 'Florida/FL'),
    (013, 'Georgia/GA'),
    (015, 'Hawaii/HI'),
    (016, 'Idaho/ID'),
    (017, 'Illinois/IL'),
    (018, 'Indiana/IN'),
    (019, 'Iowa/IA'),
    (020, 'Kansas/KS'),
    (021, 'Kentucky/KY'),
    (022, 'Louisiana/LA'),
    (023, 'Maine/ME'),
    (024, 'Maryland/MD'),
    (025, 'Massachusetts/MA'),
    (026, 'Michigan/MI'),
    (027, 'Minnesota/MN'),
    (028, 'Mississippi/MS'),
    (029, 'Missouri/MO'),
    (030, 'Montana/MT'),
    (031, 'Nebraska/NE'),
    (032, 'Nevada/NV'),
    (033, 'New Hampshire/NH'),
    (034, 'New Jersey/NJ'),
    (035, 'New Mexico/NM'),
    (036, 'New York/NY'),
    (037, 'North Carolina/NC'),
    (038, 'North Dakota/ND'),
    (039, 'Ohio/OH'),
    (040, 'Oklahoma/OK'),
    (041, 'Oregon/OR'),
    (042, 'Pennsylvania/PA'),
    (044, 'Rhode Island/RI'),
    (045, 'South Carolina/SC'),
    (046, 'South Dakota/SD'),
    (047, 'Tennessee/TN'),
    (048, 'Texas/TX'),
    (049, 'Utah/UT'),
    (050, 'Vermont/VT'),
    (051, 'Virginia/VA'),
    (053, 'Washington/WA'),
    (054, 'West Virginia/WV'),
    (055, 'Wisconsin/WI'),
    (056, 'Wyoming/WY'),
    (072, 'Puerto Rico'),
    (096, 'US Island Areas, Not Specified'),
    (109, 'France'),
    (110, 'Germany'),
    (111, 'Northern Europe, Not Specified'),
    (112, 'Western Europe, Not Specified'),
    (113, 'Eastern Europe, Not Specified'),
    (120, 'Italy'),
    (128, 'Poland'),
    (138, 'United Kingdom, Excluding England'),
    (139, 'England'),
    (163, 'Russia'),
    (164, 'Ukraine'),
    (169, 'Other Europe, Not Specified'),
    (207, 'China, Hong Kong & Paracel Islands'),
    (210, 'India'),
    (213, 'Iraq'),
    (214, 'Israel'),
    (215, 'Japan'),
    (217, 'Korea'),
    (233, 'Philippines'),
    (240, 'Taiwan'),
    (242, 'Thailand'),
    (247, 'Vietnam'),
    (251, 'Eastern Asia, Not Specified'),
    (252, 'Western Asia, Not Specified'),
    (253, 'South Central Asia or Asia, Not Specified'),
    (301, 'Canada'),
    (303, 'Mexico'),
    (312, 'El Salvador'),
    (313, 'Guatemala'),
    (314, 'Honduras'),
    (317, 'Central America, Not Specified'),
    (327, 'Cuba'),
    (329, 'Domincan Republic'),
    (333, 'Jamaica'),
    (344, 'Caribbean and North America, Not Specified'),
    (362, 'Brazil'),
    (364, 'Colombia'),
    (370, 'Peru'),
    (374, 'South America, Not Specified'),
    (462, 'Africa'),
    (463, 'Eastern Africa, Not Specified'),
    (464, 'Northern Africa, Not Specified'),
    (467, 'Western Africa, Not Specified'),
    (468, 'Other Africa, Not Specified'),
    (501, 'Australia'),
    (554, 'Australian and New Zealand Subregions, Not Specified, Oceania and at Sea'),
]

MSP = [
    (b, 'N/A (less than 15 years old)'),
    (1, 'Now married, spouse present'),
    (2, 'Now married, spouse absent'),
    (3, 'Widowed'),
    (4, 'Divorced'),
    (5, 'Separated'),
    (6, 'Never married'),
]

NAICSP = [
    (bbbbbbbb, 'N/A (less than 16 years old/unemployed who never worked/NILF who last worked more than 5 years ago)'),
    (111, 'AGR-CROP PRODUCTION'),
    (112, 'AGR-ANIMAL PRODUCTION'),
    (1133, 'AGR-LOGGING'),
    (113M, 'AGR-FORESTRY EXCEPT LOGGING'),
    (114, 'AGR-FISHING, HUNTING, AND TRAPPING'),
    (115, 'AGR-SUPPORT ACTIVITIES FOR AGRICULTURE AND FORESTRY'),
    (211, 'EXT-OIL AND GAS EXTRACTION'),
    (2121, 'EXT-COAL MINING'),
    (2122, 'EXT-METAL ORE MINING'),
    (2123, 'EXT-NONMETALLIC MINERAL MINING AND QUARRYING'),
    (213, 'EXT-SUPPORT ACTIVITIES FOR MINING'),
    (21S, 'EXT-NOT SPECIFIED TYPE OF MINING'),
    (2211P, 'UTL-ELECTRIC POWER GENERATION, TRANSMISSION AND DISTRIBUTION'),
    (2212P, 'UTL-NATURAL GAS DISTRIBUTION'),
    (22132, 'UTL-SEWAGE TREATMENT FACILITIES'),
    (2213M, 'UTL-WATER, STEAM, AIR CONDITIONING, AND IRRIGATION SYSTEMS'),
    (221MP, 'UTL-ELECTRIC AND GAS, AND OTHER COMBINATIONS'),
    (22S, 'UTL-NOT SPECIFIED UTILITIES'),
    (23, 'CON-CONSTRUCTION, INCL CLEANING DURING AND IMM AFTER'),
    (3113, 'MFG-SUGAR AND CONFECTIONERY PRODUCTS'),
    (3114, 'MFG-FRUIT AND VEGETABLE PRESERVING AND SPECIALTY FOODS'),
    (3115, 'MFG-DAIRY PRODUCTS'),
    (3116, 'MFG-ANIMAL SLAUGHTERING AND PROCESSING'),
    (311811, 'MFG-RETAIL BAKERIES'),
    (3118Z, 'MFG-BAKERIES, EXCEPT RETAIL'),
    (311M1, 'MFG-ANIMAL FOOD, GRAIN AND OILSEED MILLING'),
    (311M2, 'MFG-SEAFOOD AND OTHER MISCELLANEOUS FOODS, N.E.C.'),
    (311S, 'MFG-NOT SPECIFIED FOOD INDUSTRIES'),
    (3121, 'MFG-BEVERAGE'),
    (3122, 'MFG-TOBACCO'),
    (3131, 'MFG-FIBER, YARN, AND THREAD MILLS'),
    (3132Z, 'MFG-FABRIC MILLS, EXCEPT KNITTING'),
    (3133, 'MFG-TEXTILE AND FABRIC FINISHING AND COATING MILLS'),
    (31411, 'MFG-CARPETS AND RUGS'),
    (314Z, 'MFG-TEXTILE PRODUCT MILLS, EXCEPT CARPETS AND RUGS'),
    (3152, 'MFG-CUT AND SEW APPAREL'),
    (3159, 'MFG-APPAREL ACCESSORIES AND OTHER APPAREL'),
    (3162, 'MFG-FOOTWEAR'),
    (316M, 'MFG-LEATHER TANNING AND PRODUCTS, EXCEPT FOOTWEAR'),
    (31M, 'MFG-KNITTING MILLS'),
    (3211, 'MFG-SAWMILLS AND WOOD PRESERVATION'),
    (3212, 'MFG-VENEER, PLYWOOD, AND ENGINEERED WOOD PRODUCTS'),
    (32199M, 'MFG-PREFABRICATED WOOD BUILDINGS AND MOBILE HOMES'),
    (3219ZM, 'MFG-MISCELLANEOUS WOOD PRODUCTS'),
    (3221, 'MFG-PULP, PAPER, AND PAPERBOARD MILLS'),
    (32221, 'MFG-PAPERBOARD CONTAINERS AND BOXES'),
    (3222M, 'MFG-MISCELLANEOUS PAPER AND PULP PRODUCTS'),
    (323, 'MFG-PRINTING AND RELATED SUPPORT ACTIVITIES'),
    (32411, 'MFG-PETROLEUM REFINING'),
    (3241M, 'MFG-MISCELLANEOUS PETROLEUM AND COAL PRODUCTS'),
    (3252, 'MFG-RESIN, SYNTHETIC RUBBER AND FIBERS, AND FILAMENTS'),
    (3253, 'MFG-AGRICULTURAL CHEMICALS'),
    (3254, 'MFG-PHARMACEUTICALS AND MEDICINES'),
    (3255, 'MFG-PAINT, COATING, AND ADHESIVES'),
    (3256, 'MFG-SOAP, CLEANING COMPOUND, AND COSMETICS'),
    (325M, 'MFG-INDUSTRIAL AND MISCELLANEOUS CHEMICALS'),
    (3261, 'MFG-PLASTICS PRODUCTS'),
    (32621, 'MFG-TIRES'),
    (3262M, 'MFG-RUBBER PRODUCTS, EXCEPT TIRES'),
    (32711, 'MFG-POTTERY, CERAMICS, AND RELATED PRODUCTS'),
    (32712, 'MFG-STRUCTURAL CLAY PRODUCTS'),
    (3272, 'MFG-GLASS AND GLASS PRODUCTS'),
    (3279, 'MFG-MISCELLANEOUS NONMETALLIC MINERAL PRODUCTS'),
    (327M, 'MFG-CEMENT, CONCRETE, LIME, AND GYPSUM PRODUCTS'),
    (3313, 'MFG-ALUMINUM PRODUCTION AND PROCESSING'),
    (3314, 'MFG-NONFERROUS METAL, EXCEPT ALUMINUM, PRODUCTION AND PROCESSING'),
    (3315, 'MFG-FOUNDRIES'),
    (331M, 'MFG-IRON AND STEEL MILLS AND STEEL PRODUCTS'),
    (3321, 'MFG-METAL FORGINGS AND STAMPINGS'),
    (3322, 'MFG-CUTLERY AND HAND TOOLS'),
    (3327, 'MFG-MACHINE SHOPS; TURNED PRODUCTS; SCREWS, NUTS AND BOLTS'),
    (3328, 'MFG-COATING, ENGRAVING, HEAT TREATING AND ALLIED ACTIVITIES'),
    (33299M, 'MFG-ORDNANCE'),
    (332M, 'MFG-STRUCTURAL METALS, AND TANK AND SHIPPING CONTAINERS'),
    (332MZ, 'MFG-MISCELLANEOUS FABRICATED METAL PRODUCTS'),
    (33311, 'MFG-AGRICULTURAL IMPLEMENTS'),
    (3331M, 'MFG-CONSTRUCTION, MINING AND OIL FIELD MACHINERY'),
    (3333, 'MFG-COMMERCIAL AND SERVICE INDUSTRY MACHINERY'),
    (3335, 'MFG-METALWORKING MACHINERY'),
    (3336, 'MFG-ENGINES, TURBINES, AND POWER TRANSMISSION EQUIPMENT'),
    (333M, 'MFG-MACHINERY, N.E.C.'),
    (333S, 'MFG-NOT SPECIFIED MACHINERY'),
    (3341, 'MFG-COMPUTER AND PERIPHERAL EQUIPMENT'),
    (3345, 'MFG-NAVIGATIONAL, MEASURING, ELECTROMEDICAL, AND CONTROL INSTRUMENTS'),
    (334M1, 'MFG-COMMUNICATIONS, AUDIO, AND VIDEO EQUIPMENT'),
    (334M2, 'MFG-ELECTRONIC COMPONENTS AND PRODUCTS, N.E.C.'),
    (3352, 'MFG-HOUSEHOLD APPLIANCES'),
    (335M, 'MFG-ELECTRICAL LIGHTING, EQUIPMENT, AND SUPPLIES, N.E.C.'),
    (33641M1, 'MFG-AIRCRAFT AND PARTS'),
    (33641M2, 'MFG-AEROSPACE PRODUCTS AND PARTS'),
    (3365, 'MFG-RAILROAD ROLLING STOCK'),
    (3366, 'MFG-SHIP AND BOAT BUILDING'),
    (3369, 'MFG-OTHER TRANSPORTATION EQUIPMENT'),
    (336M, 'MFG-MOTOR VEHICLES AND MOTOR VEHICLE EQUIPMENT'),
    (337, 'MFG-FURNITURE AND RELATED PRODUCTS'),
    (3391, 'MFG-MEDICAL EQUIPMENT AND SUPPLIES'),
    (3399M, 'MFG-TOYS, AMUSEMENT, AND SPORTING GOODS'),
    (3399ZM, 'MFG-MISCELLANEOUS MANUFACTURING, N.E.C.'),
    (33MS, 'MFG-NOT SPECIFIED METAL INDUSTRIES'),
    (3MS, 'MFG-NOT SPECIFIED INDUSTRIES'),
    (4231, 'WHL-MOTOR VEHICLES PARTS AND SUPPLIES MERCHANT WHOLESALERS'),
    (4232, 'WHL-FURNITURE AND HOME FURNISHING MERCHANT WHOLESALERS'),
    (4233, 'WHL-LUMBER AND OTHER CONSTRUCTION MATERIALS MERCHANT WHOLESALERS'),
    (4234, 'WHL-PROFESSIONAL AND COMMERCIAL EQUIPMENT AND SUPPLIES MERCHANT WHOLESALERS'),
    (4235, 'WHL-METALS AND MINERALS, EXCEPT PETROLEUM, MERCHANT WHOLESALERS'),
    (4236, 'WHL-ELECTRICAL GOODS MERCHANT WHOLESALERS'),
    (4237, 'WHL-HARDWARE, PLUMBING AND HEATING EQUIPMENT, AND SUPPLIES MERCHANT WHOLESALERS'),
    (4238, 'WHL-MACHINERY, EQUIPMENT, AND SUPPLIES MERCHANT WHOLESALERS'),
    (42393, 'WHL-RECYCLABLE MATERIAL MERCHANT WHOLESALERS'),
    (4239Z, 'WHL-MISCELLANEOUS DURABLE GOODS MERCHANT WHOLESALERS'),
    (4241, 'WHL-PAPER AND PAPER PRODUCTS MERCHANT WHOLESALERS'),
    (4243, 'WHL-APPAREL, FABRICS, AND NOTIONS MERCHANT WHOLESALERS'),
    (4244, 'WHL-GROCERIES AND RELATED PRODUCTS MERCHANT WHOLESALERS'),
    (4245, 'WHL-FARM PRODUCT RAW MATERIALS MERCHANT WHOLESALERS'),
    (4247, 'WHL-PETROLEUM AND PETROLEUM PRODUCTS MERCHANT WHOLESALERS'),
    (4248, 'WHL-ALCOHOLIC BEVERAGES MERCHANT WHOLESALERS'),
    (42491, 'WHL-FARM SUPPLIES MERCHANT WHOLESALERS'),
    (4249Z, 'WHL-MISCELLANEOUS NONDURABLE GOODS MERCHANT WHOLESALERS'),
    (424M, 'WHL-DRUGS, SUNDRIES, AND CHEMICAL AND ALLIED PRODUCTS MERCHANT WHOLESALERS'),
    (4251, 'WHL-ELECTRONIC MARKETS AGENTS AND BROKERS'),
    (42S, 'WHL-NOT SPECIFIED TRADE'),
    (4411, 'RET-AUTOMOBILE DEALERS'),
    (4412, 'RET-OTHER MOTOR VEHICLE DEALERS'),
    (4413, 'RET-AUTO PARTS, ACCESSORIES, AND TIRE STORES'),
    (442, 'RET-FURNITURE AND HOME FURNISHINGS STORES'),
    (443111, 'RET-HOUSEHOLD APPLIANCE STORES'),
    (4431M, 'RET-RADIO, TV, AND COMPUTER STORES'),
    (44413, 'RET-HARDWARE STORES'),
    (4441Z, 'RET-BUILDING MATERIAL AND SUPPLIES DEALERS'),
    (4442, 'RET-LAWN AND GARDEN EQUIPMENT AND SUPPLIES STORES'),
    (4451, 'RET-GROCERY STORES'),
    (4452, 'RET-SPECIALTY FOOD STORES'),
    (4453, 'RET-BEER, WINE, AND LIQUOR STORES'),
    (44611, 'RET-PHARMACIES AND DRUG STORES'),
    (446Z, 'RET-HEALTH AND PERSONAL CARE, EXCEPT DRUG, STORES'),
    (447, 'RET-GASOLINE STATIONS'),
    (44821, 'RET-SHOE STORES'),
    (4483, 'RET-JEWELRY, LUGGAGE,AND LEATHER GOODS STORES'),
    (448ZM, 'RET-CLOTHING AND ACCESSORIES, EXCEPT SHOE, STORES'),
    (45113, 'RET-SEWING, NEEDLEWORK AND PIECE GOODS STORES'),
    (45121, 'RET-BOOK STORES AND NEWS DEALERS'),
    (451M, 'RET-MUSIC STORES'),
    (45211, 'RET-DEPARTMENT AND DISCOUNT STORES'),
    (4529, 'RET-MISCELLANEOUS GENERAL MERCHANDISE STORES'),
    (4531, 'RET-FLORISTS'),
    (45321, 'RET-OFFICE SUPPLIES AND STATIONARY STORES'),
    (45322, 'RET-GIFT, NOVELTY, AND SOUVENIR SHOPS'),
    (4533, 'RET-USED MERCHANDISE STORES'),
    (4539, 'RET-MISCELLANEOUS STORES'),
    (454111, 'RET-ELECTRONIC SHOPPING'),
    (454112, 'RET-ELECTRONIC AUCTIONS'),
    (454113, 'RET-MAIL-ORDER HOUSES'),
    (4542, 'RET-VENDING MACHINE OPERATORS'),
    (45431, 'RET-FUEL DEALERS'),
    (45439, 'RET-OTHER DIRECT SELLING ESTABLISHMENTS'),
    (4M, 'RET-SPORTING GOODS, CAMERA, AND HOBBY AND TOY STORES'),
    (4MS, 'RET-NOT SPECIFIED TRADE'),
    (481, 'TRN-AIR TRANSPORTATION'),
    (482, 'TRN-RAIL TRANSPORTATION'),
    (483, 'TRN-WATER TRANSPORTATION'),
    (484, 'TRN-TRUCK TRANSPORTATION'),
    (4853, 'TRN-TAXI AND LIMOUSINE SERVICE'),
    (485M, 'TRN-BUS SERVICE AND URBAN TRANSIT'),
    (486, 'TRN-PIPELINE TRANSPORTATION'),
    (487, 'TRN-SCENIC AND SIGHTSEEING TRANSPORTATION'),
    (488, 'TRN-SERVICES INCIDENTAL TO TRANSPORTATION'),
    (491, 'TRN-POSTAL SERVICE'),
    (492, 'TRN-COURIERS AND MESSENGERS'),
    (493, 'TRN-WAREHOUSING AND STORAGE'),
    (51111, 'INF-NEWSPAPER PUBLISHERS'),
    (5111Z, 'INF-PUBLISHING, EXCEPT NEWSPAPERS AND SOFTWARE'),
    (5112, 'INF-SOFTWARE PUBLISHING'),
    (5121, 'INF-MOTION PICTURES AND VIDEO INDUSTRIES'),
    (5122, 'INF-SOUND RECORDING INDUSTRIES'),
    (5161, 'INF-INTERNET PUBLISHING AND BROADCASTING'),
    (5171, 'INF-WIRED TELECOMMUNICATIONS CARRIERS'),
    (517Z, 'INF-OTHER TELECOMMUNICATION SERVICES'),
    (5181, 'INF-INTERNET SERVICE PROVIDERS'),
    (5182, 'INF-DATA PROCESSING, HOSTING, AND RELATED SERVICES'),
    (51912, 'INF-LIBRARIES AND ARCHIVES'),
    (5191Z, 'INF-OTHER INFORMATION SERVICES'),
    (51M, 'INF-RADIO AND TELEVISION BROADCASTING AND CABLE'),
    (5221M, 'FIN-SAVINGS INSTITUTIONS, INCLUDING CREDIT UNIONS'),
    (522M, 'FIN-NON-DEPOSITORY CREDIT AND RELATED ACTIVITIES'),
    (524, 'FIN-INSURANCE CARRIERS AND RELATED ACTIVITIES'),
    (52M1, 'FIN-BANKING AND RELATED ACTIVITIES'),
    (52M2, 'FIN-SECURITIES, COMMODITIES, FUNDS, TRUSTS, AND OTHER FINANCIAL INVESTMENTS'),
    (531, 'FIN-REAL ESTATE'),
    (5321, 'FIN-AUTOMOTIVE EQUIPMENT RENTAL AND LEASING'),
    (53223, 'FIN-VIDEO TAPE AND DISK RENTAL'),
    (532M, 'FIN-OTHER CONSUMER GOODS RENTAL'),
    (53M, 'FIN-COMMERCIAL, INDUSTRIAL, AND OTHER INTANGIBLE ASSETS RENTAL AND LEASING'),
    (5411, 'PRF-LEGAL SERVICES'),
    (5412, 'PRF-ACCOUNTING, TAX PREPARATION, BOOKKEEPING AND PAYROLL SERVICES'),
    (5413, 'PRF-ARCHITECTURAL, ENGINEERING, AND RELATED SERVICES'),
    (5414, 'PRF-SPECIALIZED DESIGN SERVICES'),
    (5415, 'PRF-COMPUTER SYSTEMS DESIGN AND RELATED SERVICES'),
    (5416, 'PRF-MANAGEMENT, SCIENTIFIC AND TECHNICAL CONSULTING SERVICES'),
    (5417, 'PRF-SCIENTIFIC RESEARCH AND DEVELOPMENT SERVICES'),
    (5418, 'PRF-ADVERTISING AND RELATED SERVICES'),
    (54194, 'PRF-VETERINARY SERVICES'),
    (5419Z, 'PRF-OTHER PROFESSIONAL, SCIENTIFIC AND TECHNICAL SERVICES'),
    (55, 'PRF-MANAGEMENT OF COMPANIES AND ENTERPRISES'),
    (5613, 'PRF-EMPLOYMENT SERVICES'),
    (5614, 'PRF-BUSINESS SUPPORT SERVICES'),
    (5615, 'PRF-TRAVEL ARRANGEMENTS AND RESERVATION SERVICES'),
    (5616, 'PRF-INVESTIGATION AND SECURITY SERVICES'),
    (56173, 'PRF-LANDSCAPING SERVICES'),
    (5617Z, 'PRF-SERVICES TO BUILDINGS AND DWELLINGS, EX CONSTR CLN'),
    (561M, 'PRF-OTHER ADMINISTRATIVE, AND OTHER SUPPORT SERVICES'),
    (562, 'PRF-WASTE MANAGEMENT AND REMEDIATION SERVICES'),
    (6111, 'EDU-ELEMENTARY AND SECONDARY SCHOOLS'),
    (611M1, 'EDU-COLLEGES AND UNIVERSITIES, INCLUDING JUNIOR COLLEGES'),
    (611M2, 'EDU-BUSINESS, TECHNICAL, AND TRADE SCHOOLS AND TRAINING'),
    (611M3, 'EDU-OTHER SCHOOLS, INSTRUCTION, AND EDUCATIONAL SERVICES'),
    (6211, 'MED-OFFICES OF PHYSICIANS'),
    (6212, 'MED-OFFICES OF DENTISTS'),
    (62131, 'MED-OFFICE OF CHIROPRACTORS'),
    (62132, 'MED-OFFICES OF OPTOMETRISTS'),
    (6213ZM, 'MED-OFFICES OF OTHER HEALTH PRACTITIONERS'),
    (6214, 'MED-OUTPATIENT CARE CENTERS'),
    (6216, 'MED-HOME HEALTH CARE SERVICES'),
    (621M, 'MED-OTHER HEALTH CARE SERVICES'),
    (622, 'MED-HOSPITALS'),
    (6231, 'MED-NURSING CARE FACILITIES'),
    (623M, 'MED-RESIDENTIAL CARE FACILITIES, WITHOUT NURSING'),
    (6241, 'SCA-INDIVIDUAL AND FAMILY SERVICES'),
    (6242, 'SCA-COMMUNITY FOOD AND HOUSING, AND EMERGENCY SERVICES'),
    (6243, 'SCA-VOCATIONAL REHABILITATION SERVICES'),
    (6244, 'SCA-CHILD DAY CARE SERVICES'),
    (711, 'ENT-INDEPENDENT ARTISTS, PERFORMING ARTS, SPECTATOR SPORTS AND RELATED INDUSTRIES'),
    (712, 'ENT-MUSEUMS, ART GALLERIES, HISTORICAL SITES, AND SIMILAR INSTITUTIONS'),
    (71395, 'ENT-BOWLING CENTERS'),
    (713Z, 'ENT-OTHER AMUSEMENT, GAMBLING, AND RECREATION INDUSTRIES'),
    (7211, 'ENT-TRAVELER ACCOMMODATION'),
    (721M, 'ENT-RECREATIONAL VEHICLE PARKS AND CAMPS, AND ROOMING AND BOARDING HOUSES'),
    (7224, 'ENT-DRINKING PLACES, ALCOHOLIC BEVERAGES'),
    (722Z, 'ENT-RESTAURANTS AND OTHER FOOD SERVICES'),
    (811192, 'SRV-CAR WASHES'),
    (8111Z, 'SRV-AUTOMOTIVE REPAIR AND MAINTENANCE'),
    (8112, 'SRV-ELECTRONIC AND PRECISION EQUIPMENT REPAIR AND MAINTENANCE'),
    (8113, 'SRV-COMMERCIAL AND INDUSTRIAL MACHINERY AND EQUIPMENT REPAIR AND MAINTENANCE'),
    (8114, 'SRV-PERSONAL AND HOUSEHOLD GOODS REPAIR AND MAINTENANCE'),
    (812111, 'SRV-BARBER SHOPS'),
    (812112, 'SRV-BEAUTY SALONS'),
    (8121M, 'SRV-NAIL SALONS AND OTHER PERSONAL CARE SERVICES'),
    (8122, 'SRV-FUNERAL HOMES, CEMETERIES AND CREMATORIES'),
    (8123, 'SRV-DRYCLEANING AND LAUNDRY SERVICES'),
    (8129, 'SRV-OTHER PERSONAL SERVICES'),
    (8131, 'SRV-RELIGIOUS ORGANIZATIONS'),
    (81393, 'SRV-LABOR UNIONS'),
    (8139Z, 'SRV-BUSINESS, PROFESSIONAL, POLITICAL AND SIMILAR ORGANIZATIONS'),
    (813M, 'SRV-CIVIC, SOCIAL, ADVOCACY ORGANIZATIONS, AND GRANTMAKING AND GIVING SERVICES'),
    (814, 'SRV-PRIVATE HOUSEHOLDS'),
    (92113, 'ADM-PUBLIC FINANCE ACTIVITIES'),
    (92119, 'ADM-OTHER GENERAL GOVERNMENT AND SUPPORT'),
    (9211MP, 'ADM-EXECUTIVE OFFICES AND LEGISLATIVE BODIES'),
    (923, 'ADM-ADMINISTRATION OF HUMAN RESOURCE PROGRAMS'),
    (928110P1, 'MIL-U.S. ARMY'),
    (928110P2, 'MIL-U.S. AIR FORCE'),
    (928110P3, 'MIL-U.S. NAVY'),
    (928110P4, 'MIL-U.S. MARINES'),
    (928110P5, 'MIL-U.S. COAST GUARD'),
    (928110P6, 'MIL-U.S. ARMED FORCES, BRANCH NOT SPECIFIED'),
    (928110P7, 'MIL-MILITARY RESERVES OR NATIONAL GUARD'),
    (928P, 'ADM-NATIONAL SECURITY AND INTERNATIONAL AFFAIRS'),
    (92M1, 'ADM-ADMINISTRATION OF ENVIRONMENTAL QUALITY AND HOUSING PROGRAMS'),
    (92M2, 'ADM-ADMINISTRATION OF ECONOMIC PROGRAMS AND SPACE RESEARCH'),
    (92MP, 'ADM-JUSTICE, PUBLIC ORDER, AND SAFETY ACTIVITIES'),
    (9920, 'UNEMPLOYED, WITH NO WORK EXPERIENCE IN THE LAST 5 YEARS **'),
]

NATIVITY = [
    (1, 'Native'),
    (2, 'Foreign born'),
]

NOP = [
    (b, 'N/A (greater than 17 years old/not an own child of householder, and not child in subfamily)'),
    (1, 'Living with two parents: Both parents NATIVE'),
    (2, 'Living with two parents: Father only FOREIGN BORN'),
    (3, 'Living with two parents: Mother only FOREIGN BORN'),
    (4, 'Living with two parents: BOTH parents FOREIGN BORN'),
    (5, 'Living with father only: Father NATIVE'),
    (6, 'Living with father only: Father FOREIGN BORN'),
    (7, 'Living with mother only: Mother NATIVE'),
    (8, 'Living with mother only: Mother FOREIGN BORN'),
]

OC = [
    (0, 'No (includes GQ)'),
    (1, 'Yes'),
]

OCCP = [
    (bbbb, 'N/A (less than 16 years old/unemployed who never worked/NILF who last worked more than 5 years ago)'),
    (0010, 'MGR-CHIEF EXECUTIVES AND LEGISLATORS'),
    (0020, 'MGR-GENERAL AND OPERATIONS MANAGERS'),
    (0040, 'MGR-ADVERTISING AND PROMOTIONS MANAGERS'),
    (0050, 'MGR-MARKETING AND SALES MANAGERS'),
    (0060, 'MGR-PUBLIC RELATIONS MANAGERS'),
    (0100, 'MGR-ADMINISTRATIVE SERVICES MANAGERS'),
    (0110, 'MGR-COMPUTER AND INFORMATION SYSTEMS MANAGERS'),
    (0120, 'MGR-FINANCIAL MANAGERS'),
    (0130, 'MGR-HUMAN RESOURCES MANAGERS'),
    (0140, 'MGR-INDUSTRIAL PRODUCTION MANAGERS'),
    (0150, 'MGR-PURCHASING MANAGERS'),
    (0160, 'MGR-TRANSPORTATION, STORAGE, AND DISTRIBUTION MANAGERS'),
    (0200, 'MGR-FARM, RANCH, AND OTHER AGRICULTURAL MANAGERS'),
    (0210, 'MGR-FARMERS AND RANCHERS'),
    (0220, 'MGR-CONSTRUCTION MANAGERS'),
    (0230, 'MGR-EDUCATION ADMINISTRATORS'),
    (0300, 'MGR-ENGINEERING MANAGERS'),
    (0310, 'MGR-FOOD SERVICE MANAGERS'),
    (0320, 'MGR-FUNERAL DIRECTORS'),
    (0330, 'MGR-GAMING MANAGERS'),
    (0340, 'MGR-LODGING MANAGERS'),
    (0350, 'MGR-MEDICAL AND HEALTH SERVICES MANAGERS'),
    (0360, 'MGR-NATURAL SCIENCES MANAGERS'),
    (0410, 'MGR-PROPERTY, REAL ESTATE, AND COMMUNITY ASSOCIATION MANAGERS'),
    (0420, 'MGR-SOCIAL AND COMMUNITY SERVICE MANAGERS'),
    (0430, 'MGR-MISCELLANEOUS MANAGERS, INCLUDING POSTMASTERS AND MAIL SUPERINTENDENTS'),
    (0500, 'BUS-AGENTS AND BUSINESS MANAGERS OF ARTISTS, PERFORMERS, AND ATHLETES'),
    (0510, 'BUS-PURCHASING AGENTS AND BUYERS, FARM PRODUCTS'),
    (0520, 'BUS-WHOLESALE AND RETAIL BUYERS, EXCEPT FARM PRODUCTS'),
    (0530, 'BUS-PURCHASING AGENTS, EXCEPT WHOLESALE, RETAIL, AND FARM PRODUCTS'),
    (0540, 'BUS-CLAIMS ADJUSTERS, APPRAISERS, EXAMINERS, AND INVESTIGATORS'),
    (0560, 'BUS-COMPLIANCE OFFICERS, EXCEPT AGRICULTURE, CONSTRUCTION, HEALTH AND SAFETY, AND TRANSPORTATION'),
    (0600, 'BUS-COST ESTIMATORS'),
    (0620, 'BUS-HUMAN RESOURCES, TRAINING, AND LABOR RELATIONS SPECIALISTS'),
    (0700, 'BUS-LOGISTICIANS'),
    (0710, 'BUS-MANAGEMENT ANALYSTS'),
    (0720, 'BUS-MEETING AND CONVENTION PLANNERS'),
    (0730, 'BUS-OTHER BUSINESS OPERATIONS SPECIALISTS'),
    (0800, 'FIN-ACCOUNTANTS AND AUDITORS'),
    (0810, 'FIN-APPRAISERS AND ASSESSORS OF REAL ESTATE'),
    (0820, 'FIN-BUDGET ANALYSTS'),
    (0830, 'FIN-CREDIT ANALYSTS'),
    (0840, 'FIN-FINANCIAL ANALYSTS'),
    (0850, 'FIN-PERSONAL FINANCIAL ADVISORS'),
    (0860, 'FIN-INSURANCE UNDERWRITERS'),
    (0900, 'FIN-FINANCIAL EXAMINERS'),
    (0910, 'FIN-LOAN COUNSELORS AND OFFICERS'),
    (0930, 'FIN-TAX EXAMINERS, COLLECTORS, AND REVENUE AGENTS'),
    (0940, 'FIN-TAX PREPARERS'),
    (0950, 'FIN-FINANCIAL SPECIALISTS, ALL OTHER'),
    (1000, 'CMM-COMPUTER SCIENTISTS AND SYSTEMS ANALYSTS'),
    (1010, 'CMM-COMPUTER PROGRAMMERS'),
    (1020, 'CMM-COMPUTER SOFTWARE ENGINEERS'),
    (1040, 'CMM-COMPUTER SUPPORT SPECIALISTS'),
    (1060, 'CMM-DATABASE ADMINISTRATORS'),
    (1100, 'CMM-NETWORK AND COMPUTER SYSTEMS ADMINISTRATORS'),
    (1110, 'CMM-NETWORK SYSTEMS AND DATA COMMUNICATIONS ANALYSTS'),
    (1200, 'CMM-ACTUARIES'),
    (1220, 'CMM-OPERATIONS RESEARCH ANALYSTS'),
    (1240, 'CMM-MISCELLANEOUS MATHEMATICAL SCIENCE OCCUPATIONS, INCLUDING MATHEMATICIANS AND STATISTICIANS'),
    (1300, 'ENG-ARCHITECTS, EXCEPT NAVAL'),
    (1310, 'ENG-SURVEYORS, CARTOGRAPHERS, AND PHOTOGRAMMETRISTS'),
    (1320, 'ENG-AEROSPACE ENGINEERS'),
    (1340, 'ENG-BIOMEDICAL AND AGRICULTURAL ENGINEERS'),
    (1350, 'ENG-CHEMICAL ENGINEERS'),
    (1360, 'ENG-CIVIL ENGINEERS'),
    (1400, 'ENG-COMPUTER HARDWARE ENGINEERS'),
    (1410, 'ENG-ELECTRICAL AND ELECTRONICS ENGINEERS'),
    (1420, 'ENG-ENVIRONMENTAL ENGINEERS'),
    (1430, 'ENG-INDUSTRIAL ENGINEERS, INCLUDING HEALTH AND SAFETY'),
    (1440, 'ENG-MARINE ENGINEERS AND NAVAL ARCHITECTS'),
    (1450, 'ENG-MATERIALS ENGINEERS'),
    (1460, 'ENG-MECHANICAL ENGINEERS'),
    (1520, 'ENG-PETROLEUM, MINING AND GEOLOGICAL ENGINEERS, INCLUDING MINING SAFETY ENGINEERS'),
    (1530, 'ENG-MISCELLANEOUS ENGINEERS, INCLUDING NUCLEAR ENGINEERS'),
    (1540, 'ENG-DRAFTERS'),
    (1550, 'ENG-ENGINEERING TECHNICIANS, EXCEPT DRAFTERS'),
    (1560, 'ENG-SURVEYING AND MAPPING TECHNICIANS'),
    (1600, 'SCI-AGRICULTURAL AND FOOD SCIENTISTS'),
    (1610, 'SCI-BIOLOGICAL SCIENTISTS'),
    (1640, 'SCI-CONSERVATION SCIENTISTS AND FORESTERS'),
    (1650, 'SCI-MEDICAL SCIENTISTS'),
    (1700, 'SCI-ASTRONOMERS AND PHYSICISTS'),
    (1710, 'SCI-ATMOSPHERIC AND SPACE SCIENTISTS'),
    (1720, 'SCI-CHEMISTS AND MATERIALS SCIENTISTS'),
    (1740, 'SCI-ENVIRONMENTAL SCIENTISTS AND GEOSCIENTISTS'),
    (1760, 'SCI-PHYSICAL SCIENTISTS, ALL OTHER'),
    (1800, 'SCI-ECONOMISTS'),
    (1810, 'SCI-MARKET AND SURVEY RESEARCHERS'),
    (1820, 'SCI-PSYCHOLOGISTS'),
    (1840, 'SCI-URBAN AND REGIONAL PLANNERS'),
    (1860, 'SCI-MISCELLANEOUS SOCIAL SCIENTISTS, INCLUDING SOCIOLOGISTS'),
    (1900, 'SCI-AGRICULTURAL AND FOOD SCIENCE TECHNICIANS'),
    (1910, 'SCI-BIOLOGICAL TECHNICIANS'),
    (1920, 'SCI-CHEMICAL TECHNICIANS'),
    (1930, 'SCI-GEOLOGICAL AND PETROLEUM TECHNICIANS'),
    (1960, 'SCI-MISCELLANEOUS LIFE, PHYSICAL, AND SOCIAL SCIENCE TECHNICIANS, INCLUDING SOCIAL SCIENCE RESEARCH ASSISTANTS AND NUCLEAR TECHNICIANS'),
    (2000, 'CMS-COUNSELORS'),
    (2010, 'CMS-SOCIAL WORKERS'),
    (2020, 'CMS-MISCELLANEOUS COMMUNITY AND SOCIAL SERVICE SPECIALISTS'),
    (2040, 'CMS-CLERGY'),
    (2050, 'CMS-DIRECTORS, RELIGIOUS ACTIVITIES AND EDUCATION'),
    (2060, 'CMS-RELIGIOUS WORKERS, ALL OTHER'),
    (2100, 'LGL-LAWYERS AND JUDGES, MAGISTRATES, AND OTHER JUDICIAL WORKERS'),
    (2140, 'LGL-PARALEGALS AND LEGAL ASSISTANTS'),
    (2150, 'LGL-MISCELLANEOUS LEGAL SUPPORT WORKERS'),
    (2200, 'EDU-POSTSECONDARY TEACHERS'),
    (2300, 'EDU-PRESCHOOL AND KINDERGARTEN TEACHERS'),
    (2310, 'EDU-ELEMENTARY AND MIDDLE SCHOOL TEACHERS'),
    (2320, 'EDU-SECONDARY SCHOOL TEACHERS'),
    (2330, 'EDU-SPECIAL EDUCATION TEACHERS'),
    (2340, 'EDU-OTHER TEACHERS AND INSTRUCTORS'),
    (2400, 'EDU-ARCHIVISTS, CURATORS, AND MUSEUM TECHNICIANS'),
    (2430, 'EDU-LIBRARIANS'),
    (2440, 'EDU-LIBRARY TECHNICIANS'),
    (2540, 'EDU-TEACHER ASSISTANTS'),
    (2550, 'EDU-OTHER EDUCATION, TRAINING, AND LIBRARY WORKERS'),
    (2600, 'ENT-ARTISTS AND RELATED WORKERS'),
    (2630, 'ENT-DESIGNERS'),
    (2700, 'ENT-ACTORS'),
    (2710, 'ENT-PRODUCERS AND DIRECTORS'),
    (2720, 'ENT-ATHLETES, COACHES, UMPIRES, AND RELATED WORKERS'),
    (2740, 'ENT-DANCERS AND CHOREOGRAPHERS'),
    (2750, 'ENT-MUSICIANS, SINGERS, AND RELATED WORKERS'),
    (2760, 'ENT-ENTERTAINERS AND PERFORMERS, SPORTS AND RELATED WORKERS, ALL OTHER'),
    (2800, 'ENT-ANNOUNCERS'),
    (2810, 'ENT-NEWS ANALYSTS, REPORTERS AND CORRESPONDENTS'),
    (2820, 'ENT-PUBLIC RELATIONS SPECIALISTS'),
    (2830, 'ENT-EDITORS'),
    (2840, 'ENT-TECHNICAL WRITERS'),
    (2850, 'ENT-WRITERS AND AUTHORS'),
    (2860, 'ENT-MISCELLANEOUS MEDIA AND COMMUNICATION WORKERS'),
    (2900, 'ENT-BROADCAST AND SOUND ENGINEERING TECHNICIANS AND RADIO OPERATORS, AND MEDIA AND COMMUNICATION EQUIPMENT WORKERS, ALL OTHER'),
    (2910, 'ENT-PHOTOGRAPHERS'),
    (2920, 'ENT-TELEVISION, VIDEO, AND MOTION PICTURE CAMERA OPERATORS AND EDITORS'),
    (3000, 'MED-CHIROPRACTORS'),
    (3010, 'MED-DENTISTS'),
    (3030, 'MED-DIETITIANS AND NUTRITIONISTS'),
    (3040, 'MED-OPTOMETRISTS'),
    (3050, 'MED-PHARMACISTS'),
    (3060, 'MED-PHYSICIANS AND SURGEONS'),
    (3110, 'MED-PHYSICIAN ASSISTANTS'),
    (3120, 'MED-PODIATRISTS'),
    (3130, 'MED-REGISTERED NURSES'),
    (3140, 'MED-AUDIOLOGISTS'),
    (3150, 'MED-OCCUPATIONAL THERAPISTS'),
    (3160, 'MED-PHYSICAL THERAPISTS'),
    (3200, 'MED-RADIATION THERAPISTS'),
    (3210, 'MED-RECREATIONAL THERAPISTS'),
    (3220, 'MED-RESPIRATORY THERAPISTS'),
    (3230, 'MED-SPEECH-LANGUAGE PATHOLOGISTS'),
    (3240, 'MED-THERAPISTS, ALL OTHER'),
    (3250, 'MED-VETERINARIANS'),
    (3260, 'MED-HEALTH DIAGNOSING AND TREATING PRACTITIONERS, ALL OTHER'),
    (3300, 'MED-CLINICAL LABORATORY TECHNOLOGISTS AND TECHNICIANS'),
    (3310, 'MED-DENTAL HYGIENISTS'),
    (3320, 'MED-DIAGNOSTIC RELATED TECHNOLOGISTS AND TECHNICIANS'),
    (3400, 'MED-EMERGENCY MEDICAL TECHNICIANS AND PARAMEDICS'),
    (3410, 'MED-HEALTH DIAGNOSING AND TREATING PRACTITIONER SUPPORT TECHNICIANS'),
    (3500, 'MED-LICENSED PRACTICAL AND LICENSED VOCATIONAL NURSES'),
    (3510, 'MED-MEDICAL RECORDS AND HEALTH INFORMATION TECHNICIANS'),
    (3520, 'MED-OPTICIANS, DISPENSING'),
    (3530, 'MED-MISCELLANEOUS HEALTH TECHNOLOGISTS AND TECHNICIANS'),
    (3540, 'MED-OTHER HEALTHCARE PRACTITIONERS AND TECHNICAL OCCUPATIONS'),
    (3600, 'HLS-NURSING, PSYCHIATRIC, AND HOME HEALTH AIDES'),
    (3610, 'HLS-OCCUPATIONAL THERAPIST ASSISTANTS AND AIDES'),
    (3620, 'HLS-PHYSICAL THERAPIST ASSISTANTS AND AIDES'),
    (3630, 'HLS-MASSAGE THERAPISTS'),
    (3640, 'HLS-DENTAL ASSISTANTS'),
    (3650, 'HLS-MEDICAL ASSISTANTS AND OTHER HEALTHCARE SUPPORT OCCUPATIONS, EXCEPT DENTAL ASSISTANTS'),
    (3700, 'PRT-FIRST-LINE SUPERVISORS/MANAGERS OF CORRECTIONAL OFFICERS'),
    (3710, 'PRT-FIRST-LINE SUPERVISORS/MANAGERS OF POLICE AND DETECTIVES'),
    (3720, 'PRT-FIRST-LINE SUPERVISORS/MANAGERS OF FIRE FIGHTING AND PREVENTION WORKERS'),
    (3730, 'PRT-SUPERVISORS, PROTECTIVE SERVICE WORKERS, ALL OTHER'),
    (3740, 'PRT-FIRE FIGHTERS'),
    (3750, 'PRT-FIRE INSPECTORS'),
    (3800, 'PRT-BAILIFFS, CORRECTIONAL OFFICERS, AND JAILERS'),
    (3820, 'PRT-DETECTIVES AND CRIMINAL INVESTIGATORS'),
    (3840, 'PRT-MISCELLANEOUS LAW ENFORCEMENT WORKERS'),
    (3850, 'PRT-POLICE OFFICERS'),
    (3900, 'PRT-ANIMAL CONTROL WORKERS'),
    (3910, 'PRT-PRIVATE DETECTIVES AND INVESTIGATORS'),
    (3920, 'PRT-SECURITY GUARDS AND GAMING SURVEILLANCE OFFICERS'),
    (3940, 'PRT-CROSSING GUARDS'),
    (3950, 'PRT-LIFEGUARDS AND OTHER PROTECTIVE SERVICE WORKERS'),
    (4000, 'EAT-CHEFS AND HEAD COOKS'),
    (4010, 'EAT-FIRST-LINE SUPERVISORS/MANAGERS OF FOOD PREPARATION AND SERVING WORKERS'),
    (4020, 'EAT-COOKS'),
    (4030, 'EAT-FOOD PREPARATION WORKERS'),
    (4040, 'EAT-BARTENDERS'),
    (4050, 'EAT-COMBINED FOOD PREPARATION AND SERVING WORKERS, INCLUDING FAST FOOD'),
    (4060, 'EAT-COUNTER ATTENDANTS, CAFETERIA, FOOD CONCESSION, AND COFFEE SHOP'),
    (4110, 'EAT-WAITERS AND WAITRESSES'),
    (4120, 'EAT-FOOD SERVERS, NONRESTAURANT'),
    (4130, 'EAT-MISCELLANEOUS FOOD PREPARATION AND SERVING RELATED WORKERS, INCLUDING DINING ROOM AND CAFETERIA ATTENDANTS AND BARTENDER HELPERS'),
    (4140, 'EAT-DISHWASHERS'),
    (4150, 'EAT-HOSTS AND HOSTESSES, RESTAURANT, LOUNGE, AND COFFEE SHOP'),
    (4200, 'CLN-FIRST-LINE SUPERVISORS/MANAGERS OF HOUSEKEEPING AND JANITORIAL WORKERS'),
    (4210, 'CLN-FIRST-LINE SUPERVISORS/MANAGERS OF LANDSCAPING, LAWN SERVICE, AND GROUNDSKEEPING WORKERS'),
    (4220, 'CLN-JANITORS AND BUILDING CLEANERS'),
    (4230, 'CLN-MAIDS AND HOUSEKEEPING CLEANERS'),
    (4240, 'CLN-PEST CONTROL WORKERS'),
    (4250, 'CLN-GROUNDS MAINTENANCE WORKERS'),
    (4300, 'PRS-FIRST-LINE SUPERVISORS/MANAGERS OF GAMING WORKERS'),
    (4320, 'PRS-FIRST-LINE SUPERVISORS/MANAGERS OF PERSONAL SERVICE WORKERS'),
    (4340, 'PRS-ANIMAL TRAINERS'),
    (4350, 'PRS-NONFARM ANIMAL CARETAKERS'),
    (4400, 'PRS-GAMING SERVICES WORKERS'),
    (4410, 'PRS-MOTION PICTURE PROJECTIONISTS'),
    (4420, 'PRS-USHERS, LOBBY ATTENDANTS, AND TICKET TAKERS'),
    (4430, 'PRS-MISCELLANEOUS ENTERTAINMENT ATTENDANTS AND RELATED WORKERS'),
    (4460, 'PRS-FUNERAL SERVICE WORKERS'),
    (4500, 'PRS-BARBERS'),
    (4510, 'PRS-HAIRDRESSERS, HAIRSTYLISTS, AND COSMETOLOGISTS'),
    (4520, 'PRS-MISCELLANEOUS PERSONAL APPEARANCE WORKERS'),
    (4530, 'PRS-BAGGAGE PORTERS, BELLHOPS, AND CONCIERGES'),
    (4540, 'PRS-TOUR AND TRAVEL GUIDES'),
    (4550, 'PRS-TRANSPORTATION ATTENDANTS'),
    (4600, 'PRS-CHILD CARE WORKERS'),
    (4610, 'PRS-PERSONAL AND HOME CARE AIDES'),
    (4620, 'PRS-RECREATION AND FITNESS WORKERS'),
    (4640, 'PRS-RESIDENTIAL ADVISORS'),
    (4650, 'PRS-PERSONAL CARE AND SERVICE WORKERS, ALL OTHER'),
    (4700, 'SAL-FIRST-LINE SUPERVISORS/MANAGERS OF RETAIL SALES WORKERS'),
    (4710, 'SAL-FIRST-LINE SUPERVISORS/MANAGERS OF NON-RETAIL SALES WORKERS'),
    (4720, 'SAL-CASHIERS'),
    (4740, 'SAL-COUNTER AND RENTAL CLERKS'),
    (4750, 'SAL-PARTS SALESPERSONS'),
    (4760, 'SAL-RETAIL SALESPERSONS'),
    (4800, 'SAL-ADVERTISING SALES AGENTS'),
    (4810, 'SAL-INSURANCE SALES AGENTS'),
    (4820, 'SAL-SECURITIES, COMMODITIES, AND FINANCIAL SERVICES SALES AGENTS'),
    (4830, 'SAL-TRAVEL AGENTS'),
    (4840, 'SAL-SALES REPRESENTATIVES, SERVICES, ALL OTHER'),
    (4850, 'SAL-SALES REPRESENTATIVES, WHOLESALE AND MANUFACTURING'),
    (4900, 'SAL-MODELS, DEMONSTRATORS, AND PRODUCT PROMOTERS'),
    (4920, 'SAL-REAL ESTATE BROKERS AND SALES AGENTS'),
    (4930, 'SAL-SALES ENGINEERS'),
    (4940, 'SAL-TELEMARKETERS'),
    (4950, 'SAL-DOOR-TO-DOOR SALES WORKERS, NEWS AND STREET VENDORS, AND RELATED WORKERS'),
    (4960, 'SAL-SALES AND RELATED WORKERS, ALL OTHER'),
    (5000, 'OFF-FIRST-LINE SUPERVISORS/MANAGERS OF OFFICE AND ADMINISTRATIVE SUPPORT WORKERS'),
    (5010, 'OFF-SWITCHBOARD OPERATORS, INCLUDING ANSWERING SERVICE'),
    (5020, 'OFF-TELEPHONE OPERATORS'),
    (5030, 'OFF-COMMUNICATIONS EQUIPMENT OPERATORS, ALL OTHER'),
    (5100, 'OFF-BILL AND ACCOUNT COLLECTORS'),
    (5110, 'OFF-BILLING AND POSTING CLERKS AND MACHINE OPERATORS'),
    (5120, 'OFF-BOOKKEEPING, ACCOUNTING, AND AUDITING CLERKS'),
    (5130, 'OFF-GAMING CAGE WORKERS'),
    (5140, 'OFF-PAYROLL AND TIMEKEEPING CLERKS'),
    (5150, 'OFF-PROCUREMENT CLERKS'),
    (5160, 'OFF-TELLERS'),
    (5200, 'OFF-BROKERAGE CLERKS'),
    (5220, 'OFF-COURT, MUNICIPAL, AND LICENSE CLERKS'),
    (5230, 'OFF-CREDIT AUTHORIZERS, CHECKERS, AND CLERKS'),
    (5240, 'OFF-CUSTOMER SERVICE REPRESENTATIVES'),
    (5250, 'OFF-ELIGIBILITY INTERVIEWERS, GOVERNMENT PROGRAMS'),
    (5260, 'OFF-FILE CLERKS'),
    (5300, 'OFF-HOTEL, MOTEL, AND RESORT DESK CLERKS'),
    (5310, 'OFF-INTERVIEWERS, EXCEPT ELIGIBILITY AND LOAN'),
    (5320, 'OFF-LIBRARY ASSISTANTS, CLERICAL'),
    (5330, 'OFF-LOAN INTERVIEWERS AND CLERKS'),
    (5340, 'OFF-NEW ACCOUNTS CLERKS'),
    (5350, 'OFF-CORRESPONDENCE CLERKS AND ORDER CLERKS'),
    (5360, 'OFF-HUMAN RESOURCES ASSISTANTS, EXCEPT PAYROLL AND TIMEKEEPING'),
    (5400, 'OFF-RECEPTIONISTS AND INFORMATION CLERKS'),
    (5410, 'OFF-RESERVATION AND TRANSPORTATION TICKET AGENTS AND TRAVEL CLERKS'),
    (5420, 'OFF-INFORMATION AND RECORD CLERKS, ALL OTHER'),
    (5500, 'OFF-CARGO AND FREIGHT AGENTS'),
    (5510, 'OFF-COURIERS AND MESSENGERS'),
    (5520, 'OFF-DISPATCHERS'),
    (5530, 'OFF-METER READERS, UTILITIES'),
    (5540, 'OFF-POSTAL SERVICE CLERKS'),
    (5550, 'OFF-POSTAL SERVICE MAIL CARRIERS'),
    (5560, 'OFF-POSTAL SERVICE MAIL SORTERS, PROCESSORS, AND PROCESSING MACHINE OPERATORS'),
    (5600, 'OFF-PRODUCTION, PLANNING, AND EXPEDITING CLERKS'),
    (5610, 'OFF-SHIPPING, RECEIVING, AND TRAFFIC CLERKS'),
    (5620, 'OFF-STOCK CLERKS AND ORDER FILLERS'),
    (5630, 'OFF-WEIGHERS, MEASURERS, CHECKERS, AND SAMPLERS, RECORDKEEPING'),
    (5700, 'OFF-SECRETARIES AND ADMINISTRATIVE ASSISTANTS'),
    (5800, 'OFF-COMPUTER OPERATORS'),
    (5810, 'OFF-DATA ENTRY KEYERS'),
    (5820, 'OFF-WORD PROCESSORS AND TYPISTS'),
    (5840, 'OFF-INSURANCE CLAIMS AND POLICY PROCESSING CLERKS'),
    (5850, 'OFF-MAIL CLERKS AND MAIL MACHINE OPERATORS, EXCEPT POSTAL SERVICE'),
    (5860, 'OFF-OFFICE CLERKS, GENERAL'),
    (5900, 'OFF-OFFICE MACHINE OPERATORS, EXCEPT COMPUTER'),
    (5910, 'OFF-PROOFREADERS AND COPY MARKERS'),
    (5920, 'OFF-STATISTICAL ASSISTANTS'),
    (5930, 'OFF-MISCELLANEOUS OFFICE AND ADMINISTRATIVE SUPPORT WORKERS, INCLUDING DESKTOP PUBLISHERS'),
    (6000, 'FFF-FIRST-LINE SUPERVISORS/MANAGERS OF FARMING, FISHING, AND FORESTRY WORKERS'),
    (6010, 'FFF-AGRICULTURAL INSPECTORS'),
    (6040, 'FFF-GRADERS AND SORTERS, AGRICULTURAL PRODUCTS'),
    (6050, 'FFF-MISCELLANEOUS AGRICULTURAL WORKERS, INCLUDING ANIMAL BREEDERS'),
    (6100, 'FFF-FISHING AND HUNTING WORKERS'),
    (6120, 'FFF-FOREST AND CONSERVATION WORKERS'),
    (6130, 'FFF-LOGGING WORKERS'),
    (6200, 'CON-FIRST-LINE SUPERVISORS/MANAGERS OF CONSTRUCTION TRADES AND EXTRACTION WORKERS'),
    (6210, 'CON-BOILERMAKERS'),
    (6220, 'CON-BRICKMASONS, BLOCKMASONS, AND STONEMASONS'),
    (6230, 'CON-CARPENTERS'),
    (6240, 'CON-CARPET, FLOOR, AND TILE INSTALLERS AND FINISHERS'),
    (6250, 'CON-CEMENT MASONS, CONCRETE FINISHERS, AND TERRAZZO WORKERS'),
    (6260, 'CON-CONSTRUCTION LABORERS'),
    (6300, 'CON-PAVING, SURFACING, AND TAMPING EQUIPMENT OPERATORS'),
    (6320, 'CON-CONSTRUCTION EQUIPMENT OPERATORS, EXCEPT PAVING, SURFACING, AND TAMPING EQUIPMENT OPERATORS'),
    (6330, 'CON-DRYWALL INSTALLERS, CEILING TILE INSTALLERS, AND TAPERS'),
    (6350, 'CON-ELECTRICIANS'),
    (6360, 'CON-GLAZIERS'),
    (6400, 'CON-INSULATION WORKERS'),
    (6420, 'CON-PAINTERS, CONSTRUCTION AND MAINTENANCE'),
    (6430, 'CON-PAPERHANGERS'),
    (6440, 'CON-PIPELAYERS, PLUMBERS, PIPEFITTERS, AND STEAMFITTERS'),
    (6460, 'CON-PLASTERERS AND STUCCO MASONS'),
    (6500, 'CON-REINFORCING IRON AND REBAR WORKERS'),
    (6510, 'CON-ROOFERS'),
    (6520, 'CON-SHEET METAL WORKERS'),
    (6530, 'CON-STRUCTURAL IRON AND STEEL WORKERS'),
    (6600, 'CON-HELPERS, CONSTRUCTION TRADES'),
    (6660, 'CON-CONSTRUCTION AND BUILDING INSPECTORS'),
    (6700, 'CON-ELEVATOR INSTALLERS AND REPAIRERS'),
    (6710, 'CON-FENCE ERECTORS'),
    (6720, 'CON-HAZARDOUS MATERIALS REMOVAL WORKERS'),
    (6730, 'CON-HIGHWAY MAINTENANCE WORKERS'),
    (6740, 'CON-RAIL-TRACK LAYING AND MAINTENANCE EQUIPMENT OPERATORS'),
    (6760, 'CON-MISCELLANEOUS CONSTRUCTION WORKERS, INCLUDING SEPTIC TANK SERVICERS AND SEWER PIPE CLEANERS'),
    (6800, 'EXT-DERRICK, ROTARY DRILL, AND SERVICE UNIT OPERATORS, AND ROUSTABOUTS, OIL, GAS, AND MINING'),
    (6820, 'EXT-EARTH DRILLERS, EXCEPT OIL AND GAS'),
    (6830, 'EXT-EXPLOSIVES WORKERS, ORDNANCE HANDLING EXPERTS, AND BLASTERS'),
    (6840, 'EXT-MINING MACHINE OPERATORS'),
    (6940, 'EXT-MISCELLANEOUS EXTRACTION WORKERS, INCLUDING ROOF BOLTERS AND HELPERS'),
    (7000, 'RPR-FIRST-LINE SUPERVISORS/MANAGERS OF MECHANICS, INSTALLERS, AND REPAIRERS'),
    (7010, 'RPR-COMPUTER, AUTOMATED TELLER, AND OFFICE MACHINE REPAIRERS'),
    (7020, 'RPR-RADIO AND TELECOMMUNICATIONS EQUIPMENT INSTALLERS AND REPAIRERS'),
    (7030, 'RPR-AVIONICS TECHNICIANS'),
    (7040, 'RPR-ELECTRIC MOTOR, POWER TOOL, AND RELATED REPAIRERS'),
    (7100, 'RPR-ELECTRICAL AND ELECTRONICS REPAIRERS, TRANSPORTATION EQUIPMENT, AND INDUSTRIAL AND UTILITY'),
    (7110, 'RPR-ELECTRONIC EQUIPMENT INSTALLERS AND REPAIRERS, MOTOR VEHICLES'),
    (7120, 'RPR-ELECTRONIC HOME ENTERTAINMENT EQUIPMENT INSTALLERS AND REPAIRERS'),
    (7130, 'RPR-SECURITY AND FIRE ALARM SYSTEMS INSTALLERS'),
    (7140, 'RPR-AIRCRAFT MECHANICS AND SERVICE TECHNICIANS'),
    (7150, 'RPR-AUTOMOTIVE BODY AND RELATED REPAIRERS'),
    (7160, 'RPR-AUTOMOTIVE GLASS INSTALLERS AND REPAIRERS'),
    (7200, 'RPR-AUTOMOTIVE SERVICE TECHNICIANS AND MECHANICS'),
    (7210, 'RPR-BUS AND TRUCK MECHANICS AND DIESEL ENGINE SPECIALISTS'),
    (7220, 'RPR-HEAVY VEHICLE AND MOBILE EQUIPMENT SERVICE TECHNICIANS AND MECHANICS'),
    (7240, 'RPR-SMALL ENGINE MECHANICS'),
    (7260, 'RPR-MISCELLANEOUS VEHICLE AND MOBILE EQUIPMENT MECHANICS, INSTALLERS, AND REPAIRERS'),
    (7300, 'RPR-CONTROL AND VALVE INSTALLERS AND REPAIRERS'),
    (7310, 'RPR-HEATING, AIR CONDITIONING, AND REFRIGERATION MECHANICS AND INSTALLERS'),
    (7320, 'RPR-HOME APPLIANCE REPAIRERS'),
    (7330, 'RPR-INDUSTRIAL AND REFRACTORY MACHINERY MECHANICS'),
    (7340, 'RPR-MAINTENANCE AND REPAIR WORKERS, GENERAL'),
    (7350, 'RPR-MAINTENANCE WORKERS, MACHINERY'),
    (7360, 'RPR-MILLWRIGHTS'),
    (7410, 'RPR-ELECTRICAL POWER-LINE INSTALLERS AND REPAIRERS'),
    (7420, 'RPR-TELECOMMUNICATIONS LINE INSTALLERS AND REPAIRERS'),
    (7430, 'RPR-PRECISION INSTRUMENT AND EQUIPMENT REPAIRERS'),
    (7510, 'RPR-COIN, VENDING, AND AMUSEMENT MACHINE SERVICERS AND REPAIRERS'),
    (7540, 'RPR-LOCKSMITHS AND SAFE REPAIRERS'),
    (7550, 'RPR-MANUFACTURED BUILDING AND MOBILE HOME INSTALLERS'),
    (7560, 'RPR-RIGGERS'),
    (7610, 'RPR-HELPERS--INSTALLATION, MAINTENANCE, AND REPAIR WORKERS'),
    (7620, 'RPR-OTHER INSTALLATION, MAINTENANCE, AND REPAIR WORKERS, INCLUDING COMMERCIAL DIVERS, AND SIGNAL AND TRACK SWITCH REPAIRERS'),
    (7700, 'PRD-FIRST-LINE SUPERVISORS/MANAGERS OF PRODUCTION AND OPERATING WORKERS'),
    (7710, 'PRD-AIRCRAFT STRUCTURE, SURFACES, RIGGING, AND SYSTEMS ASSEMBLERS'),
    (7720, 'PRD-ELECTRICAL, ELECTRONICS, AND ELECTROMECHANICAL ASSEMBLERS'),
    (7730, 'PRD-ENGINE AND OTHER MACHINE ASSEMBLERS'),
    (7740, 'PRD-STRUCTURAL METAL FABRICATORS AND FITTERS'),
    (7750, 'PRD-MISCELLANEOUS ASSEMBLERS AND FABRICATORS'),
    (7800, 'PRD-BAKERS'),
    (7810, 'PRD-BUTCHERS AND OTHER MEAT, POULTRY, AND FISH PROCESSING WORKERS'),
    (7830, 'PRD-FOOD AND TOBACCO ROASTING, BAKING, AND DRYING MACHINE OPERATORS AND TENDERS'),
    (7840, 'PRD-FOOD BATCHMAKERS'),
    (7850, 'PRD-FOOD COOKING MACHINE OPERATORS AND TENDERS'),
    (7900, 'PRD-COMPUTER CONTROL PROGRAMMERS AND OPERATORS'),
    (7920, 'PRD-EXTRUDING AND DRAWING MACHINE SETTERS, OPERATORS, AND TENDERS, METAL AND PLASTIC'),
    (7930, 'PRD-FORGING MACHINE SETTERS, OPERATORS, AND TENDERS, METAL AND PLASTIC'),
    (7940, 'PRD-ROLLING MACHINE SETTERS, OPERATORS, AND TENDERS, METAL AND PLASTIC'),
    (7950, 'PRD-CUTTING, PUNCHING, AND PRESS MACHINE SETTERS, OPERATORS, AND TENDERS, METAL AND PLASTIC'),
    (7960, 'PRD-DRILLING AND BORING MACHINE TOOL SETTERS, OPERATORS, AND TENDERS, METAL AND PLASTIC'),
    (8000, 'PRD-GRINDING, LAPPING, POLISHING, AND BUFFING MACHINE TOOL SETTERS, OPERATORS, AND TENDERS, METAL AND PLASTIC'),
    (8010, 'PRD-LATHE AND TURNING MACHINE TOOL SETTERS, OPERATORS, AND TENDERS, METAL AND PLASTIC'),
    (8030, 'PRD-MACHINISTS'),
    (8040, 'PRD-METAL FURNACE AND KILN OPERATORS AND TENDERS'),
    (8060, 'PRD-MODEL MAKERS AND PATTERNMAKERS, METAL AND PLASTIC'),
    (8100, 'PRD-MOLDERS AND MOLDING MACHINE SETTERS, OPERATORS, AND TENDERS, METAL AND PLASTIC'),
    (8130, 'PRD-TOOL AND DIE MAKERS'),
    (8140, 'PRD-WELDING, SOLDERING, AND BRAZING WORKERS'),
    (8150, 'PRD-HEAT TREATING EQUIPMENT SETTERS, OPERATORS, AND TENDERS, METAL AND PLASTIC'),
    (8200, 'PRD-PLATING AND COATING MACHINE SETTERS, OPERATORS, AND TENDERS, METAL AND PLASTIC'),
    (8210, 'PRD-TOOL GRINDERS, FILERS, AND SHARPENERS'),
    (8220, 'PRD-MISCELLANEOUS METAL WORKERS AND PLASTIC WORKERS, INCLUDING MILLING AND PLANING MACHINE SETTERS, AND MULTIPLE MACHINE TOOL SETTERS, AND LAY-OUT WORKERS'),
    (8230, 'PRD-BOOKBINDERS AND BINDERY WORKERS'),
    (8240, 'PRD-JOB PRINTERS'),
    (8250, 'PRD-PREPRESS TECHNICIANS AND WORKERS'),
    (8260, 'PRD-PRINTING MACHINE OPERATORS'),
    (8300, 'PRD-LAUNDRY AND DRY-CLEANING WORKERS'),
    (8310, 'PRD-PRESSERS, TEXTILE, GARMENT, AND RELATED MATERIALS'),
    (8320, 'PRD-SEWING MACHINE OPERATORS'),
    (8330, 'PRD-SHOE AND LEATHER WORKERS AND REPAIRERS'),
    (8340, 'PRD-SHOE MACHINE OPERATORS AND TENDERS'),
    (8350, 'PRD-TAILORS, DRESSMAKERS, AND SEWERS'),
    (8400, 'PRD-TEXTILE BLEACHING AND DYEING, AND CUTTING MACHINE SETTERS, OPERATORS, AND TENDERS'),
    (8410, 'PRD-TEXTILE KNITTING AND WEAVING MACHINE SETTERS, OPERATORS, AND TENDERS'),
    (8420, 'PRD-TEXTILE WINDING, TWISTING, AND DRAWING OUT MACHINE SETTERS, OPERATORS, AND TENDERS'),
    (8450, 'PRD-UPHOLSTERERS'),
    (8460, 'PRD-MISCELLANEOUS TEXTILE, APPAREL, AND FURNISHINGS WORKERS, EXCEPT UPHOLSTERERS'),
    (8500, 'PRD-CABINETMAKERS AND BENCH CARPENTERS'),
    (8510, 'PRD-FURNITURE FINISHERS'),
    (8530, 'PRD-SAWING MACHINE SETTERS, OPERATORS, AND TENDERS, WOOD'),
    (8540, 'PRD-WOODWORKING MACHINE SETTERS, OPERATORS, AND TENDERS, EXCEPT SAWING'),
    (8550, 'PRD-MISCELLANEOUS WOODWORKERS, INCLUDING MODEL MAKERS AND PATTERNMAKERS'),
    (8600, 'PRD-POWER PLANT OPERATORS, DISTRIBUTORS, AND DISPATCHERS'),
    (8610, 'PRD-STATIONARY ENGINEERS AND BOILER OPERATORS'),
    (8620, 'PRD-WATER AND LIQUID WASTE TREATMENT PLANT AND SYSTEM OPERATORS'),
    (8630, 'PRD-MISCELLANEOUS PLANT AND SYSTEM OPERATORS'),
    (8640, 'PRD-CHEMICAL PROCESSING MACHINE SETTERS, OPERATORS, AND TENDERS'),
    (8650, 'PRD-CRUSHING, GRINDING, POLISHING, MIXING, AND BLENDING WORKERS'),
    (8710, 'PRD-CUTTING WORKERS'),
    (8720, 'PRD-EXTRUDING, FORMING, PRESSING, AND COMPACTING MACHINE SETTERS, OPERATORS, AND TENDERS'),
    (8730, 'PRD-FURNACE, KILN, OVEN, DRIER, AND KETTLE OPERATORS AND TENDERS'),
    (8740, 'PRD-INSPECTORS, TESTERS, SORTERS, SAMPLERS, AND WEIGHERS'),
    (8750, 'PRD-JEWELERS AND PRECIOUS STONE AND METAL WORKERS'),
    (8760, 'PRD-MEDICAL, DENTAL, AND OPHTHALMIC LABORATORY TECHNICIANS'),
    (8800, 'PRD-PACKAGING AND FILLING MACHINE OPERATORS AND TENDERS'),
    (8810, 'PRD-PAINTING WORKERS'),
    (8830, 'PRD-PHOTOGRAPHIC PROCESS WORKERS AND PROCESSING MACHINE OPERATORS'),
    (8850, 'PRD-CEMENTING AND GLUING MACHINE OPERATORS AND TENDERS'),
    (8860, 'PRD-CLEANING, WASHING, AND METAL PICKLING EQUIPMENT OPERATORS AND TENDERS'),
    (8910, 'PRD-ETCHERS AND ENGRAVERS'),
    (8920, 'PRD-MOLDERS, SHAPERS, AND CASTERS, EXCEPT METAL AND PLASTIC'),
    (8930, 'PRD-PAPER GOODS MACHINE SETTERS, OPERATORS, AND TENDERS'),
    (8940, 'PRD-TIRE BUILDERS'),
    (8950, 'PRD-HELPERS-PRODUCTION WORKERS'),
    (8960, 'PRD-OTHER PRODUCTION WORKERS, INCLUDING SEMICONDUCTOR PROCESSORS AND COOLING AND FREEZING EQUIPMENT OPERATORS'),
    (9000, 'TRN-SUPERVISORS, TRANSPORTATION AND MATERIAL MOVING WORKERS'),
    (9030, 'TRN-AIRCRAFT PILOTS AND FLIGHT ENGINEERS'),
    (9040, 'TRN-AIR TRAFFIC CONTROLLERS AND AIRFIELD OPERATIONS SPECIALISTS'),
    (9110, 'TRN-AMBULANCE DRIVERS AND ATTENDANTS, EXCEPT EMERGENCY MEDICAL TECHNICIANS'),
    (9120, 'TRN-BUS DRIVERS'),
    (9130, 'TRN-DRIVER/SALES WORKERS AND TRUCK DRIVERS'),
    (9140, 'TRN-TAXI DRIVERS AND CHAUFFEURS'),
    (9150, 'TRN-MOTOR VEHICLE OPERATORS, ALL OTHER'),
    (9200, 'TRN-LOCOMOTIVE ENGINEERS AND OPERATORS'),
    (9230, 'TRN-RAILROAD BRAKE, SIGNAL, AND SWITCH OPERATORS'),
    (9240, 'TRN-RAILROAD CONDUCTORS AND YARDMASTERS'),
    (9260, 'TRN-SUBWAY, STREETCAR, AND OTHER RAIL TRANSPORTATION WORKERS'),
    (9300, 'TRN-SAILORS AND MARINE OILERS, AND SHIP ENGINEERS'),
    (9310, 'TRN-SHIP AND BOAT CAPTAINS AND OPERATORS'),
    (9350, 'TRN-PARKING LOT ATTENDANTS'),
    (9360, 'TRN-SERVICE STATION ATTENDANTS'),
    (9410, 'TRN-TRANSPORTATION INSPECTORS'),
    (9420, 'TRN-MISCELLANEOUS TRANSPORTATION WORKERS, INCLUDING BRIDGE AND LOCK TENDERS AND TRAFFIC TECHNICIANS'),
    (9510, 'TRN-CRANE AND TOWER OPERATORS'),
    (9520, 'TRN-DREDGE, EXCAVATING, AND LOADING MACHINE OPERATORS'),
    (9560, 'TRN-CONVEYOR OPERATORS AND TENDERS, AND HOIST AND WINCH OPERATORS'),
    (9600, 'TRN-INDUSTRIAL TRUCK AND TRACTOR OPERATORS'),
    (9610, 'TRN-CLEANERS OF VEHICLES AND EQUIPMENT'),
    (9620, 'TRN-LABORERS AND FREIGHT, STOCK, AND MATERIAL MOVERS, HAND'),
    (9630, 'TRN-MACHINE FEEDERS AND OFFBEARERS'),
    (9640, 'TRN-PACKERS AND PACKAGERS, HAND'),
    (9650, 'TRN-PUMPING STATION OPERATORS'),
    (9720, 'TRN-REFUSE AND RECYCLABLE MATERIAL COLLECTORS'),
    (9750, 'TRN-MISCELLANEOUS MATERIAL MOVING WORKERS, INCLUDING SHUTTLE CAR OPERATORS, AND TANK CAR, TRUCK, AND SHIP LOADERS'),
    (9800, 'MIL-MILITARY OFFICER SPECIAL AND TACTICAL OPERATIONS LEADERS/MANAGERS'),
    (9810, 'MIL-FIRST-LINE ENLISTED MILITARY SUPERVISORS/MANAGERS'),
    (9820, 'MIL-MILITARY ENLISTED TACTICAL OPERATIONS AND AIR/WEAPONS SPECIALISTS AND CREW MEMBERS'),
    (9830, 'MIL-MILITARY, RANK NOT SPECIFIED **'),
    (9920, 'UNEMPLOYED, WITH NO WORK EXPERIENCE IN THE LAST 5 YEARS **'),
]

PAOC = [
    (b, 'N/A (male/female under 16 years old/GQ)'),
    (1, 'With own children under 6 years only'),
    (2, 'With own children 6 to 17 years only'),
    (3, 'With own children under 6 years and 6 to 17 years'),
    (4, 'No own children'),
]

PERNP = [
    (bbbbbbb, 'N/A (less than 15 years old)'),
    (0000000, 'No earnings'),
    (-009999, 'Loss of $9999 or more'),
    (-000001..-009998, 'Loss $1 to $9998'),
    (0000001, '$1 or breakeven'),
    (0000002..9999999, '$2 to $9999999 (Rounded & top-coded components)'),
]

PINCP = [
    (bbbbbbb, 'N/A (less than 15 years old)'),
    (0000000, 'None'),
    (-019998, 'Loss of $19998 or more'),
    (-000001..-019997, 'Loss $1 to $19997'),
    (0000001, '$1 or breakeven'),
    (0000002..9999999, '$2 to $9999999 (Rounded & top-coded components)'),
]

POBP = [
    (001, 'Alabama/AL'),
    (002, 'Alaska/AK'),
    (004, 'Arizona/AZ'),
    (005, 'Arkansas/AR'),
    (006, 'California/CA'),
    (008, 'Colorado/CO'),
    (009, 'Connecticut/CT'),
    (010, 'Delaware/DE'),
    (011, 'District of Columbia/DC'),
    (012, 'Florida/FL'),
    (013, 'Georgia/GA'),
    (015, 'Hawaii/HI'),
    (016, 'Idaho/ID'),
    (017, 'Illinois/IL'),
    (018, 'Indiana/IN'),
    (019, 'Iowa/IA'),
    (020, 'Kansas/KS'),
    (021, 'Kentucky/KY'),
    (022, 'Louisiana/LA'),
    (023, 'Maine/ME'),
    (024, 'Maryland/MD'),
    (025, 'Massachusetts/MA'),
    (026, 'Michigan/MI'),
    (027, 'Minnesota/MN'),
    (028, 'Mississippi/MS'),
    (029, 'Missouri/MO'),
    (030, 'Montana/MT'),
    (031, 'Nebraska/NE'),
    (032, 'Nevada/NV'),
    (033, 'New Hampshire/NH'),
    (034, 'New Jersey/NJ'),
    (035, 'New Mexico/NM'),
    (036, 'New York/NY'),
    (037, 'North Carolina/NC'),
    (038, 'North Dakota/ND'),
    (039, 'Ohio/OH'),
    (040, 'Oklahoma/OK'),
    (041, 'Oregon/OR'),
    (042, 'Pennsylvania/PA'),
    (044, 'Rhode Island/RI'),
    (045, 'South Carolina/SC'),
    (046, 'South Dakota/SD'),
    (047, 'Tennessee/TN'),
    (048, 'Texas/TX'),
    (049, 'Utah/UT'),
    (050, 'Vermont/VT'),
    (051, 'Virginia/VA'),
    (053, 'Washington/WA'),
    (054, 'West Virginia/WV'),
    (055, 'Wisconsin/WI'),
    (056, 'Wyoming/WY'),
    (060, 'American Samoa'),
    (066, 'Guam'),
    (072, 'Puerto Rico'),
    (078, 'US Virgin Islands'),
    (100, 'Albania'),
    (102, 'Austria'),
    (103, 'Belgium'),
    (104, 'Bulgaria'),
    (105, 'Czechoslovakia'),
    (106, 'Denmark'),
    (108, 'Finland'),
    (109, 'France'),
    (110, 'Germany'),
    (116, 'Greece'),
    (117, 'Hungary'),
    (118, 'Iceland'),
    (119, 'Ireland'),
    (120, 'Italy'),
    (126, 'Netherlands'),
    (127, 'Norway'),
    (128, 'Poland'),
    (129, 'Portugal'),
    (130, 'Azores Islands'),
    (132, 'Romania'),
    (134, 'Spain'),
    (136, 'Sweden'),
    (137, 'Switzerland'),
    (138, 'United Kingdom, Not Specified'),
    (139, 'England'),
    (140, 'Scotland'),
    (142, 'Northern Ireland'),
    (147, 'Yugoslavia'),
    (148, 'Czech Republic'),
    (149, 'Slovakia'),
    (150, 'Bosnia and Herzegovina'),
    (151, 'Croatia'),
    (152, 'Macedonia'),
    (155, 'Estonia'),
    (156, 'Latvia'),
    (157, 'Lithuania'),
    (158, 'Armenia'),
    (159, 'Azerbaijan'),
    (160, 'Belarus'),
    (161, 'Georgia'),
    (162, 'Moldova'),
    (163, 'Russia'),
    (164, 'Ukraine'),
    (165, 'USSR'),
    (166, 'Europe, Not Specified'),
    (169, 'Other Europe, Not Specified'),
    (200, 'Afghanistan'),
    (202, 'Bangladesh'),
    (205, 'Myanmar'),
    (206, 'Cambodia'),
    (207, 'China'),
    (209, 'Hong Kong'),
    (210, 'India'),
    (211, 'Indonesia'),
    (212, 'Iran'),
    (213, 'Iraq'),
    (214, 'Israel'),
    (215, 'Japan'),
    (216, 'Jordan'),
    (217, 'Korea'),
    (218, 'Kazakhstan'),
    (222, 'Kuwait'),
    (223, 'Laos'),
    (224, 'Lebanon'),
    (226, 'Malaysia'),
    (229, 'Nepal'),
    (231, 'Pakistan'),
    (233, 'Philippines'),
    (235, 'Saudi Arabia'),
    (236, 'Singapore'),
    (238, 'Sri Lanka'),
    (239, 'Syria'),
    (240, 'Taiwan'),
    (242, 'Thailand'),
    (243, 'Turkey'),
    (246, 'Uzbekistan'),
    (247, 'Vietnam'),
    (248, 'Yemen'),
    (249, 'Asia'),
    (251, 'Eastern Asia, Not Specified'),
    (253, 'Other South Central Asia, Not Specified'),
    (254, 'Other Asia, Not Specified'),
    (300, 'Bermuda'),
    (301, 'Canada'),
    (303, 'Mexico'),
    (310, 'Belize'),
    (311, 'Costa Rica'),
    (312, 'El Salvador'),
    (313, 'Guatemala'),
    (314, 'Honduras'),
    (315, 'Nicaragua'),
    (316, 'Panama'),
    (321, 'Antigua & Barbuda'),
    (323, 'Bahamas'),
    (324, 'Barbados'),
    (327, 'Cuba'),
    (328, 'Dominica'),
    (329, 'Dominican Republic'),
    (330, 'Grenada'),
    (332, 'Haiti'),
    (333, 'Jamaica'),
    (338, 'St. Kitts-Nevis'),
    (339, 'St. Lucia'),
    (340, 'St. Vincent & the Grenadines'),
    (341, 'Trinidad & Tobago'),
    (343, 'West Indies'),
    (344, 'Caribbean, Not Specified'),
    (360, 'Argentina'),
    (361, 'Bolivia'),
    (362, 'Brazil'),
    (363, 'Chile'),
    (364, 'Colombia'),
    (365, 'Ecuador'),
    (368, 'Guyana'),
    (369, 'Paraguay'),
    (370, 'Peru'),
    (372, 'Uruguay'),
    (373, 'Venezuela'),
    (374, 'South America'),
    (399, 'Americas, Not Specified'),
    (400, 'Algeria'),
    (407, 'Cameroon'),
    (408, 'Cape Verde'),
    (414, 'Egypt'),
    (416, 'Ethiopia'),
    (417, 'Eritrea'),
    (421, 'Ghana'),
    (423, 'Guinea'),
    (427, 'Kenya'),
    (429, 'Liberia'),
    (436, 'Morocco'),
    (440, 'Nigeria'),
    (444, 'Senegal'),
    (447, 'Sierra Leone'),
    (448, 'Somalia'),
    (449, 'South Africa'),
    (451, 'Sudan'),
    (453, 'Tanzania'),
    (457, 'Uganda'),
    (461, 'Zimbabwe'),
    (462, 'Africa'),
    (463, 'Eastern Africa, Not Specified'),
    (464, 'Northern Africa, Not Specified'),
    (467, 'Western Africa, Not Specified'),
    (468, 'Other Africa, Not Specified'),
    (501, 'Australia'),
    (508, 'Fiji'),
    (512, 'Micronesia'),
    (515, 'New Zealand'),
    (523, 'Tonga'),
    (527, 'Samoa'),
    (554, 'Other US Island Areas, Oceania, Not Specified, or at Sea'),
]

POVPIP = [
    (bbb, 'N/A'),
    (000..500, 'Percent of poverty status value'),
    (501, '501 percent or more of poverty status value'),
]

POWPUMA = [
    (bbbbb, 'N/A (not a worker--not in the labor force, force, including persons under 16 years; unemployed; civilian employed, with a job not at work; Armed Forces, with a job but not at work)'),
    (00001, 'Did not work in the United States or in Puerto Rico'),
    (00100..08200, 'Assigned Place of work PUMA. Use with POWSP.'),
]

POWSP = [
    (bbb, 'N/A (not a worker--not in the labor force, including persons under 16 years; unemployed; employed, with a job not at work; Armed Forces, with a job but not at work)'),
    (001, 'Alabama/AL'),
    (002, 'Alaska/AK'),
    (004, 'Arizona/AZ'),
    (005, 'Arkansas/AR'),
    (006, 'California/CA'),
    (008, 'Colorado/CO'),
    (009, 'Connecticut/CT'),
    (010, 'Delaware/DE'),
    (011, 'District of Columbia/DC'),
    (012, 'Florida/FL'),
    (013, 'Georgia/GA'),
    (015, 'Hawaii/HI'),
    (016, 'Idaho/ID'),
    (017, 'Illinois/IL'),
    (018, 'Indiana/IN'),
    (019, 'Iowa/IA'),
    (020, 'Kansas/KS'),
    (021, 'Kentucky/KY'),
    (022, 'Louisiana/LA'),
    (023, 'Maine/ME'),
    (024, 'Maryland/MD'),
    (025, 'Massachusetts/MA'),
    (026, 'Michigan/MI'),
    (027, 'Minnesota/MN'),
    (028, 'Mississippi/MS'),
    (029, 'Missouri/MO'),
    (030, 'Montana/MT'),
    (031, 'Nebraska/NE'),
    (032, 'Nevada/NV'),
    (033, 'New Hampshire/NH'),
    (034, 'New Jersey/NJ'),
    (035, 'New Mexico/NM'),
    (036, 'New York/NY'),
    (037, 'North Carolina/NC'),
    (038, 'North Dakota/ND'),
    (039, 'Ohio/OH'),
    (040, 'Oklahoma/OK'),
    (041, 'Oregon/OR'),
    (042, 'Pennsylvania/PA'),
    (044, 'Rhode Island/RI'),
    (045, 'South Carolina/SC'),
    (046, 'South Dakota/SD'),
    (047, 'Tennessee/TN'),
    (048, 'Texas/TX'),
    (049, 'Utah/UT'),
    (050, 'Vermont/VT'),
    (051, 'Virginia/VA'),
    (053, 'Washington/WA'),
    (054, 'West Virginia/WV'),
    (055, 'Wisconsin/WI'),
    (056, 'Wyoming/WY'),
    (072, 'Puerto Rico'),
    (166, 'Europe'),
    (213, 'Iraq'),
    (251, 'Eastern Asia'),
    (254, 'Other Asia, Not Specified'),
    (303, 'Mexico'),
    (399, 'Americas, Not Specified'),
    (555, 'Other US Island Areas Not Specified, Africa, Oceania, at Sea, or Abroad, Not Specified'),
]

QTRBIR = [
    (1, 'January through March'),
    (2, 'April through June'),
    (3, 'July through September'),
    (4, 'October through December'),
]

RAC1P = [
    (1, 'White alone'),
    (2, 'Black or African American alone'),
    (3, 'American Indian alone'),
    (4, 'Alaska Native alone'),
    (5, 'American Indian and Alaska Native tribes specified; or American Indian or Alaska native, not specified and no other races'),
    (6, 'Asian alone'),
    (7, 'Native Hawaiian and Other Pacific Islander alone'),
    (8, 'Some other race alone'),
    (9, 'Two or more major race groups'),
]

RAC2P = [
    (01, 'White alone'),
    (02, 'Black or African American alone'),
    (03, 'Apache alone'),
    (04, 'Blackfeet alone'),
    (05, 'Cherokee alone'),
    (06, 'Cheyenne alone'),
    (07, 'Chickasaw alone'),
    (08, 'Chippewa alone'),
    (09, 'Choctaw alone'),
    (10, 'Colville alone'),
    (11, 'Comanche alone'),
    (12, 'Creek alone'),
    (13, 'Crow alone'),
    (14, 'Delaware alone'),
    (15, 'Houma alone'),
    (16, 'Iroquois alone'),
    (17, 'Lumbee alone'),
    (18, 'Menominee alone'),
    (19, 'Navajo alone'),
    (20, 'Paiute alone'),
    (21, 'Pima alone'),
    (22, 'Potawatomi alone'),
    (23, 'Pueblo alone'),
    (24, 'Puget Sound Salish alone'),
    (25, 'Seminole alone'),
    (26, 'Sioux alone'),
    (27, 'Tohono O'Odham alone'),
    (28, 'Yakama alone'),
    (29, 'Yaqui alone'),
    (30, 'Yuman alone'),
    (31, 'Other specified American Indian tribes alone'),
    (32, 'Combinations of American Indian tribes only'),
    (33, 'American Indian or Alaska Native, tribe not specified, or American Indian and Alaska Native'),
    (34, 'Alaska Athabascan alone'),
    (35, 'Aleut alone'),
    (36, 'Eskimo alone'),
    (37, 'Tlingit-Haida alone'),
    (38, 'Alaska Native tribes alone or in combination with other Alaska Native tribes'),
    (39, 'American Indian and Alaska Native, not specified'),
    (40, 'Asian Indian alone'),
    (41, 'Bangladeshi alone'),
    (42, 'Cambodian alone'),
    (43, 'Chinese alone'),
    (44, 'Filipino alone'),
    (45, 'Hmong alone'),
    (46, 'Indonesian alone'),
    (47, 'Japanese alone'),
    (48, 'Korean alone'),
    (49, 'Laotian alone'),
    (50, 'Malaysian alone'),
    (51, 'Pakistani alone'),
    (52, 'Sri Lankan alone'),
    (53, 'Thai alone'),
    (54, 'Vietnamese alone'),
    (55, 'Other specified Asian alone'),
    (56, 'Asian, not specified'),
    (57, 'Combinations of Asian groups only'),
    (58, 'Native Hawaiian alone'),
    (59, 'Samoan alone'),
    (60, 'Tongan alone'),
    (61, 'Other Polynesian alone or in combination with other Polynesian groups'),
    (62, 'Guamanian or Chamorro alone'),
    (63, 'Other Micronesian alone or in combination with other Micronesian groups'),
    (64, 'Melanesian alone or in combination with other Melanesian groups'),
    (65, 'Other Native Hawaiian and Other Pacific Islander groups alone or in combination with other Native Hawaiian and Other Pacific Islander groups only'),
    (66, 'Some other race alone'),
    (67, 'Two or more races'),
]

RAC3P = [
    (01, 'Some other race alone'),
    (02, 'Other Pacific Islander alone'),
    (03, 'Samoan alone'),
    (04, 'Guamanian or Chamorro alone'),
    (05, 'Native Hawaiian alone'),
    (06, 'Native Hawaiian and Other Pacific Islander groups only'),
    (07, 'Other Asian; Some other race'),
    (08, 'Other Asian alone'),
    (09, 'Vietnamese alone'),
    (10, 'Korean alone'),
    (11, 'Japanese; Some other race'),
    (12, 'Japanese; Native Hawaiian'),
    (13, 'Japanese; Korean'),
    (14, 'Japanese alone'),
    (15, 'Filipino; Some other race'),
    (16, 'Filipino; Native Hawaiian'),
    (17, 'Filipino; Japanese'),
    (18, 'Filipino alone'),
    (19, 'Chinese; Some other race'),
    (20, 'Chinese; Native Hawaiian'),
    (21, 'Chinese; Other Asian'),
    (22, 'Chinese; Vietnamese'),
    (23, 'Chinese; Japanese'),
    (24, 'Chinese; Filipino; Native Hawaiian'),
    (25, 'Chinese; Filipino'),
    (26, 'Chinese alone'),
    (27, 'Asian Indian; Some other race'),
    (28, 'Asian Indian; Other Asian'),
    (29, 'Asian Indian alone'),
    (30, 'Asian groups and/or Native Hawaiian and Other Pacific Islander groups; Some other race'),
    (31, 'Asian groups; Native Hawaiian and Other Pacific Islander groups'),
    (32, 'Asian groups only'),
    (33, 'American Indian and Alaska Native; Some other race'),
    (34, 'American Indian and Alaska Native alone'),
    (35, 'American Indian and Alaska Native race; Asian groups and/or Native Hawaiian and Other Pacific Islander groups and/or Some other race'),
    (36, 'Black or African American; Some other race'),
    (37, 'Black or African American; Other Asian'),
    (38, 'Black or African American; Korean'),
    (39, 'Black or African American; Japanese'),
    (40, 'Black or African American; Filipino'),
    (41, 'Black or African American; Chinese'),
    (42, 'Black or African American; Asian Indian'),
    (43, 'Black or African American; American Indian and Alaska Native'),
    (44, 'Black or African American alone'),
    (45, 'Black or African American race; Native Hawaiian and Other Pacific Islander groups'),
    (46, 'Black or African American race; Asian groups and/or Native Hawaiian and Other Pacific Islander groups and/or Some other race'),
    (47, 'Black or African American race; American Indian and Alaska Native race; Asian groups and/or Native Hawaiian and Other Pacific Islander groups and/or Some other race'),
    (48, 'White; Some other race'),
    (49, 'White; Other Pacific Islander'),
    (50, 'White; Samoan'),
    (51, 'White; Guamanian or Chamorro'),
    (52, 'White; Native Hawaiian'),
    (53, 'White; Other Asian'),
    (54, 'White; Vietnamese'),
    (55, 'White; Korean'),
    (56, 'White; Japanese; Native Hawaiian'),
    (57, 'White; Japanese'),
    (58, 'White; Filipino; Native Hawaiian'),
    (59, 'White; Filipino'),
    (60, 'White; Chinese; Native Hawaiian'),
    (61, 'White; Chinese; Filipino; Native Hawaiian'),
    (62, 'White; Chinese'),
    (63, 'White; Asian Indian'),
    (64, 'White; American Indian and Alaska Native; Some other race'),
    (65, 'White; American Indian and Alaska Native'),
    (66, 'White; Black or African American; Some other race'),
    (67, 'White; Black or African American; American Indian and Alaska Native'),
    (68, 'White; Black or African American'),
    (69, 'White alone'),
    (70, 'White race; two or more Asian groups'),
    (71, 'White race; Black or African American race and/or American Indian and Alaska Native race and/or Asian groups and/or Native Hawaiian and Other Pacific Islander groups'),
    (72, 'White race; Some other race; Black or African American race and/or American Indian and Alaska Native race and/or Asian groups and/or Native Hawaiian and Other Pacific Islander groups'),
]

RACAIAN = [
    (0, 'No'),
    (1, 'Yes'),
]

RACASN = [
    (0, 'No'),
    (1, 'Yes'),
]

RACBLK = [
    (0, 'No'),
    (1, 'Yes'),
]

RACNHPI = [
    (0, 'No'),
    (1, 'Yes'),
]

RACNUM = [
    (1..6, 'Race groups'),
]

RACSOR = [
    (0, 'No'),
    (1, 'Yes'),
]

RACWHT = [
    (0, 'No'),
    (1, 'Yes'),
]

RC = [
    (0, 'No (includes GQ)'),
    (1, 'Yes'),
]

SFN = [
    (b, 'N/A (GQ/not in a subfamily)'),
    (1, 'In subfamily 1'),
    (2, 'In subfamily 2'),
    (3, 'In subfamily 3'),
    (4, 'In subfamily 4'),
]

SFR = [
    (b, 'N/A (GQ/not in a subfamily)'),
    (1, 'Husband/wife no children'),
    (2, 'Husband/wife with children'),
    (3, 'Parent in a parent/child subfamily'),
    (4, 'Child in a married-couple subfamily'),
    (5, 'Child in a mother-child subfamily'),
    (6, 'Child in a father-child subfamily'),
]

SOCP = [
    (bbbbbb, 'N/A (less than 16 years old/unemployed who never worked/NILF who last worked more than 5 years ago)'),
    (111021, 'MGR-GENERAL AND OPERATIONS MANAGERS'),
    (1110XX, 'MGR-CHIEF EXECUTIVES AND LEGISLATORS *'),
    (112011, 'MGR-ADVERTISING AND PROMOTIONS MANAGERS'),
    (112020, 'MGR-MARKETING AND SALES MANAGERS'),
    (112031, 'MGR-PUBLIC RELATIONS MANAGERS'),
    (113011, 'MGR-ADMINISTRATIVE SERVICES MANAGERS'),
    (113021, 'MGR-COMPUTER AND INFORMATION SYSTEMS MANAGERS'),
    (113031, 'MGR-FINANCIAL MANAGERS'),
    (113040, 'MGR-HUMAN RESOURCES MANAGERS'),
    (113051, 'MGR-INDUSTRIAL PRODUCTION MANAGERS'),
    (113061, 'MGR-PURCHASING MANAGERS'),
    (113071, 'MGR-TRANSPORTATION, STORAGE, AND DISTRIBUTION MANAGERS'),
    (119011, 'MGR-FARM, RANCH, AND OTHER AGRICULTURAL MANAGERS'),
    (119012, 'MGR-FARMERS AND RANCHERS'),
    (119021, 'MGR-CONSTRUCTION MANAGERS'),
    (119030, 'MGR-EDUCATION ADMINISTRATORS'),
    (119041, 'MGR-ENGINEERING MANAGERS'),
    (119051, 'MGR-FOOD SERVICE MANAGERS'),
    (119061, 'MGR-FUNERAL DIRECTORS'),
    (119071, 'MGR-GAMING MANAGERS'),
    (119081, 'MGR-LODGING MANAGERS'),
    (119111, 'MGR-MEDICAL AND HEALTH SERVICES MANAGERS'),
    (119121, 'MGR-NATURAL SCIENCES MANAGERS'),
    (119141, 'MGR-PROPERTY, REAL ESTATE, AND COMMUNITY ASSOCIATION MANAGERS'),
    (119151, 'MGR-SOCIAL AND COMMUNITY SERVICE MANAGERS'),
    (1191XX, 'MGR-MISCELLANEOUS MANAGERS, INCLUDING POSTMASTERS AND MAIL SUPERINTENDENTS'),
    (131011, 'BUS-AGENTS AND BUSINESS MANAGERS OF ARTISTS, PERFORMERS, AND ATHLETES'),
    (131021, 'BUS-PURCHASING AGENTS AND BUYERS, FARM PRODUCTS'),
    (131022, 'BUS-WHOLESALE AND RETAIL BUYERS, EXCEPT FARM PRODUCTS'),
    (131023, 'BUS-PURCHASING AGENTS, EXCEPT WHOLESALE, RETAIL, AND FARM PRODUCTS'),
    (131030, 'BUS-CLAIMS ADJUSTERS, APPRAISERS, EXAMINERS, AND INVESTIGATORS'),
    (131041, 'BUS-COMPLIANCE OFFICERS, EXCEPT AGRICULTURE, CONSTRUCTION, HEALTH AND SAFETY, AND TRANSPORTATION'),
    (131051, 'BUS-COST ESTIMATORS'),
    (131070, 'BUS-HUMAN RESOURCES, TRAINING, AND LABOR RELATIONS SPECIALISTS'),
    (131081, 'BUS-LOGISTICIANS'),
    (131111, 'BUS-MANAGEMENT ANALYSTS'),
    (131121, 'BUS-MEETING AND CONVENTION PLANNERS'),
    (131XXX, 'BUS-OTHER BUSINESS OPERATIONS SPECIALISTS *'),
    (132011, 'FIN-ACCOUNTANTS AND AUDITORS'),
    (132021, 'FIN-APPRAISERS AND ASSESSORS OF REAL ESTATE'),
    (132031, 'FIN-BUDGET ANALYSTS'),
    (132041, 'FIN-CREDIT ANALYSTS'),
    (132051, 'FIN-FINANCIAL ANALYSTS'),
    (132052, 'FIN-PERSONAL FINANCIAL ADVISORS'),
    (132053, 'FIN-INSURANCE UNDERWRITERS'),
    (132061, 'FIN-FINANCIAL EXAMINERS'),
    (132070, 'FIN-LOAN COUNSELORS AND OFFICERS'),
    (132081, 'FIN-TAX EXAMINERS, COLLECTORS, AND REVENUE AGENTS'),
    (132082, 'FIN-TAX PREPARERS'),
    (132099, 'FIN-FINANCIAL SPECIALISTS, ALL OTHER'),
    (151021, 'CMM-COMPUTER PROGRAMMERS'),
    (151030, 'CMM-COMPUTER SOFTWARE ENGINEERS'),
    (151041, 'CMM-COMPUTER SUPPORT SPECIALISTS'),
    (151061, 'CMM-DATABASE ADMINISTRATORS'),
    (151071, 'CMM-NETWORK AND COMPUTER SYSTEMS ADMINISTRATORS'),
    (151081, 'CMM-NETWORK SYSTEMS AND DATA COMMUNICATIONS ANALYSTS'),
    (1510XX, 'CMM-COMPUTER SCIENTISTS AND SYSTEMS ANALYSTS *'),
    (152011, 'CMM-ACTUARIES'),
    (152031, 'CMM-OPERATIONS RESEARCH ANALYSTS'),
    (1520XX, 'CMM-MISCELLANEOUS MATHEMATICAL SCIENCE OCCUPATIONS, INCLUDING MATHEMATICIANS AND STATISTICIANS *'),
    (171010, 'ENG-ARCHITECTS, EXCEPT NAVAL'),
    (171020, 'ENG-SURVEYORS, CARTOGRAPHERS, AND PHOTOGRAMMETRISTS'),
    (172011, 'ENG-AEROSPACE ENGINEERS'),
    (172041, 'ENG-CHEMICAL ENGINEERS'),
    (172051, 'ENG-CIVIL ENGINEERS'),
    (172061, 'ENG-COMPUTER HARDWARE ENGINEERS'),
    (172070, 'ENG-ELECTRICAL AND ELECTRONICS ENGINEERS'),
    (172081, 'ENG-ENVIRONMENTAL ENGINEERS'),
    (1720XX, 'ENG-BIOMEDICAL AND AGRICULTURAL ENGINEERS *'),
    (172110, 'ENG-INDUSTRIAL ENGINEERS, INCLUDING HEALTH AND SAFETY'),
    (172121, 'ENG-MARINE ENGINEERS AND NAVAL ARCHITECTS'),
    (172131, 'ENG-MATERIALS ENGINEERS'),
    (172141, 'ENG-MECHANICAL ENGINEERS'),
    (1721XX, 'ENG-PETROLEUM, MINING AND GEOLOGICAL ENGINEERS, INCLUDING MINING SAFETY ENGINEERS *'),
    (1721YY, 'ENG-MISCELLANEOUS ENGINEERS, INCLUDING NUCLEAR ENGINEERS *'),
    (173010, 'ENG-DRAFTERS'),
    (173020, 'ENG-ENGINEERING TECHNICIANS, EXCEPT DRAFTERS'),
    (173031, 'ENG-SURVEYING AND MAPPING TECHNICIANS'),
    (191010, 'SCI-AGRICULTURAL AND FOOD SCIENTISTS'),
    (191020, 'SCI-BIOLOGICAL SCIENTISTS'),
    (191030, 'SCI-CONSERVATION SCIENTISTS AND FORESTERS'),
    (191040, 'SCI-MEDICAL SCIENTISTS'),
    (192010, 'SCI-ASTRONOMERS AND PHYSICISTS'),
    (192021, 'SCI-ATMOSPHERIC AND SPACE SCIENTISTS'),
    (192030, 'SCI-CHEMISTS AND MATERIALS SCIENTISTS'),
    (192040, 'SCI-ENVIRONMENTAL SCIENTISTS AND GEOSCIENTISTS'),
    (192099, 'SCI-PHYSICAL SCIENTISTS, ALL OTHER'),
    (193011, 'SCI-ECONOMISTS'),
    (193020, 'SCI-MARKET AND SURVEY RESEARCHERS'),
    (193030, 'SCI-PSYCHOLOGISTS'),
    (193051, 'SCI-URBAN AND REGIONAL PLANNERS'),
    (1930XX, 'SCI-MISCELLANEOUS SOCIAL SCIENTISTS, INCLUDING SOCIOLOGISTS *'),
    (194011, 'SCI-AGRICULTURAL AND FOOD SCIENCE TECHNICIANS'),
    (194021, 'SCI-BIOLOGICAL TECHNICIANS'),
    (194031, 'SCI-CHEMICAL TECHNICIANS'),
    (194041, 'SCI-GEOLOGICAL AND PETROLEUM TECHNICIANS'),
    (1940XX, 'SCI-MISCELLANEOUS LIFE, PHYSICAL, AND SOCIAL SCIENCE TECHNICIANS, INCLUDING SOCIAL SCIENCE RESEARCH ASSISTANTS AND NUCLEAR TECHNICIANS *'),
    (211010, 'CMS-COUNSELORS'),
    (211020, 'CMS-SOCIAL WORKERS'),
    (211090, 'CMS-MISCELLANEOUS COMMUNITY AND SOCIAL SERVICE SPECIALISTS'),
    (212011, 'CMS-CLERGY'),
    (212021, 'CMS-DIRECTORS, RELIGIOUS ACTIVITIES AND EDUCATION'),
    (212099, 'CMS-RELIGIOUS WORKERS, ALL OTHER'),
    (2310XX, 'LGL-LAWYERS AND JUDGES, MAGISTRATES, AND OTHER JUDICIAL WORKERS'),
    (232011, 'LGL-PARALEGALS AND LEGAL ASSISTANTS'),
    (232090, 'LGL-MISCELLANEOUS LEGAL SUPPORT WORKERS'),
    (251000, 'EDU-POSTSECONDARY TEACHERS'),
    (252010, 'EDU-PRESCHOOL AND KINDERGARTEN TEACHERS'),
    (252020, 'EDU-ELEMENTARY AND MIDDLE SCHOOL TEACHERS'),
    (252030, 'EDU-SECONDARY SCHOOL TEACHERS'),
    (252040, 'EDU-SPECIAL EDUCATION TEACHERS'),
    (253000, 'EDU-OTHER TEACHERS AND INSTRUCTORS'),
    (254010, 'EDU-ARCHIVISTS, CURATORS, AND MUSEUM TECHNICIANS'),
    (254021, 'EDU-LIBRARIANS'),
    (254031, 'EDU-LIBRARY TECHNICIANS'),
    (259041, 'EDU-TEACHER ASSISTANTS'),
    (2590XX, 'EDU-OTHER EDUCATION, TRAINING, AND LIBRARY WORKERS *'),
    (271010, 'ENT-ARTISTS AND RELATED WORKERS'),
    (271020, 'ENT-DESIGNERS'),
    (272011, 'ENT-ACTORS'),
    (272012, 'ENT-PRODUCERS AND DIRECTORS'),
    (272020, 'ENT-ATHLETES, COACHES, UMPIRES, AND RELATED WORKERS'),
    (272030, 'ENT-DANCERS AND CHOREOGRAPHERS'),
    (272040, 'ENT-MUSICIANS, SINGERS, AND RELATED WORKERS'),
    (272099, 'ENT-ENTERTAINERS AND PERFORMERS, SPORTS AND RELATED WORKERS, ALL OTHER'),
    (273010, 'ENT-ANNOUNCERS'),
    (273020, 'ENT-NEWS ANALYSTS, REPORTERS AND CORRESPONDENTS'),
    (273031, 'ENT-PUBLIC RELATIONS SPECIALISTS'),
    (273041, 'ENT-EDITORS'),
    (273042, 'ENT-TECHNICAL WRITERS'),
    (273043, 'ENT-WRITERS AND AUTHORS'),
    (273090, 'ENT-MISCELLANEOUS MEDIA AND COMMUNICATION WORKERS'),
    (274021, 'ENT-PHOTOGRAPHERS'),
    (274030, 'ENT-TELEVISION, VIDEO, AND MOTION PICTURE CAMERA OPERATORS AND EDITORS'),
    (2740XX, 'ENT-BROADCAST AND SOUND ENGINEERING TECHNICIANS AND RADIO OPERATORS, AND MEDIA AND COMMUNICATION EQUIPMENT WORKERS, ALL OTHER *'),
    (291011, 'MED-CHIROPRACTORS'),
    (291020, 'MED-DENTISTS'),
    (291031, 'MED-DIETITIANS AND NUTRITIONISTS'),
    (291041, 'MED-OPTOMETRISTS'),
    (291051, 'MED-PHARMACISTS'),
    (291060, 'MED-PHYSICIANS AND SURGEONS'),
    (291071, 'MED-PHYSICIAN ASSISTANTS'),
    (291081, 'MED-PODIATRISTS'),
    (291111, 'MED-REGISTERED NURSES'),
    (291121, 'MED-AUDIOLOGISTS'),
    (291122, 'MED-OCCUPATIONAL THERAPISTS'),
    (291123, 'MED-PHYSICAL THERAPISTS'),
    (291124, 'MED-RADIATION THERAPISTS'),
    (291125, 'MED-RECREATIONAL THERAPISTS'),
    (291126, 'MED-RESPIRATORY THERAPISTS'),
    (291127, 'MED-SPEECH-LANGUAGE PATHOLOGISTS'),
    (291129, 'MED-THERAPISTS, ALL OTHER'),
    (291131, 'MED-VETERINARIANS'),
    (291199, 'MED-HEALTH DIAGNOSING AND TREATING PRACTITIONERS, ALL OTHER'),
    (292010, 'MED-CLINICAL LABORATORY TECHNOLOGISTS AND TECHNICIANS'),
    (292021, 'MED-DENTAL HYGIENISTS'),
    (292030, 'MED-DIAGNOSTIC RELATED TECHNOLOGISTS AND TECHNICIANS'),
    (292041, 'MED-EMERGENCY MEDICAL TECHNICIANS AND PARAMEDICS'),
    (292050, 'MED-HEALTH DIAGNOSING AND TREATING PRACTITIONER SUPPORT TECHNICIANS'),
    (292061, 'MED-LICENSED PRACTICAL AND LICENSED VOCATIONAL NURSES'),
    (292071, 'MED-MEDICAL RECORDS AND HEALTH INFORMATION TECHNICIANS'),
    (292081, 'MED-OPTICIANS, DISPENSING'),
    (292090, 'MED-MISCELLANEOUS HEALTH TECHNOLOGISTS AND TECHNICIANS'),
    (299000, 'MED-OTHER HEALTHCARE PRACTITIONERS AND TECHNICAL OCCUPATIONS'),
    (311010, 'HLS-NURSING, PSYCHIATRIC, AND HOME HEALTH AIDES'),
    (312010, 'HLS-OCCUPATIONAL THERAPIST ASSISTANTS AND AIDES'),
    (312020, 'HLS-PHYSICAL THERAPIST ASSISTANTS AND AIDES'),
    (319011, 'HLS-MASSAGE THERAPISTS'),
    (319091, 'HLS-DENTAL ASSISTANTS'),
    (31909X, 'HLS-MEDICAL ASSISTANTS AND OTHER HEALTHCARE SUPPORT OCCUPATIONS, EXCEPT DENTAL ASSISTANTS *'),
    (331011, 'PRT-FIRST-LINE SUPERVISORS/MANAGERS OF CORRECTIONAL OFFICERS'),
    (331012, 'PRT-FIRST-LINE SUPERVISORS/MANAGERS OF POLICE AND DETECTIVES'),
    (331021, 'PRT-FIRST-LINE SUPERVISORS/MANAGERS OF FIRE FIGHTING AND PREVENTION WORKERS'),
    (331099, 'PRT-SUPERVISORS, PROTECTIVE SERVICE WORKERS, ALL OTHER'),
    (332011, 'PRT-FIRE FIGHTERS'),
    (332020, 'PRT-FIRE INSPECTORS'),
    (333010, 'PRT-BAILIFFS, CORRECTIONAL OFFICERS, AND JAILERS'),
    (333021, 'PRT-DETECTIVES AND CRIMINAL INVESTIGATORS'),
    (333050, 'PRT-POLICE OFFICERS'),
    (3330XX, 'PRT-MISCELLANEOUS LAW ENFORCEMENT WORKERS *'),
    (339011, 'PRT-ANIMAL CONTROL WORKERS'),
    (339021, 'PRT-PRIVATE DETECTIVES AND INVESTIGATORS'),
    (339030, 'PRT-SECURITY GUARDS AND GAMING SURVEILLANCE OFFICERS'),
    (339091, 'PRT-CROSSING GUARDS'),
    (33909X, 'PRT-LIFEGUARDS AND OTHER PROTECTIVE SERVICE WORKERS *'),
    (351011, 'EAT-CHEFS AND HEAD COOKS'),
    (351012, 'EAT-FIRST-LINE SUPERVISORS/MANAGERS OF FOOD PREPARATION AND SERVING WORKERS'),
    (352010, 'EAT-COOKS'),
    (352021, 'EAT-FOOD PREPARATION WORKERS'),
    (353011, 'EAT-BARTENDERS'),
    (353021, 'EAT-COMBINED FOOD PREPARATION AND SERVING WORKERS, INCLUDING FAST FOOD'),
    (353022, 'EAT-COUNTER ATTENDANTS, CAFETERIA, FOOD CONCESSION, AND COFFEE SHOP'),
    (353031, 'EAT-WAITERS AND WAITRESSES'),
    (353041, 'EAT-FOOD SERVERS, NONRESTAURANT'),
    (359021, 'EAT-DISHWASHERS'),
    (359031, 'EAT-HOSTS AND HOSTESSES, RESTAURANT, LOUNGE, AND COFFEE SHOP'),
    (3590XX, 'EAT-MISCELLANEOUS FOOD PREPARATION AND SERVING RELATED WORKERS, INCLUDING DINING ROOM AND CAFETERIA ATTENDANTS AND BARTENDER HELPERS *'),
    (371011, 'CLN-FIRST-LINE SUPERVISORS/MANAGERS OF HOUSEKEEPING AND JANITORIAL WORKERS'),
    (371012, 'CLN-FIRST-LINE SUPERVISORS/MANAGERS OF LANDSCAPING, LAWN SERVICE, AND GROUNDSKEEPING WORKERS'),
    (372012, 'CLN-MAIDS AND HOUSEKEEPING CLEANERS'),
    (37201X, 'CLN-JANITORS AND BUILDING CLEANERS *'),
    (372021, 'CLN-PEST CONTROL WORKERS'),
    (373010, 'CLN-GROUNDS MAINTENANCE WORKERS'),
    (391010, 'PRS-FIRST-LINE SUPERVISORS/MANAGERS OF GAMING WORKERS'),
    (391021, 'PRS-FIRST-LINE SUPERVISORS/MANAGERS OF PERSONAL SERVICE WORKERS'),
    (392011, 'PRS-ANIMAL TRAINERS'),
    (392021, 'PRS-NONFARM ANIMAL CARETAKERS'),
    (393010, 'PRS-GAMING SERVICES WORKERS'),
    (393021, 'PRS-MOTION PICTURE PROJECTIONISTS'),
    (393031, 'PRS-USHERS, LOBBY ATTENDANTS, AND TICKET TAKERS'),
    (393090, 'PRS-MISCELLANEOUS ENTERTAINMENT ATTENDANTS AND RELATED WORKERS'),
    (394000, 'PRS-FUNERAL SERVICE WORKERS'),
    (395011, 'PRS-BARBERS'),
    (395012, 'PRS-HAIRDRESSERS, HAIRSTYLISTS, AND COSMETOLOGISTS'),
    (395090, 'PRS-MISCELLANEOUS PERSONAL APPEARANCE WORKERS'),
    (396010, 'PRS-BAGGAGE PORTERS, BELLHOPS, AND CONCIERGES'),
    (396020, 'PRS-TOUR AND TRAVEL GUIDES'),
    (396030, 'PRS-TRANSPORTATION ATTENDANTS'),
    (399011, 'PRS-CHILD CARE WORKERS'),
    (399021, 'PRS-PERSONAL AND HOME CARE AIDES'),
    (399030, 'PRS-RECREATION AND FITNESS WORKERS'),
    (399041, 'PRS-RESIDENTIAL ADVISORS'),
    (399099, 'PRS-PERSONAL CARE AND SERVICE WORKERS, ALL OTHER'),
    (411011, 'SAL-FIRST-LINE SUPERVISORS/MANAGERS OF RETAIL SALES WORKERS'),
    (411012, 'SAL-FIRST-LINE SUPERVISORS/MANAGERS OF NON-RETAIL SALES WORKERS'),
    (412010, 'SAL-CASHIERS'),
    (412021, 'SAL-COUNTER AND RENTAL CLERKS'),
    (412022, 'SAL-PARTS SALESPERSONS'),
    (412031, 'SAL-RETAIL SALESPERSONS'),
    (413011, 'SAL-ADVERTISING SALES AGENTS'),
    (413021, 'SAL-INSURANCE SALES AGENTS'),
    (413031, 'SAL-SECURITIES, COMMODITIES, AND FINANCIAL SERVICES SALES AGENTS'),
    (413041, 'SAL-TRAVEL AGENTS'),
    (413099, 'SAL-SALES REPRESENTATIVES, SERVICES, ALL OTHER'),
    (414010, 'SAL-SALES REPRESENTATIVES, WHOLESALE AND MANUFACTURING'),
    (419010, 'SAL-MODELS, DEMONSTRATORS, AND PRODUCT PROMOTERS'),
    (419020, 'SAL-REAL ESTATE BROKERS AND SALES AGENTS'),
    (419031, 'SAL-SALES ENGINEERS'),
    (419041, 'SAL-TELEMARKETERS'),
    (419091, 'SAL-DOOR-TO-DOOR SALES WORKERS, NEWS AND STREET VENDORS, AND RELATED WORKERS'),
    (419099, 'SAL-SALES AND RELATED WORKERS, ALL OTHER'),
    (431011, 'OFF-FIRST-LINE SUPERVISORS/MANAGERS OF OFFICE AND ADMINISTRATIVE SUPPORT WORKERS'),
    (432011, 'OFF-SWITCHBOARD OPERATORS, INCLUDING ANSWERING SERVICE'),
    (432021, 'OFF-TELEPHONE OPERATORS'),
    (432099, 'OFF-COMMUNICATIONS EQUIPMENT OPERATORS, ALL OTHER'),
    (433011, 'OFF-BILL AND ACCOUNT COLLECTORS'),
    (433021, 'OFF-BILLING AND POSTING CLERKS AND MACHINE OPERATORS'),
    (433031, 'OFF-BOOKKEEPING, ACCOUNTING, AND AUDITING CLERKS'),
    (433041, 'OFF-GAMING CAGE WORKERS'),
    (433051, 'OFF-PAYROLL AND TIMEKEEPING CLERKS'),
    (433061, 'OFF-PROCUREMENT CLERKS'),
    (433071, 'OFF-TELLERS'),
    (434011, 'OFF-BROKERAGE CLERKS'),
    (434031, 'OFF-COURT, MUNICIPAL, AND LICENSE CLERKS'),
    (434041, 'OFF-CREDIT AUTHORIZERS, CHECKERS, AND CLERKS'),
    (434051, 'OFF-CUSTOMER SERVICE REPRESENTATIVES'),
    (434061, 'OFF-ELIGIBILITY INTERVIEWERS, GOVERNMENT PROGRAMS'),
    (434071, 'OFF-FILE CLERKS'),
    (434081, 'OFF-HOTEL, MOTEL, AND RESORT DESK CLERKS'),
    (434111, 'OFF-INTERVIEWERS, EXCEPT ELIGIBILITY AND LOAN'),
    (434121, 'OFF-LIBRARY ASSISTANTS, CLERICAL'),
    (434131, 'OFF-LOAN INTERVIEWERS AND CLERKS'),
    (434141, 'OFF-NEW ACCOUNTS CLERKS'),
    (434161, 'OFF-HUMAN RESOURCES ASSISTANTS, EXCEPT PAYROLL AND TIMEKEEPING'),
    (434171, 'OFF-RECEPTIONISTS AND INFORMATION CLERKS'),
    (434181, 'OFF-RESERVATION AND TRANSPORTATION TICKET AGENTS AND TRAVEL CLERKS'),
    (434199, 'OFF-INFORMATION AND RECORD CLERKS, ALL OTHER'),
    (434XXX, 'OFF-CORRESPONDENCE CLERKS AND ORDER CLERKS *'),
    (435011, 'OFF-CARGO AND FREIGHT AGENTS'),
    (435021, 'OFF-COURIERS AND MESSENGERS'),
    (435030, 'OFF-DISPATCHERS'),
    (435041, 'OFF-METER READERS, UTILITIES'),
    (435051, 'OFF-POSTAL SERVICE CLERKS'),
    (435052, 'OFF-POSTAL SERVICE MAIL CARRIERS'),
    (435053, 'OFF-POSTAL SERVICE MAIL SORTERS, PROCESSORS, AND PROCESSING MACHINE OPERATORS'),
    (435061, 'OFF-PRODUCTION, PLANNING, AND EXPEDITING CLERKS'),
    (435071, 'OFF-SHIPPING, RECEIVING, AND TRAFFIC CLERKS'),
    (435081, 'OFF-STOCK CLERKS AND ORDER FILLERS'),
    (435111, 'OFF-WEIGHERS, MEASURERS, CHECKERS, AND SAMPLERS, RECORDKEEPING'),
    (436010, 'OFF-SECRETARIES AND ADMINISTRATIVE ASSISTANTS'),
    (439011, 'OFF-COMPUTER OPERATORS'),
    (439021, 'OFF-DATA ENTRY KEYERS'),
    (439022, 'OFF-WORD PROCESSORS AND TYPISTS'),
    (439041, 'OFF-INSURANCE CLAIMS AND POLICY PROCESSING CLERKS'),
    (439051, 'OFF-MAIL CLERKS AND MAIL MACHINE OPERATORS, EXCEPT POSTAL SERVICE'),
    (439061, 'OFF-OFFICE CLERKS, GENERAL'),
    (439071, 'OFF-OFFICE MACHINE OPERATORS, EXCEPT COMPUTER'),
    (439081, 'OFF-PROOFREADERS AND COPY MARKERS'),
    (439111, 'OFF-STATISTICAL ASSISTANTS'),
    (439XXX, 'OFF-MISCELLANEOUS OFFICE AND ADMINISTRATIVE SUPPORT WORKERS, INCLUDING DESKTOP PUBLISHERS *'),
    (451010, 'FFF-FIRST-LINE SUPERVISORS/MANAGERS OF FARMING, FISHING, AND FORESTRY WORKERS'),
    (452011, 'FFF-AGRICULTURAL INSPECTORS'),
    (452041, 'FFF-GRADERS AND SORTERS, AGRICULTURAL PRODUCTS'),
    (4520XX, 'FFF-MISCELLANEOUS AGRICULTURAL WORKERS, INCLUDING ANIMAL BREEDERS *'),
    (453000, 'FFF-FISHING AND HUNTING WORKERS'),
    (454011, 'FFF-FOREST AND CONSERVATION WORKERS'),
    (454020, 'FFF-LOGGING WORKERS'),
    (471011, 'CON-FIRST-LINE SUPERVISORS/MANAGERS OF CONSTRUCTION TRADES AND EXTRACTION WORKERS'),
    (472011, 'CON-BOILERMAKERS'),
    (472020, 'CON-BRICKMASONS, BLOCKMASONS, AND STONEMASONS'),
    (472031, 'CON-CARPENTERS'),
    (472040, 'CON-CARPET, FLOOR, AND TILE INSTALLERS AND FINISHERS'),
    (472050, 'CON-CEMENT MASONS, CONCRETE FINISHERS, AND TERRAZZO WORKERS'),
    (472061, 'CON-CONSTRUCTION LABORERS'),
    (472071, 'CON-PAVING, SURFACING, AND TAMPING EQUIPMENT OPERATORS'),
    (47207X, 'CON-CONSTRUCTION EQUIPMENT OPERATORS, EXCEPT PAVING, SURFACING, AND TAMPING EQUIPMENT OPERATORS *'),
    (472080, 'CON-DRYWALL INSTALLERS, CEILING TILE INSTALLERS, AND TAPERS'),
    (472111, 'CON-ELECTRICIANS'),
    (472121, 'CON-GLAZIERS'),
    (472130, 'CON-INSULATION WORKERS'),
    (472141, 'CON-PAINTERS, CONSTRUCTION AND MAINTENANCE'),
    (472142, 'CON-PAPERHANGERS'),
    (472150, 'CON-PIPELAYERS, PLUMBERS, PIPEFITTERS, AND STEAMFITTERS'),
    (472161, 'CON-PLASTERERS AND STUCCO MASONS'),
    (472171, 'CON-REINFORCING IRON AND REBAR WORKERS'),
    (472181, 'CON-ROOFERS'),
    (472211, 'CON-SHEET METAL WORKERS'),
    (472221, 'CON-STRUCTURAL IRON AND STEEL WORKERS'),
    (473010, 'CON-HELPERS, CONSTRUCTION TRADES'),
    (474011, 'CON-CONSTRUCTION AND BUILDING INSPECTORS'),
    (474021, 'CON-ELEVATOR INSTALLERS AND REPAIRERS'),
    (474031, 'CON-FENCE ERECTORS'),
    (474041, 'CON-HAZARDOUS MATERIALS REMOVAL WORKERS'),
    (474051, 'CON-HIGHWAY MAINTENANCE WORKERS'),
    (474061, 'CON-RAIL-TRACK LAYING AND MAINTENANCE EQUIPMENT OPERATORS'),
    (4740XX, 'CON-MISCELLANEOUS CONSTRUCTION WORKERS, INCLUDING SEPTIC TANK SERVICERS AND SEWER PIPE CLEANERS *'),
    (475021, 'EXT-EARTH DRILLERS, EXCEPT OIL AND GAS'),
    (475031, 'EXT-EXPLOSIVES WORKERS, ORDNANCE HANDLING EXPERTS, AND BLASTERS'),
    (475040, 'EXT-MINING MACHINE OPERATORS'),
    (4750XX, 'EXT-MISCELLANEOUS EXTRACTION WORKERS, INCLUDING ROOF BOLTERS AND HELPERS *'),
    (4750YY, 'EXT-DERRICK, ROTARY DRILL, AND SERVICE UNIT OPERATORS, AND ROUSTABOUTS, OIL, GAS, AND MINING *'),
    (491011, 'RPR-FIRST-LINE SUPERVISORS/MANAGERS OF MECHANICS, INSTALLERS, AND REPAIRERS'),
    (492011, 'RPR-COMPUTER, AUTOMATED TELLER, AND OFFICE MACHINE REPAIRERS'),
    (492020, 'RPR-RADIO AND TELECOMMUNICATIONS EQUIPMENT INSTALLERS AND REPAIRERS'),
    (492091, 'RPR-AVIONICS TECHNICIANS'),
    (492092, 'RPR-ELECTRIC MOTOR, POWER TOOL, AND RELATED REPAIRERS'),
    (492096, 'RPR-ELECTRONIC EQUIPMENT INSTALLERS AND REPAIRERS, MOTOR VEHICLES'),
    (492097, 'RPR-ELECTRONIC HOME ENTERTAINMENT EQUIPMENT INSTALLERS AND REPAIRERS'),
    (492098, 'RPR-SECURITY AND FIRE ALARM SYSTEMS INSTALLERS'),
    (49209X, 'RPR-ELECTRICAL AND ELECTRONICS REPAIRERS, TRANSPORTATION EQUIPMENT, AND INDUSTRIAL AND UTILITY *'),
    (493011, 'RPR-AIRCRAFT MECHANICS AND SERVICE TECHNICIANS'),
    (493021, 'RPR-AUTOMOTIVE BODY AND RELATED REPAIRERS'),
    (493022, 'RPR-AUTOMOTIVE GLASS INSTALLERS AND REPAIRERS'),
    (493023, 'RPR-AUTOMOTIVE SERVICE TECHNICIANS AND MECHANICS'),
    (493031, 'RPR-BUS AND TRUCK MECHANICS AND DIESEL ENGINE SPECIALISTS'),
    (493040, 'RPR-HEAVY VEHICLE AND MOBILE EQUIPMENT SERVICE TECHNICIANS AND MECHANICS'),
    (493050, 'RPR-SMALL ENGINE MECHANICS'),
    (493090, 'RPR-MISCELLANEOUS VEHICLE AND MOBILE EQUIPMENT MECHANICS, INSTALLERS, AND REPAIRERS'),
    (499010, 'RPR-CONTROL AND VALVE INSTALLERS AND REPAIRERS'),
    (499021, 'RPR-HEATING, AIR CONDITIONING, AND REFRIGERATION MECHANICS AND INSTALLERS'),
    (499031, 'RPR-HOME APPLIANCE REPAIRERS'),
    (499042, 'RPR-MAINTENANCE AND REPAIR WORKERS, GENERAL'),
    (499043, 'RPR-MAINTENANCE WORKERS, MACHINERY'),
    (499044, 'RPR-MILLWRIGHTS'),
    (49904X, 'RPR-INDUSTRIAL AND REFRACTORY MACHINERY MECHANICS *'),
    (499051, 'RPR-ELECTRICAL POWER-LINE INSTALLERS AND REPAIRERS'),
    (499052, 'RPR-TELECOMMUNICATIONS LINE INSTALLERS AND REPAIRERS'),
    (499060, 'RPR-PRECISION INSTRUMENT AND EQUIPMENT REPAIRERS'),
    (499091, 'RPR-COIN, VENDING, AND AMUSEMENT MACHINE SERVICERS AND REPAIRERS'),
    (499094, 'RPR-LOCKSMITHS AND SAFE REPAIRERS'),
    (499095, 'RPR-MANUFACTURED BUILDING AND MOBILE HOME INSTALLERS'),
    (499096, 'RPR-RIGGERS'),
    (499098, 'RPR-HELPERS--INSTALLATION, MAINTENANCE, AND REPAIR WORKERS'),
    (49909X, 'RPR-OTHER INSTALLATION, MAINTENANCE, AND REPAIR WORKERS, INCLUDING COMMERCIAL DIVERS, AND SIGNAL AND TRACK SWITCH REPAIRERS *'),
    (511011, 'PRD-FIRST-LINE SUPERVISORS/MANAGERS OF PRODUCTION AND OPERATING WORKERS'),
    (512011, 'PRD-AIRCRAFT STRUCTURE, SURFACES, RIGGING, AND SYSTEMS ASSEMBLERS'),
    (512020, 'PRD-ELECTRICAL, ELECTRONICS, AND ELECTROMECHANICAL ASSEMBLERS'),
    (512031, 'PRD-ENGINE AND OTHER MACHINE ASSEMBLERS'),
    (512041, 'PRD-STRUCTURAL METAL FABRICATORS AND FITTERS'),
    (512090, 'PRD-MISCELLANEOUS ASSEMBLERS AND FABRICATORS'),
    (513011, 'PRD-BAKERS'),
    (513020, 'PRD-BUTCHERS AND OTHER MEAT, POULTRY, AND FISH PROCESSING WORKERS'),
    (513091, 'PRD-FOOD AND TOBACCO ROASTING, BAKING, AND DRYING MACHINE OPERATORS AND TENDERS'),
    (513092, 'PRD-FOOD BATCHMAKERS'),
    (513093, 'PRD-FOOD COOKING MACHINE OPERATORS AND TENDERS'),
    (514010, 'PRD-COMPUTER CONTROL PROGRAMMERS AND OPERATORS'),
    (514021, 'PRD-EXTRUDING AND DRAWING MACHINE SETTERS, OPERATORS, AND TENDERS, METAL AND PLASTIC'),
    (514022, 'PRD-FORGING MACHINE SETTERS, OPERATORS, AND TENDERS, METAL AND PLASTIC'),
    (514023, 'PRD-ROLLING MACHINE SETTERS, OPERATORS, AND TENDERS, METAL AND PLASTIC'),
    (514031, 'PRD-CUTTING, PUNCHING, AND PRESS MACHINE SETTERS, OPERATORS, AND TENDERS, METAL AND PLASTIC'),
    (514032, 'PRD-DRILLING AND BORING MACHINE TOOL SETTERS, OPERATORS, AND TENDERS, METAL AND PLASTIC'),
    (514033, 'PRD-GRINDING, LAPPING, POLISHING, AND BUFFING MACHINE TOOL SETTERS, OPERATORS, AND TENDERS, METAL AND PLASTIC'),
    (514034, 'PRD-LATHE AND TURNING MACHINE TOOL SETTERS, OPERATORS, AND TENDERS, METAL AND PLASTIC'),
    (514041, 'PRD-MACHINISTS'),
    (514050, 'PRD-METAL FURNACE AND KILN OPERATORS AND TENDERS'),
    (514060, 'PRD-MODEL MAKERS AND PATTERNMAKERS, METAL AND PLASTIC'),
    (514070, 'PRD-MOLDERS AND MOLDING MACHINE SETTERS, OPERATORS, AND TENDERS, METAL AND PLASTIC'),
    (514111, 'PRD-TOOL AND DIE MAKERS'),
    (514120, 'PRD-WELDING, SOLDERING, AND BRAZING WORKERS'),
    (514191, 'PRD-HEAT TREATING EQUIPMENT SETTERS, OPERATORS, AND TENDERS, METAL AND PLASTIC'),
    (514193, 'PRD-PLATING AND COATING MACHINE SETTERS, OPERATORS, AND TENDERS, METAL AND PLASTIC'),
    (514194, 'PRD-TOOL GRINDERS, FILERS, AND SHARPENERS'),
    (514XXX, 'PRD-MISCELLANEOUS METAL WORKERS AND PLASTIC WORKERS, INCLUDING MILLING AND PLANING MACHINE SETTERS, AND MULTIPLE MACHINE TOOL SETTERS, AND LAY-OUT WORKERS *'),
    (515010, 'PRD-BOOKBINDERS AND BINDERY WORKERS'),
    (515021, 'PRD-JOB PRINTERS'),
    (515022, 'PRD-PREPRESS TECHNICIANS AND WORKERS'),
    (515023, 'PRD-PRINTING MACHINE OPERATORS'),
    (516011, 'PRD-LAUNDRY AND DRY-CLEANING WORKERS'),
    (516021, 'PRD-PRESSERS, TEXTILE, GARMENT, AND RELATED MATERIALS'),
    (516031, 'PRD-SEWING MACHINE OPERATORS'),
    (516041, 'PRD-SHOE AND LEATHER WORKERS AND REPAIRERS'),
    (516042, 'PRD-SHOE MACHINE OPERATORS AND TENDERS'),
    (516050, 'PRD-TAILORS, DRESSMAKERS, AND SEWERS'),
    (516063, 'PRD-TEXTILE KNITTING AND WEAVING MACHINE SETTERS, OPERATORS, AND TENDERS'),
    (516064, 'PRD-TEXTILE WINDING, TWISTING, AND DRAWING OUT MACHINE SETTERS, OPERATORS, AND TENDERS'),
    (51606X, 'PRD-TEXTILE BLEACHING AND DYEING, AND CUTTING MACHINE SETTERS, OPERATORS, AND TENDERS *'),
    (516093, 'PRD-UPHOLSTERERS'),
    (51609X, 'PRD-MISCELLANEOUS TEXTILE, APPAREL, AND FURNISHINGS WORKERS, EXCEPT UPHOLSTERERS *'),
    (517011, 'PRD-CABINETMAKERS AND BENCH CARPENTERS'),
    (517021, 'PRD-FURNITURE FINISHERS'),
    (517041, 'PRD-SAWING MACHINE SETTERS, OPERATORS, AND TENDERS, WOOD'),
    (517042, 'PRD-WOODWORKING MACHINE SETTERS, OPERATORS, AND TENDERS, EXCEPT SAWING'),
    (5170XX, 'PRD-MISCELLANEOUS WOODWORKERS, INCLUDING MODEL MAKERS AND PATTERNMAKERS *'),
    (518010, 'PRD-POWER PLANT OPERATORS, DISTRIBUTORS, AND DISPATCHERS'),
    (518021, 'PRD-STATIONARY ENGINEERS AND BOILER OPERATORS'),
    (518031, 'PRD-WATER AND LIQUID WASTE TREATMENT PLANT AND SYSTEM OPERATORS'),
    (518090, 'PRD-MISCELLANEOUS PLANT AND SYSTEM OPERATORS'),
    (519010, 'PRD-CHEMICAL PROCESSING MACHINE SETTERS, OPERATORS, AND TENDERS'),
    (519020, 'PRD-CRUSHING, GRINDING, POLISHING, MIXING, AND BLENDING WORKERS'),
    (519030, 'PRD-CUTTING WORKERS'),
    (519041, 'PRD-EXTRUDING, FORMING, PRESSING, AND COMPACTING MACHINE SETTERS, OPERATORS, AND TENDERS'),
    (519051, 'PRD-FURNACE, KILN, OVEN, DRIER, AND KETTLE OPERATORS AND TENDERS'),
    (519061, 'PRD-INSPECTORS, TESTERS, SORTERS, SAMPLERS, AND WEIGHERS'),
    (519071, 'PRD-JEWELERS AND PRECIOUS STONE AND METAL WORKERS'),
    (519080, 'PRD-MEDICAL, DENTAL, AND OPHTHALMIC LABORATORY TECHNICIANS'),
    (519111, 'PRD-PACKAGING AND FILLING MACHINE OPERATORS AND TENDERS'),
    (519120, 'PRD-PAINTING WORKERS'),
    (519130, 'PRD-PHOTOGRAPHIC PROCESS WORKERS AND PROCESSING MACHINE OPERATORS'),
    (519191, 'PRD-CEMENTING AND GLUING MACHINE OPERATORS AND TENDERS'),
    (519192, 'PRD-CLEANING, WASHING, AND METAL PICKLING EQUIPMENT OPERATORS AND TENDERS'),
    (519194, 'PRD-ETCHERS AND ENGRAVERS'),
    (519195, 'PRD-MOLDERS, SHAPERS, AND CASTERS, EXCEPT METAL AND PLASTIC'),
    (519196, 'PRD-PAPER GOODS MACHINE SETTERS, OPERATORS, AND TENDERS'),
    (519197, 'PRD-TIRE BUILDERS'),
    (519198, 'PRD-HELPERS-PRODUCTION WORKERS'),
    (5191XX, 'PRD-OTHER PRODUCTION WORKERS, INCLUDING SEMICONDUCTOR PROCESSORS AND COOLING AND FREEZING EQUIPMENT OPERATORS *'),
    (531000, 'TRN-SUPERVISORS, TRANSPORTATION AND MATERIAL MOVING WORKERS'),
    (532010, 'TRN-AIRCRAFT PILOTS AND FLIGHT ENGINEERS'),
    (532020, 'TRN-AIR TRAFFIC CONTROLLERS AND AIRFIELD OPERATIONS SPECIALISTS'),
    (533011, 'TRN-AMBULANCE DRIVERS AND ATTENDANTS, EXCEPT EMERGENCY MEDICAL TECHNICIANS'),
    (533020, 'TRN-BUS DRIVERS'),
    (533030, 'TRN-DRIVER/SALES WORKERS AND TRUCK DRIVERS'),
    (533041, 'TRN-TAXI DRIVERS AND CHAUFFEURS'),
    (533099, 'TRN-MOTOR VEHICLE OPERATORS, ALL OTHER'),
    (534010, 'TRN-LOCOMOTIVE ENGINEERS AND OPERATORS'),
    (534021, 'TRN-RAILROAD BRAKE, SIGNAL, AND SWITCH OPERATORS'),
    (534031, 'TRN-RAILROAD CONDUCTORS AND YARDMASTERS'),
    (5340XX, 'TRN-SUBWAY, STREETCAR, AND OTHER RAIL TRANSPORTATION WORKERS *'),
    (535020, 'TRN-SHIP AND BOAT CAPTAINS AND OPERATORS'),
    (5350XX, 'TRN-SAILORS AND MARINE OILERS, AND SHIP ENGINEERS *'),
    (536021, 'TRN-PARKING LOT ATTENDANTS'),
    (536031, 'TRN-SERVICE STATION ATTENDANTS'),
    (536051, 'TRN-TRANSPORTATION INSPECTORS'),
    (5360XX, 'TRN-MISCELLANEOUS TRANSPORTATION WORKERS, INCLUDING BRIDGE AND LOCK TENDERS AND TRAFFIC TECHNICIANS *'),
    (537021, 'TRN-CRANE AND TOWER OPERATORS'),
    (537030, 'TRN-DREDGE, EXCAVATING, AND LOADING MACHINE OPERATORS'),
    (537051, 'TRN-INDUSTRIAL TRUCK AND TRACTOR OPERATORS'),
    (537061, 'TRN-CLEANERS OF VEHICLES AND EQUIPMENT'),
    (537062, 'TRN-LABORERS AND FREIGHT, STOCK, AND MATERIAL MOVERS, HAND'),
    (537063, 'TRN-MACHINE FEEDERS AND OFFBEARERS'),
    (537064, 'TRN-PACKERS AND PACKAGERS, HAND'),
    (537070, 'TRN-PUMPING STATION OPERATORS'),
    (537081, 'TRN-REFUSE AND RECYCLABLE MATERIAL COLLECTORS'),
    (5370XX, 'TRN-CONVEYOR OPERATORS AND TENDERS, AND HOIST AND WINCH OPERATORS *'),
    (5371XX, 'TRN-MISCELLANEOUS MATERIAL MOVING WORKERS, INCLUDING SHUTTLE CAR OPERATORS, AND TANK CAR, TRUCK, AND SHIP LOADERS *'),
    (551010, 'MIL-MILITARY OFFICER SPECIAL AND TACTICAL OPERATIONS LEADERS/MANAGERS'),
    (552010, 'MIL-FIRST-LINE ENLISTED MILITARY SUPERVISORS/MANAGERS'),
    (553010, 'MIL-MILITARY ENLISTED TACTICAL OPERATIONS AND AIR/WEAPONS SPECIALISTS AND CREW MEMBERS'),
    (559830, 'MIL-MILITARY, RANK NOT SPECIFIED **'),
    (999920, 'UNEMPLOYED, WITH NO WORK EXPERIENCE IN THE LAST 5 YEARS **'),
]

VPS = [
    (bb, 'N/A (less than 18 years old, no active duty) War Times:'),
    (01, 'Gulf War'),
    (02, 'Gulf War and Vietnam era'),
    (03, 'Vietnam era'),
    (04, 'Vietnam era and Korean War'),
    (05, 'Vietnam era, Korean War, and WWII'),
    (06, 'Korean War'),
    (07, 'Korean War and WWII'),
    (08, 'WWII Peace Times:'),
    (09, 'Post-Vietnam era only'),
    (10, 'Between Vietnam and Korean War only'),
    (11, 'Between Korean War and WWII only'),
    (12, 'Pre-WWII only'),
]

WAOB = [
    (1, 'US state (POB = 001-059)'),
    (2, 'PR and US Island Areas (POB = 060-099)'),
    (3, 'Latin America (POB = 303,310-399)'),
    (4, 'Asia (POB = 158-159,161,200-299)'),
    (5, 'Europe (POB = 100-157,160,162-199)'),
    (6, 'Africa (POB = 400-499)'),
    (7, 'Northern America (POB = 300-302,304-309)'),
    (8, 'Oceania and at Sea (POB = 500-554)'),
]

FAGEP = [
    (0, 'No'),
    (1, 'Yes'),
]

FANCP = [
    (0, 'No'),
    (1, 'Yes'),
]

FCITP = [
    (0, 'No'),
    (1, 'Yes'),
]

FCOWP = [
    (0, 'No'),
    (1, 'Yes'),
]

FDDRSP = [
    (0, 'No'),
    (1, 'Yes'),
]

FDEYEP = [
    (0, 'No'),
    (1, 'Yes'),
]

FDOUTP = [
    (0, 'No'),
    (1, 'Yes'),
]

FDPHYP = [
    (0, 'No'),
    (1, 'Yes'),
]

FDREMP = [
    (0, 'No'),
    (1, 'Yes'),
]

FDWRKP = [
    (0, 'No'),
    (1, 'Yes'),
]

FENGP = [
    (0, 'No'),
    (1, 'Yes'),
]

FESRP = [
    (0, 'No'),
    (1, 'Yes'),
]

FFERP = [
    (0, 'No'),
    (1, 'Yes'),
]

FGCLP = [
    (0, 'No'),
    (1, 'Yes'),
]

FGCMP = [
    (0, 'No'),
    (1, 'Yes'),
]

FGCRP = [
    (0, 'No'),
    (1, 'Yes'),
]

FHISP = [
    (0, 'No'),
    (1, 'Yes'),
]

FINDP = [
    (0, 'No'),
    (1, 'Yes'),
]

FINTP = [
    (0, 'No'),
    (1, 'Yes'),
]

FJWDP = [
    (0, 'No'),
    (1, 'Yes'),
]

FJWMNP = [
    (0, 'No'),
    (1, 'Yes'),
]

FJWRIP = [
    (0, 'No'),
    (1, 'Yes'),
]

FJWTRP = [
    (0, 'No'),
    (1, 'Yes'),
]

FLANP = [
    (0, 'No'),
    (1, 'Yes'),
]

FLANXP = [
    (0, 'No'),
    (1, 'Yes'),
]

FMARP = [
    (0, 'No'),
    (1, 'Yes'),
]

FMIGP = [
    (0, 'No'),
    (1, 'Yes'),
]

FMIGSP = [
    (0, 'No'),
    (1, 'Yes'),
]

FMILPP = [
    (0, 'No'),
    (1, 'Yes'),
]

FMILSP = [
    (0, 'No'),
    (1, 'Yes'),
]

FMILYP = [
    (0, 'No'),
    (1, 'Yes'),
]

FOCCP = [
    (0, 'No'),
    (1, 'Yes'),
]

FOIP = [
    (0, 'No'),
    (1, 'Yes'),
]

FPAP = [
    (0, 'No'),
    (1, 'Yes'),
]

FPOBP = [
    (0, 'No'),
    (1, 'Yes'),
]

FPOWSP = [
    (0, 'No'),
    (1, 'Yes'),
]

FRACP = [
    (0, 'No'),
    (1, 'Yes'),
]

FRELP = [
    (0, 'No'),
    (1, 'Yes'),
]

FRETP = [
    (0, 'No'),
    (1, 'Yes'),
]

FSCHGP = [
    (0, 'No'),
    (1, 'Yes'),
]

FSCHLP = [
    (0, 'No'),
    (1, 'Yes'),
]

FSCHP = [
    (0, 'No'),
    (1, 'Yes'),
]

FSEMP = [
    (0, 'No'),
    (1, 'Yes'),
]

FSEXP = [
    (0, 'No'),
    (1, 'Yes'),
]

FSSIP = [
    (0, 'No'),
    (1, 'Yes'),
]

FSSP = [
    (0, 'No'),
    (1, 'Yes'),
]

FWAGP = [
    (0, 'No'),
    (1, 'Yes'),
]

FWKHP = [
    (0, 'No'),
    (1, 'Yes'),
]

FWKLP = [
    (0, 'No'),
    (1, 'Yes'),
]

FWKWP = [
    (0, 'No'),
    (1, 'Yes'),
]

FYOEP = [
    (0, 'No'),
    (1, 'Yes'),
]

PWGTP1 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP2 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP3 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP4 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP5 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP6 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP7 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP8 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP9 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP10 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP11 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP12 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP13 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP14 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP15 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP16 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP17 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP18 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP19 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP20 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP21 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP22 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP23 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP24 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP25 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP26 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP27 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP28 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP29 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP30 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP31 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP32 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP33 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP34 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP35 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP36 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP37 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP38 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP39 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP40 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP41 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP42 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP43 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP44 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP45 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP46 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP47 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP48 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP49 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP50 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP51 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP52 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP53 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP54 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP55 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP56 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP57 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP58 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP59 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP60 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP61 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP62 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP63 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP64 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP65 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP66 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP67 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP68 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP69 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP70 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP71 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP72 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP73 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP74 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP75 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP76 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP77 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP78 = [
    (0001..9999, 'Integer weight of person'),
]

PWGTP79 = [
    (0001..9999, 'Integer weight of person'),
]

