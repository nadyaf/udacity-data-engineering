from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 quality_check_params = "",
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.quality_check_params = quality_check_params

    def execute(self, context):
        redshift_hook = PostgresHook(postgres_conn_id = self.redshift_conn_id)
        for item in self.quality_check_params:
            self.log.info(f"Executing query: {item['query']}")
            records = redshift_hook.get_records(item['query'])
            if len(records) < 1 or len(records[0]) < 1:
                raise ValueError(f"Data quality check failed. {item['query']} returned no results")
            num_records = records[0][0]
            if num_records != int(item['expected_result']):
                raise ValueError(f"Data quality check failed. Query {item['query']} returned {num_records} rows")
        self.log.info(f"Data quality check passed")