import requests
import datetime as dt
from matplotlib import pyplot as plt
import mplcursors
from dateutil.relativedelta import relativedelta
from tkinter import messagebox


def cc():
    fo = open("CC.txt").read().split("\n")
    fo.sort()
    return fo


def conv(ccf, ccl, amt):
    if ccf == ccl:
        return amt
    status = requests.get("https://api.exchangeratesapi.io/latest?base={}".format(ccf))
    rate = status.json()['rates'][ccl]
    convamt = amt * rate
    return "{0:.2f}".format(convamt)

def currencytrends(A, B, period, start, end):
    if period != "o":
        enddate = dt.datetime.now()-relativedelta(days=1)
        end = enddate.date()
    else:
        end = end
    if period == "w":
        start = (enddate - relativedelta(weeks=1)).date()
    elif period == "m":
        start = (enddate - relativedelta(months=1)).date()
    elif period == "y":
        start = (enddate - relativedelta(years=1)).date()
    else:
        start = start
    c = requests.get("https://api.exchangeratesapi.io/history?base={}&start_at={}&end_at={}&symbols={}".format(B,
                                                                                                               start,
                                                                                                               end,
                                                                                                               A)).json()
    d = []
    ccp = []
    for x in c["rates"]:
        d.append(x)
    ds = sorted(d, key=lambda x: dt.datetime.strptime(x, '%Y-%m-%d'))

    for x in ds:
        ccp.append(c["rates"][x][A])

    for x in ds:
        ds[ds.index(x)] = dt.datetime.strptime(x, '%Y-%m-%d')

    return ds, ccp



