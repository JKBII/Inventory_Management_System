#importing
#importing <file name>
#from filename import<....>
from flask import Flask, render_template


#calling/instantiating
app=Flask(__name__)

#creating of endpoints/routes
#1. declaration of aroute
#2. a function embedded to the route
@app.route('/home')
def home():
    return 'welcome to web development'

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
 
@app.route('/inventories')
def inventories():
    return render_template('inventories.html')

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/data_visualisation')
def data_visualisation():

pie_chart=pygal.pie()
pie_chart.title='Distribution of Corona virus in Kenya'
pie_chart.add('Nairobi',63)
pie_chart.add('Mombasa',20)
pie_chart.add('Kilifi',17)
pie_chart.add('Machakos',30)
pie_chart.add('Kiambu',7)



my_pie_data=[
    ('Nairobi',63),
    ('Mombasa',20),
    ('Kilifi',17),
    ('Machakos',30),
    ('Kiambu',7)
]
for each in my_pie_data:
    pieChart.add(each[0],each[1])

pie_data=pie_chart.render_data_uri()

data=[
    {'month','January','total':22},
    {'month','February','total':25}
    {'month','March','total':24}
    {'month','April','total':35}
    {'month','May','total':45}
    {'month','June','total':38}
    {'month','July','total':67}
    {'month','August','total':87}
    {'month','September','total':78}
    {'month','October','total':97}
    {'month','November','total':100}
    {'month','December','total':102}
]

a=[]

for each in data:
    x=each['month']
    y=each['total']
    a.append(x)
    b.append(y)


line_chart=pygal.line()
line_chart.title='total sales'
line

line_data=line_graph.render_data_uri()



return render_template('charts.html',pie=pie_data,line=line_data)

#Run your app
if __name__=='__main__':
    app.run()

