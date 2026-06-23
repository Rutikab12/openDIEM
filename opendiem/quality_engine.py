class QualityEngine:

    def get_quality_code(self, rule):

        rule_type = rule.type

        if rule_type == "not_null":

            return f"""
null_count = df.filter(
    df["{rule.column}"].isNull()
).count()

if null_count > 0:
    raise Exception(
        "{rule.column} contains NULL values"
    )

print(
    "[QUALITY PASS] {rule.column} NOT NULL"
)
"""

        elif rule_type == "unique":

            return f"""
total_count = df.count()

unique_count = (
    df.select("{rule.column}")
      .distinct()
      .count()
)

if total_count != unique_count:

    raise Exception(
        "{rule.column} contains duplicates"
    )

print(
    "[QUALITY PASS] {rule.column} UNIQUE"
)
"""

        elif rule_type == "row_count":

            return f"""
row_count = df.count()

if row_count < {rule.min_rows}:

    raise Exception(
        "Row count validation failed"
    )

print(
    "[QUALITY PASS] Row Count"
)
"""

        else:

            raise ValueError(
                f"Unsupported quality rule: {rule_type}"
            )