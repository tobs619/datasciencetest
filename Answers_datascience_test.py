#Q1
from numpy import genfromtxt
user_data = genfromtxt('testSamples.csv', delimiter=',')
control_group = 0
test_group = 0
total_outcome = len(user_data)

for data in user_data :
    if data[1] == 0 :
        control_group += 1
        
    elif data[1] == 1:
        test_group += 1



def approx_prob(testgroup, controlgroup, totaloutcome) :
    prob_control_group = controlgroup/totaloutcome
    prob_test_group = testgroup/totaloutcome
    total_prob = prob_control_group * prob_test_group
    print(round(total_prob,4))
    print(prob_control_group)

approx_prob(test_group,control_group,total_outcome)
    
    
    
    
    #Q2

import pandas as pd 
data1 = pd.read_csv('testSamples.csv')
data2 = pd.read_csv('transData.csv')
result = []
df = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

df.reset_index()

no_callin_user = 0
no_webform_user = 0
no_callin_rebill = 0
no_webform_rebill = 0

for  index, user in df.iterrows():
    if user[1] == 1:
        no_callin_user += 1
        for index, trans in df2.iterrows():
            if trans[2] == "REBILL" and trans[1] == user[0] :
   
                no_callin_rebill += 1
    elif user[1] == 0:
        no_webform_user += 1
        for index, trans in df2.iterrows():
            if trans[2] == "REBILL" and trans[1] == user[0] :
                
                no_webform_rebill += 1

print(no_callin_rebill)
print(no_webform_rebill)
print(no_callin_user)
print(no_webform_user)

def compare_prob (cal_rebill,cal_user,form_rebill,from_user) :
    if cal_rebill/cal_user > form_rebill/from_user  :
        print("Yes Call-in user are more likely to create a rebill")
    else:
        print("No Call-in user are not more likely to create a rebill")


compare_prob(no_callin_rebill,no_callin_user,no_webform_rebill,no_webform_user) 
                 
    
    #Yes Call in users are more likely to create an additional rebill
   
#Q3
    
    total_revenue = df['transaction_amount'].sum()
print (round(total_revenue,2))

df_revenue_callin = no_callin_user.groupby('sample_id')
revenue_callin = df_revenue_callin['transaction_amount'].sum()

mean_callin = revenue_callin.mean()
print(round(mean_callin,2))

df_revenue_webform = no_webform_user.groupby('sample_id')
revenue_webform = df_revenue_webform['transaction_amount'].sum()

mean_webform = revenue_webform.mean()
print(round(mean_webform,2))

#The revenue generated by the callin group is less than the revenue generated by the webform group.
#so users that call in wont most likely generate more revenues. 





#Q4



#The rate of chargeback of the webform group is higher than the rate of chargeback in the callin group,
#so it is unlikely that users who call back will produce higer chargeback rate. 




