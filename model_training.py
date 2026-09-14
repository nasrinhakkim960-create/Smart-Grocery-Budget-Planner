import pandas as pd
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from sklearn.pipeline import Pipeline
#Read Dataset
data=pd.read_csv("data/data.csv")
categorical_columns = [
    "Month",
    "Festival",
    "Food_Preference",
    "Guest_Arrival",
    "Price_Hike",
    "Shopping_Frequency"
]

#Features and Target
X=data.drop("Grocery_Expense",axis=1)
y=data["Grocery_Expense"]
#Create the preprocessor
preprocessor= ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_columns
        )
    ],
    remainder="passthrough"
)

#Create the complete pipeline
model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("regressor", LinearRegression())
    ]
)
#Split Dataset
X_train, X_test, y_train, y_test =train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
#Train Model
model.fit(X_train, y_train)
# Make predictions
y_pred = model.predict(X_test)
# Evaluate Model
r2= r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred) ** 0.5
print("R² Score:", r2)
print("MAE:", mae)
print("RMSE:", rmse)
#Save Model
joblib.dump(model,"grocery_model.pkl")
print("Model saved successfully!")