import datetime as dt
import numpy as np
import pandas as pd

# import the Flask dependency
from flask import Flask

# Create a new Flask App Instance
app = Flask(__name__)

# Create our first route! First, we need to define the starting point, also known as the root. To do this,
#  we'll use the function @app.route('/')
@app.route('/')

# Create a function called hello_world(). Whenever you make a route in Flask, you put the code you want in that
#  specific route below @app.route().
def hello_world():
    return "Hello World"