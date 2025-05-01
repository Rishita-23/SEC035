from flask import Flask, render_template, jsonify, request, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# In-memory dictionary to store votes for cats and dogs
votes = {'cats': 0, 'dogs': 0}

@app.route('/')
def index():
    # Render the initial voting page with current results
    return render_template('index.html', votes=votes)

@app.route('/vote', methods=['POST'])
def vote():
    vote_choice = request.json.get('vote')
    
    if vote_choice == 'cats':
        votes['cats'] += 1
    elif vote_choice == 'dogs':
        votes['dogs'] += 1

    # Send the updated results back as JSON
    return jsonify(votes=votes)

if __name__ == '__main__':
    app.run(debug=True)
