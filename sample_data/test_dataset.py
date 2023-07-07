import pandas as pd

df = pd.read_csv("wine-ratings-small.csv", index_col=0)
sql_tmpl = """INSERT INTO ratings(name, rating, region) VALUES("%s", "%s", "%s");\n"""
#sql_file = open("populate.sql", "a")

#declaring "type of wine" set
type_wine = set()
id_type_wine = 0
range_score = set()
type_region = set()

with open("populate.sql", "w") as sql_file:
    for _, row in df.iterrows():
        #sql_file.write(sql_tmpl % (row['name'], row['rating'], row['region']))
        #print(row)
        
        #this is a dictionary structure. variety is the index, last record is the value. declaration would be type_wine ={}
        #type_wine[row['variety']] = id_type_wine
        #id_type_wine = id_type_wine +1
        
        #this is a set
        type_wine.add(row['variety'])
        type_region.add(row['region'])
        if row['rating'] < 80:
            range_score.add('<80')
        else:
            range_score.add( str(row['rating']//2 *2) )

print(type_wine)
print(range_score)
print(type_region)