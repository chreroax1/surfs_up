import datetime as dt
import numpy as np
import pandas as pd

# dependencies we need for SQLAlchemy, which will help us access our data in the SQLite database
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# import the dependencies that we need for Flask.
from flask import Flask, jsonify

# set up our database engine for the Flask application in much the same way we did for climate_analysis.ipynb
# The create_engine() function allows us to access and query our SQLite database file.
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect the database into our classes
Base = automap_base()

# Reflect the DataBase
Base.prepare(engine, reflect=True)

# save our references to each table
Measurement =Base.classes.measurement
Station = Base.classes.station

# create a session link from Python to our database 
session = Session(engine)

# define our Flask app
app = Flask(__name__)

# Define the welcome route
@app.route("/")

# create a function welcome() with a return statement
def welcome():
    return(    
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')