from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("customer_ingestion")
    .getOrCreate()
)

print("Starting Pipeline: customer_ingestion")

df = (
    spark.read
    .format("csv")
    .load("sample_data/users.csv")
)

df = df.dropDuplicates()

null_count = df.filter(
    df["customer_id"].isNull()
).count()

if null_count > 0:
    raise Exception("customer_id contains NULL values")

print("[QUALITY PASS] customer_id NOT NULL")

total_count = df.count()

unique_count = (
    df.select("customer_id")
      .distinct()
      .count()
)

if total_count != unique_count:
    raise Exception("customer_id contains duplicates")

print("[QUALITY PASS] customer_id UNIQUE")

row_count = df.count()

if row_count < 1:
    raise Exception("Row count validation failed")

print("[QUALITY PASS] Row Count")

(
    df.write
    .mode("overwrite")
    .format("parquet")
    .save("output/customers")
)

(
    df.write
    .mode("overwrite")
    .format("parquet")
    .save("output/customers")
)

print("Pipeline Completed Successfully")