# IMPORT PYTHON MODULES
import requests
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

# SEASON ID LIST
seasons_list = ["40557","27591","22931","16183"]

# FUNCTION SUCCESS MAIL
def success_email(context):
    """
    Sends an email when a Directed Acyclic Graph (DAG) has run successfully.

    Args:
        context (dict): A dictionary with metadata about the DAG run, including the 'dag_run' key.

    Returns:
        None. Sends an email to a predetermined email address upon successful DAG execution.
    """
    dag_run = context.get('dag_run')
    msg = f"DAG {dag_run} RAN successfully"
    subject = f"DAG RAN successfully"
    send_email(to='example@example.com', subject=subject, html_content=msg)

# FUNCTION FAIL MAIL
def fail_email(context):
    """
    Sends an email when a Directed Acyclic Graph (DAG) has not run successfully.

    Args:
        context (dict): A dictionary with metadata about the DAG run, including the 'dag_run' key.

    Returns:
        None. Sends an email to a predetermined email address upon unsuccessful DAG execution.
    """
    dag_run = context.get('dag_run')
    msg = f"DAG {dag_run} NOT RAN successfully"
    subject = f"DAG NOT RAN successfully"
    send_email(to='example@example.com', subject=subject, html_content=msg)

# FUNCTION
def save_json_clubs_average_season():
    """
    For each season in the seasons list, fetches top teams data from an API, 
    saves the data to a JSON format, and uploads it to a Google Cloud Platform bucket.

    Args:
        None

    Returns:
        None. Fetches data and writes it to a JSON file in a GCP bucket for each season in the seasons list.
    """

    for season in seasons_list:
        file_name = f"filename_{season}"
        URL = "https://divanscore.p.rapidapi.com/tournaments/get-top-teams"
        headers = {"X-RapidAPI-Key":"CHIHUAHUA", "X-RapidAPI-Host":"divanscore.p.rapidapi.com"}
        querystring = {"tournamentId":"325","seasonId":season,"type":"total"}
        response = requests.get(URL, headers=headers, params=querystring, timeout=120)
        data = response.json()
        my_data = json.dumps(data)
        blob = gcp_bucket.blob(file_name)
        blob.upload_from_string(my_data, content_type='application/json')

# DAG ARGUMENTS
default_args = {'owner': 'NAME', 'on_failure_callback': fail_email, 'on_success_callback': success_email, 'retries': 0}

# DAG PARAMETERS
dag_json_clubs_average_season = DAG('JSON_Clubs_Average_Season', default_args=default_args, start_date=datetime(2023, 1, 31), schedule_interval='0 * * * *', catchup=False) 

# TASK PARAMETERS
save_json_clubs_average_season_task = PythonOperator(task_id='save_json_clubs_average_season', python_callable=save_json_clubs_average_season, dag=dag_json_clubs_average_season)
