import pandas as pd
import numpy as np

# --------------| Creating DataFrame |--------------

df = pd.DataFrame({
    'weekday': ['Mon','Tues','Wed','Thurs']*5,
    'Quarter': ['Q1']*5 + ['Q2']*5 + ['Q3']*5 + ['Q4']*5,
    'delay': [9.9, 5.4, 8.8, 6.9, 49, 9.7, 79, 5, 8.3, 11.1, 10.2, 9.3, 12.2, 10.2, 9.2, 9.7, 12.2, 8.1, 7.9, 5.6]
})

df_np = pd.DataFrame({
    "weekday": np.repeat(['Mon','Tues','Wed','Thurs'],5),
    "quarter": ["Q" + str(x) for x in np.repeat(range(1,5),5)],
    "delay" : [9.9, 5.4, 8.8, 6.9, 49,9.7, 79, 5, 8.3, 11.1, 10.2, 9.3, 12.2, 10.2,9.2, 9.7, 12.2,8.1,7.9,5.6]
})
# --------------| Grouping |--------------

grouped_df = df.groupby('weekday').agg(
    SD=('delay', 'std'),
    maxDelay=('delay', 'max'),
    minDelay=('delay', 'min')
).reset_index()

# --------------| Creating DataFrame |--------------

df1 = pd.DataFrame({
    'Quarter': ['Q1']*4 + ['Q2']*4 + ['Q3']*4 + ['Q4']*4,
    'week': ['weekday', 'weekday', 'weekend', 'weekend']*4,
    'direction': ['Inbound', 'Outbound']*8,
    'delay': [10.8, 9.7, 15.5, 10.4, 11.8, 3.9, 5.5, 3.3, 10.6, 8.8, 6.6, 5.2, 9.1, 7.3, 5.3, 4.4]
})



df1_np = pd.DataFrame({
    'Quarter': ["Q" + str(x) for x in np.repeat(range(1,5),4)],
    'week': np.tile(np.repeat(['weekday', 'weekend'],2),4),
    'direction': np.tile(['Inbound', 'Outbound'],8),
    'delay': [10.8, 9.7, 15.5, 10.4, 11.8, 3.9, 5.5, 3.3, 10.6, 8.8, 6.6, 5.2, 9.1, 7.3, 5.3, 4.4]
})

# --------------| Grouping |--------------

grouped_df1 = df1.groupby(['Quarter', 'week']).agg(
    SD=('delay', 'std'),
    maxDelay=('delay', 'max'),
    minDelay=('delay', 'min')
).reset_index()
