
import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

# Reference data: original data
reference_data = pd.DataFrame({
    "value": [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
})

# Current data: new data to monitor
current_data = pd.DataFrame({
    "value": [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
})

# Generate data drift report
report = Report(metrics=[DataDriftPreset()])

result = report.run(
    reference_data=reference_data,
    current_data=current_data
)

result.save_html("evidently_report.html")

print("Evidently monitoring report generated successfully!")
