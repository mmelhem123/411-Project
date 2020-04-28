const https = require('https');

https.get('https://api.spoonacular.com/recipes/findByIngredients?ingredients=cheese&number=2&apiKey=95d2bf9a71c94e58b5e18e0cf2ffb930', (resp) => {
  let data = '';

  // A chunk of data has been recieved.
  resp.on('data', (chunk) => {
    data += chunk;
  });

  // The whole response has been received. Print out the result.
  resp.on('end', () => {
    console.log(JSON.parse(data));
  });

}).on("error", (err) => {
  console.log("Error: " + err.message);
});


