#  Copyright (c) 2023 - All rights reserved.
#  Created by Curtis Poon for PROCTECH 4IT3/SEP 6IT3.
#  SoA Notice: I Curtis Poon, 400263978 certify that this material is my original work.
#  I certify that no other person's work has been used without due acknowledgement.
#  I have also not made my work available to anyone else without their due acknowledgement.

from django.shortcuts import render
from django.db import connection
from Final import views
import requests


def index(request):
    events()


def events(request):
    views.getInfo(request)
    weatherData = getWeather()
    airData = getAir()
    tempData = getTemp()
    genData = getGen()
    userData = getUser()
    context = {
        'weatherData': weatherData,
        'airData': airData,
        'tempData': tempData,
        'genData': genData,
        'userData': userData
    }
    if request.resolver_match.url_name == 'weather':
        url = 'api/Weather.html'
    elif request.resolver_match.url_name == 'remote':
        url = 'api/remote.html'

    return render(request, url, context)


def get_userinfo(request):
    if not request.session.get('userinfo_fetched', False):
        url = 'http://api.ipstack.com/check?access_key=d042e6bb160e97992d8743d4d6900be6'
        response = requests.get(url)
        request.session['userinfo'] = response.json()
        request.session['userinfo_fetched'] = True
    return request.session['userinfo']


def get_weatherinfo(request):
    baseurl = 'http://api.weatherapi.com/v1/current.json?key=8e6a6c6a2f3b4395b8a60525231404&q='

    if request.method == 'GET':
        current = request.GET.get('location')
    else:
        current = get_userinfo(request)["city"]

    if current == '' or current == None:
        current = get_userinfo(request)["city"]

    aqi = '&aqi=yes'

    url = baseurl + current + aqi
    print(url)
    response = requests.get(url)
    data = response.json()
    return data


def getWeather():
    cur = connection.cursor()
    command = "SELECT location, region, country, timezone, localt, lat, lon FROM api_weatherdata WHERE id = (SELECT  MAX(id) FROM api_weatherdata) "
    cur.execute(command)
    return dictfetchall(cur)


def getUser():
    cur = connection.cursor()
    command = "SELECT ip, ipType, contCode, contName, countryCode, countryName, regCode, regName, city, zip FROM api_userinfo WHERE id = (SELECT  MAX(id) FROM api_userinfo) "
    cur.execute(command)
    return dictfetchall(cur)


def getAir():
    cur = connection.cursor()
    command = "SELECT carbon, nox, o3, so2, fine, ultra, usa, eu FROM api_airquality WHERE id = (SELECT  MAX(id) FROM api_airquality) "
    cur.execute(command)
    return dictfetchall(cur)


def getTemp():
    cur = connection.cursor()
    command = "SELECT tempc, tempf, hum, flc, flf, wskm, wsm, wd, wdd, epmm, epin FROM api_temp WHERE id = (SELECT  MAX(id) FROM api_temp) "
    cur.execute(command)
    return dictfetchall(cur)


def getGen():
    cur = connection.cursor()
    command = "SELECT lst, tod, cloud, cond, uv, vkm, vm, pmb, piw FROM api_general WHERE id = (SELECT  MAX(id) FROM api_general) "
    cur.execute(command)
    return dictfetchall(cur)


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]
