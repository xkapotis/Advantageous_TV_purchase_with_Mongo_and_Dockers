import pymongo
from pymongo import MongoClient
import dns
import pandas as pd
from datetime import date
import sys

import numpy as np
import streamlit as st
import altair as alt


if __name__=="__main__":
    cluster = MongoClient(f"mongodb+srv://{sys.argv[1]}:{sys.argv[2]}@cluster0-hpms9.mongodb.net/Comparison_Results?retryWrites=true&w=majority")
    db = cluster["Comparison_Results"]
    collection = db["Data"]

    today = str(date.today())

    data = collection.find()
    data = pd.DataFrame(list(data))
    data = data.loc[data["Date"] == today]
    data = data.drop_duplicates(subset = "Tv Id")
    # print(data)

    same_price = data["Store"].loc[data["Store"] == "Same Price"].count()
    kotsovolos = data["Store"].loc[data["Store"] == "KOTSOVOLOS"].count()
    plaisio = data["Store"].loc[data["Store"] == "PLAISIO" ].count()
    df_for_vizualization = data["Store"]


    # print(same_price.count())
    # print(kotsovolos.count())
    # print(plaisio.count())

    st.title("Advantageous TV Purchase")
    st.markdown("## Here you can see the store with the best TV prices currently in the market")


    objects = ('same price', 'kotsovolos', 'plaisio')
    # y_pos = np.arange(len(objects))
    # performance = [same_price,kotsovolos,plaisio]
    performance = [same_price,kotsovolos,plaisio]




    data = pd.DataFrame({
        'Stores': ['same price', 'kotsovolos', 'plaisio'],
        'Stores With Better Prices': [same_price,kotsovolos,plaisio],
    })

    st.write(data)
    st.write(alt.Chart(data).mark_bar().encode(
        x=alt.X('Stores', sort=None, scale=alt.Scale(zero=False)),
        y='Stores With Better Prices',
    ).properties(width=600, height=370))


