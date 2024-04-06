from flask import Flask, render_template, request, jsonify #flask = pyt web framework 

app = Flask(__name__)

@app.route('/') #decorator 
def index():
    return render_template('index.html')

@app.route('/bot', methods=['POST']) #to give msg to server/webpage
def bot_response():
    user_message = request.form['message']
    import google.generativeai as genai

    model = genai.GenerativeModel('gemini-pro')
    
    my_api_key_gemini = '' 
    
    genai.configure(api_key=my_api_key_gemini)
    
    response = model.generate_content(user_message)
    bot_response = response.text #json format = text
    return jsonify({'message': bot_response})

if __name__ == '__main__': 
    app.run(debug=True) #to run flask server
