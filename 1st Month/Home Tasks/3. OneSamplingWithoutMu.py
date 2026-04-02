from scipy import stats

# 1️⃣ Education
entrance_score = [72,74,76,70,73,75,71,69,77,74]
print(stats.ttest_1samp(entrance_score, 0))

# 2️ Business
monthly_sales = [48000,51000,49500,50500,49000,52000,50000,48500]
print(stats.ttest_1samp(monthly_sales, 0))

# 3️⃣ Medical
bp = [118,122,119,121,117,123,120,116,124]
print(stats.ttest_1samp(bp, 0))

# 4️⃣ Industrial
fill_weight = [9.8,10.1,9.9,10.2,9.7,10.0,10.3,9.6,10.1,9.8]
print(stats.ttest_1samp(monthly_sales, 0))

# 5️⃣ Agriculture
wheat_yeild = [3.8,4.1,4.3,3.9,4.0,4.2,3.7]
print(stats.ttest_1samp(wheat_yeild, 0))

# 6️⃣ IT
res_time = [2.9,3.1,3.0,3.2,2.8,3.3,3.1,2.7,3.0,3.2,2.9,3.1]
print(stats.ttest_1samp(res_time, 0))

# 7️⃣ Finance
returns = [11.5,12.8,13.0,10.9,12.5,11.8,12.2,13.1]
print(stats.ttest_1samp(returns, 0))

# 8️⃣ Manufacturing
defect_rate = [2.1,1.9,2.3,2.0,1.8,2.2]
print(stats.ttest_1samp(defect_rate, 0))

# 9️⃣ Health_Care
rec_days = [6,8,7,5,9,6,7,8]
print(stats.ttest_1samp(rec_days, 0))

# 🔟 Marketing
ratings = [4.3, 4.6, 4.4 ,4.7, 4.2, 4.5, 4.6, 4.3, 4.8, 4.4]
print(stats.ttest_1samp(ratings, 0))

# 1️⃣1️⃣ Energy
solar_output = [295,310,305,290,315,300,285]
print(stats.ttest_1samp(solar_output, 0))

# 1️2️⃣ Psychology
iq_scores = [98,102,105,95,100,99,101,97,103]
print(stats.ttest_1samp(iq_scores, 0))
