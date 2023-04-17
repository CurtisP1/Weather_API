#  Copyright (c) 2023 - All rights reserved.
#  Created by Curtis Poon for PROCTECH 4IT3/SEP 6IT3.
#  SoA Notice: I Curtis Poon, 400263978 certify that this material is my original work.
#  I certify that no other person's work has been used without due acknowledgement.
#  I have also not made my work available to anyone else without their due acknowledgement.

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import mysql.connector

from Final.settings import BASE_DIR
from api import views
import os


@login_required(login_url='/accounts/login/')
def index(request):
    if request.user.is_authenticated:
        print("Welcome")
    else:
        print("Denied")

    return redirect('weather/')


def getInfo(request):
    cnx = mysql.connector.connect(read_default_file=str(os.path.join(BASE_DIR, 'configs', 'my.cnf')))
    cur = cnx.cursor()

    if 'data_inserted' in request.session:
        data = views.get_userinfo()
        ip = data['ip']
        type = data['type']
        contCode = data['continent_code']
        contName = data['continent_name']
        countCode = data['country_code']
        countName = data['country_name']
        regCode = data['region_code']
        regName = data['region_name']
        city = data['city']
        zip = data['zip']
        cur.execute('insert into api_userinfo (ip, ipType, contCode, contName, countryCode, countryName, regCode, regName, city, zip) values'
                    ' (%s,%s,%s,%s ,%s,%s,%s,%s,%s,%s)', (ip, type, contCode, contName, countCode, countName, regCode, regName, city, zip))

    data = views.get_weatherinfo(request)
    location = data["location"]['name']
    region = data["location"]['region']
    country = data["location"]['country']
    timezone = data["location"]['tz_id']
    localtime = data["location"]['localtime']
    lat = data["location"]['lat']
    long = data["location"]['lon']

    cur.execute('insert into api_weatherdata (location, region, country, timezone, localt, lat, lon) values'
                ' (%s,%s,%s,%s ,%s,%s,%s)', (location, region, country, timezone, localtime, lat, long))

    co = data["current"]["air_quality"]['co']
    no2 = data["current"]["air_quality"]['no2']
    o3 = data["current"]["air_quality"]['o3']
    so2 = data["current"]["air_quality"]['so2']
    fine = data["current"]["air_quality"]['pm2_5']
    ultra = data["current"]["air_quality"]['pm10']
    usa = data["current"]["air_quality"]['us-epa-index']
    eu = data["current"]["air_quality"]['gb-defra-index']

    cur.execute('insert into api_airquality (carbon, nox, o3, so2, fine, ultra, usa, eu) values'
                ' (%s,%s,%s,%s ,%s,%s,%s,%s)', (co, no2, o3, so2, fine, ultra, usa, eu))

    tempc = data["current"]["temp_c"]
    tempf = data["current"]["temp_f"]
    hum = data["current"]["humidity"]
    flc = data["current"]["feelslike_c"]
    flf = data["current"]["feelslike_f"]
    wskm = data["current"]["wind_kph"]
    wsm = data["current"]["wind_mph"]
    wd = data["current"]["wind_dir"]
    wdd = data["current"]["wind_degree"]
    epmm = data["current"]["precip_mm"]
    epin = data["current"]["precip_in"]

    cur.execute('insert into api_temp (tempc, tempf, hum, flc, flf, wskm, wsm, wd, wdd, epmm, epin) values'
                ' (%s,%s,%s,%s ,%s,%s,%s,%s,%s,%s,%s)', (tempc, tempf, hum, flc, flf, wskm, wsm, wd, wdd, epmm, epin))

    last = data["current"]["last_updated"]
    if data["current"]["is_day"] == 1:
        tod = "Day Time"
    else:
        tod = "Night Time"
    cloud = data["current"]["cloud"]
    cond = data["current"]["condition"]['icon']
    uv = data["current"]["uv"]
    vkm = data["current"]["vis_km"]
    vm = data["current"]["vis_miles"]
    pmb = data["current"]["pressure_mb"]
    piw = data["current"]["pressure_in"]

    cur.execute('insert into api_general (lst, tod, cloud, cond, uv, vkm, vm, pmb, piw) values'
                ' (%s,%s,%s,%s ,%s,%s,%s,%s,%s)', (last, tod, cloud, cond, uv, vkm, vm, pmb, piw))

    cnx.commit()
    cnx.close()
