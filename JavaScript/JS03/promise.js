function wakeUp() {
    console.log("아침에 일어나서 강의 듣기!");
}

function eatLunch_promise() {
    return new Promise(function (resolve) {
        setTimeout(function () {
            console.log("점심시간!");
            resolve();
        }, 3000)
    })


}

function endClass() {
    console.log("강의가 끝났다! 놀아야지!");
}

wakeUp();
eatLunch_promise().then(function () {
    endClass();
});
// endClass();