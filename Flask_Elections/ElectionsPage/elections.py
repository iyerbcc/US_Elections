
########### Imports #########################
import base64
import io
import matplotlib
matplotlib.use('agg')

from flask import jsonify, Flask, render_template, Response, request
from flask_sqlalchemy  import SQLAlchemy


from matplotlib import pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

plt.style.use('fivethirtyeight')

import numpy as np
import pandas as pd
app = Flask(__name__, template_folder='templates')



################### /home  ###############
@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def elections_page():
    cat_df= pd.read_csv('../../elections/categories.csv')
    mylist = cat_df['Categories'].to_list()
    types = ['Population','Registration','Voting']
    graphs = ['Line Plot', 'Bar Graph']
    home_items ={'categories':mylist, 'types':types, 'graphs':graphs}
    return render_template('home.html',home_items = home_items)
    

###################### function get_items  ########

def get_items(cat,type, graph):
    popcategory = cat.replace(' ','-')
    type = type
    title = type+' (in thousands)'

    ## pathname######
    if type[0]=='P':
        pathname = '../../elections/PopulationWithPredictions/'+popcategory+'.csv'
    elif type[0]=='R':
        pathname = '../../elections/RegistrationWithPredictions/'+popcategory+'.csv'
    else:
        pathname = '../../elections/VotingWithPredictions/'+popcategory+'.csv'
    ### items
    items = {'item_name':title, 
            'tab_name':popcategory, 
            'src': plot_png(graph,cat,pathname,title)}
    return items, pathname


##### function plot_png    ###############
def plot_png(graph,cat, pathname,title):
    data = pd.read_csv(pathname)
    xaxis = data['year']
    yaxis = data[cat+'/Predictions']
    
    img = io.BytesIO()
    plt.figure(figsize=(8,5))
    if graph[0]=='L':
        plt.plot(xaxis,yaxis, linewidth=1)
    else:
        plt.bar(xaxis,yaxis)

    plt.xlabel('Year')
    plt.ylabel('Number of People')
    plt.title(cat+' '+title)
    
    plt.tight_layout()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return "data:image/png;base64,{}".format(plot_url)
    #return '<img src="data:image/png;base64,{}">'.format(plot_url)


########################## /table #####################

@app.route('/table', methods=['POST']) 
def table():
    print(request.form)
    cat = request.form.get('cat')
    type = request.form.get('type')
    graph = request.form.get('graph')
    items,pathname = get_items(str(cat),str(type),str(graph))
    data = pd.read_csv(pathname)
    return render_template('table.html', tables=[data.to_html()],items=items)

  


'''
At this point, go to terminal, go to the directory where
this file is kept and type: export FLASK_APP=elections.py (or, for windows:  set FLASK_APP=elections.py)
If you want to keep debug mode on, type: export FLASK_DEBUG=1  (resp. set FLASK_DEBUG=1)
Then type: flask run
This will get you a link to a website.
'''
