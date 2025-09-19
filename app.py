from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Quiz page
@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

# Results page
@app.route("/result", methods=["POST"])
def result():
    sentences = json.loads(request.form["sentences"])
    
    intro = "Dear Hiring Manager,<br><br>I am pleased to recommend Zi Jing for your esteemed position."
    outro = "Her unique qualities make her an outstanding candidate for any role.<br><br>Sincerely,<br>CareBear"

    final_paragraph = intro + "<br><br>" + " ".join(sentences) + "<br><br>" + outro

    return render_template("result.html", paragraph=final_paragraph)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
