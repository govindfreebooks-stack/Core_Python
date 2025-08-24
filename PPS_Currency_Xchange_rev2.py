Currency_To_INR = {
    "USD_to_INR":83.43,
    "AUD_to_INR":54.92,
    "SGD_to_INR":62.22
    }
INR_To_Currency = {
    "INR_to_USD" :1/Currency_To_INR["USD_to_INR"],
    "INR_to_AUD":1/Currency_To_INR["AUD_to_INR"],
    "INR_to_SGD":1/Currency_To_INR["SGD_to_INR"]
    }

def convert_USD_To_INR(USD):
    return USD*Currency_To_INR["USD_to_INR"]

def convert_INR_to_USD(INR):
    return INR*INR_To_Currency["INR_to_USD"]
