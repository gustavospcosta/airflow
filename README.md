
<div align="center" dir="auto">
  <h1> Airflow Data Pipeline </h1>
</div>

This project includes two separate DAGs (dag1.py and dag2.py) designed to pull data from an API, store the data on Google Cloud Storage, and finally, process and append the data to a MySQL database using the Python library Pandas.

Description
- In dag1.py, we connect to an API, retrieve JSON data for several seasons, and store the JSON data in a GCP bucket. This DAG includes a PythonOperator that runs the save_json_clubs_average_season function, which handles all data retrieval and storage.
- In dag2.py, we download the stored JSON data from the GCP bucket, process it into a Pandas DataFrame, and append it to a MySQL database. The processing and storage is handled by the save_sql_clubs_average_season function.
- In both DAGs, we have email alerts set up for successes and failures of the DAG runs.

Getting Started
- Install the required Python packages: requests, json, datetime, google.cloud.storage, sqlalchemy, pandas, and airflow.
- You need to have access to a MySQL server.
- You need a Google Cloud Storage bucket to store JSON files.
- Make sure you have the necessary API access and keys.
- Make sure you replace all placeholder values in the scripts (//CREDENTIALS//PATH//file.json, USER:PASSWORD@localhost:PORT/DATABASE, etc.).

Executing the Program
- Set up the dag1.py and dag2.py files in your Airflow DAGs folder.
- Turn on the DAGs in your Airflow UI.

Author
- Gustavo de Souza Pessanha da Costa

License
- This project is licensed under the MIT license.
