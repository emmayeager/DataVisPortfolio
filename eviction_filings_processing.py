# Setup -------------------------------------------------------------------
import pandas as pd

# Import data from Eviction Lab -------------------------------------------
df = pd.read_csv('pittsburgh_weekly_2020_2021.csv')

# Aggregate by week -------------------------------------------------------
# Use dictionary of column names to desired aggregate functions
# https://stackoverflow.com/questions/46303919/pandas-dataframe-group-sum-one-column-take-first-element-from-others
aggDict = {'week':'first', 'week_date':'first','filings_2020':'sum','filings_avg':'sum'}
aggDf = df.groupby('week',as_index=False).agg(aggDict)

# Reshape to wide format --------------------------------------------------
# Clean up col names
aggDf = aggDf.rename(columns = {'filings_2020':'filings', 'filings_avg':'avg'})

# Create month and day-of-month col
aggDf['MM-DD'] = pd.to_datetime(aggDf['week_date']).dt.strftime('%m-%d')

# Create year col
aggDf.insert(1, 'year', pd.DatetimeIndex(aggDf['week_date']).year)
aggDf = aggDf.drop(['week_date'], axis=1)

# Drop first row with 2019 data
aggDf = aggDf.iloc[1:]

# Pivot to wide
aggDf = aggDf.pivot(index='MM-DD', columns='year')[['filings','avg']]

# Export to CSV -----------------------------------------------------------
aggDf.to_csv('pittsburgh_aggregate_data.csv')
