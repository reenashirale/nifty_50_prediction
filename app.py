from flask import Flask, jsonify, request, render_template
import warnings
warnings.filterwarnings('ignore')
from config import FLASK_PORT_NUMBER
from utils import StockPriceClass

app = Flask(__name__)

stock_object = StockPriceClass()

@app.route('/')
def home():
    return render_template("index.html", data="", closing_price="")

@app.route('/', methods=['POST'])
def prediction():
    try:
        data = request.form
        symbol = data.get('symbol')
        open = data.get('open')
        high = data.get('high')
        low = data.get('low')
        ltp = data.get('ltp')
        change = data.get('change')
        volume = data.get('volume')
        high52 = data.get('high52')
        low52 = data.get('low52')
        closing_price = stock_object.stock_prediction(symbol, open, high, low, ltp, change, volume, high52, low52)
        return render_template("index.html", data=data, closing_price=closing_price)
    except Exception as e:
        return render_template("index.html", data="", closing_price=e)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=FLASK_PORT_NUMBER, debug=True)