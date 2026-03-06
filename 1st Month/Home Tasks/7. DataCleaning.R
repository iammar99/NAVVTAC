library(dplyr)

df1 <- data.frame(
  id = c(1, 2, 3, NA, 5),
  age = c(25, NA, 35, 40, NA),
  income = c(50000, 60000, NA, 80000, 90000)
)

# -------------| Removing missing values |-------------

# 1. Removing rows with missing values
df1_copy <- na.omit(df1)

# 2. Replacing with mean
df1_age <- df1
df1_age$age[is.na(df1_age$age)] <- mean(df1_age$age, na.rm = TRUE)

# 3. Replacing with zero
df1_income <- df1
df1_income$income[is.na(df1_income$income)] <- 0


# -------------| Convert Types |-------------

df2 <- data.frame(
  student = c("A", "B", "C", "D"),
  score = c("90", "85", "88", "92"),
  passed = c("yes", "yes", "no", "yes"),
  stringsAsFactors = FALSE
)

str(df2)
summary(df2)
summary(df_num)

df_num <- df2
df_num$score <- as.numeric(df_num$score)
df_num$passed <- as.factor(df_num$passed)


# -------------| Duplicates |-------------

df3 <- data.frame(
  product = c("A", "B", "A", "C", "C"),
  price = c(10, 20, 10, 15, 15)
)

df3_all <- distinct(df3)
df3_prod <- distinct(df3, product, .keep_all = TRUE)


# -------------| Rename |-------------

df4 <- data.frame(
  x1 = c(10, 20, 30),
  x2 = c(5, 6, 7)
)

df4_rename <- rename(df4, height = x1, weight = x2)


# -------------| Filter Invalid |-------------

df5 <- data.frame(
  person = c("john", "anna", "mike", "sara"),
  age = c(22, -5, 200, 30)
)

df_filter <- filter(df5, age > 0 & age < 100)


# -------------| New Variables |-------------

df6 <- data.frame(
  name = c("A", "B", "C"),
  math = c(80, 90, 70),
  science = c(85, 88, 78)
)

df6_new <- df6
df6_new$total <- df6_new$math + df6_new$science
df6_new$avg <- df6_new$total / 2
