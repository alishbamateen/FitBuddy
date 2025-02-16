from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your DeepSeek API key
DEEPSEEK_API_KEY = "sk-d9ced50fdead44e287d1192590f5c7db"
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"  # Replace with the actual DeepSeek API endpoint

def get_workout_plan(gender, weight, height, age, goal, additional_preferences, available_time_per_week):
    """
    Generate a personalized weekly workout plan using DeepSeek API.
    """
    prompt = (
        f"Create a personalized weekly workout plan for a {age}-year-old {gender}, weighing {weight} kg, "
        f"and {height} cm tall. The goal is {goal}, with preferences for {additional_preferences} workouts. "
        f"The total available time per week is {available_time_per_week} minutes. "
        "Provide a detailed plan that includes exercises, duration, and frequency for each day of the week."
    )

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
    }

    data = {
        "model": "deepseek-chat",  # Replace with the correct DeepSeek model name
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 1,
        "max_tokens": 2048
    }

    try:
        response = requests.post(DEEPSEEK_API_URL, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        print(f"Error calling DeepSeek API: {e}")
        return None

@app.route('/generate-workout-plan', methods=['POST'])
def generate_workout_plan():
    data = request.json
    workout_plan = get_workout_plan(
        gender=data['gender'],
        weight=data['weight'],
        height=data['height'],
        age=data['age'],
        goal=data['goal'],
        additional_preferences=data['additional_preferences'],
        available_time_per_week=data['available_time_per_week']
    )
    return jsonify({"workout_plan": workout_plan})

if __name__ == '__main__':
    app.run(debug=True)