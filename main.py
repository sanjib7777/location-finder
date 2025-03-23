from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for locations (for demonstration purposes)
locations = []

@app.route('/api/location', methods=['POST'])
def receive_location():
    # Get JSON data from the request
    data = request.json
    if not data or 'latitude' not in data or 'longitude' not in data:
        return jsonify({"error": "Invalid data"}), 400

    # Extract latitude and longitude
    latitude = data['latitude']
    longitude = data['longitude']
    timestamp = data.get('timestamp', 'N/A')

    # Store the location (for demonstration)
    locations.append({
        "latitude": latitude,
        "longitude": longitude,
        "timestamp": timestamp
    })

    print(f"Received location: {latitude}, {longitude} at {timestamp}")
    return jsonify({"message": "Location received"}), 200

@app.route('/api/locations', methods=['GET'])
def get_locations():
    # Return all stored locations (for demonstration)
    return jsonify(locations), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)  # Use port 10000 (or any port supported by Render)