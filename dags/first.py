from airflow.models import DAG
from airflow.utils.dates import days_ago
from datetime import datetime
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
with DAG(
  "first",
  start_date=datetime(2022, 11, 2,20,28),
  schedule_interval='@daily',
) as dag:

    for i in range(0,5):
      b1=BashOperator(task_id=f"bashtask1_{i}",bash_command="echo started",dag=dag)
      b2 = BashOperator(task_id=f"bashtask2_{i}", bash_command="sleep 10 ", dag=dag)
      b3 = BashOperator(task_id=f"bashtask3_{i}", bash_command="echo finished", dag=dag)
      task_a = DummyOperator(task_id=f"task_a_{i}")
      task_b = DummyOperator(task_id=f"task_b_{i}")
      task_c = DummyOperator(task_id=f"task_c_{i}")
      task_d = DummyOperator(task_id=f"task_d_{i}")


      task_a >> [task_b, task_c]>>task_d >>b1>>b2>>b3
