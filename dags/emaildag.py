from airflow.utils.dates import days_ago
from airflow.decorators import dag,task
from datetime import datetime
from airflow.decorators import task

import os
import pandas as pd
from airflow.operators.email_operator import EmailOperator
@dag(
    "email_dag",
    start_date=datetime(2022, 11, 21,12,12),
    schedule_interval='@daily'

)
def taskflow():
    @task(task_id="writing_data",retries=2)
    def writing_data():
        print("writing_data working")
        df=pd.read_csv("https://raw.githubusercontent.com/juliencohensolal/BankMarketing/master/rawData/bank-additional-full.csv",sep=';')
        df.to_csv("data.csv")

    @task(task_id="reading_data",retries=2)
    def reading_data():
        print("reading_data working")


    email_notification=EmailOperator(task_id="email_notification",
                                     to="example@gmail.com",
                                     subject="attempt",
                                     html_content="the dag has finished",
                                     files="data.csv",
    )



    writing_data()>>reading_data()>>email_notification
dag=taskflow()