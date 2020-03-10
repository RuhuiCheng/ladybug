# Data Quality Platform

## Data Issue
![alt data issue](https://raw.githubusercontent.com/RuhuiCheng/ladybug/master/doc/o_Data_Issue.png)

## Framework architecture
![alt architecture](https://raw.githubusercontent.com/RuhuiCheng/ladybug/master/doc/o_data_quality_platform.png)

## Add new test case
````sql
INSERT INTO data_quality.task_case
(task_case_name, description, source_sql, source_connect_id, destination_sql, destination_connect_id, is_enabled, match_type, threshlod_low, threshlod_high, duration_limit, last_run,owner_id,dq_email_id)
VALUES
('ladybug_dw-demo6', 'exactly match for schemal check', "SELECT case column_name when 'user_id' then 'id' when 'user_name' then 'foo' when 'addr' then 'bar' else column_name end as 'field' FROM information_schema.columns WHERE table_name = 'source_user' AND table_schema = 'ladybug_source'", 2, 'SHOW COLUMNS FROM ladybug_dw.demo1', 1, 1, 1, 0, 0, 10, NULL,1,1);
````
| column | comment |
| ------ | ------- |
| task_case_name | Unique key for the test case. It should be named as what it does|
| description | Comments of current case |
| source_sql | SQL text from source side |
| source_connect_id | source database connection id |
| destination_sql | SQL text from destination (data warehouse) |
| destination_connect_id | destination database connection id  |
| is_enabled | Enable or not |
| match_type | 1.exactly, 2.range |
| threshlod_low | Lowest value that the case result allows |
| threshlod_high | Highest value that the case result allows |
| duration_limit | The time limitation that the case allows running (unit: seconds). It is used for test case monitor |
| last_run | The test case last running time. |
| owner_id | The test case owner id |
| dq_email_id | dq email id |

## How to run
   1. Schedule run   
     * hera   
     * cron   
   2. Append to the last step of ETL   
     * E >> T >> L >> C
   3. Manual run   
       | id | Framework provide three running level |
       | --- | --------------------------------------|
       | 1 | ladybug case=ladybug_dw-demo1 |
       | 2 | ladybug group=group_demo1 |
       | 3 | ladybug scenarios=ladybug_scenarios_demo1 |
## Disable a case   
    Update IsEnabled to false
## Extend plugin    
    setup column "dq_extend"   
    1. email
    2. sms
    3. dingding
    4. tel
    5. service_api

## View Result    
```` sql
select * from data_quality.task_case_result;
select * from data_quality.task_execution;
````