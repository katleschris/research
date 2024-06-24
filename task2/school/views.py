from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from models import SchoolData

school_data = SchoolData()
all_schools = school_data.get_schools_from_csv()
html_table = all_schools.to_html()


def index(request):

    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'school/table1.html', {'html_table': html_table})



