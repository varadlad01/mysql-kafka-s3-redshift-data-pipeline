**Summary:**

This project revolves around constructing a containerized data capture pipeline, orchestrating the seamless transfer of information from a MySQL database to Amazon Redshift for visualization purposes. Docker containers are employed for their ability to ensure consistency and portability across diverse environments. A Change Data Capture (CDC) pipeline is used to tracking changes made to data within a database system over time. The pipeline utilizes Kafka as a pivotal intermediary for real-time data streaming, facilitating ingestion of MySQL data into Redshift. Amazon S3 serving as an intermediate repository for raw data prior to any transformation. Redshift plays a crucial role in enabling efficient processing of analytics, empowering users to extract actionable insights from the data.

Export data from mysql-database to REDSHIFT using kafka

![Data flow diagram](./diagrams/dataflow-diagram.png)

Problem Statement:
We need to build an ETL pipeline to dump mysql data base record to redshift using kafka
![MY SQL DATABASE](./diagrams/mysql-oltp-database.png)

RedShift Data warehouse (Transfored data in fact and dimentional tables)
![Red Shift](./diagrams/redshift-olap-diagram.png)

Approach:

1.Read data from mysql and  send to kafka topic and from kafka topic we will dump to s3 bucket
![mysql-kafka-s3](./diagrams/mysql-kafka-s3.png)

2.Read data from s3 bucket and dump in REDSHIFT
![s3-redshift](./diagrams/s3-redshift.png)

Solution:

1. Docker Container
![s3-redshift](./Snaps/docker_container.png)

2. Created SQL tables using database-dump/mysqlsampledatabase.sql file
![s3-redshift](./Snaps/mysql_tables.png)

3. Sample MySQL employee table data
![s3-redshift](./Snaps/Sample_mysql_data_new.png)

4. Sample Kafka Topics
![s3-redshift](./Snaps/sample_kafka_topics.png)

5. Sample data from customers kafka topic
![s3-redshift](./Snaps/sample_kafka_data.png)

6. S3 Objects
![s3-redshift](./Snaps/s3_objects.png)

7. Sample s3 data from customers object
![s3-redshift](./Snaps/sample_s3_data.png)

8. Sample Redshift tables and data
![s3-redshift](./Snaps/sample_redshilft_data.png)

9. Data Visualization in Bar Chart format
![s3-redshift](./Snaps/visualization1.png)

10. Data Visualization in Area Chart format
![s3-redshift](./Snaps/visualization2.png)

11. Data Visualization in Pie Chart format
![s3-redshift](./Snaps/visualization3.png)

12. Data Visualization in Line Chart format
![s3-redshift](./Snaps/visualization4.png)
