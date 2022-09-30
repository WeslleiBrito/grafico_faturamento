from dash import Dash, dcc, html
from datetime import date

app = Dash(__name__)

app.layout = html.Div([
    dcc.DatePickerRange(
        id='date-picker-range',
        start_date=date(date.today().year, date.today().month, date.today().day),
        end_date_placeholder_text='Select a date!'
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)