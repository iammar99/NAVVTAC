# ===============| 1.) MTCARS |===============


model_mtcars = lm(mpg ~ hp+wt+qsec+drat,data=mtcars)
summary(model_mtcars)

# ===============| 2.) IRIS |===============


model_iris <- lm(Petal.Length ~ Petal.Width + Sepal.Length + Sepal.Width ,data=iris)
summary(model_iris)


# ===============| 3.) Diamonds |===============

library(ggplot2)
model_diamonds = lm(price ~ carat + cut + carat + color ,data = diamonds)
summary(model_diamonds)

# ===============| 4.) AirQuality |===============
airquality

model_airquality <- lm(Ozone ~ Solar.R + Wind + Temp ,data=airquality)
summary(model_airquality)

# ===============| 5.) MASS |===============

library(MASS)
model_mass = lm(medv ~ crim + zn + indus + nox + rm + age 
                + dis + rad + tax + ptratio + black + lstat ,data=Boston)
summary(model_mass)
