from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head><title>FitBuddy</title></head>
    <body style="font-family:Arial; text-align:center; padding:50px; background:#f0f8ff;">
        <h1>🏋️ FitBuddy</h1>
        <h3>Your Personal Fitness Partner</h3>
        <form method="post" action="/generate">
            <input name="name" placeholder="Enter Your Name" required style="padding:10px; width:250px;"><br><br>
            <input name="age" type="number" placeholder="Age" required style="padding:10px; width:250px;"><br><br>
            <input name="weight" type="number" placeholder="Weight (kg)" required style="padding:10px; width:250px;"><br><br>
            <select name="goal" required style="padding:10px; width:270px;">
                <option value="weight loss">Weight Loss</option>
                <option value="muscle gain">Muscle Gain</option>
                <option value="fitness">General Fitness</option>
            </select><br><br>
            <select name="intensity" required style="padding:10px; width:270px;">
                <option value="low">Low Intensity</option>
                <option value="medium">Medium Intensity</option>
                <option value="high">High Intensity</option>
            </select><br><br>
            <button type="submit" style="padding:10px 20px; background:blue; color:white; border:none;">Generate My Plan</button>
        </form>
    </body>
    </html>
    """

@app.post("/generate", response_class=HTMLResponse)
def generate(name: str = Form(...), age: int = Form(...), weight: int = Form(...), goal: str = Form(...), intensity: str = Form(...)):
    
    if goal == "weight loss":
        plan = "Daily 30min Cardio, 1500-1800 calories, No sugar, More water"
    elif goal == "muscle gain":
        plan = "5 Days Strength Training, High Protein Food, 2500 calories"
    else:
        plan = "Mix Cardio + Yoga, Balanced Diet, Daily 45min Exercise"

    return f"""
    <html><body style="font-family:Arial; padding:50px; text-align:center; background:#e6ffe6;">
    <h1>Hi {name} 💪</h1>
    <h2>Your Fitness Plan is Ready!</h2>
    <p><b>Age:</b> {age} | <b>Weight:</b> {weight}kg</p>
    <p><b>Goal:</b> {goal} | <b>Level:</b> {intensity}</p>
    <hr>
    <h3>📋 Your Plan: {plan}</h3>
    <br><br>
    <a href="/"><button style="padding:10px 20px;">Create Another Plan</button></a>
    </body></html>
    """
