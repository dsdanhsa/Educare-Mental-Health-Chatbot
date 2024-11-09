# Educare Mental Health Chatbot

Educare is an AI-powered chatbot designed to provide emotional support and assistance specifically for students struggling with depression. Its primary purpose is to help students access mental health resources, offer guidance, and provide empathetic support as they navigate the challenges of depression. With integrated language translation capabilities, Educare efficiently breaks down language barriers, making support accessible to a diverse student population.

## Key Features

- **Emotional Support**: Provides a compassionate, understanding presence for students in need.
- **Mental Health Resources**: Guides students to reliable mental health resources and information tailored to managing depression.
- **Language Translation**: Overcomes language barriers, enabling multilingual support to reach students from different backgrounds.
- **Privacy Focused**: Ensures confidentiality and respects user privacy to create a safe space for students.

## Why Educare?

Educare’s specialized focus on supporting students with depression has the potential to make a real difference in academic environments. It can serve as a valuable tool across:

- **Educational Institutions**: Supports students by providing resources and emotional guidance directly through a familiar interface.
- **Student Support Services**: Complements counseling services by offering immediate and accessible support around the clock.
- **Inclusive Mental Health Support**: Bridges linguistic and cultural gaps, fostering an inclusive environment for students worldwide.

Educare ensures that all students have access to help and support whenever they need it, fostering a more supportive and understanding educational community.

# How to run it?
The following instructions were tested on the Windows and Linux with Python 3.11
To get started with Educare:

## Getting Started

1. **Clone the repository**:
    ```bash
    git clone https://github.com/dsdanhsa/Educare-Mental-Health-Chatbot.git
    ```
    cd EduCare
2. **Install requirements**:
    ```
    pip install  -r requirements.txt
    ```
3. **Create and activate virtual environment**:
    ```
    python -m venv venv
    ```
    on Linux system
    ```
    source venv/bin/activate
    ```
    on Windows system
    ```
    .\venv\Scripts\activate.bat
    ```
4. **Update path**:
    ```
    go to file folder copy path of each file
    bash into chatbot/app.py
    ```
5. **Set up the Django project**:
- **Make database migrations**:
    ```
    python manage.py migrate
    ```
6. **Run the Django development server**:
    ```
    python manage.py runserver
    ```
6. **Access the application**
Open your browser and go to http://127.0.0.1:8000 to view and use the chatbot.