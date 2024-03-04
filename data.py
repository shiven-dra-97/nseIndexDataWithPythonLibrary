from flask import Flask, jsonify
from flask_cors import CORS  
from nselib import capital_market
import os

app = Flask(__name__)
CORS(app)  

additional_indices = ["NIFTY 50", "NIFTY ENERGY"]

@app.route('/api/market-watch', methods=['GET'])
def get_market_watch_data():
    data = capital_market.market_watch_all_indices()
    filtered_data = data[(data['key'] == 'SECTORAL INDICES') | data['indexSymbol'].isin(additional_indices)]
    market_watch_data = filtered_data.to_dict(orient='records')
    return jsonify(market_watch_data)

if __name__ == '__main__':
    app.run()
