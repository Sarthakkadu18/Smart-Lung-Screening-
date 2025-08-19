Smart Lung Screening 🩺An intelligent web application that uses a deep learning model to classify lung CT scan images as potentially cancerous or non-cancerous. This project leverages transfer learning with the VGG16 architecture to provide a fast and accessible tool for preliminary analysis.<!-- It's highly recommended to add a screenshot of your app here -->FeaturesAI-Powered Classification: Utilizes a powerful Convolutional Neural Network (CNN) to analyze images.Interactive Web Interface: A clean, modern, and user-friendly interface for uploading images and viewing results.Confidence Score: Provides a probability score to indicate the model's confidence in its prediction.Fast & Accessible: Built with Flask, making it a lightweight and deployable web application.Tech StackBackend: Python, FlaskDeep Learning: TensorFlow, KerasImage Processing: Pillow, NumPyFrontend: HTML5, CSS3, JavaScriptProject Structuresmart-lung-screening/
│
├── flask_app/              # Contains the Flask web application
│   ├── static/
│   │   └── style.css
│   ├── templates/
│   │   └── index.html
│   ├── app.py
│   └── requirements.txt
│
└── model_training/         # Contains the model training notebook and final model
    ├── lung_cancer_model.h5
    └── Lung_Cancer_Detection_Training.ipynb
Setup and InstallationFollow these steps to get the project running on your local machine.PrerequisitesPython 3.8+pip and venv1. Clone the Repositorygit clone https://github.com/your-username/smart-lung-screening.git
cd smart-lung-screening
2. Prepare the Dataset & Train the ModelBefore running the app, you must train the model.Download an Image Dataset: Obtain a dataset of lung CT scans with 'cancerous' and 'non-cancerous' classifications (e.g., from Kaggle).Organize the Dataset: Create a dataset folder in the root directory and structure it as follows:dataset/
├── train/
│   ├── cancerous/
│   └── non_cancerous/
└── test/
    ├── cancerous/
    └── non_cancerous/
Run the Training Notebook:Install Jupyter Notebook: pip install notebookStart the server: jupyter notebookIn your browser, navigate to model_training/ and open Lung_Cancer_Detection_Training.ipynb.Run all cells to train the model. This will generate the lung_cancer_model.h5 file.3. Set Up the Flask AppNavigate to the app directory:cd flask_app
Create and activate a virtual environment:# Create the environment
python -m venv venv

# Activate it (Windows)
.\venv\Scripts\activate

# Activate it (macOS/Linux)
source venv/bin/activate
Install the required packages:pip install -r requirements.txt
UsageWith the virtual environment activated and the model trained, run the Flask application:python app.py
Open your web browser and navigate to http://127.0.0.1:5000 to use the application.⚠️ DisclaimerThis tool is for informational and educational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. The predictions made by this AI model should not be used to make medical decisions. Always consult a qualified healthcare professional with any questions you may have regarding a medical condition.
