from flask import Flask, render_template, redirect

app = Flask(__name__)

# GANTI DENGAN NOMOR WA KAMU
WA_NUMBER = "6285272680981"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/jawab", methods=["POST"])
def jawab():
    pesan = "Mabarr woyyy"
    return redirect(f"https://wa.me/{WA_NUMBER}?text={pesan}")

if __name__ == "__main__":
    app.run(debug=True)