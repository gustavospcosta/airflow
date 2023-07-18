<h1 align="center"> Airflow Data Pipeline </h1>

<div dir="auto">
  <br>
  <a target="_blank" rel="noopener noreferrer nofollow" href="https://raw.githubusercontent.com/devicons/devicon/master/icons/vscode/vscode-original.svg"><img align="center" alt="Gustavo-VSCode" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/vscode/vscode-original.svg" style="max-width: 100%;"></a>
  <a target="_blank" rel="noopener noreferrer nofollow" href="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg"><img align="center" alt="Gustavo-Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" style="max-width: 100%;"></a>
  <a target="_blank" rel="noopener noreferrer nofollow" href="https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original-wordmark.svg"><img align="center" alt="Gustavo-Pandas" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original-wordmark.svg" style="max-width: 100%;"></a>
  <a target="_blank" rel="noopener noreferrer nofollow" href="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original.svg"><img align="center" alt="Gustavo-MySQL" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original.svg" style="max-width: 100%;"></a>
  <a target="_blank" rel="noopener noreferrer nofollow" href="https://raw.githubusercontent.com/devicons/devicon/master/icons/googlecloud/googlecloud-original.svg"><img align="center" alt="Gustavo-GCP" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/googlecloud/googlecloud-original.svg" style="max-width: 100%;"></a>
</br>
</div>

### TOPICS
* [Files](#files)
* [Project Description](#project-description)
* [Code Description](#code-description)
* [Author](#author)


## Files

<p align="justify">
<b>• dag.py</b>: the original Python script.

<b>• source_data.csv</b>: the original input CSV file.

<b>• main.py</b>: improved Python script (based on the original script).

<b>• processed_data.py</b>: the output CSV file (created by main.py).
</p>


## Project Description

<p align="justify">
With the small information who was given about this task, I decide to keep some aspects of the original script (like use only a few libraries, keep all the code in a single file etc.) and use it as a guidelines when I wrote this code.

In the code, I try to keep it as clean, simple and readable (human friendly) as possible. 

In my humble opinion (based on my professional experience), the best code (besides of course, of all the technical aspects about write a good code)  it's the code who fits the business process and needs. For example: I could use Great Expectations Python library to validate the data from the source CSV file ("source_data.csv") in order to improve the data integrity, but I assumed that this would be not necessary, based on the steps that was used in the original script ("exercise.py").

In order to improve this script even more and provides even better quality data, it's very important to deep understand the business and IT process about this required data. Once we have this, we can write the code using the best methods and practices, this also allow us to avoid multiple errors scenarios, since we can anticipated their and work in their solutions on a approach who minimize the risks. Without this specific knowledge, sometimes it's better keep the code simple and functional than use <i>"a cannon to kill an ant"</i> who would use more computational resources than the task really need.
</p>

## Code Description

<p align="justify">
This project includes two separate DAGs (dag1.py and dag2.py) designed to pull data from an API, store the data on Google Cloud Storage, and finally, process and append the data to a MySQL database using the Python library Pandas.
</p>



## Author

<p align="justify"> Gustavo de Souza Pessanha da Costa. </p>














<div align="center" dir="auto">
  <h1> Airflow Data Pipeline </h1>
</div>
<div> :us: </div>


Project Description
- 

Code Description
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

<div> :brazil: </div>
Descrição do projeto

- Este projeto inclui duas DAGs separadas (dag1.py e dag2.py) projetadas para extrair dados de uma API, armazenar os dados no Google Cloud Storage e, finalmente, processar e anexar os dados a um banco de dados MySQL usando a biblioteca Python Pandas.

Descrição do código
- Em dag1.py, nos conectamos a uma API, recuperamos dados JSON para várias temporadas e armazenamos os dados JSON em um bucket do GCP. Este DAG inclui um PythonOperator que executa a função save_json_clubs_average_season, que lida com toda a recuperação e armazenamento de dados.
- Em dag2.py, baixamos os dados JSON armazenados do bucket do GCP, processamos-os em um DataFrame do Pandas e os anexamos a um banco de dados MySQL. O processamento e o armazenamento são tratados pela função save_sql_clubs_average_season.
- Em ambos as DAGs, temos alertas de email configurados para sucessos e falhas das execuções do DAG.

Iniciando
- Instale os pacotes necessários do Python : requests, json, datetime, google.cloud.storage, sqlalchemy, pandas e airflow.
- Você precisa ter acesso a um servidor MySQL.
- Você precisa de um bucket do Google Cloud Storage para armazenar arquivos JSON.
- Certifique-se de ter os acessos e as chaves da API necessários.
- Certifique-se de substituir todos os valores de espaço reservado nos scripts (//CREDENTIALS//PATH//file.json, USER:PASSWORD@localhost:PORT/DATABASE, etc.).

Executando o programa
- Coloque os arquivos dag1.py e dag2.py na sua pasta Airflow DAGs.
- Ative as DAGs na sua interface do usuário do Airflow.

Autor
- Gustavo de Souza Pessanha da Costa

Licença
- Este projeto é licenciado sob a licença MIT.
