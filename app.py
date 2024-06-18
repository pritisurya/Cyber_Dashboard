#app.py

from dash import Dash, dcc, html
import pandas as pd

# Load the data
file_path = 'C:\\Users\\priti\\PycharmProjects\\pythonProject\\cyber_dash\\venv\\Cyber Security Breaches.csv'
data = pd.read_csv(file_path)

# Clean the date column
data["Date_of_Breach"] = data["Date_of_Breach"].str.strip().str.extract(r'(\d{1,2}/\d{1,2}/\d{4})', expand=False)

# Convert the cleaned date column to datetime
data["Date_of_Breach"] = pd.to_datetime(data["Date_of_Breach"], format="%m/%d/%Y", errors='coerce')

# Drop rows with invalid dates
data = data.dropna(subset=["Date_of_Breach"])

# Sort the data by date
data.sort_values("Date_of_Breach", inplace=True)

# Initialize the Dash app
app = Dash(__name__)

# Define the layout of the app
app.layout = html.Div(
    children=[
        html.P(
            children="Analyze the behavior of Cyber Breaches "
                     "and the number of breaches occurred in the surroundings",
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date_of_Breach"],
                        "y": data["Type_of_Breach"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Average breach occurred"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date_of_Breach"],
                        "y": data["Individuals_Affected"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Security Breach"},
            },
        ),
    ]
)

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)

