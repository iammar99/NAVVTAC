# ========================================
#       Choosing dataset
# ========================================


data = read.csv(file.choose())
head(data)


# ========================================
#       Column names
# ========================================

colnames(data)

# [1] "Symboling"         "Normalized_Losses" "Make"              "fuel_type"         "aspiration"        "doors"             "body_style"       
# [8] "drive_wheels"      "engine_location"   "wheel_base"        "length"            "width"             "height"            "curb_weight"      
# [15] "engine_type"       "num_of_cylinders"  "engine_size"       "fuel_system"       "bore"              "stroke"            "compression_ratio"
# [22] "horsepower"        "peak_rpm"          "city_mpg"          "highway_mpg"       "price" 



# ========================================
#       import libraries
# ========================================


model <- glm()