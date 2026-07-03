# Databricks notebook source
# MAGIC %md
# MAGIC # Single Table Column Transformation (col names)

# COMMAND ----------

# dbutils.fs.ls('mnt/silver/SalesLT/')
dbutils.fs.ls('abfss://silver@dataengsg.dfs.core.windows.net/SalesLT/')

# COMMAND ----------

dbutils.fs.ls('abfss://gold@dataengsg.dfs.core.windows.net/')

# COMMAND ----------

df = spark.read.format('delta').load('abfss://silver@dataengsg.dfs.core.windows.net/SalesLT/Address/')

# COMMAND ----------

display(df)

# COMMAND ----------

from pyspark.sql.functions import col

def rename_columns_to_snake_case(df):
    """
    Convert column names from PascalCase or camelCase to snake_case in a PySpark DataFrame.

    Args:
        df (DataFrame): The input DataFrame with columns to be renamed.

    Returns:
        DataFrame: A new DataFrame with column names converted to snake_case.
    """
    # Get the list of column names
    column_names = df.columns

    # Dictionary to hold old and new column name mappings
    rename_map = {}

    for old_col_name in column_names:
        # Convert column name from PascalCase or camelCase to snake_case
        new_col_name = "".join([
            "_" + char.lower() if (
                char.isupper()              # Check if the current character is uppercase
                and idx > 0                 # Ensure it's not the first character
                and not old_col_name[idx - 1].isupper()  # Ensure the previous character is not uppercase
            ) else char.lower()  # Convert character to lowercase
            for idx, char in enumerate(old_col_name)
        ]).lstrip("_")  # Remove any leading underscore

        # Avoid renaming to an existing column name
        if new_col_name in rename_map.values():
            raise ValueError(f"Duplicate column name found after renaming: '{new_col_name}'")

        # Map the old column name to the new column name
        rename_map[old_col_name] = new_col_name

    # Rename columns using the mapping
    for old_col_name, new_col_name in rename_map.items():
        df = df.withColumnRenamed(old_col_name, new_col_name)

    return df

# Example usage
# df = rename_columns_to_snake_case(df)

# COMMAND ----------

df = rename_columns_to_snake_case(df)

# COMMAND ----------

display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC # All Table Columns Transformation (col names)
# MAGIC

# COMMAND ----------

# To show the basic format of ls
table_name_temp = []

for i in dbutils.fs.ls('abfss://silver@dataengsg.dfs.core.windows.net/SalesLT'):
    table_name_temp.append(i)

table_name_temp

# COMMAND ----------

table_name = []

for i in dbutils.fs.ls('abfss://silver@dataengsg.dfs.core.windows.net/SalesLT'):
    table_name.append(i.name.split('/')[0])

table_name

# COMMAND ----------

for name in table_name:
    path = 'abfss://silver@dataengsg.dfs.core.windows.net/SalesLT/' + name
    print(path)
    df = spark.read.format('delta').load(path)

    df = rename_columns_to_snake_case(df)

    output_path = 'abfss://gold@dataengsg.dfs.core.windows.net/SalesLT/' + name + '/'
    df.write.format('delta').mode('overwrite').save(output_path)

# COMMAND ----------

display(df)