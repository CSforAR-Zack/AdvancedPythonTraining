# NORTH LITTLE ROCK, AR US
# ID - GHCND:USW00003952

import requests
import json

from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Day

# Get the data from the NOAA API
token = "TOKEN GOES HERE"
datatype_ids = 'TMAX,TMIN'
units = 'standard'
dataset_id = 'GHCND'
station_id = 'GHCND:USW00003952'
start_date = '2022-01-01'
end_date = '2022-12-31'

request_url = f"https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid={dataset_id}&datatypeid={datatype_ids}&stationid={station_id}&startdate={start_date}&enddate={end_date}&limit=1000&units={units}"

r = requests.get(request_url, headers={'token': token})

data = json.loads(r.text)['results']

engine = create_engine("sqlite:///data.db")

Session = sessionmaker(bind=engine)
session = Session()

for d in data:
    date = datetime.strptime(d['date'], '%Y-%m-%dT%H:%M:%S')

    day = session.query(Day).filter(Day.date == date).first()

    if day is None:
        day = Day()
        day.date = date

    if d['datatype'] == 'TMIN':
        day.tmin = int(d['value'])
    elif d['datatype'] == 'TMAX':
        day.tmax = int(d['value'])

    session.add(day)
    session.commit()
