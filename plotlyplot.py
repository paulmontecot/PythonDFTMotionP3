import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

def plotdatabeautyful(dfinal) :

   # fig = make_subplots(rows=2, cols=3)

    fig =  px.scatter(dfinal, x='DC', y='Deviation', color='target')#,
        #row=1, col=1


    # fig.add_trace(
    #     px.scatter(dfinal, x=dfinal['DC'], y=dfinal['energy'],color='target'),
    #     row=1, col=2
    # )
    #
    # fig.add_trace(
    #     px.scatter(dfinal, x=dfinal['DC'], y=dfinal['entropyDFT'],color='target'),
    #     row=1, col=3
    # )
    #
    # fig.add_trace(
    #     px.scatter(dfinal, x='energy', y=dfinal['entropyDFT'], color='target'),
    #     row=2, col=1
    # )
    #
    # fig.add_trace(
    #     px.scatter(dfinal, x=dfinal['energy'], y=dfinal['Deviation'], color='target'),
    #     row=2, col=2
    # )
    #
    # fig.add_trace(
    #     px.scatter(dfinal, x=dfinal['entropy'], y=dfinal['Deviation'], color='target'),
    #     row=2, col=3
    # )

    fig.update_layout(height=600, width=800, title_text="Side By Side Subplots")
    fig.show()

