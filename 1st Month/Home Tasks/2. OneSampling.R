# 1️⃣ Education


entrance_score <- c(72,74,76,70,73,75,71,69,77,74)

print(t.test(entrance_score,mu=75))


# 2️ Buisness

monthly_sales <- c(48000,51000,49500,50500,49000,52000,50000,48500)
print(t.test(monthly_sales,mu=50000))


# 3️⃣ Medical


bp <- c(118,122,119,121,117,123,120,116,124)
print(t.test(monthly_sales,mu=120))

# 4️⃣ Industrial

fill_weight <- c(9.8,10.1,9.9,10.2,9.7,10.0,10.3,9.6,10.1,9.8)
print(t.test(monthly_sales,mu=10))


# 5️⃣ Agriculture


wheat_yeild <- c(3.8,4.1,4.3,3.9,4.0,4.2,3.7)
print(t.test(wheat_yeild,mu=4))



# 6️⃣ IT

res_time <- c(2.9,3.1,3.0,3.2,2.8,3.3,3.1,2.7,3.0,3.2,2.9,3.1)
print(t.test(res_time,mu=3))



# 7️⃣ Finance

returns <- c(11.5,12.8,13.0,10.9,12.5,11.8,12.2,13.1)
print(t.test(returns,mu=12))



# 8️⃣ Manufacturing

defect_rate <- c(2.1,1.9,2.3,2.0,1.8,2.2)
print(t.test(defect_rate,mu=2))



# 9️⃣ Health_Care

rec_days <- c(6,8,7,5,9,6,7,8)
print(t.test(rec_days,mu=7))



# 🔟 Marketing

ratings <- c(4.3, 4.6, 4.4 ,4.7, 4.2, 4.5, 4.6, 4.3, 4.8, 4.4)
print(t.test(ratings,mu=4.5))



# 1️⃣1️⃣ Energy

solar_output <- c(295,310,305,290,315,300,285)
print(t.test(solar_output,mu=300))


# 1️2️⃣ Psychology

iq_scores <- c(98,102,105,95,100,99,101,97,103)
print(t.test(iq_scores,mu=100))
