import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'schoolRecommender.settings')
from school.models import School

import csv
import pandas as pd

def import_schools(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            School.objects.create(
                school_name=row['School Name'],
                street=row['Street'],
                suburb=row['Suburb'],
                state=row['State'],
                postcode=row['Postcode'],
                postal_street=row['Postal Street'],
                postal_suburb=row['Postal Suburb'],
                postal_state=row['Postal State'],
                postal_postcode=row['Postal Postcode'],
                latitude=row['Latitude'],
                longitude=row['Longitude'],
                phone=row['Phone'],
                education_region=row['Education Region'],
                broad_classification=row['Broad Classification'],
                classification_group=row['Classification Group'],
                low_year=row['Low Year'],
                high_year=row['High Year'],
                total_students=row['Total Students'],
                be_score=row['BE Score'],
                icsea=row['ICSEA'],
                atar_rank=row['ATAR Rank'],
                median_atar=row['Median ATAR'],
                percent_students_with_atar=row['% students with ATAR']
            )

if __name__ == '__main__':
    csv_file_path = 'file1.csv'
    import_schools(csv_file_path)
