import urllib, json
import matplotlib.pyplot as plt
import numpy as np

api_url = "API URL"
token_auth = "TOKEN AUTH"
period = "day"
date = "today"

# Eingbabe wie viele User abgefragt werden sollen
usercount = raw_input('Wie viele User sollen ueberprueft werden? ')
print("Ok. Hole " + str(usercount) + " User aus Matomo.")

# Erhalte eine Liste an Matomo-Ids
url = api_url + "UserId.getUsers&idSite=1&period=" + period + "&date=" + date +"&format=json&filter_limit=" + str(usercount) + "&token_auth=" + token_auth
response = urllib.urlopen(url)
id_data = json.loads(response.read())

alterall = []
visits = 0
group1 = 0
group2 = 0
group3 = 0
group4 = 0
group5 = 0
group6 = 0
group7 = 0
group8 = 0
group9 = 0
group10 = 0
group11 = 0

print("Frage nun die Details der IDs ab. Dies kann einen Moment dauern.")
for id in id_data:
    url = api_url + "Live.getLastVisitsDetails&idSite=1&period=" + period +"&date=" + date + "&format=json&segment=userId==" + id['label'] + "&filter_limit=1&token_auth=" + token_auth
    response = urllib.urlopen(url)
    visit_data = json.loads(response.read())

    for user in visit_data:
        # print(user['userId'] + ": " + user['daysSinceFirstVisit']+ " Tage")
        alterall.append(int(user['daysSinceFirstVisit']))
        alter = int(user['daysSinceFirstVisit'])
        visits = visits + int(user['visitCount'])

        # Einteilung der User in Gruppen nach Alter
        if alter < 1:
            group1 = group1 +1
        elif alter == 1:
            group2 = group2 +1
        elif alter == 2:
            group3 = group3 +1
        elif alter > 2 and alter < 4:
            group4 = group4 +1
        elif alter >= 4 and alter < 8:
            group5 = group5 +1
        elif alter >= 8 and alter < 16:
            group6 = group6 +1
        elif alter >=16 and alter < 32:
            group7 = group7 +1
        elif alter >=32 and alter < 64:
            group8 = group8 +1
        elif alter >=64 and alter < 128:
            group9 = group9 +1
        elif alter >=128 and alter < 256:
            group10 = group10 +1
        elif alter >=256:
            group11 = group11 +1


# Ausgabe der Gruppen
alter_durchschnitt = reduce(lambda x, y: x + y, alterall) / len(alterall)
print("Die User ("+ usercount +") sind im Durchschnitt " + str(alter_durchschnitt) + " Tage alt und haben insgesamt " + str(visits) + " Besuche. Das sind " + str(visits / int(usercount)) + " Besuche pro User.\n")
print("0 Tage alt: " + str(group1) + " / " + str((float(group1) / int(usercount) * 100 )) + "%\n")
print("1 Tag alt: " + str(group2) + " / " + str((float(group2) / int(usercount) * 100 )) + "%\n")
print("2 Tage alt: " + str(group3) + " / " + str((float(group3) / int(usercount) * 100 )) + "%\n")
print("3 bis 4 Tage alt: " + str(group4) + " / " + str((float(group4) / int(usercount) * 100 )) + "%\n")
print("4 bis 8 Tage alt: " + str(group5) + " / " + str((float(group5) / int(usercount) * 100 )) + "%\n")
print("8 bis 16 Tage alt: " + str(group6) + " / " + str((float(group6) / int(usercount) * 100 )) + "%\n")
print("16 bis 32 Tage alt: " + str(group7) + " / " + str((float(group7) / int(usercount) * 100 )) + "%\n")
print("32 bis 64 Tage alt: " + str(group8) + " / " + str((float(group8) / int(usercount) * 100 )) + "%\n")
print("64 bis 128 Tage alt: " + str(group9) + " / " + str((float(group9) / int(usercount) * 100 )) + "%\n")
print("128 bis 256 Tage alt: " + str(group10) + " / " + str((float(group10) / int(usercount) * 100 )) + "%\n")
print("ueber 265 Tage alt: " + str(group11) + " / " + str((float(group11) / int(usercount) * 100 )) + "%\n \n")

with open("log.txt", "a") as f:
        f.write("Die User ("+ usercount +") sind im Durchschnitt " + str(alter_durchschnitt) + " Tage alt und haben insgesamt " + str(visits) + " Besuche. Das sind " + str(visits / int(usercount)) + " Besuche pro User.\n")
        f.write("0 Tage alt: " + str(group1) + " / " + str((float(group1) / int(usercount) * 100 )) + "%\n")
        f.write("1 Tag alt: " + str(group2) + " / " + str((float(group2) / int(usercount) * 100 )) + "%\n")
        f.write("2 Tage alt: " + str(group3) + " / " + str((float(group3) / int(usercount) * 100 )) + "%\n")
        f.write("3 bis 4 Tage alt: " + str(group4) + " / " + str((float(group4) / int(usercount) * 100 )) + "%\n")
        f.write("4 bis 8 Tage alt: " + str(group5) + " / " + str((float(group5) / int(usercount) * 100 )) + "%\n")
        f.write("8 bis 16 Tage alt: " + str(group6) + " / " + str((float(group6) / int(usercount) * 100 )) + "%\n")
        f.write("16 bis 32 Tage alt: " + str(group7) + " / " + str((float(group7) / int(usercount) * 100 )) + "%\n")
        f.write("32 bis 64 Tage alt: " + str(group8) + " / " + str((float(group8) / int(usercount) * 100 )) + "%\n")
        f.write("64 bis 128 Tage alt: " + str(group9) + " / " + str((float(group9) / int(usercount) * 100 )) + "%\n")
        f.write("128 bis 256 Tage alt: " + str(group10) + " / " + str((float(group10) / int(usercount) * 100 )) + "%\n")
        f.write("ueber 265 Tage alt: " + str(group11) + " / " + str((float(group11) / int(usercount) * 100 )) + "%\n \n")



# Ausgabe des Diagramms
alterall.sort()

plt.plot(alterall)
plt.xticks(np.arange(0, len(alterall), step=5))
plt.ylabel('Alter')
plt.xlabel('User Nummer')
plt.show()
