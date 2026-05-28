from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.email import EmailOperator
from datetime import datetime, timedelta


def fun1():
    print("Welcome to Airflow")

def write_names():
    names = ['Gamal', 'Menna', 'Ahmed', 'Omar', 'Hossam']
    with open('/data/output.txt', 'w') as f:
        for name in names:
            f.write(name + '\n')
    print("File written successfully!")


with DAG(
    dag_id='Dag2',
    start_date=datetime(2026, 5, 28),
    schedule_interval=timedelta(minutes=10),
    catchup=False
) as dag:

    task1 = EmailOperator(
        task_id='send_email',
        to='yousif.eldeib@ejust.edu.eg',
        subject='Test Airflow Mail',
        html_content='<h1>Hello from Airflow!</h1>',
    )

    task2 = PythonOperator(
        task_id='write_names_to_file',
        python_callable=write_names
    )

    task1 >> task2