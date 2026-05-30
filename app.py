from flask import *

from enrichment import enrich_company

from storage import *

app=Flask(__name__)

@app.route("/")
def home():

    return render_template(
        "index.html"
    )

@app.route(
"/enrich",
methods=["POST"]
)
def enrich():

    data=request.json

    url=data["url"]

    result=enrich_company(url)

    save_result(result)

    return jsonify(result)

@app.route("/results")
def results():

    return jsonify(
        get_results()
    )

if __name__=="__main__":
    app.run(debug=True)