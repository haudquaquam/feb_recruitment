from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.express as px

app = Flask(__name__)

# Process CSV into multiple CSVs based on Message. https://stackoverflow.com/questions/46847803/splitting-csv-file-based-on-a-particular-column-using-python
# Creates new CSV files, returns the list of new file names.
def process_csv(): 
    data = pd.read_csv("templates/dataset.csv")

    data_category_range = data['Message'].unique()
    data_category_range = data_category_range.tolist()

    for i,value in enumerate(data_category_range):
        data[data['Message'] == value].to_csv(r'templates/Message_'+str(value)+r'.csv',index = False, na_rep = 'N/A')
    return data_category_range

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chart1')
def chart1():
    data_list = process_csv()
    df = pd.DataFrame({
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    })

    fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Fruit in North America"
    description = """
    A academic study of the number of apples, oranges and bananas in the cities of
    San Francisco and Montreal would probably not come up with this chart.
    """
    return render_template('notdash2.html', graphJSON=graphJSON, header=header,description=description)

