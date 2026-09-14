import pandas as pd
from flask import Flask, render_template, request
import joblib
model=joblib.load("grocery_model.pkl")
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        # Your input collection
        income = int(request.form["Monthly_Income"])
        family_size = int(request.form["Family_Size"])
        children = int(request.form["Children"])
        previous_expense = int(request.form["Previous_Expense"])

        month = request.form["Month"]
        festival = request.form["Festival"]
        food_preference = request.form["Food_Preference"]
        guest_arrival = request.form["Guest_Arrival"]
        price_hike = request.form["Price_Hike"]
        shopping_frequency = request.form["Shopping_Frequency"]
        # Create input
        input_data = pd.DataFrame([{
            "Monthly_Income": income,
            "Family_Size": family_size,
            "Children": children,
            "Previous_Expense": previous_expense,
            "Month": month,
            "Festival": festival,
            "Food_Preference": food_preference,
            "Guest_Arrival": guest_arrival,
            "Price_Hike": price_hike,
            "Shopping_Frequency": shopping_frequency
        }])

        # Prediction
        prediction = model.predict(input_data)[0]

        if income >0:
            grocery_percentage=(prediction/ income)*100
        else:
            grocery_percentage=0
        buffer = prediction * 0.10
        recommended_budget = prediction + buffer
        # recommended_budget = prediction * 1.10
        print("Grocery spending percentage:",grocery_percentage)
        print("Predicted Grocery Expense:", prediction)
        return render_template(
        "result.html",
        prediction=prediction,
        grocery_percentage=grocery_percentage,
        recommended_budget=recommended_budget
        )
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)