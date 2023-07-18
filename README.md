
<div align="center" dir="auto">
  <h1> Airflow Data Pipeline </h1>
</div>
<div> :us: </div>


Project Description
- This project includes two separate DAGs (dag1.py and dag2.py) designed to pull data from an API, store the data on Google Cloud Storage, and finally, process and append the data to a MySQL database using the Python library Pandas.
  

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
