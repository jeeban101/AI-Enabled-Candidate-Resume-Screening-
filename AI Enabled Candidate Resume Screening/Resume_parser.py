from pyresparser import ResumeParser
import smtplib

# SMTP initialization for Outlook
s = smtplib.SMTP('smtp.office365.com', 587)
s.starttls()
s.login("autoResumeResponse@outlook.com", "Masu6bhat@")

SUBJECT = "Interview Call"
python_skills = ["ml", "ai", "matplotlib", "seaborn",
                 "python", "regression", "algorithms",
                 "pandas", "data analysis", "keras",
                 "tensorflow", "artificial intelligence",
                 "data visualization", "opencv"]
java_skills = ["java", "object-oriented programming",
               "data structures", "algorithms",
               "spring framework", "hibernate",
               "SQL", "multithreading", "JavaFX",
               "RESTful API", "Maven", "JUnit", "JSP",
               "Servlets", "OOP"]
data_Scientist = ["Machine Learning (ML)", "Deep Learning (DL)",
                  "Data Mining", "Statistical Analysis",
                  "Data Visualization", "Natural Language Processing (NLP)",
                  "Big Data", "Predictive Modeling", "Feature Engineering",
                  "Regression Analysis", "Classification Algorithms",
                  "Clustering Algorithms", "Time Series Analysis",
                  "Dimensionality Reduction", "Ensemble Methods", "Neural Networks",
                  "Python for Data Science", "R Programming", "SQL", "Tableau",
                  "Apache Spark", "Hadoop"]


def extract_skills(filename):
    data = ResumeParser(filename).get_extracted_data()
    name = data['name']
    email = data['email']
    skills = data['skills']
    actual_skills = [i.lower() for i in skills]
    return name, email, actual_skills


def extract_education(filename):
    data = ResumeParser(filename).get_extracted_data()
    education = []
    if 'education' in data:
        education = data['education']
    return education


def extract_certificates(filename):
    data = ResumeParser(filename).get_extracted_data()
    certificates = []
    if 'certificate' in data:
        certificates = data['certificate']
    return certificates


def compare_skills(appliedJob, skills):
    skills_matched = []
    if appliedJob == "AI/ML Dev":
        for ele in skills:
            if ele in python_skills:
                skills_matched.append(ele)
    if appliedJob == "Java Dev":
        for ele in skills:
            if ele in java_skills:
                skills_matched.append(ele)
    if appliedJob == "Data Scientist":
        for ele in skills:
            if ele in data_Scientist:
                skills_matched.append(ele)
    return skills_matched


def send_email(email, name, is_rejected, appliedJob):
    if is_rejected:
        TEXT = f"Hello {name}, \n\nThanks for applying to the job post {appliedJob} . Your candidature is " \
               f"rejected.\n\n\n\nThanks and Regards,\n\nTalent Acquisition Team,\n\nSmartInternz by Smartbridge"
    else:
        TEXT = f"Hello {name}, \n\nThanks for applying to the job post {appliedJob}. Your skills match our " \
               f"requirements. Kindly let us know the available time for the initial round of " \
               f"interview.\n\n\n\nThanks and Regards,\n\nTalent Acquisition Team,\n\nSmartInternz by Smartbridge"
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    s.sendmail("autoResumeResponse@outlook.com", email, message)
    s.quit()
