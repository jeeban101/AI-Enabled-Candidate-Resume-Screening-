# AI-Enabled Candidate Resume Screening

This repository contains the code for an AI-enabled candidate resume screening system. It allows you to automatically screen resumes based on job requirements and skills.

## Prerequisites

Before running the project, ensure you have the following dependencies installed:

- Python 3.7 or higher
- All the packages listed in the `requirements.txt` file.

## Getting Started

1. Clone this repository to your local machine.
2. Install the required dependencies by running the following command:
3. Update the necessary configurations in the `config.py` file.
4. Place your resume files in the designated folder.
5. Run the Flask application by executing the following command:
6. Open your web browser and navigate to `http://127.0.0.1:5000/` to access the application.

## Folder Structure

- `app.py`: Main Flask application file.
- `Resume_parser.py`: Resume parsing module.
- `templates/`: HTML templates for the web application.
- `static/`: Static files (CSS, images, etc.) for the web application.
- `Assignments-AI-20BIT0441/`: Folder containing assignment notebooks and datasets.

## Additional Resources

- [Demo Video](link-to-demo-video): Watch a demonstration of the project in action.
- [Project Report](will be here or link:-): Read the report documenting the assignments.
- [Drive Folder](https://drive.google.com/drive/folders/1Sxp0-cwl0nEDT5cbkbB3b8RUhwZSfi9h?usp=sharing): Access the assignments and datasets on Google Drive.

## Contributors

- Jeeban Bhagat (https://github.com/jeeban101/AI-Enabled-Candidate-Resume-Screening-)


## Requirements

- Python 3.x
- Flask
- Pyresparser
- Pandas
- NLTK
- scikit-learn

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/jeeban101/AI-Enabled-Candidate-Resume-Screening-
   1.Navigate to the project directory:
	cd AI-Enabled-Candidate-Resume-Screening-
   2.Install the required Python packages:
	pip install -r requirements.txt
Usage
1.Run the Flask web application:
	python app.py
The application will be accessible at http://127.0.0.1:5000/.(may differ by flask version)

2.Access the web application in your web browser and fill in the required information, including the job position and resume file.

3.Upon submission, the system will extract skills from the resume, compare them with the job requirements, and send an email notification to the candidate regarding the screening outcome.

if Error:
	OSError: [E053] Could not read config.cfg from .....\venv\lib\site-packages\pyresparser\config.cfg #46
		then,do the following:
-pip install nltk
-pip install spacy==2.3.5
-pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.1/en_core_web_sm-2.3.1.tar.gz
-pip install pyresparser
does the trick. Also try different spacy versions and models, because they produce different results. Haven't tested any further myself. Hope this helps :)

Assignments(https://drive.google.com/drive/folders/1Sxp0-cwl0nEDT5cbkbB3b8RUhwZSfi9h?usp=sharing)
The "Assignments-AI-20BIT0441" folder contains assignments in Jupyter Notebook format. Each assignment is a separate .ipynb file that demonstrates different concepts and techniques related to AI.

Additional Files
Report: The project report is available in the repository. It provides detailed information about the system architecture, algorithms used, and evaluation results.

Demo Video: A demo video showcasing the project functionality is available here.

Data Sets(for assignments)(Link:https://drive.google.com/drive/folders/1Sxp0-cwl0nEDT5cbkbB3b8RUhwZSfi9h?usp=sharing): The project utilizes specific data sets for training and evaluation purposes. These data sets can be accessed via the Google Drive link provided in the repository.

Contributing
Contributions to this project are welcome. If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

