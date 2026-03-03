from flask import Flask, jsonify, request
from src.agents.crew_head import build_crew_agent
from config.settings import app_port

app = Flask(__name__)

@app.route('/get_travel_plan', methods=['GET'])
def get_travel_plan():

    data = request.get_json()

    from_city = data.get('from_city')
    destination_city = data.get('destination_city')
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    hobbies = data.get('hobbies')

    crew = build_crew_agent(
        from_city=from_city,
        destination_city=destination_city,
        start_date=start_date,
        end_date=end_date,
        hobbies=hobbies
    )

    result = crew.kickoff()

    return jsonify({'result': str(result)})

if __name__ == '__main__':
    app.run(debug=True, port=app_port)