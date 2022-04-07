# Uncomment this once if you need to install the packages on your system 

### DATA MANIPULATION ###
# install.packages("haven")                 # data import from spss
# install.packages("dplyr")                 # data manipulation
# install.packages("psych")                 # descriptives
# install.packages("stringr")               # string manipulation

### MODELING ###
# install.packages("lavaan")                # SEM modelling

### VISUALIZATION ###
# install.packages("tidySEM")               # plotting SEM models
# install.packages("corrplot")              # correlation/covariance plots


#install.packages("MVN")  




# Load the packages 

### DATA MANIPULATION ###
library("haven")        
library("dplyr")      
library("psych")
library('stringr')

### MODELING ###
library("lavaan")       

### VISUALIZATION ###
library("corrplot")     
library("tidySEM")
library("MVN")


#loading in our data..
full_df <- read.csv("/Users/steven/Documents/SEM/full_clean_df.csv")

#head(full_df, 10)

nrow(full_df)      # number of subjects , 119581
ncol(full_df)    #number of columns, 21
names(full_df)


#creating the subset for CFA
full_df_selected <- full_df %>% select(
  Inflight.wifi.service,  #edge case, prior and during..
  Departure.Arrival.time.convenient,
  Ease.of.Online.booking,
  Gate.location,
  Food.and.drink,
  Online.boarding, #not sure
  Seat.comfort,
  Inflight.entertainment,
  On.board.service,
  Leg.room.service, #not sure, is service but msotly comfort during flight..
  Baggage.handling,
  Checkin.service, #not sure, is service but also pre.. 
  Inflight.service, 
  Cleanliness
)

descriptive_airplane_csat <- as.data.frame(psych::describe(full_df_selected))
# and here I see the zeros are indeed gone :) //done with messy python script

descriptive_airplane_csat <- dplyr::select(descriptive_airplane_csat, 
                                           n,
                                           mean,
                                           sd,
                                           median,
                                           min,
                                           max,
                                           skew,
                                           kurtosis)
descriptive_airplane_csat



#variance covariance matrix of all items



# let's calculate the sample implied covariance matrix 
full_df_selected_cov <- cov(full_df_selected,          # data frame 
                            use = "pairwise.complete.obs" # remove NAs 
)


#full_df_selected_cov


#make it visual..

full_df_selected_cor <- cov2cor(full_df_selected_cov)
full_df_selected_cor

corrplot::corrplot(full_df_selected_cor,
                   is.corr = FALSE,       # whether is a correlation matrix 
                   method = "circle",     # magnitude of covariances as circles 
                   type = "upper",        # remove the bottom of the covariance matrix
                   addCoef.col = "black"  # add to the plot the coefficients
)


ks_Departure.Arrival.time.convenient <- ks.test(full_df$Departure.Arrival.time.convenient, "pnorm", mean=mean(full_df$Departure.Arrival.time.convenient, na.rm=T), sd=sd(full_df$Departure.Arrival.time.convenient, na.rm=T))
ks_Ease.of.Online.booking<- ks.test(full_df$Ease.of.Online.booking, "pnorm", mean=mean(full_df$Ease.of.Online.booking, na.rm=T), sd=sd(full_df$Ease.of.Online.booking, na.rm=T))
ks_Gate.location <- ks.test(full_df$Gate.location, "pnorm", mean=mean(full_df$Gate.location, na.rm=T), sd=sd(full_df$Gate.location, na.rm=T))
ks_Food.and.drink<- ks.test(full_df$Food.and.drink, "pnorm", mean=mean(full_df$Food.and.drink, na.rm=T), sd=sd(full_df$Food.and.drink, na.rm=T))
ks_Online.boarding<- ks.test(full_df$Online.boarding, "pnorm", mean=mean(full_df$Online.boarding, na.rm=T), sd=sd(full_df$Online.boarding, na.rm=T))
ks_Seat.comfort<- ks.test(full_df$Seat.comfort, "pnorm", mean=mean(full_df$Seat.comfort, na.rm=T), sd=sd(full_df$Seat.comfort, na.rm=T))
ks_Inflight.entertainment<- ks.test(full_df$Inflight.entertainment, "pnorm", mean=mean(full_df$Inflight.entertainment, na.rm=T), sd=sd(full_df$Inflight.entertainment, na.rm=T))
ks_On.board.service<- ks.test(full_df$On.board.service, "pnorm", mean=mean(full_df$On.board.service, na.rm=T), sd=sd(full_df$On.board.service, na.rm=T))
ks_Baggage.handling<- ks.test(full_df$Baggage.handling, "pnorm", mean=mean(full_df$Baggage.handling, na.rm=T), sd=sd(full_df$Baggage.handling, na.rm=T))
ks_Inflight.service<- ks.test(full_df$Inflight.service, "pnorm", mean=mean(full_df$Inflight.service, na.rm=T), sd=sd(full_df$Inflight.service, na.rm=T))
ks_Cleanliness<- ks.test(full_df$Cleanliness, "pnorm", mean=mean(full_df$Cleanliness, na.rm=T), sd=sd(full_df$Cleanliness, na.rm=T))


data.frame(Variables= c("Departure.Arrival.time.convenient", "Ease.of.Online.booking","Gate.location", "Food.and.drink", "Online.boarding", "Seat.comfort", "Inflight.entertainment", "On.board.service", "Baggage.handling", "Inflight.service", "Cleanliness"),
           D = round(c(ks_Departure.Arrival.time.convenient$statistic, ks_Ease.of.Online.booking$statistic, ks_Gate.location$statistic, ks_Food.and.drink$statistic, ks_Online.boarding$statistic, ks_Seat.comfort$statistic, ks_Inflight.entertainment$statistic, ks_On.board.service$statistic, ks_Baggage.handling$statistic, ks_Inflight.service$statistic, ks_Cleanliness$statistic),2),
           "P-value" = c(ks_Departure.Arrival.time.convenient$p.value, ks_Ease.of.Online.booking$p.value, ks_Gate.location$p.value, ks_Food.and.drink$p.value, ks_Online.boarding$p.value, ks_Seat.comfort$p.value, ks_Inflight.entertainment$p.value, ks_On.board.service$p.value, ks_Baggage.handling$p.value, ks_Inflight.service$p.value, ks_Cleanliness$p.value)
)

mvn_test <- mvn(data = full_df_selected, # our data without NAs
                mvnTest = c("hz")    # type of normality test to perform
)

mvn_test$multivariateNormality



# here we go, 3 factor CFA usinf lavaaan


model_3factor_CFA <-'
## DuringFlightComfort ##
lf_DuringFlightComfort =~ 
  Food.and.drink +
  Seat.comfort +
  Inflight.entertainment +
  Cleanliness
## OverallService ## 
lf_F2Fservice =~ 
  On.board.service +
  Baggage.handling +
  Inflight.service 
##  PreflightEase ##
lf_PrePostFlight =~ 
  Departure.Arrival.time.convenient +
  Ease.of.Online.booking +
  Gate.location
'

fit_3f <- cfa(model_3factor_CFA,              # model formula
              data = full_df_selected,
              estimator = 'MLM' # data frame
)

summary(fit_3f, standardized=TRUE)




#plotting the SEM

# first, let's define our plot layout 
lay <- get_layout("lf_DuringFlightComfort", "", "", "", "lf_F2Fservice","", "", "", "lf_PrePostFlight", "",
                  "", "Food.and.drink", "Seat.comfort", "Inflight.entertainment", "Cleanliness", "On.board.service", "Baggage.handling", "Inflight.service", "Departure.Arrival.time.convenient", "Ease.of.Online.booking", "Gate.location", "", rows = 2)

# let's take a look at our plot layout.
lay


# let's plot our results
plot_3f <- graph_sem(model = fit_3f,      # model fit
                     layout = lay, # layout 
                     angle = 170          # adjust the arrows 
                     #label = "est_std",  # get standardized results (not rounded)
                     )   

plot_3f


lavInspect(fit_3f, "sampstat")

summary(fit_3f,            # fitted model 
        fit.measures = TRUE, # returns commonly used fit measures 
        standardized = TRUE  # indicates that we want standardized results
)

## Local fit measures: modification indices ##
mi <- inspect(fit_3f,"mi")
mi.sorted <- mi[order(-mi$mi),] # sort from high to low mi.sorted[1:5,] # only display some large MI values
mi.sorted[1:5] # only display some large MI values

# let's plot the modification indices 
plot(mi.sorted$mi[1:20]) # plot the MI values
abline(h=3.84) # add a horizontal reference line (chisq value for 1 df where p=0.05)

