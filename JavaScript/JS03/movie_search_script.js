function loadMovieInfo() {
    let movieTitle = document.getElementById("movieTitle").value; // 영화 제목 가져오기
    if (movieTitle === "") {
        alert("영화 제목을 입력하세요.");
        return;
    }

    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                // 데이터가 잘 로딩됐을 때 처리
                let data = JSON.parse(xhr.responseText);
                if (data.Response === "False") {
                    alert("영화 정보를 가져오는데 실패했습니다.")
                } else {
                    let movieInfo = "";
                    movieInfo += "<h2>" + data.Title + "</h2>";
                    movieInfo += "<p><strong>장르: </strong>" + data.Genre + "</p>";
                    movieInfo += "<p><strong>감독: </strong>" + data.Director + "</p>";
                    movieInfo += "<p><strong>배우: </strong>" + data.Actors + "</p>";
                    movieInfo += "<p><strong>포스터: </strong>" + '<img src = "' + data.Poster + '"></p>';
                    document.getElementById("movieInfo").innerHTML = movieInfo;
                }
            } else {
                alert("영화 정보를 가져오는데 실패했습니다.");
            }

            // ?: query가 시작되는 곳
            // i=tt3896198: ket-value 한 쌍
            // &: query를 추가하는 새로운 key-value 한 쌍
            // apikey: key-value 한 쌍
            // t=: key 타이틀 제목에 vlaue 영화 제목 입력
        }
    }
    xhr.open("GET", "http://www.omdbapi.com/?i=tt3896198&apikey=ef251424&t=" +
        encodeURIComponent(movieTitle), true);
    xhr.send();

}