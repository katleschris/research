from django.shortcuts import render
import pandas as pd
from data import SchoolData

school_data = SchoolData()
all_schools = school_data.get_schools_from_csv()
html_table = all_schools.to_html()

def pandas_example_view(request):
    # Convert DataFrame to HTML for rendering in template
    html_table = all_schools.to_html()

    return render(request, 'myapp/pandas_example.html', {'html_table': html_table})



