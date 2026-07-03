# Databricks notebook source
# MAGIC %md
# MAGIC # Transformation for Single Table Column
# MAGIC

# COMMAND ----------

# dbutils.fs.ls('mnt/bronze/SalesLT/')

dbutils.fs.ls("abfss://bronze@dataengsg.dfs.core.windows.net/SalesLT")

# COMMAND ----------

# dbutils.fs.ls('mnt/silver/')
dbutils.fs.ls("abfss://silver@dataengsg.dfs.core.windows.net/")

# COMMAND ----------

df = spark.read.format('parquet').load('abfss://bronze@dataengsg.dfs.core.windows.net/SalesLT/Address/Address.parquet')

# COMMAND ----------

display(df)

# COMMAND ----------

from pyspark.sql.functions import from_utc_timestamp, date_format
from pyspark.sql.types import TimestampType

df = df.withColumn("ModifiedDate", date_format(from_utc_timestamp(df['ModifiedDate'].cast(TimestampType()), "UTC"), "yyyy-MM-dd"))

# COMMAND ----------

display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC # Date Transformation for All Tables

# COMMAND ----------

table_name = []

for i in dbutils.fs.ls('abfss://bronze@dataengsg.dfs.core.windows.net/SalesLT'):
    table_name.append(i.name.split('/')[0])

table_name

# COMMAND ----------

# DBTITLE 1,Cell 10
from pyspark.sql.functions import from_utc_timestamp, date_format
from pyspark.sql.types import TimestampType

for i in table_name:
    path = 'abfss://bronze@dataengsg.dfs.core.windows.net/SalesLT/' + i + '/' + i +'.parquet'
    df = spark.read.format('parquet').load(path)
    column = df.columns

    for col in column:
        if "Date" in col or "date" in col:
            df = df.withColumn(col, date_format(from_utc_timestamp(df[col].cast(TimestampType()), "UTC"), "yyyy-MM-dd"))
    
    output_path = 'abfss://silver@dataengsg.dfs.core.windows.net/SalesLT/' + i + '/'
    df.write.format('delta').mode('overwrite').save(output_path)

# COMMAND ----------

display(df)