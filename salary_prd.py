import streamlit as st
import joblib

# Load the pre-trained model
model = joblib.load("salary_prd.pkl")

# Streamlit app title
st.title(" 💼 Employee Salary Prediction 🏆")
st.image("salary prd_3.jpeg", width=600)
# Streamlit app description
st.markdown("""
    <style>
    .description {
        font-family: 'Arial', sans-serif;
        color: #6A5ACD; /* Slate Blue */
        font-size: 20px;
        text-align: center;
        background-color: #F0F8FF; /* Light background */
        border-radius: 15px;
        padding: 20px;
        margin: 10px;
        box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.2);
    }
    .highlight {
        color: #FF4500; /* OrangeRed for highlights */
        font-weight: bold;
    }
    </style>
    
    <div class="description">
        <h3>🚀 Welcome to the <span class="highlight">Employee Salary Prediction App</span> 🚀</h3>
        <p>This application predicts the salary of an employee based on various factors such as:</p>
        <ul>
            <li><span class="highlight">Age</span>: Your current age.</li>
            <li><span class="highlight">Gender</span>: Male or Female.</li>
            <li><span class="highlight">Education Level</span>: Choose between Bachelor's, Master's, or PhD.</li>
            <li><span class="highlight">Job Title</span>: Select the appropriate job title from the list.</li>
            <li><span class="highlight">Years of Experience</span>: Your work experience in years.</li>
        </ul>
        <p>The prediction is based on a <span class="highlight">machine learning model</span> trained on real-world salary data.</p>
    </div>
""", unsafe_allow_html=True)

# Inputs from the user
Age = st.number_input("Please enter your age:", min_value=20, step=1)
Gender = st.selectbox("Gender", ["Male", "Female"])
Education_Level = st.selectbox("Education Qualification", ["Bachelor's", "Master's", "PhD"])
Job_Title = st.selectbox("Select Job Title", [
    'Senior Business Analyst', 'Operations Analyst', 'Technical Writer', 'Director of Marketing', 
    'Product Marketing Manager', 'Human Resources Director', 'Senior Financial Manager', 'Principal Scientist', 
    'Director of Product Management', 'Senior Marketing Director', 'Senior Training Specialist', 
    'Junior Operations Coordinator', 'Senior Quality Assurance Analyst', 'Junior Advertising Coordinator', 
    'Junior Account Manager', 'Customer Service Rep', 'Sales Representative', 'Senior Product Marketing Manager', 
    'Software Manager', 'Junior Accountant', 'Web Developer', 'Junior Sales Representative', 'VP of Operations', 
    'Supply Chain Manager', 'Senior Product Manager', 'Project Engineer', 'Technical Recruiter', 'Financial Analyst', 
    'Junior Web Designer', 'Marketing Analyst', 'Sales Director', 'Junior Customer Support Specialist', 
    'Senior HR Specialist', 'Senior HR Generalist', 'Senior Financial Analyst', 'Director of HR', 
    'Senior Research Scientist', 'Senior UX Designer', 'Account Manager', 'Principal Engineer', 'Customer Service Manager', 
    'Senior Software Developer', 'Customer Success Rep', 'Social Media Specialist', 'Marketing Specialist', 
    'Senior Product Designer', 'Recruiter', 'Marketing Coordinator', 'Product Designer', 'Senior Software Architect', 
    'Junior Product Manager', 'Junior Research Scientist', 'Senior Engineer', 'Senior Project Coordinator', 
    'Sales Operations Manager', 'Junior Marketing Specialist', 'Graphic Designer', 'Junior Data Scientist', 
    'Data Entry Clerk', 'Help Desk Analyst', 'Senior Account Manager', 'Senior IT Consultant', 'Network Engineer', 
    'Senior Financial Advisor', 'Director of Sales and Marketing', 'Senior Operations Coordinator', 
    'Senior Sales Manager', 'Junior Business Development Associate', 'CEO', 'VP of Finance', 'Marketing Manager', 
    'Financial Advisor', 'Senior Marketing Manager', 'Senior Marketing Specialist', 'Senior Human Resources Specialist', 
    'Junior Social Media Specialist', 'Senior Data Engineer', 'Content Marketing Manager', 'Senior Account Executive', 
    'Junior Project Manager', 'Research Director', 'Junior Marketing Coordinator', 'Junior Marketing Manager', 
    'Office Manager', 'Senior Software Engineer', 'Director', 'Senior Consultant', 'Senior Data Analyst', 'UX Researcher', 
    'Junior Business Operations Analyst', 'Senior Scientist', 'Software Developer', 'Financial Manager', 'IT Manager', 
    'Business Intelligence Analyst', 'Senior Manager', 'Junior Marketing Analyst', 'Director of Human Capital', 
    'Junior Designer', 'Junior Financial Analyst', 'Junior Recruiter', 'Senior IT Project Manager', 'Creative Director', 
    'Research Scientist', 'Junior Software Developer', 'Junior HR Coordinator', 'Senior Business Development Manager', 
    'Junior Operations Manager', 'Business Development Manager', 'Software Engineer', 'Junior HR Generalist', 
    'Junior Software Engineer', 'Training Specialist', 'Director of Engineering', 'Customer Service Representative', 
    'Director of Sales', 'Data Scientist', 'Digital Marketing Manager', 'Senior Researcher', 'Director of Operations', 
    'Senior Data Scientist', 'Junior Operations Analyst', 'Sales Associate', 'Public Relations Manager', 'IT Support', 
    'Senior Project Manager', 'Technical Support Specialist', 'Accountant', 'HR Generalist', 'Copywriter', 
    'Senior Human Resources Coordinator', 'Senior Accountant', 'Director of Business Development', 'Business Analyst', 
    'Junior Financial Advisor', 'Digital Content Producer', 'Product Manager', 'Sales Executive', 'Event Coordinator', 
    'Junior Web Developer', 'Strategy Consultant', 'Operations Director', 'Social Media Manager', 'Senior Marketing Analyst', 
    'Junior Developer', 'Senior Operations Analyst', 'Junior Copywriter', 'IT Support Specialist', 'Senior Sales Representative', 
    'Senior Marketing Coordinator', 'Senior Human Resources Manager', 'Junior UX Designer', 'Director of Human Resources', 
    'Chief Data Officer', 'Customer Success Manager', 'Senior IT Support Specialist', 'Junior Business Analyst', 
    'Senior Product Development Manager', 'Supply Chain Analyst', 'Junior Data Analyst', 'Chief Technology Officer', 
    'HR Manager', 'Project Manager', 'UX Designer', 'Sales Manager', 'Director of Finance', 'Senior Operations Manager', 
    'Senior HR Manager', 'Operations Manager', 'Administrative Assistant', 'Senior Graphic Designer', 'Data Analyst', 
    'Junior Social Media Manager', 'Software Project Manager'
])

Years_of_Experience = st.number_input("Enter your Experience (in years):", min_value=0, step=1)

# Map the gender input to a numeric value
Gender_value = 0 if Gender == "Male" else 1

# Map the education level to a numeric value
Education_Level_value = {"Bachelor's": 0, "Master's": 1, "PhD": 2}[Education_Level]

# Map the job title to its corresponding numeric value
Job_Title_value = {
    'Senior Business Analyst': 0, 'Operations Analyst': 1, 'Technical Writer': 2, 'Director of Marketing': 3,
    'Product Marketing Manager': 4, 'Human Resources Director': 5, 'Senior Financial Manager': 6, 'Principal Scientist': 7,
    'Director of Product Management': 8, 'Senior Marketing Director': 9, 'Senior Training Specialist': 10,
    'Junior Operations Coordinator': 11, 'Senior Quality Assurance Analyst': 12, 'Junior Advertising Coordinator': 13,
    'Junior Account Manager': 14, 'Customer Service Rep': 15, 'Sales Representative': 16, 'Senior Product Marketing Manager': 17,
    'Software Manager': 18, 'Junior Accountant': 19, 'Web Developer': 20, 'Junior Sales Representative': 21,
    'VP of Operations': 22, 'Supply Chain Manager': 23, 'Senior Product Manager': 24, 'Project Engineer': 25,
    'Technical Recruiter': 26, 'Financial Analyst': 27, 'Junior Web Designer': 28, 'Marketing Analyst': 29,
    'Sales Director': 30, 'Junior Customer Support Specialist': 31, 'Senior HR Specialist': 32, 'Senior HR Generalist': 33,
    'Senior Financial Analyst': 34, 'Director of HR': 35, 'Senior Research Scientist': 36, 'Senior UX Designer': 37,
    'Account Manager': 38, 'Principal Engineer': 39, 'Customer Service Manager': 40, 'Senior Software Developer': 41,
    'Customer Success Rep': 42, 'Social Media Specialist': 43, 'Marketing Specialist': 44, 'Senior Product Designer': 45,
    'Recruiter': 46, 'Marketing Coordinator': 47, 'Product Designer': 48, 'Senior Software Architect': 49,
    'Junior Product Manager': 50, 'Junior Research Scientist': 51, 'Senior Engineer': 52, 'Senior Project Coordinator': 53,
    'Sales Operations Manager': 54, 'Junior Marketing Specialist': 55, 'Graphic Designer': 56, 'Junior Data Scientist': 57,
    'Data Entry Clerk': 58, 'Help Desk Analyst': 59, 'Senior Account Manager': 60, 'Senior IT Consultant': 61,
    'Network Engineer': 62, 'Senior Financial Advisor': 63, 'Director of Sales and Marketing': 64, 'Senior Operations Coordinator': 65,
    'Senior Sales Manager': 66, 'Junior Business Development Associate': 67, 'CEO': 68, 'VP of Finance': 69,
    'Marketing Manager': 70, 'Financial Advisor': 71, 'Senior Marketing Manager': 72, 'Senior Marketing Specialist': 73,
    'Senior Human Resources Specialist': 74, 'Junior Social Media Specialist': 75, 'Senior Data Engineer': 76,
    'Content Marketing Manager': 77, 'Senior Account Executive': 78, 'Junior Project Manager': 79, 'Research Director': 80,
    'Junior Marketing Coordinator': 81, 'Junior Marketing Manager': 82, 'Office Manager': 83, 'Senior Software Engineer': 84,
    'Director': 85, 'Senior Consultant': 86, 'Senior Data Analyst': 87, 'UX Researcher': 88, 'Junior Business Operations Analyst': 89,
    'Senior Scientist': 90, 'Software Developer': 91, 'Financial Manager': 92, 'IT Manager': 93, 'Business Intelligence Analyst': 94,
    'Senior Manager': 95, 'Junior Marketing Analyst': 96, 'Director of Human Capital': 97, 'Junior Designer': 98,
    'Junior Financial Analyst': 99, 'Junior Recruiter': 100, 'Senior IT Project Manager': 101, 'Creative Director': 102,
    'Research Scientist': 103, 'Junior Software Developer': 104, 'Junior HR Coordinator': 105, 'Senior Business Development Manager': 106,
    'Junior Operations Manager': 107, 'Business Development Manager': 108, 'Software Engineer': 109, 'Junior HR Generalist': 110,
    'Junior Software Engineer': 111, 'Training Specialist': 112, 'Director of Engineering': 113, 'Customer Service Representative': 114,
    'Director of Sales': 115, 'Data Scientist': 116, 'Digital Marketing Manager': 117, 'Senior Researcher': 118, 'Director of Operations': 119,
    'Senior Data Scientist': 120, 'Junior Operations Analyst': 121, 'Sales Associate': 122, 'Public Relations Manager': 123, 'IT Support': 124,
    'Senior Project Manager': 125, 'Technical Support Specialist': 126, 'Accountant': 127, 'HR Generalist': 128, 'Copywriter': 129,
    'Senior Human Resources Coordinator': 130, 'Senior Accountant': 131, 'Director of Business Development': 132, 'Business Analyst': 133,
    'Junior Financial Advisor': 134, 'Digital Content Producer': 135, 'Product Manager': 136, 'Sales Executive': 137, 'Event Coordinator': 138,
    'Junior Web Developer': 139, 'Strategy Consultant': 140, 'Operations Director': 141, 'Social Media Manager': 142, 'Senior Marketing Analyst': 143,
    'Junior Developer': 144, 'Senior Operations Analyst': 145, 'Junior Copywriter': 146, 'IT Support Specialist': 147, 'Senior Sales Representative': 148,
    'Senior Marketing Coordinator': 149, 'Senior Human Resources Manager': 150, 'Junior UX Designer': 151, 'Director of Human Resources': 152,
    'Chief Data Officer': 153, 'Customer Success Manager': 154, 'Senior IT Support Specialist': 155, 'Junior Business Analyst': 156,
    'Senior Product Development Manager': 157, 'Supply Chain Analyst': 158, 'Junior Data Analyst': 159, 'Chief Technology Officer': 160,
    'HR Manager': 161, 'Project Manager': 162, 'UX Designer': 163, 'Sales Manager': 164, 'Director of Finance': 165, 'Senior Operations Manager': 166,
    'Senior HR Manager': 167, 'Operations Manager': 168, 'Administrative Assistant': 169, 'Senior Graphic Designer': 170, 'Data Analyst': 171,
    'Junior Social Media Manager': 172, 'Software Project Manager': 173
}[Job_Title]

# Prediction
# Prediction output
if st.button("Predict Salary"):
    try:
        # Perform prediction using the trained model
        result = model.predict([[Age, Years_of_Experience, Gender_value, Education_Level_value, Job_Title_value]])
        
        # Display the result with custom styling
        st.markdown(f"""
            <h2 style="color: #4CAF50; text-align: center;">
                Predicted Estimated Salary: ₹ <span style="font-weight: bold; font-size: 36px;">{result[0]:,.2f}</span>
            </h2>
        """, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error: {e}")


