# IMPORT PYTHON MODULES
from sqlalchemy import create_engine
import pandas as pd
import json
from datetime import datetime
from google.cloud import storage
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator
from airflow.utils.email import send_email

# SET THE DATETIME
tempo = datetime.now()
datetime_att = tempo.strftime("%Y/%m/%d %H:%M:%S")

# KEY FOR GCP STORAGE
key_file = "//CREDENTIALS//PATH//file.json"

# AUTHENTICATE ON GCP STORAGE
gcp_storage = storage.Client.from_service_account_json(key_file)

# SET BUCKET NAME
bucket_name = 'project'

# SET THE GCP BUCKET
gcp_bucket = gcp_storage.get_bucket(bucket_name)

# DATABASE CONNECTION SETUP
engine = create_engine('mysql://USER:PASSWORD@localhost:PORT/DATABASE')

# SEASON ID LIST
seasons_list = ["40557","27591","22931","16183"]

# FUNCTION SUCCESS MAIL
def success_email(context):
    dag_run = context.get('dag_run')
    msg = f"DAG {dag_run} RAN successfully"
    subject = f"DAG RAN successfully"
    send_email(to='example@example.com', subject=subject, html_content=msg)

# FUNCTION FAIL MAIL
def fail_email(context):
    dag_run = context.get('dag_run')
    msg = f"DAG {dag_run} NOT RAN successfully"
    subject = f"DAG NOT RAN successfully"
    send_email(to='example@example.com', subject=subject, html_content=msg)

# FUNCTION
def save_sql_clubs_average_season():

    df_final = pd.DataFrame()

    for season in seasons_list:
        file = f"filename_{season}"
        blob = gcp_bucket.blob(file)
        data = json.loads(blob.download_as_string(client=None))
        data_aux = data["topTeams"]["avgRating"]
        df = pd.json_normalize(data_aux)
        df["season_id"] = season
        df_final = df_final.append(df)
        df_final["last_update"] = datetime_att
        df_final = df_final.fillna(0)
        df_final.reset_index()

    df_final = df_final[["team.name","team.id","statistics.avgRating","statistics.matches","season_id","last_update"]]

    # RENAME DATAFRAME COLUMNS
    df_final.rename(columns={
        "team.name": "team_name",
        "team.id": "team_id",
        "statistics.avgRating": "average_rating",
        "statistics.matches":"matches"
        }, inplace=True)

    df_final.to_sql("c_average_season", engine, index=False, index_label=None, method=None, if_exists="append")

# DAG ARGUMENTS
default_args = {'owner': 'Gustavo', 'on_failure_callback': fail_email, 'on_success_callback': success_email, 'retries': 0}

# DAG PARAMETERS
dag_sql_clubs_average_season = DAG('SQL_Clubs_Average_Season', default_args=default_args, start_date=datetime(2023, 1, 31), schedule_interval='0 17 * * *', catchup=False) 

# TASK PARAMETERS
save_sql_clubs_average_season_task = PythonOperator(task_id='save_sql_clubs_average_season', python_callable=save_sql_clubs_average_season, dag=dag_sql_clubs_average_season)
