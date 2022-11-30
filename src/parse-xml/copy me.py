
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

                    # go into <prods>
                    if film.tag == "prods":
                        
                        for prods in film:

                            for prod in prods:

                                if prod.tag == "pname":

                                    prod_name = prod.text

                    if film.tag == "awards":
                        
                        for awards in film:

                            for award in awards:

                                if award.tag == "awtype":

                                    awtype = award.text

                    if film.tag == "awards":
                        
                        for awards in film:

                            for award in awards:

                                if award.tag == "awattr":

                                    awattr = award.text

                    if film.tag == "loc":
                        
                        for sites in film:

                            for site in sites:

                                if site.tag == "sitename":

                                    location = site.text

                    if film.tag == "studios":

                        for studios in film:

                            if studios.tag == "studio":

                                studio_name = studios.text

                    if film.tag == "cats":

                        for cats in film:

                            if cats.tag == "cat":

                                cat = cats.text

                    if film.tag == "prcs":

                        for prcs in film:

                            if prcs.tag == "prc":

                                prc = prcs.text

                    if film.tag == "t":

                        title = film.text
                    
                    if film.tag == "year":

                        year = film.text

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
df.to_csv('output2.csv')