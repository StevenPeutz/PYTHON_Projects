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
  Cleanliness,
  Type.of.Travel  #only for MIMIC
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




# here we go, 3 factor CFA usinf lavaaan


model_3factor_CFA_2ndOrderMIMIC <-'
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
## SECOND ORDER HERE ##
Second_lf_CSat =~
  lf_DuringFlightComfort +
  lf_F2Fservice +
  lf_PrePostFlight
Second_lf_CSat ~ Type.of.Travel
'



fit_3f_2nd_MIMIC <- cfa(model_3factor_CFA_2ndOrderMIMIC,              # model formula
              data = full_df_selected,  # data frame
              estimator = "MLM" #tried WLS as well. Most likely problem with multiclllinearity (heywood case)
)

summary(fit_3f_2nd_MIMIC, standardized=TRUE)

inspect(fit_3f_2nd_MIMIC, "r2")


#plotting the SEM

# first, let's define our plot layout 
lay <- get_layout("", "", "", "Type.of.Travel", "", "", "", "", "", "", "", 
                  "", "", "", "", "Second_lf_CSat", "", "", "", "", "", "",
                  "lf_DuringFlightComfort", "", "", "", "lf_F2Fservice","", "", "", "lf_PrePostFlight", "",
                  "", "Food.and.drink", "Seat.comfort", "Inflight.entertainment", "Cleanliness", "On.board.service", "Baggage.handling", "Inflight.service", "Departure.Arrival.time.convenient", "Ease.of.Online.booking", "Gate.location", "", rows = 4)

# let's take a look at our plot layout.
lay


# let's plot our results
plot_3f_2nd_MIMIC <- graph_sem(model = fit_3f_2nd_MIMIC,      # model fit
                     layout = lay, # layout 
                     angle = 170          # adjust the arrows 
                     #label = "est_std",  # get standardized results (not rounded)
                     )   

plot_3f_2nd_MIMIC


lavInspect(fit_3f_2nd_MIMIC, "sampstat")

summary(fit_3f_2nd_MIMIC,            # fitted model 
        fit.measures = TRUE, # returns commonly used fit measures 
        standardized = TRUE  # indicates that we want standardized results
)





## Local fit measures: modification indices ##
mi <- inspect(fit_3f_2nd_MIMIC,"mi")
mi.sorted <- mi[order(-mi$mi),] # sort from high to low mi.sorted[1:5,] # only display some large MI values
mi.sorted[1:5] # only display some large MI values

# let's plot the modification indices 
plot(mi.sorted$mi[1:20]) # plot the MI values
abline(h=3.84) # add a horizontal reference line (chisq value for 1 df where p=0.05)


