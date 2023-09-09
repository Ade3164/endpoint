from flask import Flask, request, jsonify
import datetime
import pytz

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
  
    slack_name = request.args.get('idris_adebayo')
    track = request.args.get('backend')

    current_day = datetime.datetime.now(pytz.utc).astimezone(pytz.timezone('UTC')).strftime('%A')
    current_utc_time = datetime.datetime.now(pytz.utc).astimezone(pytz.timezone('UTC'))
    min_time = current_utc_time - datetime.timedelta(minutes=2)
    max_time = current_utc_time + datetime.timedelta(minutes=2)
    github_file_url = "https://github.com/username/repo/blob/main/file_name.ext"
    github_repo_url = "https://github.com/username/repo"
    status_code = 200

   
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_utc_time.strftime('%Y-%m-%dT%H:%M:%SZ'),
        "track": track, 
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": status_code
    }

    # Set the response content type to JSON
    response = jsonify(response_data)

    return response

if __name__ == '__main__':
    # Run the Flask app on a publicly accessible server (e.g., on localhost)
    app.run(host='0.0.0.0', port=5000)

