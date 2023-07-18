// 2.주어진 숫자를 제곱한 후, 콜백 함수를 통해 결과를 전달하는 함수 squareWithCallback을 작성하세요.
function squareWithCallback(num, callback) {
    if (typeof num !== "number") {
        const error = "숫자를 입력하세요.";
        const result = 0;
        callback(error, result);
        return;
    }
    const result = num ** 2;
    const error = 1;
    callback(error, result);
}

function foo(error, result) {
    if (error != 1) {
        return console.log(error);
    }
    return console.log(result);
}

squareWithCallback(3, foo);
squareWithCallback("Hello", foo);

// 답안
// function squareWithCallback(number, callback) {
//     if (typeof number !== 'number') {
//         const error = new Error('유효하지 않은 숫자입니다.');
//         callback(error, undefined);
//         return;
//     }
//     const result = number * number;
//     callback(null, result);
// }

// // 콜백 함수
// function callbackFunction(error, result) {
//     if (error) {
//         console.log("에러: ", error);
//     } else {
//         console.log("결과: ", result);
//     }
// }

// squareWithCallback(4, callbackFunction);
// squareWithCallback('hello', callbackFunction);

//3. 주어진 숫자에서 10을 만들기 위해 얼마를 더해야 하는지 계산한 후, 프로미스를 사용하여 결과를 반환하는 함수 makeTenWithPromise를 작성하세요.
function makeTenWithPromise(number) {
    return new Promise((resolve, reject) => {
        // 1. 유효한 숫자인지 확인하여 아닌 경우는 어떤함수를 호출할지 구현
        if (typeof number != "number") {
            // reject(new Error("유효하지 않은 숫자입니다."));
            reject("유효하지 않은 숫자입니다.");
            return;
        }
        const result = 10 - number;
        if (result < 0) {
            reject("유효한 숫자가 아닙니다.");
            return;
        }
        // 2. 정상 숫자인 경우는 얼마를 더 해야하는지 성공함수를 호출하여 구현
        resolve(result);
        return;
    });
}

// 예시 테스트
makeTenWithPromise(5)
    .then((amount) => {
        console.log('더해야 하는 값:', amount);
    })
    .catch((error) => {
        console.log('에러:', error);
    });

makeTenWithPromise('hello')
    .then((amount) => {
        console.log('더해야 하는 값:', amount);
    })
    .catch((error) => {
        console.log('에러:', error);
    });

// CharGPT
// function makeTenWithPromise(number) {
//     return new Promise((resolve, reject) => {
//         const difference = 10 - number;
//         if (difference >= 0) {
//             resolve(difference);
//         } else {
//             reject("Given number is greater than 10");
//         }
//     });
// }

// // 프로미스 사용하여 결과 처리하는 예시
// makeTenWithPromise(7)
//     .then(result => {
//         console.log(`To make 10, add ${result}`);
//     })
//     .catch(error => {
//         console.error(error);
//     });
