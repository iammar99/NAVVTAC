library(dplyr)

#  Names of the columns were updated but code has been lost 


data = read.csv(file.choose())

head(data)

# ==========| 1. Symboling |==========

table(data$Symboling) # Almost cleaned | range (-3~3)


# ==========| 2. Normalized losses |==========



data <- data %>%
  rename(Normalized_Losses = `Normalized.Losses`)



table(data$Normalized_Losses) # not cleaned |range (65 ~ 256)


data$Normalized_Losses[data$Normalized_Losses == "?"] <- NA #converting ? to NA
data$Normalized_Losses <- as.integer(data$Normalized_Losses) # converting str to int


min(data$Normalized_Losses, na.rm = TRUE)
max(data$Normalized_Losses, na.rm = TRUE)



# ==========| 3. Make |==========


table(data$Make) # Almost Cleaned




# ==========| 4. fuel type |==========




data <- data %>%
  rename(fuel_type = `fuel.type`)

table(data$fuel_type) # Almost Cleaned | Range (Diesel , Gas)



# ==========| 5. aspiration  |==========


table(data$aspiration) # Almost Cleaned | Range (std , turbo)



# ==========| 6. Doors  |==========


table(data$doors) # not Cleaned | Range (four , two)


# ==========| 7. body style  |==========


data <- data %>% 
  rename (body_style = body.style)


table(data$body_style) # Almost Cleaned | Range (convertible, hardtop, hatchback, sedan, wagon)



# ==========| 8. drive wheels  |==========


data <- data %>% 
  rename (drive_wheels = drive.wheels)


table(data$drive_wheels) # Almost Cleaned | Range (4wd, fwd, rwd)



# ==========| 9. engine location  |==========


data <- data %>% 
  rename (engine_location = engine.location)


table(data$engine_location) # Almost Cleaned | Range (front, rear)



# ==========| 10. Wheel Base  |==========


data <- data %>% 
  rename (wheel_base = wheel.base)


table(data$wheel_base) # Almost Cleaned | Range (86.6 ~ 120.9)


# ==========| 11. length   |==========


table(data$length) # Almost Cleaned | Range (141.1 ~ 208.1)


# ==========| 12. width   |==========


table(data$width) # Almost Cleaned | Range (60.3 ~ 72.3)


# ==========| 13. height   |==========


table(data$height) # Almost Cleaned | Range (47.8 ~ 59.8)



# ==========| 14. curb weight   |==========


data <- data %>% 
  rename(curb_weight = curb.weight)


table(data$curb_weight) # Almost Cleaned | Range (1488 ~ 4066)



# ==========| 15. engine type   |==========


data <- data %>% 
  rename(engine_type = engine.type)


table(data$engine_type) # Almost Cleaned | Range (dohc, dohcv, l, ohc, ohcf, ohcv, rotor)


# ==========| 16. num of cylinders   |==========


data <- data %>% 
  rename(num_of_cylinders = num.of.cylinders)


table(data$num_of_cylinders) # Almost Cleaned | Range (eight, five, four, six, three, twelve, two)


# ==========| 17. engine size   |==========


data <- data %>% 
  rename(engine_size = engine.size)


table(data$engine_size) # Almost Cleaned | Range (61 ~ 326)


# ==========| 18. fuel system   |==========


data <- data %>% 
  rename(fuel_system = fuel.system)


table(data$fuel_system) # Almost Cleaned | Range (1bbl, 2bbl, 4bbl,  idi,  mfi, mpfi, spdi, spfi)


# ==========| 19. bore    |==========



table(data$bore) # not Cleaned | Range (2.54 ~ 3.94)


# ==========| 20. stroke   |==========


table(data$stroke) # not Cleaned | Range (2.07 ~ 4.17)


# ==========| 21. compression ratio   |==========


data <- data %>% 
  rename(compression_ratio = compression.ratio)


table(data$compression_ratio) # Almost Cleaned | Range (7 ~ 23)


# ==========| 22. horsepower    |==========


table(data$horsepower ) # not Cleaned | Range (48 ~ 288)



data$horsepower[data$horsepower == "?"] <- NA #converting ? to NA
data$horsepower <- as.integer(data$horsepower) # converting str to int


min(data$horsepower, na.rm = TRUE)
max(data$horsepower, na.rm = TRUE)

# ==========| 23. Peak RPM   |==========


data <- data %>% 
  rename(peak_rpm = peak.rpm)


table(data$peak_rpm) # Almost Cleaned | Range (4150 ~ 6600)


data$peak_rpm[data$peak_rpm == "?"] <- NA #converting ? to NA
data$peak_rpm <- as.integer(data$peak_rpm) # converting str to int


min(data$peak_rpm, na.rm = TRUE)
max(data$peak_rpm, na.rm = TRUE)


# ==========| 24. city mpg   |==========


data <- data %>% 
  rename(city_mpg = city.mpg)


table(data$city_mpg) # Almost Cleaned | Range (13 ~ 49)



# ==========| 25. highway mpg   |==========


data <- data %>% 
  rename(highway_mpg = highway.mpg)


table(data$highway_mpg) # Almost Cleaned | Range (16 ~ 54)



# ==========| 26. price   |==========


table(data$price) # not Cleaned | Range (5118 ~ 45400)


data$price[data$price == "?"] <- NA #converting ? to NA
data$price <- as.integer(data$price) # converting str to int


min(data$price, na.rm = TRUE)
max(data$price, na.rm = TRUE)


names(data)[colSums(is.na(data)) > 0] # to Find values with NA

#  ====================== | Columns with NA |======================

# "Normalized_Losses" "horsepower"        "peak_rpm"          "price"       




#  ====================== | Removing NA from Normalized_Losses  |======================

data$Normalized_Losses
mean_Normalized_Losses <- mean(data$Normalized_Losses, na.rm = TRUE)
data$Normalized_Losses[is.na(data$Normalized_Losses)] <- mean_Normalized_Losses



#  ====================== | Removing NA from horse_power  |======================

data$horsepower
mean_horsepower <- as.integer(mean(data$horsepower, na.rm = TRUE))
data$horsepower[is.na(data$horsepower)] <- mean_horsepower

#  ====================== | Removing NA from peak_rpm  |======================

data$peak_rpm
mean_peak_rpm <- as.integer(mean(data$peak_rpm, na.rm = TRUE))
data$peak_rpm[is.na(data$peak_rpm)] <- mean_peak_rpm



#  ====================== | Removing NA from price  |======================

data$price
mean_price <- as.integer(mean(data$price, na.rm = TRUE))
data$price[is.na(data$price)] <- mean_price





# For saving

write.csv(data, "G:/Courses/NAVVTAC/1st Month/Practice/Auto Cleaning/data_updated.csv", row.names = FALSE)


