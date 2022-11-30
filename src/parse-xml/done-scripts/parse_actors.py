
# Importing the required libraries
import xml.etree.ElementTree as Xet
import pandas as pd
import requests

# cols = ["stagename", "dowstart", "dowend", "lname", "fname", "gender", "dob", "dod", "roletype", "origin", "award"]
cols = ["stagename", "award"]
rows = []

# define cols
stagename = ""
dowstart = ""
dowend = ""
lname = ""
fname = ""
gender = ""
dob = ""
dod = ""
roletype = ""
origin = ""
award = ""

# Parsing the XML file
url = "http://infolab.stanford.edu/pub/movies/actors63.xml"
r = requests.get(url)
root = Xet.fromstring(r.content)

for actors in root:

    for actor in actors:

        # assign columns to variables
        if actor.tag == "stagename":   
            stagename = actor.text
        
        if actor.tag == "dowstart":
            dowstart = actor.text
        
        if actor.tag == "dowend":
            dowend = actor.text

        if actor.tag == "familyname":
            lname = actor.text

        if actor.tag == "firstname":
            fname = actor.text
        
        if actor.tag == "gender":
            gender = actor.text
        
        if actor.tag == "dob":
            dob = actor.text
        
        if actor.tag == "dod":
            dod = actor.text
        
        if actor.tag == "roletype":
            roletype = actor.text
        
        if actor.tag == "origin":
            origin = actor.text

        if actor.tag == "awards":
 
            for award in actor:
                
                if award.tag == "award":

                    for item in award:
                        
                        if item.tag == "awtype":
                            award = item.text

                rows.append([stagename, award])

    # append to rows the rest who don't have awards
    # append to rows
    # rows.append([stagename, dowstart, dowend, lname, fname, gender, dob, dod, roletype, origin])

df = pd.DataFrame(rows, columns=cols)

# Writing dataframe to csv
# df.to_csv('actors.csv')
df.to_csv('LEFTOUTAWARDS_ACTORS.csv')