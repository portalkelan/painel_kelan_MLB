"""
############ Alertas ##################

import dash_bootstrap_components as dbc
from dash import html

alerts = html.Div(
    [
        dbc.Alert("This is a primary alert", color="primary"),
        dbc.Alert("This is a secondary alert", color="secondary"),
        dbc.Alert("This is a success alert! Well done!", color="success"),
        dbc.Alert("This is a warning alert... be careful...", color="warning"),
        dbc.Alert("This is a danger alert. Scary!", color="danger"),
        dbc.Alert("This is an info alert. Good to know!", color="info"),
        dbc.Alert("This is a light alert", color="light"),
        dbc.Alert("This is a dark alert", color="dark"),
    ]
)

############ Distintivos - Notificasoes ##################

import dash_bootstrap_components as dbc

badge = dbc.Button(
    [
        "Notifications",
        dbc.Badge("4", color="light", text_color="primary", className="ms-1"),
    ],
    color="primary",
)


############ 2 ###################

import dash_bootstrap_components as dbc

badge = dbc.Button(
    [
        "Notifications",
        dbc.Badge(
            "99+",
            color="danger",
            pill=True,
            text_color="white",
            className="position-absolute top-0 start-100 translate-middle",
        ),
    ],
    color="primary",
    className="position-relative",
)

############ cartoes ##################
import dash_bootstrap_components as dbc
from dash import html

card = dbc.Card(
    [
        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
        dbc.CardBody(
            [
                html.H4("Card title", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and "
                    "make up the bulk of the card's content.",
                    className="card-text",
                ),
                dbc.Button("Go somewhere", color="primary"),
            ]
        ),
    ],
    style={"width": "18rem"},
)

######### 2 - Horizontal ###########

import dash_bootstrap_components as dbc
from dash import html

card = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.CardImg(
                        src="/static/images/portrait-placeholder.png",
                        className="img-fluid rounded-start",
                    ),
                    className="col-md-4",
                ),
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H4("Card title", className="card-title"),
                            html.P(
                                "This is a wider card with supporting text "
                                "below as a natural lead-in to additional "
                                "content. This content is a bit longer.",
                                className="card-text",
                            ),
                            html.Small(
                                "Last updated 3 mins ago",
                                className="card-text text-muted",
                            ),
                        ]
                    ),
                    className="col-md-8",
                ),
            ],
            className="g-0 d-flex align-items-center",
        )
    ],
    className="mb-3",
    style={"maxWidth": "540px"},
)

######### 3 - Fundo e cor ###########

import dash_bootstrap_components as dbc
from dash import html

card_content = [
    dbc.CardHeader("Card header"),
    dbc.CardBody(
        [
            html.H5("Card title", className="card-title"),
            html.P(
                "This is some card content that we'll reuse",
                className="card-text",
            ),
        ]
    ),
]

cards = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dbc.Card(card_content, color="primary", inverse=True)),
                dbc.Col(
                    dbc.Card(card_content, color="secondary", inverse=True)
                ),
                dbc.Col(dbc.Card(card_content, color="info", inverse=True)),
            ],
            className="mb-4",
        ),
        dbc.Row(
            [
                dbc.Col(dbc.Card(card_content, color="success", inverse=True)),
                dbc.Col(dbc.Card(card_content, color="warning", inverse=True)),
                dbc.Col(dbc.Card(card_content, color="danger", inverse=True)),
            ],
            className="mb-4",
        ),
        dbc.Row(
            [
                dbc.Col(dbc.Card(card_content, color="light")),
                dbc.Col(dbc.Card(card_content, color="dark", inverse=True)),
            ]
        ),
    ]
)






######### Carrossel ########
################ Use o componente Carrossel para criar uma apresentação de slides que percorre uma série de conteúdos. ###############

import dash_bootstrap_components as dbc

carousel = dbc.Carousel(
    items=[
        {"key": "1", "src": "/static/images/slide1.svg"},
        {"key": "2", "src": "/static/images/slide2.svg"},
        {"key": "3", "src": "/static/images/slide3.svg"},
    ],
    controls=False,
    indicators=False,
    interval=2000,
    ride="carousel",
)

######### Carrossel - comseta para mudar ########

import dash_bootstrap_components as dbc

carousel = dbc.Carousel(
    items=[
        {"key": "1", "src": "/static/images/slide1.svg"},
        {"key": "2", "src": "/static/images/slide2.svg"},
        {"key": "3", "src": "/static/images/slide3.svg"},
    ],
    controls=True,
    indicators=False,
)


############ Formulários ##################

import dash_bootstrap_components as dbc

form = dbc.Form(
    dbc.Row(
        [
            dbc.Label("Email", width="auto"),
            dbc.Col(
                dbc.Input(type="email", placeholder="Enter email"),
                className="me-3",
            ),
            dbc.Label("Password", width="auto"),
            dbc.Col(
                dbc.Input(type="password", placeholder="Enter password"),
                className="me-3",
            ),
            dbc.Col(dbc.Button("Submit", color="primary"), width="auto"),
        ],
        className="g-2",
    )
)



############ Barra de navegação ##################

import dash_bootstrap_components as dbc
from dash import Input, Output, State, html
from dash_bootstrap_components._components.Container import Container

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="search", placeholder="Search")),
        dbc.Col(
            dbc.Button(
                "Search", color="primary", className="ms-2", n_clicks=0
            ),
            width="auto",
        ),
    ],
    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("Navbar", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="https://plotly.com",
                style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                search_bar,
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
)


# add callback for toggling the collapse on small screens
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


############ Progresso ##################

import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

progress = html.Div(
    [
        dcc.Interval(id="progress-interval", n_intervals=0, interval=500),
        dbc.Progress(id="progress"),
    ]
)


@app.callback(
    [Output("progress", "value"), Output("progress", "label")],
    [Input("progress-interval", "n_intervals")],
)
def update_progress(n):
    # check progress of some background process, in this example we'll just
    # use n_intervals constrained to be in 0-100
    progress = min(n % 110, 100)
    # only add text after 5% progress to ensure text isn't squashed too much
    return progress, f"{progress} %" if progress >= 5 else ""


    
############ girador - spinner ############

import time

import dash_bootstrap_components as dbc
from dash import Input, Output, html

loading_spinner = html.Div(
    [
        dbc.Button("Load", id="loading-button", n_clicks=0),
        dbc.Spinner(html.Div(id="loading-output")),
    ]
)


@app.callback(
    Output("loading-output", "children"), [Input("loading-button", "n_clicks")]
)
def load_output(n):
    if n:
        time.sleep(1)
        return f"Output loaded {n} times"
    return "Output not reloaded yet"


############ Temas gratuitos para Bootstrap ############




############ girador - spinner ############

Cerulearn, Cyborg, Darkly, Lux, Minty, Pulse, Quartz, Slate, Superhero, Vapor, Zephyr


############ girador - spinner ############







"""