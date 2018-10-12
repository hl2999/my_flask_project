from app import app
from flask import render_template, flash
from app.forms import InputForm, PlotForm, EnergyPlotForm
import pandas as pd





@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Hang'}
    posts = [
        {   'title' : 'POST 1',
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {   'title' : 'POST 2',
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',user=user,posts=posts)


@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    form = InputForm()

    if form.validate_on_submit(): # need to insert the CSRF field in the HTML form
        flash("you have succesfully calculated")
        a = form.input_a_number.data
        b = a + 1
        return render_template('calculate.html',form=form,output=b) # these specified variables are the only variables go into the html file
    else:
        flash(f"the input number is {form.input_a_number.data}")
        return render_template('calculate.html', form=form)

@app.route('/plot', methods=['GET', 'POST'])
def build_plot():
    import matplotlib.pyplot as plt
    import io
    import base64

    form = PlotForm()
    if form.validate_on_submit():  # need to insert the CSRF field in the HTML form
        flash("you have successfully plotted")
        img = io.BytesIO()

        x = [1,2,3,4,5]
        c = form.coefficient.data
        y = [i * c for i in x]
        plt.plot(x,y)
        plt.savefig(img, format='png')
        img.seek(0)

        plot_url = base64.b64encode(img.getvalue()).decode()
        plot_url = f"data:image/png;base64,{plot_url}"

        return render_template('plot.html',form=form, plot_url=plot_url)
    return render_template('plot.html',form=form)


@app.route('/pictures')
def pictures():
    return render_template("pictures.html")

df = pd.read_excel(r'C:\Users\apple\Desktop\EIS\301W45th\eQUEST_CHP_files_9.20\result-final-forplotting.xlsx')
@app.route('/energyplot', methods=['GET', 'POST'])
def energyplot():

    import matplotlib.pyplot as plt
    import io
    import base64

    form = EnergyPlotForm()


    if form.validate_on_submit():  # need to insert the CSRF field in the HTML form
        flash("you have successfully plotted")
        img = io.BytesIO()

        plt.figure(figsize=(20, 10))
        df['Building cool load (total)'].plot()
        plt.xlim(form.xlow.data, form.xhigh.data)
        plt.ylabel('building cooling load (Btu)')
        plt.xlabel('hour of the year')

        plt.savefig(img, format='png')
        img.seek(0)

        plot_url = base64.b64encode(img.getvalue()).decode()
        plot_url = f"data:image/png;base64,{plot_url}"

        return render_template('energy.html', form=form, plot_url=plot_url)
    return render_template('energy.html', form=form)