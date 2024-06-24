import pandas as pd
import _csv
class SchoolData():
    def __init__(self):
        self.file_path = 'schools.csv'
        self.df = pd.read_csv(self.file_path)

    def get_schools_from_csv(self):

        df2 = self.df[['School Name', 'Street', 'Suburb', 'State', 'Postcode',
            'Postal Street', 'Postal Suburb', 'Postal State', 'Postal Postcode',
            'Latitude', 'Longitude', 'Phone', 'Education Region',
            'Broad Classification', 'Classification Group', 'Low Year', 'High Year', 'Total Students', 'BE Score',
            'ICSEA', 'ATAR Rank', 'Median ATAR','% students with ATAR']].copy()
        
        return df2
    
# school_data = SchoolData()
# all_schools = school_data.get_schools_from_csv()