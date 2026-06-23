class TransformationEngine:

    def get_transformation_code(self, transformation):

        transformation_type = transformation.type

        if transformation_type == "drop_duplicates":

            return """
df = df.dropDuplicates()
"""

        elif transformation_type == "trim_columns":

            return """
from pyspark.sql.functions import trim,col

for c in df.columns:
    df = df.withColumn(
        c,
        trim(col(c))
    )
"""

        elif transformation_type == "lowercase_columns":

            return """
for c in df.columns:
    df = df.withColumnRenamed(
        c,
        c.lower()
    )
"""

        elif transformation_type == "rename_columns":

            mappings = transformation.mappings or {}

            code = []

            for old_col, new_col in mappings.items():

                code.append(
                    f'df = df.withColumnRenamed("{old_col}", "{new_col}")'
                )

            return "\n".join(code)

        elif transformation_type == "filter_rows":

            condition = transformation.condition

            return f'''
df = df.filter("{condition}")
'''

        else:

            raise ValueError(
                f"Unsupported transformation: {transformation_type}"
            )