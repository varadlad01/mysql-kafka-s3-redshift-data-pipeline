Export data from mysql-database to REDSHIFT using kafka

![Data flow diagram](./diagrams/dataflow-diagram.png)

Problem Statement:
We need to build an ETL pipeline to dump mysql data base record to redshift using kafka
![MY SQL DATABASE](./diagrams/mysql-oltp-database.png)

RedShift Data warehouse
![Red Shift](./diagrams/redshift-olap-diagram.png)

Approach:

1.Read data from mysql and  send to kafka topic and from kafka topic we will dump to s3 bucket
![mysql-kafka-s3](./diagrams/mysql-kafka-s3.png)

2.Read data from s3 bucket and dump in REDSHIFT
![s3-redshift](./diagrams/s3-redshift.png)

Solution:

1.Read data from mysql and  send to kafka topic and from kafka topic we will dump to s3 bucket
![mysql-kafka-s3](./diagrams/snaps/mysql_tables.png)
