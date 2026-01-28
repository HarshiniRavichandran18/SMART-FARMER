from flask import Flask, render_template
from routes.weather_routes import weather_bp

app = Flask(__name__)

# Register API routes
app.register_blueprint(weather_bp)

# Frontend route
@app.route("/")
def home():
    return render_template("index.html")

# Required for Render deployment
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
