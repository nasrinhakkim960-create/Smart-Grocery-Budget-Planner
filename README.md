# Smart Grocery Budget Planner

A machine learning-based web application that estimates monthly grocery expenses based on household details, previous grocery spending, shopping habits, and other contextual factors.

The application also provides a recommended grocery budget by adding a 10% planning buffer to the estimated expense.
## Features

- Estimates monthly grocery expenses using machine learning
- Uses household and spending-related information as input
- Considers previous grocery expense, family size, income, and shopping habits
- Accounts for contextual factors such as festival months, guest arrival, price hikes, and month
- Calculates grocery spending as a percentage of monthly income
- Provides a recommended grocery budget with a 10% planning buffer
- Simple and responsive web interface
## Technology Stack

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- Linear Regression
- One-Hot Encoding
- Pandas
- NumPy

### Web Application
- Flask
- HTML
- CSS
- Jinja2

### Model Persistence
- Joblib

### Development Tools
- Visual Studio Code
## Machine Learning Model

The project uses Linear Regression to estimate monthly grocery expenses.

### Input Features

- Monthly Income
- Family Size
- Number of Children
- Previous Grocery Expense
- Month
- Festival
- Food Preference
- Guest Arrival
- Price Hike
- Shopping Frequency

### Target

- Grocery Expense

Categorical features are converted into numerical representations using One-Hot Encoding. The preprocessing and Linear Regression model are combined into a single Scikit-learn Pipeline so that the same preprocessing is automatically applied during prediction.
### Model Evaluation

The model was evaluated using a held-out test set containing 20% of the dataset.

| Metric | Result |
|---|---:|
| R² Score | 0.9896 |
| MAE | 374.43 |
| RMSE | 454.93 |

The evaluation results indicate that the model performs well on the test data used during development. Since the dataset is synthetic, these results should not be interpreted as real-world prediction accuracy.
## Project Structure

```text
Smart_grocery_planner/
│
├── data/
│   └── data.csv
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── app.py
├── generate_dataset.py
├── model_training.py
├── grocery_model.pkl
├── requirements.txt
├── .gitignore
└── README.md
```
## How It Works
1. The user enters household, spending, and shopping-related information.
2. Flask collects the submitted information.
3. The input is converted into a Pandas DataFrame.
4. The saved machine learning pipeline applies the required preprocessing.
5. The Linear Regression model estimates the monthly grocery expense.
6. The application calculates grocery spending as a percentage of monthly income.
7. A recommended grocery budget is calculated by adding a 10% planning buffer.
8. The results are displayed on a dedicated result page.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd Smart_grocery_planner
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

#### Windows

```powershell
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python app.py
```

The application will start on the local Flask development server.

Open the displayed local URL in a web browser to use the application.

---

## 9. Example Usage

## Example Usage

A user can provide details such as:

- Monthly income: ₹50,000
- Family size: 4
- Number of children: 1
- Previous grocery expense: ₹12,000
- Month: January
- Festival month: No
- Food preference: Vegetarian
- Guest arrival: No
- Price hike: No
- Shopping frequency: Monthly

The application processes these inputs and provides:

- Estimated monthly grocery expense
- Grocery spending as a percentage of income
- Recommended grocery budget with a 10% planning buffer
## Dataset

The project uses a synthetic dataset containing household, spending, shopping, and contextual information.

The dataset contains 500 records and 11 columns, including the target variable `Grocery_Expense`.

The dataset was created specifically for developing and demonstrating the machine learning model. Therefore, the model's evaluation results should not be interpreted as representing real-world grocery spending accuracy.
## Limitations

- The dataset used in this project is synthetic and may not represent real-world grocery spending patterns.
- The prediction depends on the quality and range of the input data.
- Linear Regression may not capture complex relationships between household factors and grocery expenses.
- The recommended budget uses a fixed 10% planning buffer and does not dynamically assess a user's financial situation.
- The application provides an estimate and should not be considered a financial decision-making tool.
## Future Improvements

- Use a larger real-world grocery spending dataset.
- Compare multiple machine learning algorithms to identify a better-performing model.
- Add grocery category-wise budget recommendations.
- Allow users to track actual spending over multiple months.
- Add visual charts to compare estimated and actual grocery expenses.
- Improve the budget recommendation using historical spending patterns.
## Project Screenshots

### Input Page

_Add screenshot of the grocery expense input form here._

### Prediction Result

_Add screenshot of the prediction result page here._
## Author

**Nasrin Hakkim**
