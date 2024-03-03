from flask import Flask,render_template,redirect,url_for,request,flash
app =Flask (__name__)
app.secret_key="Khushi@129"
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
@app.route("/display",methods=["POST","GET"])
def dis():
    flash("Recipe"+str(request.form(['nm']))+"is sucessfully added!")
    return render_template("addrecipe.html")
@app.route("/delete",methods=["DELETE"])
def delete():
    if request.method=="POST":
        name = input("Enter recipe name to delete: ")
    for recipe in recipes:
        if recipe["name"] == name:
            recipes.remove(recipe)
            print(f"Recipe '{name}' deleted successfully!")
            break
    else:
        print(f"Recipe '{name}' not found.")

if __name__ == "__main__":
    app.run(debug=True)