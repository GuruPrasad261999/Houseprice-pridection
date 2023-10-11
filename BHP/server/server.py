from flask import Flask,request,jsonify
import utils
# Create a Flask app
app = Flask(__name__)

@app.route('/get_location_name')
def get_location_name():
    response= jsonify({
        'locations':utils.get_location_name()
    })
    response.headers.add('Access-Control-Allow-Origin','*')

    return response

@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
    total_sqft =float(request.form['total_sqft'])
    bath=float(request.form['bath'])
    bhk=float(request.form['bhk'])
    location = request.form['location']

    response=jsonify({
        'estimated_price':utils.get_estimated_price(location,total_sqft,bath,bhk)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response



if __name__ == '__main__':
    print("staring server to predict home prices")
    utils.load_saved_artifacts()
    app.run(debug=True)
