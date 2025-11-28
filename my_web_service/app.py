from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/predict", methods=["POST"])
def predict():
    user_text = request.form.get("text", "")

    text_lower = user_text.lower()
    if any(word in text_lower for word in ["good", "great", "love", "awesome"]):
        sentiment = "긍정 👍"
    elif any(word in text_lower for word in ["bad", "terrible", "hate", "awful"]):
        sentiment = "부정 👎"
    else:
        sentiment = "중립 😐 (잘 모르겠어요)"

    return render_template("result.html",
                           user_text=user_text,
                           sentiment=sentiment)

if __name__ == "__main__":
    app.run(debug=True)
