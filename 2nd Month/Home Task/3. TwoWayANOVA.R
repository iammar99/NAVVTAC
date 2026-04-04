
# = ✓ Full R code: dataset + model + interaction




# **1. Teaching Method x Gender (Education)**

method <- factor(rep (c("Lecture", "Online", "Blended"), each=6)) 
gender <- factor(rep (c("Male", "Female"), each=3, times=3))
score <- c(60,62,65, 58, 59, 61, 70,72,74, 68, 69, 71, 80, 82, 85, 78,79,81)
df <- data.frame(method, gender, score)
model <- aov (score ~ method * gender, data=df)
summary (model)



  # **2. Machine Type x Shift (Manufacturing)**
machine <- factor(rep(c("A", "B", "C"), each=6))
shift <- factor(rep(c("Day", "Night"), each=3, times=3))
output <- c(20, 22, 21, 18, 19, 20, 25,27,26, 23, 24, 25, 30,32,31, 28,29,30)
df <- data.frame(machine, shift, output)
summary (aov (output~ machine * shift, data=df))

  
    
# **3. Campaign x Region (Marketing)**



campaign <- factor(rep (c("Social", "TV", "Email"), each=6))
region <- factor(rep (c("Urban", "Rural"), each=3, times=3))
sales <- c(200, 210, 205, 180, 190,185, 250,260,255, 230,240,235, 170, 175, 180, 160,165,170)
df <- data.frame(campaign, region, sales)
summary(aov(sales~ campaign * region, data=df))
  
  
  
  
  
  
# **4. Drug x Dosage (Healthcare)**
drug <-factor(rep(c("D1", "D2", "D3"), each=6))
dose <- factor (rep(c("Low", "High"), each=3, times=3))
recovery <- c(5,6,7, 8,9,10, 6,7,8, 9,10,11, 4,5,6, 7,8,9)
df <- data.frame(drug, dose, recovery)
summary(aov(recovery ~ drug * dose, data=df))






# **5. Store Type x Location (Retail)**


store <-factor(rep (c("Supermarket", "Mall", "Online"), each=6))
location <- factor (rep(c("City", "Town"), each=3, times=3))
revenue <- c(500,520,510, 480,490,495, 600, 620, 610, 580,590,600, 550,560,570, 530,540,545)
df <- data.frame(store, location, revenue)
summary(aov(revenue ~ store * location, data=df))



# **6. Study Hours x Teaching Style**
hours <- factor (rep (c("Low", "Medium", "High"), each=6))
style <- factor(rep(c("Traditional", "Modern"), each=3, times=3))
marks <- c(50,52,55, 48, 49, 51, 65, 67, 66, 63, 64, 65, 80, 82, 81, 78, 79, 80)
df <- data.frame(hours, style, marks)
summary(aov(marks ~ hours * style, data=df))





# **7. Fuel Type x Engine Size**
fuel <- factor(rep(c("Petrol", "Diesel", "Hybrid"), each=6))
engine <- factor(rep(c("Small", "Large"), each=3, times=3))
efficiency <- c(12,13,11, 10, 11, 12, 15,16,14, 13,14,15, 20, 22, 21, 18, 19, 20)
df <- data.frame(fuel, engine, efficiency)
summary(aov(efficiency ~  fuel * engine, data=df))


# **8. Fertilizer x Soil Type (Agriculture) **
fertilizer <- factor (rep(c("F1", "F2", "F3"), each=6)) 
soil <- factor (rep(c("Clay", "Sandy"), each=3, times=3))
yield <- c(30,32,31, 28, 29, 30, 35,37,36, 33, 34, 35, 25,27,26, 23,24,25)
df <- data.frame(fertilizer, soil, yield)
summary(aov(yield ~ fertilizer * soil, data=df))


 
# **9. Department x Experience Level (HR)**


dept <- factor(rep(c("HR", "IT", "Finance"), each=6))
experience <- factor (rep(c("Junior", "Senior"), each=3, times=3)) 
performance <- c(60, 62, 61, 65, 66, 67, 75,78,77, 80, 82, 81, 70, 72, 71, 74,75,76)
df <- data.frame(dept, experience, performance)
summary(aov(performance ~ dept * experience, data=df))



# ***10. Process x Temperature (Engineering)**
process <- factor (rep(c("P1", "P2", "P3"), each=6)) 
temp <- factor(rep(c("Low", "High"), each=3, times=3))
strength <- c(100,102,101, 95, 96, 97, 110, 112, 111, 105, 106, 107, 90, 92, 91, 85, 86, 87) 
df <- data.frame(process, temp, strength)
summary(aov(strength ~ process * temp, data=df))


# **Interpretation Framework (Important for Students) **
#   For each model:
#   ***Factor 1 effect** First variable impact
# # * **Factor 2 effect** - Second variable impact
# # * **Interaction effect (A x B) Combined influence




# **Industrial Insight**
#   Two-way ANOVA is heavily used in:
#   * ✓ Six Sigma DOE (Factorial Designs)
# # * ✓ Manufacturing optimization
# # * ✓ Marketing segmentation
# ✓ Clinical trials
