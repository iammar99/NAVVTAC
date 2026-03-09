data = read.csv(file = file.choose()) # Will open Dialog box to select
data = read.csv("G:\\Courses\\NAVVTAC\\1st Month\\Data Files\\dat.csv")


library("dplyr")

# ==============|1. Count Numbers of records in each group |==============



data_ctry <- data %>% 
  group_by(Country) %>% 
  count
data_ctry


# --------| Crop |--------


data_crop <- data %>% 
  group_by(Crop) %>% 
  summarise(Count=n())



# --------| Information |--------


data_info <- data %>% 
  group_by(Information) %>% 
  summarise(Count=n())



# --------| Year |--------


data_year <- data %>% 
  filter(
    Year >= 2000
  ) %>% 
  group_by(Year) %>% 
  summarise(Count=n())



# --------| Source |--------


data_src <- data %>% 
  group_by(Source) %>% 
  summarise(Count=n())


# ==============|2. Summarise by Mean yeild and year Range  |==============


data_mean <- data %>% 
  filter(
    Year >= 2000 & Year <= 2005
  ) %>% 
  group_by(Crop) %>% 
  summarise(Yeild_mean = mean(Value))


# ==============|3. Summarise by Crop  |==============


# --------| Value |--------


data_min <- data %>% 
  group_by(Crop) %>% 
  summarise(min_val = min(Value), max_val = max(Value))


# --------| Year |--------


data_min <- data %>% 
  group_by(Crop) %>% 
  summarise(min_year = min(Year), max_year = max(Year))



# ==============|3. Mutate Column  |==============


data_mut <- data %>% 
  mutate(
    ctry = ifelse(Country == "United States of America","USA",Country)
  )



# ==============|4. Sorting  |==============



data_sort <- data[order(data$Crop,data$Value),]

