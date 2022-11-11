
# Importing the required libraries
import xml.etree.ElementTree as Xet
import pandas as pd

cols = ["dir_name", "prod_name", "studio_name", "title", "year", "prc", "cat", "awattr", "awtype", "location"]
rows = []

# Parsing the XML file
xmlparse = Xet.parse('./resource/movies.xml')
root = xmlparse.getroot()

for i in root:

    dir_name = i.find("dirn").text
    prod_name = i.find("prod").text
    studio_name = i.find("studio").text
    title = i.find("t").text
    year = i.find("year").text
    prc = i.find("prc").text
    cat = i.find("cat").text
    award_type = i.find("awtype").text
    award_attr = i.find("awattr").text
    location = i.find("loc").text

    rows.append({"dir_name": dir_name,
                 "prod_name": prod_name,
                 "studio_name": studio_name,
                 "title": title,
                 "year": year,
                 "prc": prc,
                 "cat": cat,
                 "awattr": award_attr,
                 "awtype": award_type,
                 "location": location})


df = pd.DataFrame(rows, columns=cols)

# Writing dataframe to csv
df.to_csv('output.csv')