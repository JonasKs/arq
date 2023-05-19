arq_prefix = 'arq:'
default_queue_name = 'queue'
default_job_key_suffix = ':job:'
default_in_progress_key_suffix = ':in-progress:'
default_result_key_suffix = ':result:'
default_retry_key_suffix = ':retry:'
abort_jobs_ss = 'abort'
# age of items in the abort_key sorted set after which they're deleted
abort_job_max_age = 60
health_check_key_suffix = ':health-check'
# how long to keep the "in_progress" key after a cron job ends to prevent the job duplication
# this can be a long time since each cron job has an ID that is unique for the intended execution time
keep_cronjob_progress = 60

# used by `ms_to_datetime` to get the timezone
timezone_env_vars = 'ARQ_TIMEZONE', 'arq_timezone', 'TIMEZONE', 'timezone'

# extra time after the job is expected to start when the job key should expire, 1 day in ms
expires_extra_ms = 86_400_000
