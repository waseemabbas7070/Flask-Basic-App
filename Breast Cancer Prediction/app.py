from flask import Flask, request, render_template
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# ---------------------
# Train the model once
# ---------------------
df = pd.read_csv("breast cancer.csv")
df['diagnosis'] = df['diagnosis'].map({'M': 1, 'B': 0})

features = ['radius_mean', 'texture_mean', 'perimeter_mean', 'smoothness_mean', 'compactness_mean']
X = df[features]
y = df['diagnosis']

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier(n_estimators=500, n_jobs=-1)
model.fit(x_train, y_train)

# ---------------------
# Route
# ---------------------
@app.route("/", methods=['GET', 'POST'])
def cancerPrediction():
    if request.method == 'POST':
        data = [[
            float(request.form['query1']),
            float(request.form['query2']),
            float(request.form['query3']),
            float(request.form['query4']),
            float(request.form['query5'])
        ]]

        new_df = pd.DataFrame(data, columns=features)
        single = model.predict(new_df)[0]
        proba = model.predict_proba(new_df)[:, 1][0]

        if single == 1:
            output = "The Patient is Diagnosed with Breast Cancer"
            output1 = f"Confidence: {proba*100:.2f}%"
        else:
            output = "The Patient is not Diagnosed with Breast Cancer"
            output1 = ""

        return render_template(
            'home.html',
            output=output,
            output1=output1,
            inputQuery1=request.form['query1'],
            inputQuery2=request.form['query2'],
            inputQuery3=request.form['query3'],
            inputQuery4=request.form['query4'],
            inputQuery5=request.form['query5']
        )

    return render_template('home.html')

# ---------------------
# Run App
# ---------------------
if __name__ == "__main__":
    app.run(debug=True)
