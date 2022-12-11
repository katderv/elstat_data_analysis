import urllib.request
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector
import csv


# DOWNLOADS

# 2011

dls4 = 'https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ' \
       '&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2' \
       '&p_p_col_count=4&p_p_col_pos=3&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource' \
       '=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources' \
       '&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113865' \
       '&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el '

urllib.request.urlretrieve(dls4, "4trimino2011.xls")

excel_file4 = '4trimino2011.xls'

#diavazo ta stoixeia gia erotima 1 xronia 2011

tetartΟtrim11Coll = pd.read_excel(excel_file4, sheet_name='ΔΕΚ', usecols=[6])
tetartotrim11Row = tetartΟtrim11Coll.iloc[133]

#topothetisi se list pou tha mazepsei ta stoixeia gia oles tis xronies
arrivalsPY = []
arrivalsPY.append(tetartotrim11Row)

#diavazo ta stoixeia gia erotima 2 xronia 2011

tetartΟtrim11Coll1 = pd.read_excel(excel_file4, sheet_name='ΔΕΚ', usecols=[1, 6]).dropna()#dropna() gia na afairethoun oses grammes exoyn NaN
tetartΟtrim11Coll1.columns = ["country", "plithos"]
tetartotrim11Row1 = tetartΟtrim11Coll1.iloc[57:110]

#xrisimopoio ti head() gia na paro ta 5 prota stoixeia
tetartotrim11Row1 = tetartotrim11Row1.sort_values("plithos", ascending=False).head()

#diavazo ta stoixeia gia erotima 3 xronia 2011

metaforika11Coll = pd.read_excel(excel_file4, sheet_name='ΔΕΚ', usecols=[2, 3, 4, 5])
metaforika11Row = metaforika11Coll.iloc[133]

#diavazo ta stoixeia gia erotima 4 xronia 2011

trimino1tou11Coll = pd.read_excel(excel_file4, sheet_name='ΜΑΡ', usecols=[6])
trimino1tou11Row = trimino1tou11Coll.iloc[133]

trimina11PY = [] #list poy krataei ta dedomena ana trimino kathe xronias
trimina11PY.append(trimino1tou11Row)

temp2tou11Coll = pd.read_excel(excel_file4, sheet_name='ΙΟΥΝ', usecols=[6])
temp2tou11Row = temp2tou11Coll.iloc[133]
trimino2tou11Row = temp2tou11Row - trimino1tou11Row
trimina11PY.append(trimino2tou11Row)

temp3tou11Coll = pd.read_excel(excel_file4, sheet_name='ΣΕΠ', usecols=[6])
temp3tou11Row = temp3tou11Coll.iloc[133]
trimino3tou11Row = temp3tou11Row - temp2tou11Row
trimina11PY.append(trimino3tou11Row)

temp4tou11Coll = pd.read_excel(excel_file4, sheet_name='ΔΕΚ', usecols=[6])
temp4tou11Row = temp4tou11Coll.iloc[133]
trimino4tou11Row = temp4tou11Row - temp3tou11Row
trimina11PY.append(trimino4tou11Row)

#OI KODIKES EINAI PAROMOIOI GIA KATHE XRONIA TA SXOLIA EINAI IDIA GIA TIS EPOMENES XRONIES

# 2012


dls8 = 'https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ' \
       '&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2' \
       '&p_p_col_count=4&p_p_col_pos=3&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource' \
       '=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources' \
       '&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113886' \
       '&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el '

urllib.request.urlretrieve(dls8, "4trimino2012.xls")
excel_file8 = '4trimino2012.xls'

tetartΟtrim12Coll = pd.read_excel(excel_file8, sheet_name='ΔΕΚ', usecols=[6])
tetartotrim12Row = tetartΟtrim12Coll.iloc[135]

arrivalsPY.append(tetartotrim12Row)

tetartΟtrim12Coll1 = pd.read_excel(excel_file8, sheet_name='ΔΕΚ', usecols=[1, 6]).dropna()
tetartΟtrim12Coll1.columns = ["country", "plithos"]
tetartotrim12Row1 = tetartΟtrim12Coll1.iloc[57:110]


tetartotrim12Row1 = tetartotrim12Row1.sort_values("plithos",ascending=False).head()

metaforika12Coll = pd.read_excel(excel_file8, sheet_name='ΔΕΚ', usecols=[2, 3, 4, 5])
metaforika12Row = metaforika12Coll.iloc[135]

trimino1tou12Coll = pd.read_excel(excel_file8, sheet_name='ΜΑΡ', usecols=[6])
trimino1tou12Row = trimino1tou12Coll.iloc[133]
trimina12PY = []
trimina12PY.append(trimino1tou12Row)

temp2tou12Coll = pd.read_excel(excel_file8, sheet_name='ΙΟΥΝ', usecols=[6])
temp2tou12Row = temp2tou12Coll.iloc[133]
trimino2tou12Row = temp2tou12Row - trimino1tou12Row
trimina12PY.append(trimino2tou12Row)

temp3tou12Coll = pd.read_excel(excel_file8, sheet_name='ΣΕΠΤ', usecols=[6])
temp3tou12Row = temp3tou12Coll.iloc[133]
trimino3tou12Row = temp3tou12Row - temp2tou12Row
trimina12PY.append(trimino3tou12Row)

temp4tou12Coll = pd.read_excel(excel_file8, sheet_name='ΔΕΚ', usecols=[6])
temp4tou12Row = temp4tou12Coll.iloc[135]
trimino4tou12Row = temp4tou12Row - temp3tou12Row
trimina12PY.append(trimino4tou12Row)

# 2013

dls12 = 'https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ' \
        '&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2' \
        '&p_p_col_count=4&p_p_col_pos=3&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource' \
        '=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources' \
        '&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113905' \
        '&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el '

urllib.request.urlretrieve(dls12, "4trimino2013.xls")

excel_file12 = '4trimino2013.xls'

tetartΟtrim13Coll = pd.read_excel(excel_file12, sheet_name='ΔΕΚ', usecols=[6])
tetartotrim13Row = tetartΟtrim13Coll.iloc[135]

arrivalsPY.append(tetartotrim13Row)

tetartΟtrim13Coll1 = pd.read_excel(excel_file12, sheet_name='ΔΕΚ', usecols=[1, 6]).dropna()
tetartΟtrim13Coll1.columns = ["country", "plithos"]
tetartotrim13Row1 = tetartΟtrim13Coll1.iloc[57:110]


tetartotrim13Row1 = tetartotrim13Row1.sort_values("plithos", ascending=False).head()

metaforika13Coll = pd.read_excel(excel_file12, sheet_name='ΔΕΚ', usecols=[2, 3, 4, 5])
metaforika13Row = metaforika13Coll.iloc[135]

trimino1tou13Coll = pd.read_excel(excel_file12, sheet_name='ΜΑΡ', usecols=[6])
trimino1tou13Row = trimino1tou13Coll.iloc[131]
trimina13PY = []
trimina13PY.append(trimino1tou13Row)

temp2tou13Coll = pd.read_excel(excel_file12, sheet_name='ΙΟΥΝ', usecols=[6])
temp2tou13Row = temp2tou13Coll.iloc[131]
trimino2tou13Row = temp2tou13Row - trimino1tou13Row
trimina13PY.append(trimino2tou13Row)

temp3tou13Coll = pd.read_excel(excel_file12, sheet_name='ΣΕΠ', usecols=[6])
temp3tou13Row = temp3tou13Coll.iloc[135]
trimino3tou13Row = temp3tou13Row - temp2tou13Row
trimina13PY.append(trimino3tou13Row)

temp4tou13Coll = pd.read_excel(excel_file12, sheet_name='ΔΕΚ', usecols=[6])
temp4tou13Row = temp4tou13Coll.iloc[135]
trimino4tou13Row = temp4tou13Row - temp3tou13Row
trimina13PY.append(trimino4tou13Row)


# 2014


dls16 = 'https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ' \
        '&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2' \
        '&p_p_col_count=4&p_p_col_pos=3&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource' \
        '=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources' \
        '&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113925' \
        '&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el '

urllib.request.urlretrieve(dls16, "4trimino2014.xls")

excel_file16 = '4trimino2014.xls'

tetartΟtrim14Coll = pd.read_excel(excel_file16, sheet_name='ΔΕΚ', usecols=[6])
tetartotrim14Row = tetartΟtrim14Coll.iloc[135]

arrivalsPY.append(tetartotrim14Row)

tetartΟtrim14Coll1 = pd.read_excel(excel_file16, sheet_name='ΔΕΚ', usecols=[1, 6]).dropna()
tetartΟtrim14Coll1.columns = ["country", "plithos"]
tetartotrim14Row1 = tetartΟtrim14Coll1.iloc[57:110]


tetartotrim14Row1 = tetartotrim14Row1.sort_values("plithos", ascending=False).head()

metaforika14Coll = pd.read_excel(excel_file16, sheet_name='ΔΕΚ', usecols=[2, 3, 4, 5])
metaforika14Row = metaforika14Coll.iloc[135]

trimino1tou14Coll = pd.read_excel(excel_file16, sheet_name='ΜΑΡ', usecols=[6])
trimino1tou14Row = trimino1tou14Coll.iloc[134]
trimina14PY = []
trimina14PY.append(trimino1tou14Row)

temp2tou14Coll = pd.read_excel(excel_file16, sheet_name='ΙΟΥΝ', usecols=[6])
temp2tou14Row = temp2tou14Coll.iloc[135]
trimino2tou14Row = temp2tou14Row - trimino1tou14Row
trimina14PY.append(trimino2tou14Row)

temp3tou14Coll = pd.read_excel(excel_file16, sheet_name='ΣΕΠΤ', usecols=[6])
temp3tou14Row = temp3tou14Coll.iloc[133]
trimino3tou14Row = temp3tou14Row - temp2tou14Row
trimina14PY.append(trimino3tou14Row)

temp4tou14Coll = pd.read_excel(excel_file16, sheet_name='ΔΕΚ', usecols=[6])
temp4tou14Row = temp4tou14Coll.iloc[135]
trimino4tou14Row = temp4tou14Row - temp3tou14Row
trimina14PY.append(trimino4tou14Row)


########################################################################################################################

#ksekinao ta plot

#erotima 1

#metatropi tis listas se type int gia to plot
arrivalsPYlist = [int(i) for i in arrivalsPY]

years = [2011, 2012, 2013, 2014]
plt.figure(figsize=(8, 6))
plt.bar(years, arrivalsPYlist, width=0.5) #plot me bar
plt.xticks([2011, 2012, 2013, 2014])
plt.ticklabel_format(style='plain')


plt.title('Aφίξεις τουριστών στην Ελλάδα για την τετραετία 2011-2014')
plt.xlabel('Έτη')
plt.ylabel('Αφίξεις')

plt.figure(1)

#erotima 2

plt.figure(figsize=(8, 6))
x1 = tetartotrim11Row1["country"]
y1 = tetartotrim11Row1["plithos"]
plt.ticklabel_format(style='plain')


plt.title('Χώρες καταγωγής με το μεγαλύτερο μερίδιο στις αφίξεις τουριστών στην Ελλάδα το 2011')
plt.xlabel('Χώρα')
plt.ylabel('Αφίξεις')

plt.bar(x1, y1, width=0.5)

plt.figure(2)

plt.figure(figsize=(8, 6))
x2 = tetartotrim12Row1["country"]
y2 = tetartotrim12Row1["plithos"]
plt.ticklabel_format(style='plain')


plt.title('Χώρες καταγωγής με το μεγαλύτερο μερίδιο στις αφίξεις τουριστών στην Ελλάδα το 2012')
plt.xlabel('Χώρα')
plt.ylabel('Αφίξεις')

plt.bar(x2, y2, width=0.5)

plt.figure(3)

plt.figure(figsize=(8, 6))
x3 = tetartotrim13Row1["country"]
y3 = tetartotrim13Row1["plithos"]
plt.ticklabel_format(style='plain')


plt.title('Χώρες καταγωγής με το μεγαλύτερο μερίδιο στις αφίξεις τουριστών στην Ελλάδα το 2013')
plt.xlabel('Χώρα')
plt.ylabel('Αφίξεις')

plt.bar(x3, y3, width=0.5)

plt.figure(4)

plt.figure(figsize=(8, 6))
x4 = tetartotrim14Row1["country"]
y4 = tetartotrim14Row1["plithos"]
plt.ticklabel_format(style='plain')


plt.title('Χώρες καταγωγής με το μεγαλύτερο μερίδιο στις αφίξεις τουριστών στην Ελλάδα το 2014')
plt.xlabel('Χώρα')
plt.ylabel('Αφίξεις')

plt.bar(x4, y4, width=0.5)


plt.figure(5)

#erotima 3

plt.figure(figsize=(8, 6))
plt.ticklabel_format(style='plain')

plt.title('Aφίξεις τουριστών στην Ελλάδα ανά μέσο μεταφοράς για το 2011')
plt.xlabel('Μέσο')
plt.ylabel('Αφίξεις')

mesa = ["ΑΕΡΟΠΟΡΙΚΩΣ", "ΣΙΔ/ΚΩΣ", "ΘΑΛΑΣΣΙΩΣ", "ΟΔΙΚΩΣ"]

metaforika11Rowlist = [int(i) for i in metaforika11Row]

plt.bar(mesa, metaforika11Rowlist, width=0.5)

plt.figure(6)

plt.figure(figsize=(8, 6))
plt.ticklabel_format(style='plain')

plt.title('Aφίξεις τουριστών στην Ελλάδα ανά μέσο μεταφοράς για το 2012')
plt.xlabel('Μέσο')
plt.ylabel('Αφίξεις')

metaforika12Rowlist = [int(i) for i in metaforika12Row]

plt.bar(mesa, metaforika12Rowlist, width=0.5)

plt.figure(7)

plt.figure(figsize=(8, 6))
plt.ticklabel_format(style='plain')

plt.title('Aφίξεις τουριστών στην Ελλάδα ανά μέσο μεταφοράς για το 2013')
plt.xlabel('Μέσο')
plt.ylabel('Αφίξεις')

metaforika13Rowlist = [int(i) for i in metaforika13Row]

plt.bar(mesa, metaforika13Rowlist, width=0.5)

plt.figure(8)

plt.figure(figsize=(8, 6))
plt.ticklabel_format(style='plain')

plt.title('Aφίξεις τουριστών στην Ελλάδα ανά μέσο μεταφοράς για το 2014')
plt.xlabel('Μέσο')
plt.ylabel('Αφίξεις')

metaforika14Rowlist = [int(i) for i in metaforika14Row]

plt.bar(mesa, metaforika14Rowlist, width=0.5)

plt.figure(9)

#erotima 4

plt.figure(figsize=(8, 6))
plt.ticklabel_format(style='plain')

plt.title('Αφίξεις τουριστών στην Ελλάδα ανά τρίμηνο για το 2011')
plt.xlabel('Τρίμηνα')
plt.ylabel('Αφίξεις')

trimina11PYlist = [int(i) for i in trimina11PY]

semesters = ["ΙΑΝ-ΜΑΡ", "ΑΠΡ-ΙΟΥΝ", "ΙΟΥΛ-ΣΕΠ", "ΟΚΤ-ΔΕΚ"]

plt.bar(semesters, trimina11PYlist, width=0.5)

plt.figure(10)

plt.figure(figsize=(8, 6))
plt.ticklabel_format(style='plain')

plt.title('Αφίξεις τουριστών στην Ελλάδα ανά τρίμηνο για το 2012')
plt.xlabel('Τρίμηνα')
plt.ylabel('Αφίξεις')

trimina12PYlist = [int(i) for i in trimina12PY]

plt.bar(semesters, trimina12PYlist, width=0.5)

plt.figure(11)

plt.figure(figsize=(8, 6))
plt.ticklabel_format(style='plain')

plt.title('Αφίξεις τουριστών στην Ελλάδα ανά τρίμηνο για το 2013')
plt.xlabel('Τρίμηνα')
plt.ylabel('Αφίξεις')

trimina13PYlist = [int(i) for i in trimina13PY]

plt.bar(semesters, trimina13PYlist, width=0.5)

plt.figure(12)

plt.figure(figsize=(8, 6))
plt.ticklabel_format(style='plain')

plt.title('Αφίξεις τουριστών στην Ελλάδα ανά τρίμηνο για το 2014')
plt.xlabel('Τρίμηνα')
plt.ylabel('Αφίξεις')

trimina14PYlist = [int(i) for i in trimina14PY]

plt.bar(semesters, trimina14PYlist, width=0.5)

plt.figure(13)

########################################################################################################################

#ftiaxno mia sundesi

conn = mysql.connector.connect(user='root', password='1234', host='127.0.0.1',port=3306,
auth_plugin='mysql_native_password')

mycursor = conn.cursor()

#ftiaxno th vasi mou

mycursor.execute("drop database if exists elstat")
mycursor.execute("CREATE DATABASE elstat")
mycursor.execute("use elstat")

#ksekinao ta create tables gia ta opoia ftiaxno ena table ana diagramma

mycursor.execute("create table arrivals_per_year("
                 "arrivals INT,"
                 "year VARCHAR(4) NOT NULL,"
                 "PRIMARY KEY (year))engine=InnoDB;")

mycursor.execute("create table most_arrivals_per_country2011("
                 "country VARCHAR(200) NOT NULL,"
                 "arrivals INT NOT NULL,"
                 "PRIMARY KEY (country,arrivals)"
                 ")engine=InnoDB;")

mycursor.execute("create table most_arrivals_per_country2012("
                 "country VARCHAR(100) NOT NULL,"
                 "arrivals INT NOT NULL,"
                 "PRIMARY KEY (country,arrivals)"
                 ")engine=InnoDB;")

mycursor.execute("create table most_arrivals_per_country2013("
                 "country VARCHAR(100) NOT NULL,"
                 "arrivals INT NOT NULL,"
                 "PRIMARY KEY (country,arrivals)"
                 ")engine=InnoDB;")

mycursor.execute("create table most_arrivals_per_country2014("
                 "country VARCHAR(100) NOT NULL,"
                 "arrivals INT NOT NULL,"
                 "PRIMARY KEY (country,arrivals)"
                 ")engine=InnoDB;")

mycursor.execute("create table arrivals_per_transport2011("
                 "transport VARCHAR(100) NOT NULL,"
                 "arrivals INT NOT NULL,"
                 "PRIMARY KEY (transport,arrivals)"
                 ")engine=InnoDB;")

mycursor.execute("create table arrivals_per_transport2012("
                 "transport VARCHAR(100) NOT NULL,"
                 "arrivals INT NOT NULL,"
                 "PRIMARY KEY (transport,arrivals)"
                 ")engine=InnoDB;")

mycursor.execute("create table arrivals_per_transport2013("
                 "transport VARCHAR(100) NOT NULL,"
                 "arrivals INT NOT NULL,"
                 "PRIMARY KEY (transport,arrivals)"
                 ")engine=InnoDB;")

mycursor.execute("create table arrivals_per_transport2014("
                 "transport VARCHAR(100) NOT NULL,"
                 "arrivals INT NOT NULL,"
                 "PRIMARY KEY (transport,arrivals)"
                 ")engine=InnoDB;")

mycursor.execute("create table arrivals_per_semester2011("
                 "semester VARCHAR(100) NOT NULL,"
                 "arrivals INT NOT NULL,"
                 "PRIMARY KEY (semester,arrivals)"
                 ")engine=InnoDB;")

mycursor.execute("create table arrivals_per_semester2012("
                 "semester VARCHAR(100) NOT NULL,"
                 "arrivals INT NOT NULL,"
                 "PRIMARY KEY (semester,arrivals)"
                 ")engine=InnoDB;")

mycursor.execute("create table arrivals_per_semester2013("
                 "semester VARCHAR(100) NOT NULL,"
                 "arrivals INT NOT NULL,"
                 "PRIMARY KEY (semester,arrivals)"
                 ")engine=InnoDB;")

mycursor.execute("create table arrivals_per_semester2014("
                 "semester VARCHAR(100) NOT NULL,"
                 "arrivals INT NOT NULL,"
                 "PRIMARY KEY (semester,arrivals)"
                 ")engine=InnoDB;")

#ksekinao ta inserts

for i in range(3):
        query = "INSERT INTO arrivals_per_year VALUES (%s,%s)"
        values = [arrivalsPYlist[i], years[i]]
        mycursor.execute(query,values)
        conn.commit()


x1 = x1.to_numpy()
y1 = [int(i) for i in y1]

for i in range(5):
        query = "INSERT INTO most_arrivals_per_country2011 VALUES(%s,%s)"
        values = [x1[i], y1[i]]
        mycursor.execute(query,values)
        conn.commit()

x2 = x2.to_numpy()
y2 = [int(i) for i in y2]

for i in range(5):
        query = "INSERT INTO most_arrivals_per_country2012 VALUES(%s,%s)"
        values = [x2[i], y2[i]]
        mycursor.execute(query,values)
        conn.commit()

x3 = x3.to_numpy()
y3 = [int(i) for i in y3]

for i in range(5):
        query = "INSERT INTO most_arrivals_per_country2013 VALUES(%s,%s)"
        values = [x3[i], y3[i]]
        mycursor.execute(query,values)
        conn.commit()

x4 = x4.to_numpy()
y4 = [int(i) for i in y4]

for i in range(5):
        query = "INSERT INTO most_arrivals_per_country2014 VALUES(%s,%s)"
        values = [x4[i], y4[i]]
        mycursor.execute(query,values)
        conn.commit()


for i in range(4):
    query = "INSERT INTO arrivals_per_transport2011 VALUES(%s,%s)"
    values = [mesa[i], metaforika11Row[i]]
    mycursor.execute(query, values)
    conn.commit()

for i in range(4):
    query = "INSERT INTO arrivals_per_transport2012 VALUES(%s,%s)"
    values = [mesa[i], metaforika12Row[i]]
    mycursor.execute(query, values)
    conn.commit()

for i in range(4):
    query = "INSERT INTO arrivals_per_transport2013 VALUES(%s,%s)"
    values = [mesa[i], metaforika13Row[i]]
    mycursor.execute(query, values)
    conn.commit()

for i in range(4):
    query = "INSERT INTO arrivals_per_transport2014 VALUES(%s,%s)"
    values = [mesa[i], metaforika14Row[i]]
    mycursor.execute(query, values)
    conn.commit()

for i in range(4):
    query = "INSERT INTO arrivals_per_semester2011 VALUES(%s,%s)"
    values = [semesters[i], trimina11PYlist[i]]
    mycursor.execute(query, values)
    conn.commit()

for i in range(4):
    query = "INSERT INTO arrivals_per_semester2012 VALUES(%s,%s)"
    values = [semesters[i], trimina12PYlist[i]]
    mycursor.execute(query, values)
    conn.commit()

for i in range(4):
    query = "INSERT INTO arrivals_per_semester2013 VALUES(%s,%s)"
    values = [semesters[i], trimina13PYlist[i]]
    mycursor.execute(query, values)
    conn.commit()

for i in range(4):
    query = "INSERT INTO arrivals_per_semester2014 VALUES(%s,%s)"
    values = [semesters[i], trimina14PYlist[i]]
    mycursor.execute(query, values)
    conn.commit()

########################################################################################################################

#ftiaxno ena Results.csv kai arxizo na grafo ta dedomena

with open('Results.csv', mode='w',newline='') as results_file:
    results_writer = csv.writer(results_file, delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
    results_writer.writerow(["Aφίξεις τουριστών στην Ελλάδα για την τετραετία 2011-2014"])
    temp = zip(years,arrivalsPYlist)
    for row in temp:
        results_writer.writerow(row)

    results_writer.writerow(["Χώρες καταγωγής με το μεγαλύτερο μερίδιο στις αφίξεις τουριστών στην Ελλάδα το 2011"])
    temp = zip(x1, y1)
    for row in temp:
        results_writer.writerow(row)

    results_writer.writerow(["Χώρες καταγωγής με το μεγαλύτερο μερίδιο στις αφίξεις τουριστών στην Ελλάδα το 2012"])
    temp = zip(x2, y2)
    for row in temp:
        results_writer.writerow(row)

    results_writer.writerow(["Χώρες καταγωγής με το μεγαλύτερο μερίδιο στις αφίξεις τουριστών στην Ελλάδα το 2013"])
    temp = zip(x3, y3)
    for row in temp:
        results_writer.writerow(row)

    results_writer.writerow(["Χώρες καταγωγής με το μεγαλύτερο μερίδιο στις αφίξεις τουριστών στην Ελλάδα το 2014"])
    temp = zip(x4, y4)
    for row in temp:
        results_writer.writerow(row)

    results_writer.writerow(["Aφίξεις τουριστών στην Ελλάδα ανά μέσο μεταφοράς για το 2011"])
    temp = zip(mesa, metaforika11Rowlist)
    for row in temp:
        results_writer.writerow(row)

    results_writer.writerow(["Aφίξεις τουριστών στην Ελλάδα ανά μέσο μεταφοράς για το 2012"])
    temp = zip(mesa, metaforika12Rowlist)
    for row in temp:
        results_writer.writerow(row)

    results_writer.writerow(["Aφίξεις τουριστών στην Ελλάδα ανά μέσο μεταφοράς για το 2013"])
    temp = zip(mesa, metaforika13Rowlist)
    for row in temp:
        results_writer.writerow(row)

    results_writer.writerow(["Aφίξεις τουριστών στην Ελλάδα ανά μέσο μεταφοράς για το 2014"])
    temp = zip(mesa, metaforika14Rowlist)
    for row in temp:
        results_writer.writerow(row)

    results_writer.writerow(["Αφίξεις τουριστών στην Ελλάδα ανά τρίμηνο για το 2011"])
    temp = zip(semesters, trimina11PYlist)
    for row in temp:
        results_writer.writerow(row)

    results_writer.writerow(["Αφίξεις τουριστών στην Ελλάδα ανά τρίμηνο για το 2012"])
    temp = zip(semesters, trimina12PYlist)
    for row in temp:
        results_writer.writerow(row)

    results_writer.writerow(["Αφίξεις τουριστών στην Ελλάδα ανά τρίμηνο για το 2013"])
    temp = zip(semesters, trimina13PYlist)
    for row in temp:
        results_writer.writerow(row)

    results_writer.writerow(["Αφίξεις τουριστών στην Ελλάδα ανά τρίμηνο για το 2014"])
    temp = zip(semesters, trimina14PYlist)
    for row in temp:
        results_writer.writerow(row)

#telos kano plot ta diagrammata pou exo etoimasei pio pano
plt.show()