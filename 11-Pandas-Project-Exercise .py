#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'><img src='../Pierian_Data_Logo.png'/></a>
# ___
# <center><em>Copyright by Pierian Data Inc.</em></center>
# <center><em>For more information, visit us at <a href='http://www.pieriandata.com'>www.pieriandata.com</a></em></center>

# # Pandas Project Exercise 
# 
# # The Data
# 
# This data set contains booking information for a city hotel and a resort hotel, and includes information such as when the booking was made, length of stay, the number of adults, children, and/or babies, and the number of available parking spaces, among other things.
# 
# All personally identifying information has been removed from the data.
# 
# Acknowledgements
# The data is originally from the article Hotel Booking Demand Datasets, written by Nuno Antonio, Ana Almeida, and Luis Nunes for Data in Brief, Volume 22, February 2019.
# 
# 
# ----------------------------
# 
# #### NOTE: Names, Emails, Phone Numbers, and Credit Card numbers in the data are synthetic and not real information from people. The hotel data is real from the publication listed above.
# 
# ## <div style="text-align: center">Data Column Reference</div>

# <table><thead><tr class="rowsep-1"><th scope="col"><strong>Variable</strong></th><th scope="col"><strong>Type</strong></th><th scope="col"><strong>Description</strong></th><th scope="col"><strong>Source/Engineering</strong></th></tr></thead><tbody><tr><th scope="row"><em>ADR</em></th><td>Numeric</td><td>Average Daily Rate as defined by <a name="bbib5" href="#bib5" class="workspace-trigger">[5]</a></td><td>BO, BL and TR / Calculated by dividing the sum of all lodging transactions by the total number of staying nights</td></tr><tr><th scope="row"><em>Adults</em></th><td>Integer</td><td>Number of adults</td><td>BO and BL</td></tr><tr><th scope="row"><em>Agent</em></th><td>Categorical</td><td>ID of the travel agency that made the booking<a name="btbl1fna" href="#tbl1fna" class="workspace-trigger"><sup>a</sup></a></td><td>BO and BL</td></tr><tr><th scope="row"><em>ArrivalDateDayOfMonth</em></th><td>Integer</td><td>Day of the month of the arrival date</td><td>BO and BL</td></tr><tr><th scope="row"><em>ArrivalDateMonth</em></th><td>Categorical</td><td>Month of arrival date with 12 categories: “January” to “December”</td><td>BO and BL</td></tr><tr><th scope="row"><em>ArrivalDateWeekNumber</em></th><td>Integer</td><td>Week number of the arrival date</td><td>BO and BL</td></tr><tr><th scope="row"><em>ArrivalDateYear</em></th><td>Integer</td><td>Year of arrival date</td><td>BO and BL</td></tr><tr><th scope="row"><em>AssignedRoomType</em></th><td>Categorical</td><td>Code for the type of room assigned to the booking. Sometimes the assigned room type differs from the reserved room type due to hotel operation reasons (e.g. overbooking) or by customer request. Code is presented instead of designation for anonymity reasons</td><td>BO and BL</td></tr><tr><th scope="row"><em>Babies</em></th><td>Integer</td><td>Number of babies</td><td>BO and BL</td></tr><tr><th scope="row"><em>BookingChanges</em></th><td>Integer</td><td>Number of changes/amendments made to the booking from the moment the booking was entered on the PMS until the moment of check-in or cancellation</td><td>BO and BL/Calculated by adding the number of unique iterations that change some of the booking attributes, namely: persons, arrival date, nights, reserved room type or meal</td></tr><tr><th scope="row"><em>Children</em></th><td>Integer</td><td>Number of children</td><td>BO and BL/Sum of both payable and non-payable children</td></tr><tr><th scope="row"><em>Company</em></th><td>Categorical</td><td>ID of the company/entity that made the booking or responsible for paying the booking. ID is presented instead of designation for anonymity reasons</td><td>BO and BL.</td></tr><tr><th scope="row"><em>Country</em></th><td>Categorical</td><td>Country of origin. Categories are represented in the ISO 3155–3:2013 format <a name="bbib6" href="#bib6" class="workspace-trigger">[6]</a></td><td>BO, BL and NT</td></tr><tr><th scope="row"><br></th><td><br></td><td><br></td><td><br></td></tr><tr><th scope="row" rowspan="5"><em>CustomerType</em></th><td rowspan="5">Categorical</td><td>Type of booking, assuming one of four categories:</td><td rowspan="5">BO and BL</td></tr><tr><td>Contract - when the booking has an allotment or other type of contract associated to it;</td></tr><tr><td>Group – when the booking is associated to a group;</td></tr><tr><td>Transient – when the booking is not part of a group or contract, and is not associated to other transient booking;</td></tr><tr><td>Transient-party – when the booking is transient, but is associated to at least other transient booking</td></tr><tr><th scope="row"><em>DaysInWaitingList</em></th><td>Integer</td><td>Number of days the booking was in the waiting list before it was confirmed to the customer</td><td>BO/Calculated by subtracting the date the booking was confirmed to the customer from the date the booking entered on the PMS</td></tr><tr><th scope="row"><br></th><td><br></td><td><br></td><td><br></td></tr><tr><th scope="row" rowspan="7"><em>DepositType</em></th><td rowspan="7">Categorical</td><td>Indication on if the customer made a deposit to guarantee the booking. This variable can assume three categories:</td><td rowspan="2">BO and TR/Value calculated based on the payments identified for the booking in the transaction (TR) table before the booking׳s arrival or cancellation date.</td></tr><tr><td rowspan="3">No Deposit – no deposit was made;</td></tr><tr><td>In case no payments were found the value is “No Deposit”.</td></tr><tr><td rowspan="2">If the payment was equal or exceeded the total cost of stay, the value is set as “Non Refund”.</td></tr><tr><td rowspan="2">Non Refund – a deposit was made in the value of the total stay cost;</td></tr><tr><td rowspan="2">Otherwise the value is set as “Refundable”</td></tr><tr><td>Refundable – a deposit was made with a value under the total cost of stay.</td></tr><tr><th scope="row"><em>DistributionChannel</em></th><td>Categorical</td><td>Booking distribution channel. The term “TA” means “Travel Agents” and “TO” means “Tour Operators”</td><td>BO, BL and DC</td></tr><tr><th scope="row"><em>IsCanceled</em></th><td>Categorical</td><td>Value indicating if the booking was canceled (1) or not (0)</td><td>BO</td></tr><tr><th scope="row"><em>IsRepeatedGuest</em></th><td>Categorical</td><td>Value indicating if the booking name was from a repeated guest (1) or not (0)</td><td>BO, BL and C/ Variable created by verifying if a profile was associated with the booking customer. If so, and if the customer profile creation date was prior to the creation date for the booking on the PMS database it was assumed the booking was from a repeated guest</td></tr><tr><th scope="row"><em>LeadTime</em></th><td>Integer</td><td>Number of days that elapsed between the entering date of the booking into the PMS and the arrival date</td><td>BO and BL/ Subtraction of the entering date from the arrival date</td></tr><tr><th scope="row"><em>MarketSegment</em></th><td>Categorical</td><td>Market segment designation. In categories, the term “TA” means “Travel Agents” and “TO” means “Tour Operators”</td><td>BO, BL and MS</td></tr><tr><th scope="row"><br></th><td><br></td><td><br></td><td><br></td></tr><tr><th scope="row" rowspan="5"><em>Meal</em></th><td rowspan="5">Categorical</td><td>Type of meal booked. Categories are presented in standard hospitality meal packages:</td><td rowspan="5">BO, BL and ML</td></tr><tr><td>Undefined/SC – no meal package;</td></tr><tr><td>BB – Bed &amp; Breakfast;</td></tr><tr><td>HB – Half board (breakfast and one other meal – usually dinner);</td></tr><tr><td>FB – Full board (breakfast, lunch and dinner)</td></tr><tr><th scope="row"><em>PreviousBookingsNotCanceled</em></th><td>Integer</td><td>Number of previous bookings not cancelled by the customer prior to the current booking</td><td>BO and BL / In case there was no customer profile associated with the booking, the value is set to 0. Otherwise, the value is the number of bookings with the same customer profile created before the current booking and not canceled.</td></tr><tr><th scope="row"><em>PreviousCancellations</em></th><td>Integer</td><td>Number of previous bookings that were cancelled by the customer prior to the current booking</td><td>BO and BL/ In case there was no customer profile associated with the booking, the value is set to 0. Otherwise, the value is the number of bookings with the same customer profile created before the current booking and canceled.</td></tr><tr><th scope="row"><em>RequiredCardParkingSpaces</em></th><td>Integer</td><td>Number of car parking spaces required by the customer</td><td>BO and BL</td></tr><tr><th scope="row"><br></th><td><br></td><td><br></td><td><br></td></tr><tr><th scope="row" rowspan="4"><em>ReservationStatus</em></th><td rowspan="4">Categorical</td><td>Reservation last status, assuming one of three categories:</td><td rowspan="4">BO</td></tr><tr><td>Canceled – booking was canceled by the customer;</td></tr><tr><td>Check-Out – customer has checked in but already departed;</td></tr><tr><td>No-Show – customer did not check-in and did inform the hotel of the reason why</td></tr><tr><th scope="row"><em>ReservationStatusDate</em></th><td>Date</td><td>Date at which the last status was set. This variable can be used in conjunction with the <em>ReservationStatus</em> to understand when was the booking canceled or when did the customer checked-out of the hotel</td><td>BO</td></tr><tr><th scope="row"><em>ReservedRoomType</em></th><td>Categorical</td><td>Code of room type reserved. Code is presented instead of designation for anonymity reasons</td><td>BO and BL</td></tr><tr><th scope="row"><em>StaysInWeekendNights</em></th><td>Integer</td><td>Number of weekend nights (Saturday or Sunday) the guest stayed or booked to stay at the hotel</td><td>BO and BL/ Calculated by counting the number of weekend nights from the total number of nights</td></tr><tr><th scope="row"><em>StaysInWeekNights</em></th><td>Integer</td><td>Number of week nights (Monday to Friday) the guest stayed or booked to stay at the hotel</td><td>BO and BL/Calculated by counting the number of week nights from the total number of nights</td></tr><tr><th scope="row"><em>TotalOfSpecialRequests</em></th><td>Integer</td><td>Number of special requests made by the customer (e.g. twin bed or high floor)</td><td>BO and BL/Sum of all special requests</td></tr></tbody></table>

# -----------

# # TASKS
# 
# **Complete the tasks shown in bold below. The expected output is shown in a cell below. Be careful not to run the cell above the expected output, as it will clear the expected output. Try your best to solve these in one line of pandas code (not every single question can be solved in one line, but many can be!) Refer to solutions notebook and video to view possible solutions. NOTE: Many tasks have multiple correct solution methods!**
# 
# -----
# ### TASK: Run the following code to read in the "hotel_booking_data.csv" file. Feel free to explore the file a bit before continuing with the rest of the exercise.

# In[1]:


import pandas as pd


# In[2]:


hotels = pd.read_csv("hotel_booking_data.csv")


# In[3]:


hotels.head()


# ---
# **TASK: How many rows are there?**

# In[ ]:


# CODE HERE
len(hotels)


# In[12]:





# **TASK: Is there any missing data? If so, which column has the most missing data?**

# In[14]:


# CODE HERE
hotels.isnull().sum()


# In[13]:





# In[16]:





# **TASK: Drop the "company" column from the dataset.**

# In[15]:


# CODE HERE
hotels.drop(["company"], axis=1)


# In[17]:





# **TASK: What are the top 5 most common country codes in the dataset?**

# In[168]:


# CODE HERE
hotels["country"].value_counts()[:5]


# In[ ]:





# **TASK: What is the name of the person who paid the highest ADR (average daily rate)? How much was their ADR?**

# In[173]:


# CODE HERE
hotels.sort_values("adr", ascending= False)[["adr","name"]].iloc[0]


# In[ ]:





# **TASK: The adr is the average daily rate for a person's stay at the hotel. What is the mean adr across all the hotel stays in the dataset?**

# In[174]:


# CODE HERE
round(hotels["adr"].mean(),2)


# In[50]:





# **TASK: What is the average (mean) number of nights for a stay across the entire data set? Feel free to round this to 2 decimal points.**

# In[176]:


# CODE HERE
hotels["total_stay_nights"] = hotels["stays_in_weekend_nights"].mean() + hotels["stays_in_week_nights"].mean() 
round(hotels["total_stay_nights"],2)        
 


# In[44]:





# **TASK: What is the average total cost for a stay in the dataset? Not *average daily cost*, but *total* stay cost. (You will need to calculate total cost your self by using ADR and week day and weeknight stays). Feel free to round this to 2 decimal points.**

# In[178]:


# CODE HERE
hotels["total_cost"] = hotels["total_stay_nights"] * hotels["adr"]
round(hotels["total_cost"].mean(),2)


# In[43]:





# **TASK: What are the names and emails of people who made exactly 5 "Special Requests"?**

# In[179]:


# CODE HERE
# filt = (hotels["total_of_special_requests"] == 5)
# hotels.loc[filt,["name","email"]]

hotels[hotels["total_of_special_requests"] == 5][["name","email"]]


# In[56]:





# **TASK: What percentage of hotel stays were classified as "repeat guests"? (Do not base this off the name of the person, but instead of the is_repeated_guest column)**

# In[184]:


#CODE HERE


repeat =  hotels["is_repeated_guest"].sum()/len(hotels)*100
round(repeat,2)


# In[67]:





# **TASK: What are the top 5 most common last name in the dataset? Bonus: Can you figure this out in one line of pandas code? (For simplicity treat the a title such as MD as a last name, for example Caroline Conley MD can be said to have the last name MD)**

# In[190]:


#CODE HERE
hotels["name"].apply(lambda name: name.split()[-1]).value_counts()


# In[70]:





# **TASK: What are the names of the people who had booked the most number children and babies for their stay? (Don't worry if they canceled, only consider number of people reported at the time of their reservation)**

# In[204]:


#CODE HERE


hotels["total_kids"] = hotels["babies"] + hotels["children"]
hotels.sort_values("total_kids",ascending = False)[["name","total_kids"]][:5]


# In[ ]:





# **TASK: What are the top 3 most common area code in the phone numbers? (Area code is first 3 digits)**

# In[218]:


#CODE HERE
hotels["phone-number"].apply(lambda num: num.split("-")[0]).value_counts().head(3)


# In[89]:





# **TASK: How many arrivals took place between the 1st and the 15th of the month (inclusive of 1 and 15) ? Bonus: Can you do this in one line of pandas code?**

# In[219]:


#CODE HERE
hotels["arrival_date_day_of_month"].apply(lambda day: day in range(1,16)).sum()


# In[95]:





# 
# **HARD BONUS TASK: Create a table for counts for each day of the week that people arrived. (E.g. 5000 arrivals were on a Monday, 3000 were on a Tuesday, etc..)**

# In[105]:


# CODE HERE


# In[115]:





# ---
# 
# ---
