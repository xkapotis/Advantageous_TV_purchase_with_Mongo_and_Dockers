import pandas as pd
from datetime import date

def comparison():

    today = str(date.today())
    kotsovolos_df = pd.read_csv('./results/kotsovolos_prices_'+today+'.csv')  

    plaisio_df = pd.read_csv('./results/plaisio_prices_'+today+'.csv')  

    tv_id_kotsovolos = []
    for row in kotsovolos_df["Title"]:
        row = row.split(" ")
        x = row[2]
        if x == "QLED" or x == "OLED":
            id = row[3]
        else:
            id = row[2]
        tv_id_kotsovolos.append(id)

    tv_id_kotsovolos_df = pd.DataFrame(tv_id_kotsovolos, columns = ["Tv Id"])

    tv_id_plaisio = []
    for row in plaisio_df["Title"]:
        row = row.split(" ")
        x = row[3]
        if x == "TV" or x == '24"' or x == '28"':
            id = row[4]
        else:
            id = row[3]
        tv_id_plaisio.append(id)

    tv_id_plaisio_df = pd.DataFrame(tv_id_plaisio, columns = ["Tv Id"])

    kotsovolos_df["Tv Id"] = tv_id_kotsovolos_df
    plaisio_df["Tv Id"] = tv_id_plaisio_df

    kotsovolos_list = kotsovolos_df.values.tolist()
    plaisio_list = plaisio_df.values.tolist()
    final = []
    for kotsovolos_tv in kotsovolos_list:
        row = []
        kotsovolos_id = kotsovolos_tv[4]
        kotsovolos_price = int(float(kotsovolos_tv[2]))
        kotsovolos_title_tv = kotsovolos_tv[0]
        kotsovolos_store = kotsovolos_tv[3]
        for plaisio_tv in plaisio_list:
            plaisio_id = plaisio_tv[4]
            plaisio_price = int(float(plaisio_tv[2]))
            plaisio_title_tv = plaisio_tv[0]
            plaisio_store = plaisio_tv[3]
            if kotsovolos_id == plaisio_id and kotsovolos_price > plaisio_price :
                row.append(plaisio_title_tv)
                row.append(plaisio_id)
                row.append(plaisio_price)
                row.append(plaisio_store)
            elif kotsovolos_id == plaisio_id and kotsovolos_price < plaisio_price:
                row.append(kotsovolos_title_tv)
                row.append(kotsovolos_id)
                row.append(kotsovolos_price)
                row.append(kotsovolos_store)
            elif kotsovolos_id == plaisio_id and kotsovolos_price == plaisio_price:
                row.append(kotsovolos_title_tv)
                row.append(kotsovolos_id)
                row.append(kotsovolos_price)
                row.append("Same Price")
            else:
                continue
            final.append(row)         

    results_df = pd.DataFrame(final)
    # print(results_df)
    cols_selected = [0,1,2,3]
    results_df = results_df[[col for col in results_df.columns if col in cols_selected]]
    # X_train
    # cols = range(4,32)
    # for i in cols:
    #     results_df = results_df.drop(columns=[i], axis=1)
    results_df.columns = ["Title", "Tv Id", "Current Price", "Store"]
    results_df["Date"] = date.today()
    
    # print(results_df.head(40))

    # ### Create csv with results
    today = str(date.today())
    file_name = "results_"+today+".csv"
    path = "./results/"+file_name
    results_df.to_csv(path, index = False)



# comparison()
#### edw to exoume to provlima mismatch columns allon arithmo perimenei kai telika allos arithmos apo kolwnes emfanizetai


        

