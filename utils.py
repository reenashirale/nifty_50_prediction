
import pickle
import numpy as np
import json
from config import MODEL_FILE_NAME, JSON_COLUMNS_FILE_NAME

class StockPriceClass():

    def __init__(self):
        pass


    def load_data(self):
        with open(MODEL_FILE_NAME, 'rb') as f:
            self.model = pickle.load(f)

        with open(JSON_COLUMNS_FILE_NAME, 'r') as f:
            self.columns = json.load(f)

    def stock_prediction(self, symbol, open, high, low, ltp, change, volume, high52, low52):
        self.load_data()
        col_length = len(self.columns['columns'])
        data = np.zeros(col_length)
        symbol = self.columns['symbols'][symbol]
        data[0] = symbol
        data[1] = open
        data[2] = high
        data[3] = low
        data[4] = ltp
        data[5] = change
        data[6] = volume
        data[7] = high52
        data[8] = low52
        predict_closing_price = self.model.predict([data])
        print(predict_closing_price)
        return round(predict_closing_price[0],2)
