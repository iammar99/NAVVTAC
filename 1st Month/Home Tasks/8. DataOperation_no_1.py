import numpy as np
import pandas as pd

data = pd.read_csv("G:\\Courses\\NAVVTAC\\1st Month\\Data Files\\dat.csv")

# # ==============|1. Count Numbers of records in each group |==============


# --------| Crop |--------

data_ctry = data.groupby('Country').size().reset_index(name='count')

# --------| Crop |--------

data_crop = data.groupby('Crop').size().reset_index(name='Count')

# --------| Information |--------

data_info = data.groupby('Information').size().reset_index(name='Count')

# --------| Year |--------

data_year = data[data['Year'] >= 2000].groupby('Year').size().reset_index(name='Count')

# --------| Source |--------

data_src = data.groupby('Source').size().reset_index(name='Count')

# ==============|2. Summarise by Mean yield and year Range |==============

data_mean = data[(data['Year'] >= 2000) & (data['Year'] <= 2005)].groupby('Crop')['Value'].mean().reset_index(name='Yeild_mean')



# ==============|3. Summarise by Crop  |==============


# --------| Value |--------

data_crop__val = data.groupby('Crop').agg(
  min_val = ("Value",min),
  max_val = ("Value",min),
)


# --------| Year |--------

data_crop_year = data.groupby('Crop').agg(
  min_val = ("Year",min),
  max_val = ("Year",min),
)



# ==============|3. Mutate Column  |==============


data["ctry"] = np.where(
  data["Country"] == "United States of America",
  "USA",
  data["Country"]
)



# ==============|4. Sorting  |==============

data.sort_values(by=["Crop","Value"])


