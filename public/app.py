from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', message="")

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    age = data.get("age")
    gender = data.get("gender")
    weight = data.get("weight")
    height = data.get("height")
    goal = data.get("goal")
    preference = data.get("preferences")
    time = data.get("available_time_per_week")

    prompt = f"""Create a whole wee personal plan for a {age} years old {gender}. Who weights {weight}kg and is {height}cm tall. 
    The want to workout {time} hours a week. The goal for the plan should be to {goal}. The workout should be according to a 
    {preference} workout. The plan should include warmup/stretches, exercises, and cooldown."""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a fitness coach."},
                  {"role": "user", "content": prompt}]
    )

    workout_plan = response["choices"][0]["message"]["content"]

    return jsonify({"plan": workout_plan})


if __name__ == '__main__':
    app.run(debug=True)
        