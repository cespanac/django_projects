from django.http import HttpResponse
from django.shortcuts import render
# from django.template import loader, Template, Context

import datetime


class Names:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


def welcome(request):  # first view

    tasks = ['View course', 'Develop test web', 'Develop portfolio']

    n1 = Names('Cristian', 'España Ces')
    date_now = datetime.datetime.now()

    #home_temp = loader.get_template('home_template.html')

    # If we not use loader, we have to code from line 21 to 26.

    """
    home_template = open('PATH')

    plt = Template(home_template.read())

    home_template.close()
    """

    # If we use the loader, we should dispense with ctx.
    # We should pass dict directly to the render.

    """
    ctx = Context({'first_name': n1.first_name,
                   'last_name': n1.last_name,
                   'date': date_now,
                   'tasks': tasks})
    

    text = home_temp.render({'first_name': n1.first_name,
                             'last_name': n1.last_name,
                             'date': date_now,
                             'tasks': tasks})
    """

    ctx = ({'first_name': n1.first_name,
            'last_name': n1.last_name,
            'date': date_now,
            'tasks': tasks})

    return render(request, template_name='home_template.html', context=ctx)


def current_date(request):

    date_now = datetime.datetime.now()

    return HttpResponse('Fecha y hora actuales %s' % date_now)


def age_estimator(request, current_age, future_year):

    difference_year = future_year - 2021
    age_pred = current_age + difference_year

    text = ("<html><body><h2>In the year %s, you'll have %s years." % (future_year, age_pred))

    return HttpResponse(text)
