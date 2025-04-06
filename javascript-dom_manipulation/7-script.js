fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const results = data.results;
    const list = document.getElementById('list_movies');
    results.forEach(movie => {
      const listItem = document.createElement('li');
      listItem.textContent = movie.title;
      list.appendChild(listItem);
    });
  })
