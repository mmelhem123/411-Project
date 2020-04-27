function callAPI() {
    
    const ingredient = document.getElementById("item1").value;
    const numRecipes = document.getElementById("nRecipes").value;
    
    const nameAPI = "https://api.spoonacular.com/recipes/findByIngredients?ingredients=" + ingredient + "&number=" + numRecipes + "&apiKey=62398c3d538f461f977a1ad87dc9fe90";
    /* hide this key */
    const request = new XMLHttpRequest();
    
    request.open('GET', nameAPI, true);
    request.onload = function() {
    /*check on data*/
    /*fetch api for http request*/
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
        
    var allRecNoDup = [];
    var allIMGsNoDup = [];
        
    allRec.forEach(element => {
        if(!allRecNoDup.includes(element)){
            allRecNoDup.push(element);
        }
    })
        
    foodIMGs.forEach(element => {
        if(!allIMGsNoDup.includes(element)){
            allIMGsNoDup.push(element);
        }
    })
    document.getElementById("recipesAndPics").innerHTML = "";
    for (i = 0; i < allIMGsNoDup.length; i++)
        {
            var para = document.createElement("P");
            para.innerHTML = allRecNoDup[i];
            document.getElementById("recipesAndPics").appendChild(para);
            var imgs = document.createElement("img");
            imgs.src = allIMGsNoDup[i];
            document.getElementById("recipesAndPics").appendChild(imgs);
        }
    }
    
    /*
    for error 
    1)put one about when asking for 5 recipes get duplicates but still get 5 unique ones
    2) pictures and foods were stacking on each other, added part before loop to fix this
    */
    request.send();
}