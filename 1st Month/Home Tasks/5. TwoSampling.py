import numpy as np
from scipy import stats


#Compare the test scores of students from two different classes.
class_A = [85, 88, 90, 87, 84, 92, 89, 93, 85, 86]
class_B = [78, 75, 80, 77, 72, 70, 74, 79, 75, 72]

t_stat, p_value = stats.ttest_ind(class_A, class_B, equal_var=False)

# Result interpretation.
# The Welch two-sample t-test shows a statistically significant difference between the mean scores of
# class_A and class_B. Class_A had a higher mean score (87.9) compared to class_B (75.2), and this 
# difference of about 12.7 points is statistically significant, t(17.913) = 8.9185 p = 5.247e-08 
# Since the p-value is far below the conventional significance level, we reject the null hypothesis that
# the true difference in means is zero. Additionally, the 95% confidence interval (9.71 to 15.69) does not
# include zero, further confirming that a real difference exists between the two classes. Overall, the results
# indicate that class_A performed significantly better than class_B.

# Calculate means
mean_A = sum(class_A) / len(class_A)
mean_B = sum(class_B) / len(class_B)

# Calculate degrees of freedom for Welch's t-test
var_A = stats.tvar(class_A)
var_B = stats.tvar(class_B)
n_A = len(class_A)
n_B = len(class_B)
df = (var_A/n_A + var_B/n_B)**2 / ((var_A**2)/((n_A**2)*(n_A-1)) + (var_B**2)/((n_B**2)*(n_B-1)))

# Calculate 95% confidence interval for the difference in means
diff = mean_A - mean_B
se_diff = (var_A/n_A + var_B/n_B)**0.5
ci_low = diff - stats.t.ppf(0.975, df) * se_diff
ci_high = diff + stats.t.ppf(0.975, df) * se_diff

t_stat, p_value, df, mean_A, mean_B, diff, ci_low, ci_high
stats.t
print("t = ",t_stat,", df = ",df,", p-value = ",p_value)
print("95 percent confidence interval:")
print(ci_low, ci_high)
print("sample estimates:")
print("mean of x mean of y ")
print(mean_A, mean_B)


# Output


# t =  8.918535416345152 , df =  17.913252662131722 , p-value =  5.2469329325001136e-08
# 95 percent confidence interval:     
# 9.707246888474764 15.692753111525242
# sample estimates:
# mean of x mean of y 
# 87.9 75.2
# 
