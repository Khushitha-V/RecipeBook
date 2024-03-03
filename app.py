from flask import Flask,render_template,redirect,url_for,request
app =Flask (__name__)
recipes=[]
@app.route("/")
def home():
    return render_template("name.html")
@app.route("/add",methods=["POST","GET"])
def add():
    if request.method=="POST":
        name=request.form["nm"]
        ingredients=request.form["ingredients"]
        instructions=request.form["instructions"]
        data={"name": name, "ingredients": ingredients, "instructions": instructions}
        recipes.append(data)
    return render_template("addrecipe.html")

if __name__ == "__main__":
    app.run(debug=True)