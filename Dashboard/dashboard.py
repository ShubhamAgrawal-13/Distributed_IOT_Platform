import io
import random
from flask import Flask, Response, request
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_svg import FigureCanvasSVG


from matplotlib.figure import Figure


app = Flask(__name__)


@app.route("/")
def index():
    """ Returns html with the img tag for your plot.
    """
    
    
    # in a real app you probably want to use a flask template.
    return f"""
    <h1>Dashboard</h1>
    
    
    <h3>Ploting the temp data</h3>
    <img src="/image.svg"
         alt="random points as svg"
         height="200"
    >
    """
    # from flask import render_template
    # return render_template("yourtemplate.html", num_x_points=num_x_points)




@app.route("/image.svg")
def plot_svg(num_x_points=50):
    """ renders the plot on the fly.
    """
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    with open('temperature.txt') as f:
            lines = f.read().splitlines()
    print(lines)
    axis.plot(lines)

    output = io.BytesIO()
    FigureCanvasSVG(fig).print_svg(output)
    return Response(output.getvalue(), mimetype="image/svg+xml")


if __name__ == "__main__":
    import webbrowser

    webbrowser.open("http://127.0.0.1:5000/")
    app.run(debug=True)