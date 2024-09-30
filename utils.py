
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
        # data[1] = eval(open)**self.columns['lambda']['Open']
        # data[2] = eval(high)**self.columns['lambda']['High']
        # data[3] = eval(low)**self.columns['lambda']['Low']
        # data[4] = eval(ltp)**self.columns['lambda']['LTP']
        # data[5] = eval(change)**self.columns['lambda']['Chng']
        # data[6] = eval(volume)**self.columns['lambda']['Volume (lacs)']
        # data[7] = eval(high52)**self.columns['lambda']['52w H']
        # data[8] = eval(low52)**self.columns['lambda']['52w L']
        data[1] = eval(open)
        data[2] = eval(high)
        data[3] = eval(low)
        data[4] = eval(ltp)
        data[5] = eval(change)
        data[6] = eval(volume)
        data[7] = eval(high52)
        data[8] = eval(low52)
        print(data)
        predict_closing_price = self.model.predict([data])
        print(predict_closing_price)
        return round(predict_closing_price[0],2)
