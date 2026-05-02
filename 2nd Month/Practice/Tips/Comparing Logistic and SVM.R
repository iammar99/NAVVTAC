data = read.csv(file.choose())


head(data)


data$gender <- as.factor(data$gender)
data$day <- as.factor(data$day)
data$time <- as.factor(data$time)
data$smoker <- as.factor(data$smoker)

# -------------------------------------
#       Logistic Regression
# -------------------------------------


model_log <- glm(smoker ~ total_bill + tip + gender + smoker + day + time + size, data = data , family = binomial)
summary(model_log)

pred_prob <- predict(model_log, type = "response")
pred_class <- ifelse(pred_prob > 0.5, 1, 0)
pred_class



# -------------------------------------
#       Support Vector Machine
# -------------------------------------



library(e1071)

# Linear kernel
svm_linear <- svm(smoker ~ total_bill + tip + gender + day + time + size ,data = data, kernel = "linear")
pred_linear <- predict(svm_linear)

# Radial kernel (RBF)
svm_radial <- svm(smoker ~ total_bill + tip + gender + day + time + size, data = data, kernel = "radial")
pred_radial <- predict(svm_radial)

# Polynomial kernel
svm_poly <- svm(smoker ~ total_bill + tip + gender + day + time + size, data = data, kernel = "polynomial")
pred_poly <- predict(svm_poly)



# -------------------------------------
#       Confusion Matrix
# -------------------------------------


table(Predicted = pred_class, Actual = data$smoker)
table(Predicted = pred_linear, Actual = data$smoker)
table(Predicted = pred_radial, Actual = data$smoker)
table(Predicted = pred_poly, Actual = data$smoker)




# -------------------------------------
#       Plotting Matrix
# -------------------------------------


make_cm_df <- function(pred, actual, model_name) {
  cm <- as.data.frame(table(Predicted = pred, Actual = actual))
  cm$model <- model_name
  return(cm)
}

df_all <- rbind(
  make_cm_df(pred_class, data$smoker, "Logistic"),
  make_cm_df(pred_linear, data$smoker, "SVM Linear"),
  make_cm_df(pred_radial, data$smoker, "SVM Radial"),
  make_cm_df(pred_poly, data$smoker, "SVM Polynomial")
)

ggplot(df_all, aes(x = Actual, y = Predicted, fill = Freq)) +
  geom_tile(color = "white") +
  geom_text(aes(label = Freq), size = 4, fontface = "bold") +
  scale_fill_gradient(low = "#E0F7FA", high = "#006064") +
  facet_wrap(~model) +
  theme_minimal() +
  labs(title = "Confusion Matrices Comparison") +
  theme(
    plot.title = element_text(face = "bold", size = 14),
    strip.text = element_text(face = "bold")
  )
# ----------------------| Logistic Regression |----------------------


#                  Actual
#        Predicted   0   1
#                0 130  53
#                1  21  40


# ----------------------| SVM (Linear) |----------------------


#                   Actual
#         Predicted   0   1
#                  0 144  65
#                  1   7  28


# ----------------------| SVM (Radidal) |----------------------


#                   Actual
#         Predicted   0   1
#                 0 147  73
#                 1   4  20


# ----------------------| SVM (Polynomial) |----------------------


#                   Actual
#         Predicted   0   1
#                 0 151  83
#                 1   0  10





# -------------------------------------
#       Conclusion
# -------------------------------------



# Model	Correct Predictions out of 244


# Logistic     =>    170
# Linear      =>    172 (best)
# Radial      =>    167
# Polynomial  =>    161


# So Linear SVM is best among  all as it predicts most accurate values 




