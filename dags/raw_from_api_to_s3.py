import logging
import duckdb

from airflow import DAG
from airflow.models import Variable
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

OWNER = 'danisty'
DAG_ID = 'raw_from_api_to_s3'

LAYER = 'raw'
SOURCE = 'earthquake'

ACCESS_KEY = Variable.get('access_key')
SECRET_KEY = Variable.get('secret_key')

LONG_DESCRIPTION = """ # """
SHORT_DESCRIPTION = "SHORT"