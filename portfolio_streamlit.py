import streamlit as st 

output_a= st.sidebar.radio("Please Navigate To:",("About","Certifications",'Work Experience','Projects','Resume','Contact'))

if output_a == "About":
    st.header('About Me')
    st.markdown("<h1 style='text-align: center; color: blue;'>Kishore Chandra Uppadi</h1>", unsafe_allow_html=True)
    st.subheader('An aspiring Data Scientist pursuing data science training at Innomatics Research Labs, Hyderabad. I have completed my Mechanical Engineering in 2014.') 

    st.markdown("<h2 style='text-align: center; color: orange;'>Timeline</h1>", unsafe_allow_html=True)

    st.subheader('1993') 

    st.text('Born.')

    st.subheader('2008') 
    st.text('Completed 10th grade.')

    st.subheader('2014') 
    st.text('Graduated with B.Tech(Mechanical Engineering)-RGUKT-R.K.Valley Campus.')

    st.subheader('2018') 
    st.text('Graduated with M.Tech(Industrial Engineering)-Sri Venkateswara University-Tirupati.')

    st.subheader('2020') 
    st.text('Completed Teach For India Fellowship-Hyderabad.')

    st.subheader('2020_May - 2021_Sept') 
    st.text('Worked as a Curriculum Designer lead for Science 6th-10th grade')

    st.subheader('2021_Sept - Present') 
    st.text('Started Learning DATA SCIENCE at Innomatic Research Labs, Hyderabad.')

    
if output_a == "Certifications":
    st.header('Certifications')
    st.subheader('1. Machine Learning- Standford University(Coursera)')
    st.markdown("-by Andrew Ng")
    st.subheader('2. Google Sheets-Advanced (Udemy)')
    st.markdown("-by Intellezy Trainers")
    
    st.subheader('3. Customer Success: How to Reduce Churn and Increase Retention')
    st.markdown("-by Gustavo Escobar Henriquez")
    
    st.subheader('3. Python for Data Science and Machine Learning Bootcamp- (Udemy)')
    st.markdown("-by Jose Portilla")
    
    
    
if output_a == "Work Experience":
    st.header('Work Experience')
    st.subheader('1. Junior Research Fellow (IIT Guwahati)-Jan 2015 - Jun- 2015')
    st.markdown("1. Design and conduct experiments on endoscope design using shape memory alloys")
    st.markdown("2. Analyse the experimental data using MATLAB")
    st.markdown("3. Procure the materials and project documentation")
    
    st.subheader('2. Physics trainer for NDA coaching camp- Social Welfare Schools March 2018 - April 2018')
    st.markdown("1. Taught physics to students who prepare for National Defence Academy(NDA) exam.")
    
    st.subheader('3. Teaching Fellow- Teach For India, Hyderabad Jun 2018 to May 2020')
    st.markdown("1. Taught mathematics and science to 6-9 th grades.")
    st.markdown("2. Trained students on debating and won the first price in Hyderabad city level event.")
    st.markdown("3. Improved academic average of the class by 20%")
    st.markdown("4. Trained a group of 50 students on public speaking and anchoring")
    st.markdown("5. Helped an NGO with setting up a rural school in Kadapa District.")
    st.markdown("6. Traind a group of 6 students for LEGO league competetion focusing on problem solving skills.")
    
    st.subheader('5.Curriculum Designer -Science - Vedantu Innovations Pvt Ltd. 2020 May- 2021 Sept')
    st.markdown("1. Taught mathematics 6th and 7th grades.")
    st.markdown("2. Recruited and Trained Teachers on pedagogy")
    st.markdown("3. Created trackers and dashboards and participated in data analysis sessions for the multiple metrics of the programme.")
    st.markdown("4. Designed curriculum for CBSE/ICSE/Maha Rastra Boards")
    st.markdown('5. Handled operatinal aspects and cross functional coordination of the curriculum design team')
    
if output_a == "Projects":
    st.header('Projects')
    st.subheader('Note Pad Application')
    st.markdown("Note pad application that can ask the user the enter the input and store and presents on the screen.")
    st.markdown("The application is made using FLASK framework in python, HTML, CSS and Bootstrap")

    st.subheader('URL Shortner')
    st.markdown("Handling the large URLs while sharing with others and during advertisements is a cumbersome, url shortening allows us to use the shortened url and redirects it to the orignial page when entered in the browser.")
    st.markdown("The application is made using FLASK framework in python, HTML, CSS and Bootstrap")
    
    st.subheader('Web Scraping and EDA')
    st.markdown("Web scraping is a process of extracting the required information form the website. EDA defined as exploratory data analysis, in which the scraped data from the website is analysed by using statistical measurement techniques and the visualzation techniques and the usefull insights can be drawn from the data.")
    st.markdown("The project is done with the help of Python libraries like requests, BeautifulSoup, pandas, numpy, matplotlib and seaborn.")
    
    

if output_a == "Resume":
    st.header('Resume')
    st.image('resume.png',caption ='Kishore Chandra Uppadi')
    
if output_a == "Contact":
    st.header('Contact')
    st.subheader('Name: Kishore Chandra Uppadi')
    st.subheader('Email: kishore.rkv@gmail.com')
    st.subheader('Linkdin: https://www.linkedin.com/in/kishore-chandra-45110372/')
    st.subheader('Phone: 8500704191')
    


st.sidebar.header('About Me:')
st.sidebar.image('kishorephoto.jpg',caption ='Kishore Chandra Uppadi')
st.sidebar.subheader("Name: Kishore Chandra Uppadi")
st.sidebar.subheader('Email: kishore.rkv@gmail.com')
st.sidebar.subheader('Phone: 8500704191')
st.sidebar.markdown("**SKILLS:** Python, Data Analysis, Machine Learning, Problem Solving, Story Telling, Teaching, Training",unsafe_allow_html=True)
st.sidebar.markdown(":heavy_minus_sign:"*12)
st.sidebar.subheader("Hello!, Thanks for spending your time and viewing my profile.")









