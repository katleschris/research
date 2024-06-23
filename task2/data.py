import pandas as pd

file_path = './schools.csv'  
df = pd.read_csv(file_path)


df2 = df[['School Name', 'Street', 'Suburb', 'State', 'Postcode',
    'Postal Street', 'Postal Suburb', 'Postal State', 'Postal Postcode',
    'Latitude', 'Longitude', 'Phone', 'Education Region',
    'Broad Classification', 'Classification Group', 'Low Year', 'High Year', 'Total Students', 'BE Score',
    'ICSEA', 'ATAR Rank', 'Median ATAR','% students with ATAR']].copy()

print(df2)