
# Importing the required libraries
import xml.etree.ElementTree as Xet
import pandas as pd
import requests

cols = ["movie_id", "year", "title"]
rows = []

# define cols
movie_id = ""
title = ""
year = ""

# Parsing the XML file
url = "http://infolab.stanford.edu/pub/movies/mains243.xml"
r = requests.get(url)
root = Xet.fromstring(r.content)

for directorfilms in root:

    for directorfilm in directorfilms:

        if directorfilm.tag == "films":

            for films in directorfilm:
                
                for film in films:

                    if film.tag == "t":

                        title = film.text
                    
                    if film.tag == "year":

                        year = film.text
                    
                    if film.tag == "fid":
                            
                        movie_id = film.text

                rows.append({"movie_id": movie_id, "year": year, "title": title})


df = pd.DataFrame(rows, columns=cols)

# Writing dataframe to csv
df.to_csv('movieskeyid.csv')
