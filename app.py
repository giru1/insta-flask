from flask import Flask
import logging
from logging.config import dictConfig



app = Flask(__name__)

import views

