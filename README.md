## Gmail Spam Detection with Streamlit

This repository provides a user-friendly web application built with Streamlit to predict whether an email is spam or not. It leverages a pre-trained machine learning model for classification.

### Features

* **Intuitive Interface:** Enter your email text in a designated area and receive a prediction with a single click.
* **Machine Learning Powered:** The app utilizes a pre-trained model trained on labeled email data to identify spam characteristics.
* **Streamlit Integration:** Streamlit enables a visually appealing and interactive user experience.
* **Customizable (Optional):** With programming knowledge, you can modify the app's appearance and functionalities.

### Requirements

* **Python 3.7 or Later:** The programming language used to build the app.
* **Streamlit:** A Python library for creating web applications. You can install it using `pip install streamlit`.
* **joblib:** A Python library for saving and loading machine learning models. Install with `pip install joblib`.
* **scikit-learn (if training a model):** A Python library for machine learning algorithms. Install with `pip install scikit-learn`.
* **NumPy (if training a model):** A Python library for numerical computations needed during model training. Install with `pip install numpy`.

**Installing Required Libraries:**

Open a terminal or command prompt and run the following command:

```bash
pip install streamlit joblib scikit-learn numpy
```

### Usage

1. **Clone the Repository:**

   Use Git to clone this repository to your local machine:

   ```bash
   git clone https://github.com/Shreesh-Sree/Email_spam_detection.git
   ```

2. **Navigate to the Project Directory:**

   Use the `cd` command to change directories:

   ```bash
   cd Email_spam_detection
   ```

3. **Ensure Model Files Exist (Optional):**

   The app relies on pre-trained model files (`model.pkl` and `vectorizer.pkl`) located in the same directory as the `app.py` script. These files are crucial for the app to function. If you don't have them, you'll need to train your own model (see the "Model Training" section below).

4. **Run the Streamlit App:**

   In your terminal within the project directory, execute the following command to launch the app:

   ```bash
   streamlit run app.py
   ```

This will open the web app in your default web browser, usually at http://localhost:8501.

**Using the Web App:**

* You'll see a text area labeled "Enter Your Mail".
* Paste or type the email content you want to check for spam.
* Click the "Predict" button.
* The app will display the prediction below the button, indicating "Spam" (in red) or "Normal Mail" (in green).

### Model Training (Optional)

If you want to train a custom model using your own email data, here's a basic example using scikit-learn:

**Understanding the Code (Optional):**

* **pandas:** A Python library for data analysis (used for loading and manipulating the email dataset).
* **train_test_split:** A function from scikit-learn to split the data into training and testing sets for model evaluation.
* **TfidfVectorizer:** A scikit-learn tool to convert text data into numerical features suitable for machine learning algorithms.
* **LogisticRegression:** A machine learning algorithm used for classification tasks (spam vs. non-spam in this case).
* **joblib:** Used to save the trained model (`model.pkl`) and vectorizer (`vectorizer.pkl`) for future use by the app.

**Important Note:** This code snippet serves as a basic example. Training a robust model requires careful data preparation, feature engineering, and hyperparameter tuning for optimal performance.

### Contributing

We welcome contributions to this project! Feel free to fork the repository, make changes, and submit a pull request.

### License

This project is licensed under the MIT License. See the LICENSE file for details.
