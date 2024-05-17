from celery import shared_task
import time

@shared_task
def simulate_processing(movie_id):
    print("Movie ID avant:", movie_id)
    time.sleep(10)
    print("Movie ID après:", movie_id)