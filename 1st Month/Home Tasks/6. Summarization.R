# --------------| Creating DataFrame |--------------

df <- data.frame(
  weekday = rep(c("Mon","Tues","Wed","Thurs"),each=5),
  Quarter = paste0("Q",rep(1:4,each=5)),
  delay = c(9.9, 5.4, 8.8, 6.9, 49,9.7, 79, 5, 8.3, 11.1, 10.2, 9.3, 12.2, 10.2,9.2, 9.7, 12.2,8.1,7.9,5.6)
)

library(dplyr)

# --------------| Grouping |--------------

df %>% 
  group_by(weekday) %>% 
  summarise(SD=sd(delay),maxDelay=max(delay),minDelay=min(delay))





# --------------| Creating DataFrame |--------------
  
  df1 <- data.frame(
    Quarter = paste0("Q",rep(1:4,each=4)),
    week = rep(c("weekday","weekend"),each=2,times=4),
    direction = rep(c("Inbound","Outbound"),times=8),
    delay = c(10.8, 9.7, 15.5, 10.4, 11.8, 3.9, 5.5, 3.3, 10.6,8.8,6.6, 5.2, 9.1, 7.3, 5.3,4.4)
  )

library(dplyr)

# --------------| Grouping |--------------

df1 %>% 
  group_by(Quarter,week) %>% 
  summarise(SD=sd(delay),maxDelay=max(delay),minDelay=min(delay))
  
  
  