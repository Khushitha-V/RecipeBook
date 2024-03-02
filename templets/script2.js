// Sample recipe data (you can replace this with your actual recipes)
const recipes = [
    {
        name: 'Chocolate Chip Cookies',
        ingredients: ['flour', 'sugar', 'chocolate chips'],
        instructions: 'Mix ingredients, bake at 350°F for 10 minutes.',
    },
    // Add more recipe objects as needed
];

// Function to display recipes
function displayRecipes() {
    const recipeList = document.getElementById('recipeList');
    recipeList.innerHTML = ''; // Clear existing content

    recipes.forEach((recipe) => {
        const recipeDiv = document.createElement('div');
        recipeDiv.classList.add('recipe-card'); // Add styling as needed

        // Populate recipe details
        recipeDiv.innerHTML = `
            <h2>${recipe.name}</h2>
            <ul>
                <li>Ingredients: ${recipe.ingredients.join(', ')}</li>
                <li>Instructions: ${recipe.instructions}</li>
            </ul>
        `;

        recipeList.appendChild(recipeDiv);
    });
}

// Call the function to display recipes
displayRecipes();
