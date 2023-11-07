#importing streamlit library
import streamlit as st
from PIL import Image
import pickle


model1= pickle.load(open('C:\\Users\\GEETHU\\finalcapstone\\loanstatus.pkl', 'rb'))
model2=pickle.load(open('C:\\Users\\GEETHU\\finalcapstone\\CUSTOMER_SEGMENTATION1.pkl','rb'))
model3=pickle.load(open('C:\\Users\\GEETHU\\finalcapstone\\CUSTOMER_SEGMENTATION2.pkl','rb'))
def run():
    img1 = Image.open('C:\\Users\\GEETHU\\Downloads\\bank image1.jfif')
    img1 = img1.resize((156,145))
    st.image(img1,use_column_width=False)
    st.title("Customer Credibility Prediction for Bank Loan Approval System")

    ## Account No
    account_no = st.text_input('Account number')

    ## Full Name
    fn = st.text_input('Full Name')

    ## For gender
    gen_display = ('Female','Male')
    gen_options = list(range(len(gen_display)))
    gen = st.selectbox("Gender",gen_options, format_func=lambda x: gen_display[x])

    ## For Marital Status
    mar_display = ('No','Yes')
    mar_options = list(range(len(mar_display)))
    mar = st.selectbox("Marital Status", mar_options, format_func=lambda x: mar_display[x])

    ## No of dependets
    dep_display = ('No','One','Two','More than Two')
    dep_options = list(range(len(dep_display)))
    dep = st.selectbox("Dependents",  dep_options, format_func=lambda x: dep_display[x])

    ## For edu
    edu_display = ('Not Graduate','Graduate')
    edu_options = list(range(len(edu_display)))
    edu = st.selectbox("Education",edu_options, format_func=lambda x: edu_display[x])

    ## For emp status
    emp_display = ('Job','Business')
    emp_options = list(range(len(emp_display)))
    emp = st.selectbox("Employment Status",emp_options, format_func=lambda x: emp_display[x])

    ## For Credit Score
    cred_display = ('0','1')
    cred_options = list(range(len(cred_display)))
    cred = st.selectbox("Credit Score",cred_options, format_func=lambda x: cred_display[x])    

    ## For Property status
    prop_display = ('Rural','Semi-Urban','Urban')
    prop_options = list(range(len(prop_display)))
    prop = st.selectbox("Property Area",prop_options, format_func=lambda x: prop_display[x])

   

    ## Applicant Monthly Income
    mon_income = st.number_input("Applicant's Monthly Income($)",value=0)

    ## Co-Applicant Monthly Income
    co_mon_income = st.number_input("Co-Applicant's Monthly Income($)",value=0)

    ## Loan AMount
    loan_amt = st.number_input("Loan Amount",value=0)

    ## loan duration
    dur_display = ['2 Month','6 Month','8 Month','1 Year','16 Month']
    dur_options = range(len(dur_display))
    dur = st.selectbox("Loan Duration",dur_options, format_func=lambda x: dur_display[x])

    if st.button("Submit"):
        duration = 0
        if dur == 0:
            duration = 60
        if dur == 1:
            duration = 180
        if dur == 2:
            duration = 240
        if dur == 3:
            duration = 360
        if dur == 4:
            duration = 480
        features = [[gen, mar, dep, edu, emp, mon_income, co_mon_income, loan_amt, duration, cred, prop]]
        print(features)
        prediction = model1.predict(features)
        
        if prediction == 1 and cred==1:
            st.success(
                "Hello: " + fn +" || "
                "Account number: "+account_no +' || '
                'Congratulations!! you are eligible to get the loan from Bank'
            )
            cluster = model2.predict([[mon_income,cred,loan_amt]])
            print(f'The Applicant belongs to approved cluster {cluster[0]}')
            if cluster[0] == 0:
               print('The Applicant is having less chance of defaulting\n')
               st.success("The Applicant is with low monthly income and good credit history")  
            elif cluster[0]==1:
               print('The Applicant is having no chance of defaulting\n')
               st.success("The Applicant is with high monthly income and good credit history")
            elif cluster[0]==2:
               print('The Applicant is having no chance of defaulting\n')
               st.success("The Applicant is with medium monthly income and good credit history")
            
        
        else:
            st.error(
                "Hello: " + fn +" || "
                "Account number: "+account_no +' || '
                'According to our eligibility criteria, you are not eligible to get the loan from Bank'
            )
            cluster = model3.predict([[mon_income,cred,loan_amt]])
            print(f'The Applicant belongs to unapproved cluster {cluster[0]} ')
            if cluster[0] == 0:
               print('The Applicant is having high chance of defaulting\n')
               st.error("The Applicant is with low monthly income with poor credit history")
            elif cluster[0]==1:
               print('The Applicant is having high chance of defaulting\n')
               st.error("The Applicant is with high monthly income with poor credit history")
            elif cluster[0]==2:
               print('The Applicant is having high chance of defaulting\n')
               st.error("The Applicant is with medium monthly income with poor  credit history")
             

run()