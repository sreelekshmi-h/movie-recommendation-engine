async function searchMovies(){

    const query=document.getElementById("query").value;

    if(query===""){
        alert("Enter a movie description");
        return;
    }

    const response=await fetch("http://127.0.0.1:8000/search",{

        method:"POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            query: query,
            n_results: 5
        })

    });

    const movies=await response.json();

    const results=document.getElementById("results");

    results.innerHTML="";

    movies.forEach(movie=>{

        results.innerHTML+=`

        <div class="card">

            <img src="${movie.poster}" alt="${movie.title}">

            <div class="info">

                <h2>${movie.title}</h2>

                <div class="rating">
                    ⭐ ${movie.rating}
                </div>

                <div class="year">
                    ${movie.year}
                </div>

                <div class="overview">
                    ${movie.overview}
                </div>

            </div>

        </div>

        `;

    });

}