import plotly.graph_objects as go

class Plotter:
    def __init__(self, list):
        self.list = list

    def displayBubblePlot(self, title, xtitle, ytitle):
            lst = self.list
            x_val = [x[0] for x in lst]
            y_val = [x[1] for x in lst]
            nbSample = len(x_val)
            colorList = y_val
            sizeList = list(reversed(range(1, nbSample + 1)))

            fig = go.Figure(data=[go.Scatter(
            x=x_val,
            y=y_val,
            mode='markers',
            marker=dict(
                color=colorList,
                size=sizeList,
                sizemode='area',
                sizeref=2.* max(sizeList)/(130.**2),
                showscale=True
                )
            )])
            fig.update_layout(
            title=title,
            xaxis=dict(
                title=xtitle,
                ),
            yaxis=dict(
                title=ytitle,
                gridcolor='white',
                gridwidth=2,
            ),
                paper_bgcolor='rgb(243, 243, 243)',
                plot_bgcolor='rgb(243, 243, 243)',
            )
            fig.show()