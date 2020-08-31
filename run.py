import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipeDB'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
app.secret_key = 'keys'

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/message_sent', methods=['POST'])
def send_message():
    messages =  mongo.db.messages
    messages.insert_one(request.form.to_dict())
    return render_template("messagesent.html")

@app.route('/recipes')
def recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())

@app.route('/show_recipe')
def show_recipe():
    all_recipes = mongo.db.recipes.find()
    all_categories = mongo.db.categories.find()
    all_authors = mongo.db.authors.find()
    return render_template("showrecipe.html", recipes=all_recipes, categories=all_categories, authors=all_authors)

@app.route('/show_recipe/<item_name>')
def search(item_name):
    all_categories = mongo.db.categories.find()
    all_authors = mongo.db.authors.find()
    some_recipes_one = mongo.db.recipes.find({"category": item_name})
    some_recipes_two = mongo.db.recipes.find({"author": item_name})
    if some_recipes_two.count() == 0:
        return render_template("search.html", recipes=some_recipes_one, categories=all_categories, authors=all_authors)
    elif some_recipes_one.count() == 0:
        return render_template("search.html", recipes=some_recipes_two, categories=all_categories, authors=all_authors)

@app.route('/display_one/<recipe_id>')
def display_one(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('displayone.html', recipe=the_recipe)

@app.route('/add_recipe')
def add_recipe():
    all_categories = mongo.db.categories.find()
    return render_template('addrecipe.html', categories=all_categories)

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes =  mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('show_recipe'))

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('editrecipe.html', recipe=the_recipe, categories=all_categories)

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
                    {
                        'recipe_name':request.form.get('recipe_name'),
                        'author':request.form.get('author'),
                        'category':request.form.get('category'),
                        'prep_time':request.form.get('prep_time'),
                        'ingredients':request.form.get('ingredients'),
                        'img':request.form.get('img'),
                        'method': request.form.get('method'),
                        'description':request.form.get('description')
                    })
    return redirect(url_for('show_recipe'))

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('show_recipe'))



@app.route('/manage_category')
def manage_category():
    all_categories =  mongo.db.categories.find()
    return render_template('categories.html', categories=all_categories)

@app.route('/insert_category', methods=['POST'])
def insert_category():
    categories =  mongo.db.categories
    categories.insert_one(request.form.to_dict())
    return redirect(url_for('manage_category'))

@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    the_category =  mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template('editcategory.html', category=the_category)


@app.route('/update_category/<category_id>', methods=["POST"])
def update_category(category_id):
    categories = mongo.db.categories
    categories.update( {'_id': ObjectId(category_id)},
                       {
                           'category_name':request.form.get('category_name')
                       })
    return redirect(url_for('manage_category'))


@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('manage_category'))



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)