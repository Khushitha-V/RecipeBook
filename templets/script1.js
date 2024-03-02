const recipe = {
    name: "Delicious Banana Bread",
    ingredients: ["2 ripe bananas", "1 cup flour", "1/2 cup sugar", "1 tsp baking powder"],
    method: "Mix ingredients, bake at 350°F for 45 minutes."
};

// Create a recipe item div
const recipeDiv = document.createElement("div");
recipeDiv.classList.add("recipe-item");
recipeDiv.innerHTML = `
    <h3>${recipe.name}</h3>
    <ul>
        ${recipe.ingredients.map(ingredient => `<li>${ingredient}</li>`).join("")}
    </ul>
    <p>${recipe.method}</p>
    <button class="delete-button">Delete</button>
`;

// Append the recipe item to the recipe list
const recipeList = document.querySelector(".recipe-list");
recipeList.appendChild(recipeDiv);
