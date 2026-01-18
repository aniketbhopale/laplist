
from flask import Flask, request, redirect, render_template
import pymysql
app = Flask(__name__)

con = pymysql.connect(host='localhost', user='root', password='aniket1234@', database='LaptopInfo')
cursor = con.cursor()

@app.route('/findlaptop', methods=['GET', 'POST'])
def findlaptop():
    if request.method == 'POST':
        RAM = request.form['RAM']
        price = request.form['price']
        query = " Select * from Laplist where ram = %s and price <= %s"
        cursor.execute(query,(RAM, price))
        result = cursor.fetchall()
        return render_template('results.html', result=result)
    return render_template('findlaptop.html')

if __name__ == '__main__':
    app.run(debug=True)   


