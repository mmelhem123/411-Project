function callAPI() {
    const ingredient = document.getElementById("item1").value;
    const numRecipes = document.getElementById("nRecipes").value;
    
    const nameAPI = "https://api.spoonacular.com/recipes/findByIngredients?ingredients=" + ingredient + "&number=" + numRecipes + "&apiKey=95d2bf9a71c94e58b5e18e0cf2ffb930";
    
    const request = new XMLHttpRequest();
    
    request.open('GET', nameAPI, true);
    request.onload = function() {
        
    const data = JSON.parse(this.response)
        
    var allRec = [];
    var foodIMGs = [];
    if (request.status >= 200 && request.status < 400) {
        data.forEach(recipe => {            
            allRec.push(" " + recipe.title);
            foodIMGs.push(recipe.image);
        })
        }
    else {
        console.log('error')
        }
        
        
    document.getElementById("recipes").innerHTML = allRec;
        
    document.getElementById("pics").innerHTML = foodIMGs;
        
    
    
  /*  
    for (i = 0, i < foodIMGs.length; i++){
        var pic = document.createElement("IMG");
        pic.setAttribute("src", foodIMGs[0]);
        pic.setAttribute("width", "304");
        pic.setAttribute("height", "228");
        pic.setAttribute("alt", "FoodPic");
        document.body.appendChild(x);
    }
    */
    }
    
    
    request.send();
}