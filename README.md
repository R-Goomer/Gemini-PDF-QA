# Gemini Pro PDF Question Answering App

This Streamlit web application utilizes the Gemini Pro model to answer questions based on PDF documents uploaded by the user.

## Features

- Allows users to upload multiple PDF files.
- Processes the text from the PDF files and stores them in a vector store for efficient querying.
- Provides a chat interface where users can ask questions related to the content of the PDF files.
- Utilizes the Gemini Pro model for generating responses to user questions.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/gemini-pro-pdf-qa-app.git
    ```

2. Navigate into the project directory:

    ```bash
    cd gemini-pro-pdf-qa-app
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. Access the app in your web browser at `http://localhost:8501`.

3. Upload one or more PDF files using the file uploader.

4. Ask questions related to the content of the PDF files in the text input field.

5. Click the "Submit and Process" button to process the uploaded PDF files and receive answers to your questions.

## Configuration

- You need to set up a Google API key and provide it as an environment variable named `GOOGLE_API_KEY` in order to use the Gemini Pro model.

## Dependencies

- Streamlit
- PyPDF2
- langchain
- google.generativeai
- dotenv

## Credits

This project utilizes the following technologies and libraries:

- [Streamlit](https://streamlit.io/)
- [PyPDF2](https://pythonhosted.org/PyPDF2/)
- [LangChain](https://github.com/ConsenSys/langchain)
- [Google Generative AI](https://github.com/google/generativeai)
- [dotenv](https://github.com/theskumar/python-dotenv)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize the README file according to your project's specific details and requirements.
