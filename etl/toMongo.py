import pymongo
from pymongo import MongoClient
import dns
import pandas as pd
from datetime import date

def toMongo():

    cluster = MongoClient("mongodb+srv://xkapotis:xkapotis222222@cluster0-hpms9.mongodb.net/Comparison_Results?retryWrites=true&w=majority")
    db = cluster["Comparison_Results"]
    collection = db["Data"]


    today = str(date.today())
    file_name = "results_"+today+".csv"
    data = pd.read_csv("./results/"+file_name)  
    # print(data.head())

    collection.insert_many(data.to_dict('records'))

