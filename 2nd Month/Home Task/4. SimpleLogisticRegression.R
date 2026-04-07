#  1️⃣ Education: Study Hours vs Pass


data <- data.frame(
hours = c(1,2,3,4,5,6,7,8,9,10), 
  pass = c(0,0,0,1,0,1,1,1,1,1)
)
model <- glm (pass ~ hours, data=data, family=binomial) 
summary(model)



#  2️⃣ Education: Attendance vs Pass


data <- data.frame(
attendance = c(50,55,60,65,70,75,80,85,90,95), 
  pass = c(0,0,0,1,0,1,1,1,1,1)
)
model <- glm (pass ~ attendance, data=data, family=binomial) 
summary(model)



#  3️⃣ Buisness: Marketing spending  vs Purchase


data <- data.frame(
spending = c(100,200,150,300,250,400,350,450,500,550), 
purchase = c(0,0,0,1,0,1,1,1,1,1)
)
model <- glm(purchase ~ spending, data=data, family=binomial) 
summary(model)



#  4️⃣ Buisness:Website Time vs Signup


data <- data.frame(
time = c(1,2,3,4,5,6,7,8,9,10), 
signup = c(0,0,0,1,0,1,1,1,1,1)
)
model <- glm (signup ~ time, data=data, family=binomial) 
summary(model)



#  5️⃣ Medical :Age vs Disease


data <- data.frame(
age = c(20,25,30,35,40,45,50,55,60,65), 
disease = c(0,0,0,1,0,1,1,1,1,1)
)
model <- glm (disease ~ age, data=data, family=binomial) 
summary(model)



#  6️⃣ Medical : BMI vs Diabetes


data <- data.frame(
bmi = c(18,20,22,24,26,28,30,32,34,36), 
diabetes = c(0,0,0,1,0,1,1,1,1,1)
)
model <- glm (diabetes ~ bmi, data=data, family=binomial) 
summary(model)



#  7️⃣ Industrial : Machine temp vs Failiure


data <- data.frame(
temp = c(50,55,60,65,70,75,80,85,90,95), 
failiure = c(0,0,0,1,0,1,1,1,1,1)
)
model <- glm (failiure ~ temp, data=data, family=binomial) 
summary(model)



#  8️⃣ Industrial : Pressure  vs defect


data <- data.frame(
pressure = c(10,15,20,25,30,35,40,45,50,55), 
defect = c(0,0,0,1,0,1,1,1,1,1)
)
model <- glm (defect ~ pressure, data=data, family=binomial) 
summary(model)



#  9️⃣ Banking: Income  vs Loan Approval


data <- data.frame(
income = c(1,2,3,4,5,6,7,8,9,10), 
loan = c(0,0,0,1,0,1,1,1,1,1)
)
model <- glm (loan ~ income, data=data, family=binomial) 
summary(model)



#  1️0️⃣ Banking : Credit Score vs Default


data <- data.frame(
score = c(1,2,3,4,5,6,7,8,9,10), 
default = c(0,0,0,1,0,1,1,1,1,1)
)
model <- glm (default ~ score, data=data, family=binomial) 
summary(model)


