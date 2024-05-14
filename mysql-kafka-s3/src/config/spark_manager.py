from pyspark.sql import SparkSession
from .environment import EnvironmentVariable

# Create SparkSession
env = EnvironmentVariable()
spark_session = (SparkSession.builder
                    .master('local[*]')
                    .appName('bigdata')
                    .config("spark.executor.instances", "1")
                    .config("spark.executor.memory", "6g")
                    .config("spark.driver.memory", "6g")
                    .config("spark.executor.memoryOverhead", "8g")
                    .config('spark.jars.packages', 'org.apache.hadoop:hadoop-aws:3.2.2,org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.1,mysql:mysql-connector-java:8.0.11')
                    .getOrCreate())

# Set AWS credentials for S3 access
spark_session.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.access.key", env.aws.access_key_id)
spark_session.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.secret.key", env.aws.secret_access_key)

# Set S3 endpoint and S3A filesystem implementation
spark_session.sparkContext._jsc.hadoopConfiguration().set('fs.s3a.endpoint', 's3.amazonaws.com')
spark_session.sparkContext._jsc.hadoopConfiguration().set('fs.s3a.impl', 'org.apache.hadoop.fs.s3a.S3AFileSystem')

spark_session.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.signing-algorithm", "S3SignerType")
spark_session.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.aws.credentials.provider", "com.amazonaws.auth.DefaultAWSCredentialsProviderChain")
