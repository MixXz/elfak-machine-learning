import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('./input/raw.csv')

profile = ProfileReport(df, title="Profiling Report")

profile.to_file("./output/profiling_report.html")
