broker_url = "amqp://rabbit:password@localhost:15672/test"
result_backend = "db+postgresql://postgres:password@localhost:15432/test_db"
worker_concurrency = 1    # optional
task_acks_late = True
# task_track_started = True
# task_reject_on_worker_lost = True
