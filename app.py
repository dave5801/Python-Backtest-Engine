from dash import Dash, html
from dashboard.layout import create_layout

app = Dash(__name__)
app.title = "Quant Strategy Dashboard"

app.layout = create_layout()

if __name__ == "__main__":
    app.run(debug=True)
