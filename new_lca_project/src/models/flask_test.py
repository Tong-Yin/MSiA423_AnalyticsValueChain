from flask import Flask, render_template

import pandas as pd
import matplotlib.pyplot as plt
import string
import numpy as np
import datetime as dt

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def parser():
 return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=True)
