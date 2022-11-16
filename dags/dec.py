from airflow.utils.dates import days_ago
from airflow.decorators import dag,task
from datetime import datetime
from airflow.decorators import task
import os
import pandas as pd

@dag(
  "dec1",
  start_date=datetime(2022, 11, 2,20,28),
  schedule_interval='@daily',
)
def taskflow():
    @task(task_id="first_task",retries=2)
    def task_1():
        print("task_1 working")
        df=pd.read_csv("https://raw.githubusercontent.com/juliencohensolal/BankMarketing/master/rawData/bank-additional-full.csv",sep=';')
        print(df.head())
        with open("deneme.txt","w") as f:
            f.write(df)
        return 5
    @task(task_id="second_task", retries=2)
    def task_2(a):
        print("task_2 working")
        print(a+5)
        with open("deneme.txt", "r") as f:
            b=f.read()
        print(b)
        return a+5
    @task(task_id="third_task", retries=2)
    def task_3(b):
        print("task_3 working")
        print(b+5)

    @task(task_id="forth_task", retries=2)
    def task_4():
        print("task_4 working")


    #


    task_3(task_2(task_1()))

dag=taskflow()