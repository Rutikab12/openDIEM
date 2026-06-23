# OpenDIEM

**OpenDIEM (Open Data Integration Engineering Modules)** is an open-source, metadata-driven data engineering framework inspired by enterprise-grade platforms used by large organizations to accelerate data pipeline development.

The framework generates production-ready Spark pipelines from YAML metadata definitions, reducing repetitive engineering effort and enforcing standardized development practices.

---

# Vision

Traditional data engineering projects repeatedly implement:

* Data ingestion
* Data transformations
* Data quality checks
* Logging and auditing
* Deployment structures

OpenDIEM aims to automate these activities through a metadata-driven approach.

Instead of writing hundreds of lines of Spark code, engineers define pipelines declaratively using YAML.

---

# Current Version

**Version:** V0.2.3

Implemented Features:

* Metadata-driven pipeline generation
* YAML-based pipeline configuration
* Pydantic configuration validation
* Jinja2 code generation
* Transformation framework
* Data Quality Engine
* Spark pipeline generation

---

# Project Architecture

```text
YAML Configuration
        │
        ▼
   Config Parser
        │
        ▼
  Pydantic Validation
        │
        ▼
 Transformation Engine
        │
        ▼
 Data Quality Engine
        │
        ▼
   Code Generator
        │
        ▼
 Generated Spark Pipeline
```

---

# Folder Structure

```text
OpenDIEM/

├── configs/
│   └── sample_pipeline.yml
│
├── generated/
│   └── customer_ingestion.py
│
├── sample_data/
│
├── opendiem/
│   ├── models.py
│   ├── parser.py
│   ├── generator.py
│   ├── transformation_engine.py
│   ├── transformation_generator.py
│   ├── quality_engine.py
│   ├── quality_generator.py
│   │
│   └── templates/
│       └── spark_pipeline.j2
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Installation

Clone repository:

```bash
git clone https://github.com/<your-username>/OpenDIEM.git

cd OpenDIEM
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Dependencies

```text
pydantic
PyYAML
jinja2
pyspark
```

Install manually:

```bash
pip install pydantic pyyaml jinja2 pyspark
```

---

# Pipeline Configuration Example

```yaml
pipeline_name: customer_ingestion

source:
  type: csv
  path: sample_data/users.csv

target:
  type: parquet
  path: output/customers

load_type: full

transformations:

  - type: drop_duplicates

  - type: trim_columns

  - type: lowercase_columns

quality_rules:

  - type: not_null
    column: customer_id

  - type: unique
    column: customer_id

  - type: row_count
    min_rows: 1
```

---

# Supported Transformations

## Drop Duplicates

```yaml
- type: drop_duplicates
```

Generated:

```python
df = df.dropDuplicates()
```

---

## Trim Columns

```yaml
- type: trim_columns
```

Generated:

```python
for c in df.columns:
    df = df.withColumn(
        c,
        trim(col(c))
    )
```

---

## Lowercase Columns

```yaml
- type: lowercase_columns
```

Generated:

```python
for c in df.columns:
    df = df.withColumnRenamed(
        c,
        c.lower()
    )
```

---

## Rename Columns

```yaml
- type: rename_columns
  mappings:
    fname: first_name
    lname: last_name
```

Generated:

```python
df = df.withColumnRenamed(
    "fname",
    "first_name"
)
```

---

## Filter Rows

```yaml
- type: filter_rows
  condition: age > 18
```

Generated:

```python
df = df.filter(
    "age > 18"
)
```

---

# Supported Data Quality Rules

## Not Null Validation

```yaml
- type: not_null
  column: customer_id
```

Generated:

```python
null_count = df.filter(
    df["customer_id"].isNull()
).count()

if null_count > 0:
    raise Exception(
        "customer_id contains NULL values"
    )
```

---

## Unique Validation

```yaml
- type: unique
  column: customer_id
```

Generated:

```python
total_count = df.count()

unique_count = (
    df.select("customer_id")
      .distinct()
      .count()
)

if total_count != unique_count:
    raise Exception(
        "customer_id contains duplicates"
    )
```

---

## Row Count Validation

```yaml
- type: row_count
  min_rows: 1
```

Generated:

```python
row_count = df.count()

if row_count < 1:
    raise Exception(
        "Row count validation failed"
    )
```

---

# Generate Pipeline

Run:

```bash
python main.py
```

Example output:

```text
Loading pipeline configuration...

Pipeline Name : customer_ingestion

Generating Spark Pipeline...

Pipeline generated successfully!

Location:
generated/customer_ingestion.py
```

---

# Example Generated Pipeline

```python
df = spark.read.format(
    "csv"
).load(
    "sample_data/users.csv"
)

df = df.dropDuplicates()

null_count = df.filter(
    df["customer_id"].isNull()
).count()

if null_count > 0:
    raise Exception(
        "customer_id contains NULL values"
    )

df.write.mode(
    "overwrite"
).parquet(
    "output/customers"
)
```

---

# Roadmap

## V0.1

* Initial Spark Pipeline Generator
* Project scaffolding

## V0.2

* YAML Configuration Support
* Pydantic Validation
* Jinja Template Engine

## V0.2.2

* Transformation Framework
* Metadata-driven Transformations

## V0.2.3

* Data Quality Engine
* Metadata-driven Quality Rules

## Upcoming

### V0.2.4

Audit & Logging Framework

* Pipeline start/end time
* Record counts
* Status tracking
* Audit reports

### V0.3

Databricks Integration

* Delta Lake
* Auto Loader
* Unity Catalog
* Databricks Asset Bundles

### V0.4

Multi-Cloud Support

* Azure Databricks
* AWS EMR
* GCP Dataproc

### V1.0

Enterprise Metadata Platform

* Lineage
* Monitoring
* Governance
* CI/CD Integration

---

# License

MIT License

---

# Author

Rutik Bhoyar

Data Engineer | GCP | Databricks | Spark | Open Source Builder
