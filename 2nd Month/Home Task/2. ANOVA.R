# 1. Teaching Methods (Education)**




library(ggplot2)

method = factor(rep(c("Lecture", "Online", "Blended"), each=5))
scores <- c(60,65,70,62,68, 72,75,78,74,77, 80,82,85,83,88)

df_blue <-  data.frame(method, scores)

ggplot(df_blue, aes(method, scores)) + geom_boxplot(fill="skyblue")

anova_model <- aov(scores ~ method, data=df_blue)
anova_model <- lm(scores ~ method, data=df_blue)

summary(anova_model)

# 2. Machine Types Manufacturing)**


machine <- factor(rep(c("A", "B", "C"), each=6))
output <-  c(20,77,19,23,21,20, 25,22,26,28,29,30, 18,17,19,16,20,18)

df_orange <-  data.frame(machine, output)

ggplot(df_orange, aes(machine, output)) +  geom_boxplot(fil="orange")

summary(aov(output~machine, data=df_orange))
summary(lm(output~machine, data=df_orange))






# 3. Marketing Campaigns**


campaign <- factor(rep(c("Social","TV", "Email"), each=5))
sales  <- c(200,210,190,205,198, 250,260,255,270,265, 180, 175, 190,185,178)

df_green <- data.frame(campaign, sales)

ggplot(df_green, aes(campaign, sales)) + geom_boxplot(fill="green")


summary(aov(sales ~ campaign, data=df_green))
summary(lm(sales ~ campaign, data=df_green))



# 4. Student Groups**



group <- factor (rep(c("A", "B", "C"), each=4))
marks <- c(55,60,58,62, 65,68,70,66, 75,78,80,77)


df_purple <-  data.frame(group, marks)
ggplot(df_purple, aes(group, marks)) + geom_boxplot(fill="purple")

summary (aov(marks ~ group, data = df_purple))
summary (lm(marks ~ group, data = df_purple))



#5. Drug Effectivness

drug <- factor(rep(c("Drug1","Drug2","Drug3"),each=5)) 
recovery <- c(5,6,7,5,6,8,9,7,8,9,6,7,6,7,8)

df_red <- data.frame(drug,recovery)
ggplot(df_red , aes(drug,recovery)) + geom_boxplot(fill="red")

summary(aov(recovery~drug,data=df_red))
summary(lm(recovery~drug,data=df_red))







#6. Store Location

location <- factor(rep(c("Urban","Suburban","Rural"),each=5)) 
revenue <- c(500,520,510,530,515, 450,460,470,455,465, 400, 420, 410,405,415)

df_cyan <- data.frame(location,revenue)
ggplot(df_cyan , aes(loation,revenue)) + geom_boxplot(fill="cyan")

summary(aov(revenue~location,data=df_cyan))
summary(lm(revenue~location,data=df_cyan))



