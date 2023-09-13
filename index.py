import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import dash_bootstrap_templates
from dash_bootstrap_templates import load_figure_template
import plotly.graph_objs as go
import plotly.express as px
import plotly.graph_objects as go
from dash_bootstrap_templates import ThemeSwitchAIO

#from app import *

template_theme1 = "quartz"
template_theme2 = "zephyr"
url_theme1 = dbc.themes.QUARTZ
url_theme2 = dbc.themes.ZEPHYR

#load_figure_template("minty")
#app = dash.Dash(external_stylesheets=[dbc.themes.QUARTZ])
search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="search", placeholder="Search")),
        dbc.Col(
           ThemeSwitchAIO(aio_id="theme", themes=[url_theme1, url_theme2]),
            width="auto",
        ),
    ],
    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)
PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

app = dash.Dash(__name__)
server = app.server

n1 = "001"
#==================== Layout ====================
app.layout = html.Div([
                dbc.Navbar(
                    # Use row and col to control vertical alignment of logo / brand
                    dbc.Row(
                        [
                            dbc.Col([
                                dbc.Row(html.Img(src=PLOTLY_LOGO, height="50px", style={'align':'left'})),
                            ]),
                            dbc.Col([
                                dbc.Row(dbc.NavbarBrand("Dashboard para análise"), style={'height':'20%'}),
                            ]),
                            dbc.Col(
                                ThemeSwitchAIO(aio_id="theme", themes=[url_theme1, url_theme2]),
                                    width="auto",
                            ),
                        ],
                    ),
                    
                    style={"textDecoration": "none"},
                    color="dark",
                    dark=True,
                ),
                
            ],style={'align':'left','overflowY': 'scroll', 'height': '300px', 'border': '1px solid black'}
        )

                
        #html.Img(src=app.get_asset_url('logo_kelan2.png'),style={"display": "flex", "justify-content": "center","lenght":"50%", "width":"70%"}),
        #ThemeSwitchAIO(aio_id="theme", themes=[url_theme1, url_theme2]),
        #html.Hr(),

                    

#, style={"display": "flex", "justify-content": "top"}
#============ Call Backs ===============
# DropDawn






#================ Run Server ==============
if __name__=="__main__":
    app.run_server(debug=True, port=8050, host='172.20.20.33')

