from flask import Flask, request, jsonify
from weather_main import WeatherAgent
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

agent = WeatherAgent(model="gemini-1.5-flash")

@app.route('/weather', methods=['POST'])
def weather_query():
    data = request.json
    query = data.get('query')
    
    if not query:
        return jsonify({"error": "No query provided"}), 400
    
    try:
        # Lightweight sentiment placeholder to keep responses conversational without external corpora
        sentiment = 0.0
        # Include sentiment for tone-adaptive responses; stateless (no chat history)
        final_prompt = f"Sentiment score: {sentiment:.2f}\n" + query
        response = agent.process_weather_query(final_prompt)
        return jsonify({"response": response, "sentiment": sentiment})
    
    except Exception as e:
        return jsonify({"error": f"Error processing query: {str(e)}"}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))  # Render provides PORT
    app.run(debug=True, host='0.0.0.0', port=port)
