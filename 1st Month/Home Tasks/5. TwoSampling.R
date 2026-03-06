#Compare the test scores of students from two different classes.
class_A <- c(85, 88, 90, 87, 84, 92, 89, 93, 85, 86)
class_B <- c(78, 75, 80, 77, 72, 70, 74, 79, 75, 72)

t.test(class_A,class_B)

# Result interpretation.
# The welch two-sample t-test shows a statistically significant difference between the mean scores of
# class A and class_B. Class_A had a higher mean score (87.9) compared to class_B (75.2), and this 
# difference of about 12.7 points is statistically significant, t(17.913) = 8.9185 p = 5.247e-08 
# Since the p-value is far below the conventional significance level, we reject the null hypothesis that
# the true difference in means is zero. Additionally, the 95% confidence interval (9.71 to 15.69) does not
# include zero, further confirming that a real difference exists between the two classes. overall, the results
# indicate that class_A performed significantly better than class_8.