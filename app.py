from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Import necessary libraries and functions

def process_csv():
    df = pd.read_csv('data/dataset.csv')
    # Add data processing logic here as needed
    return df

@app.route('/')
def index():
    df = process_csv()
    return render_template('index.html', data=df.to_html(classes='table table-striped'))

if __name__ == '__main__':
    app.run(debug=True)