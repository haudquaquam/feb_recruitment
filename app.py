from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    data = [
        (0, "BMS", "BMS_TEMPERATURE", 600),
        (0.01, "BMS", "BMS_TEMPERATURE", 599.98),
        (0.02, "BMS", "BMS_TEMPERATURE", 599.96),
        (0.03, "BMS", "BMS_TEMPERATURE", 599.93),
        (0.04, "BMS", "BMS_TEMPERATURE", 599.98),
        (0.05, "BMS", "BMS_TEMPERATURE", 599.87),
        (0.06, "BMS", "BMS_TEMPERATURE", 599.85),
        (0.07, "BMS", "BMS_TEMPERATURE", 599.83),
        (0.08, "BMS", "BMS_TEMPERATURE", 599.82),
        (0.09, "BMS", "BMS_TEMPERATURE", 599.8),
        (0.10, "BMS", "BMS_TEMPERATURE", 599.78),
    ]

    labels = [row[0] for row in data]
    values = [row[3] for row in data]
    
    return render_template("graph.html", labels=labels, values=values)
