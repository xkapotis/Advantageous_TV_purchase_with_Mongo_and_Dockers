## How to run

Run:
* $ git clone https://github.com/xkapotis/Advantageous_TV_purchase_with_Mongo_and_Dockers.git
* $ cd Advantageous_TV_purchase_with_Mongo_and_Dockers/
* $ sudo USR=<mongo_username> PSWD=<mongo password> docker-compose up

Compose will launch 2 services , etl and ui. 
Etl will scrap TV prices, preprocess them ,store them on a mongo databade on the cloud and then exit.
Ui will ping poll etl until it exits and then launch a Streamlit dashboard to read and visualize the data etl stored on the mongo database.
Once the dashboard is launched you can access it through your browser on http://localhost:8551/

Both Etl and Ui use the same image , but each is run with a different command.
If the image is already built docker-compose will use it to launch the containers . Otherwise it will first build the image and then launch them. 
