from flask import Flask, jsonify, render_template
import pandas as pd
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)


# 📍 Home Page Route
@app.route('/')
def home():
    return render_template('index.html')


# 📍 System Status Check
@app.route('/api/status', methods=['GET'])
def get_status():
    return jsonify({
        "status": "Running",
        "milestone": "5.3",
        "ai_engine": "Gemini-1.5-Flash"
    })


# 📍 The Data Bridge for Milestone 5.3
@app.route('/api/alerts', methods=['GET'])
def get_alerts():
    try:
        file_path = '../data/processed_vitals.csv'

        if os.path.exists(file_path):
            # We use usecols to ensure we only pull what the dashboard needs
            # This makes the API faster as the CSV grows
            df = pd.read_csv(file_path)

            # Fill any NaN values to prevent JavaScript 'null' errors
            df = df.fillna(0)

            # Send the last 30 records to give the charts a nice history
            data = df.tail(30).to_dict(orient='records')
            return jsonify(data)
        else:
            # Return empty list if AI hasn't generated the file yet
            return jsonify([])

    except Exception as e:
        print(f"Error in /api/alerts: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    # We run on port 5000 as requested
    app.run(debug=True, port=5000)

