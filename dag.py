# Import required modules
from datetime import datetime
import pandas as pd
import json
from sqlalchemy import create_engine
from google.cloud import storage
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator
from airflow.utils.email import send_email

# Set constants
TEMP = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
KEY_FILE = "//CREDENTIALS//PATH//key.json"
BUCKET_NAME = 'SProject'
SEASONS_LIST = ["40557","27591","22931","16183"]
DB_ENGINE = create_engine('mysql://USER:PASSWORD@localhost:PORT/DBNAME')

def success_email(context):
    """
    Sends a success email after a DAG run is completed.
    """
    dag_run = context.get('dag_run')
    msg = f"DAG {dag_run} RAN successfully"
    subject = f"DAG RAN successfully"
    send_email(to='example@example.com', subject=subject, html_content=msg)

def fail_email(context):
    """
    Sends a failure email if a DAG run fails.
    """
    dag_run = context.get('dag_run')
    msg = f"DAG {dag_run} NOT RAN successfully"
    subject = f"DAG NOT RAN successfully"
    send_email(to='example@example.com', subject=subject, html_content=msg)

def save_sql_clubs_average_season():
    """
    Pulls JSON data from a Google Cloud Storage bucket, processes the data, and saves it to a MySQL database.
    """
    gcp_storage = storage.Client.from_service_account_json(KEY_FILE)
    gcp_bucket = gcp_storage.get_bucket(BUCKET_NAME)

    df_final = pd.DataFrame()

    for season in SEASONS_LIST:
        file = f"media_clubes_por_temporada_{season}"
        blob = gcp_bucket.blob(file)
        data = json.loads(blob.download_as_string(client=None))
        data_aux = data["topTeams"]["avgRating"]
        df = pd.json_normalize(data_aux)
        df["season_id"] = season
        df_final = df_final.append(df)
        df_final["last_update"] = TEMP
        df_final = df_final.fillna(0)

    df_final.reset_index(drop=True, inplace=True)
    df_final = df_final[["team.name","team.id","statistics.avgRating","statistics.matches","season_id","last_update"]]
    df_final.rename(columns={
        "team.name": "team_name",
        "team.id": "team_id",
        "statistics.avgRating": "average_rating",
        "statistics.matches":"matches"
        }, inplace=True)

    df_final.to_sql("c_average_season", DB_ENGINE, index=False, if_exists="append")

def main():
    default_args = {'owner': 'NAME', 'on_failure_callback': fail_email, 'on_success_callback': success_email, 'retries': 0}
    dag_sql_clubs_average_season = DAG('SQL_Clubs_Average_Season', default_args=default_args, start_date=datetime(2023, 1, 31), schedule_interval='0 17 * * *', catchup=False) 
    save_sql_clubs_average_season_task = PythonOperator(task_id='save_sql_clubs_average_season', python_callable=save_sql_clubs_average_season, dag=dag_sql_clubs_average_season)

if __name__ == '__main__':
    main()
