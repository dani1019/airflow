import pendulum
# Airflow 3.0 부터 아래 경로로 import 합니다.
from airflow.operators.python import PythonOperator
import random
from airflow.sdk import DAG

with DAG(
    dag_id="dags_python_operator",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    def select_fruits():
        fruit = ['APPLE','BANANA','ORANGE','AVOGADO']
        rand_int = random.ranint(0,3)
        print(fruit[rand_int])
    
    py_t1 = PythonOperator(
        task_id = 'py_t1'
        python_callable=select_fruit
    )

    py_t1