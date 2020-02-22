#Preliminaries
rm(list=ls())
library("utils")
library("tidyverse")
library('tibble')

#Getting the data
gender_data <- as_tibble(read.csv("Gender_StatsData.csv"))
teenager_fr <- filter(gender_data, Indicator.Code == "SP.ADO.TFRT")

mean(teenager_fr$X1960, na.rm = TRUE)
sd(teenager_fr$X1960, na.rm = TRUE)

mean(teenager_fr$X2000, na.rm = TRUE)
sd(teenager_fr$X2000, na.rm = TRUE)

byincomelevel <- filter(teenager_fr,Country.Code%in%c("LIC","MIC","HIC", "WLD"))

plotdata_bygroupyear <- gather(byincomelevel,Year,FertilityRate,X1960:X2015) %>%
  select(Year, Country.Name, Country.Code, FertilityRate)

plotdata_byyear<-select(plotdata_bygroupyear, Country.Code, Year, FertilityRate) %>%
  spread(  Country.Code  ,  FertilityRate  )

# plotdata_bygroupyear %>%
#   spread(  Country.Code  ,  FertilityRate  )

plotdata_bygroupyear <- mutate(plotdata_bygroupyear, Year=as.numeric(str_replace(Year,"X","")))

ggplot(plotdata_bygroupyear, aes(x=  Year  ,y=  FertilityRate  , group=  Country.Code, color=Country.Code  )) + geom_line() + labs(title='Fertility Rate by Country-Income-Level over Time')