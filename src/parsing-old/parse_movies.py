
# Importing the required libraries
import xml.etree.ElementTree as Xet
import pandas as pd
import requests

cols = ["dir_name", "prod_name", "studio_name", "title", "year", "prc", "cat", "awattr", "awtype", "location"]
rows = []

# define cols
dir_name = ""
prod_name = ""
studio_name = ""
title = ""
year = ""
prc = ""
cat = ""
awattr = ""
awtype = ""
location = ""


# Parsing the XML file
url = "http://infolab.stanford.edu/pub/movies/mains243.xml"
r = requests.get(url)
root = Xet.fromstring(r.content)

for directorfilms in root:

    for directorfilm in directorfilms:

        if directorfilm.tag == "director":

            for director in directorfilm:

                if director.tag == "dirname":

                    dir_name = director.text

        if directorfilm.tag == "films":

            for films in directorfilm:
                
                for film in films:

                    if film.tag == "t":

                        title = film.text
                    
                    if film.tag == "year":

                        year = film.text
                    
                    if film.tag == "cat":

                        cat = film.text
                    
                    if film.tag == "prc":
                    
                        prc = film.text
                    
                    if film.tag == "awards":

                        for awards in film:

                            for award in awards:

                                if award.tag == "awattr":

                                    awattr = award.text

                                if award.tag == "awtype":

                                    awtype = award.text

                    if film.tag == "loc":
                            
                        location = film.text

    rows.append({"dir_name": dir_name,
                 "prod_name": prod_name,
                 "studio_name": studio_name,
                 "title": title,
                 "year": year,
                 "prc": prc,
                 "cat": cat,
                 "awattr": awattr,
                 "awtype": awtype,
                 "location": location})


df = pd.DataFrame(rows, columns=cols)

# Writing dataframe to csv
df.to_csv('output.csv')