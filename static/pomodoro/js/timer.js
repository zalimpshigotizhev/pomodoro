
// function startTimer(
//     durationInSeconds,
//     theme_id,
//     restInSeconds,
//     relax_img,
//     work_img,
//     relax_mp3,
//     work_mp3
// ) {
//     // durationInSeconds = durationInSeconds * 60;
//     // restInSeconds = restInSeconds *60;
//     console.log(relax_mp3)
//     console.log(work_mp3)
//     let workInSeconds = durationInSeconds;
//     let relaxInSeconds = restInSeconds  ;
//     let timerElement = document.getElementById('timer');
//     let conditionElement = document.getElementById('imgCond');
//     let buttonElement = document.getElementById('startButton');
//     let remainingTime = workInSeconds;
//     let timerInterval;
//     let isRunning = false;
//     let isWork = true;

//     function updateTimer() {
//         previewData();
//         remainingTime--;

//         if (remainingTime < 0) {
//             if (isWork) {
//                 conditionElement.src = relax_img;
//                 remainingTime = relaxInSeconds;
//                 isWork = false;
//                 playNotificationSound(work_mp3);
//                 showNotification('Время отдыха!', 'Отойдите от экранов и разомнитесь')
//                 updateTimer()

//             } else {
//                 conditionElement.src = work_img;
//                 remainingTime = workInSeconds;
//                 isWork = true;
//                 playNotificationSound(relax_mp3);
//                 showNotification('Время интенсивной работы!', 'Сконцентрируйтесь максимально!')
//                 updateTimer()
//             }
//             // let uuu = document.getElementById('iframeContainer1').contentWindow.location.reload(true);

//             isRunning = false;
//             buttonElement.textContent = 'СТАРТ';
//             clearInterval(timerInterval);
//         }
//     }

//     function previewData() {
//         let minutes = Math.floor(remainingTime / 60);
//         let seconds = remainingTime % 60;

//         minutes = minutes < 10 ? '0' + minutes : minutes;
//         seconds = seconds < 10 ? '0' + seconds : seconds;

//         timerElement.textContent = `${minutes}:${seconds}`;
//     }
//     previewData();

//     function toggleStartPause() {
//         if (isRunning) {
//             pause();
//         } else {
//             start();
//         }
//     }

//     function start() {
//         buttonElement.textContent = 'ПАУЗА';
//         isRunning = true;
//         clearInterval(timerInterval); // Очистка предыдущего интервала
//         updateTimer();
//         timerInterval = setInterval(updateTimer, 1000);
//     }

//     function pause() {
//         buttonElement.textContent = 'СТАРТ';
//         isRunning = false;
//         clearInterval(timerInterval); // Очистка текущего интервала
//     }

//     function completed() {
//         buttonElement.textContent = 'СТАРТ';
//         isRunning = false;
//         clearInterval(timerInterval);
//         remainingTime = isWork ? workInSeconds : relaxInSeconds;
//         updateTimer();
//     }

//     function stop() {
//         buttonElement.textContent = 'СТАРТ';
//         isRunning = false;
//         clearInterval(timerInterval); // Очистка текущего интервала
//         remainingTime = isWork ? workInSeconds : relaxInSeconds;
//         updateTimer();
//     }

//     // Обработчики событий для кнопок
//     document.getElementById('startButton').addEventListener('click', toggleStartPause);
//     document.getElementById('stopButton').addEventListener('click', stop);
//     document.getElementById('completed').addEventListener('click', completed);
// }



function startTimer(
    durationInSeconds,
    restInSeconds,  
    restLongInSeconds,
    theme_id,
    relax_img,
    work_img,
    relax_mp3,
    work_mp3,
  ) {
    let timerElement = document.getElementById('timer');
    let conditionNumber = document.getElementById('conditionRest')
    let conditionElement = document.getElementById('imgCond');
    let buttonElement = document.getElementById('startButton');
    let remainingTime = durationInSeconds;
    let timerInterval;
    let isRunning = false;
    let isWork = true;



    let cachedDataRestOrWork = localStorage.getItem('restOrWork')
    let cachedData = localStorage.getItem('condition')
    if(cachedData == null || cachedDataRestOrWork == null){
        localStorage.setItem('condition', 1);
        localStorage.setItem('restOrWork', 'Work');
        cachedDataRestOrWork = localStorage.getItem('restOrWork')
        cachedData = localStorage.getItem('condition')
    }


    function playNotificationSound(song) {
        var audio = new Audio(song); 
        audio.play();
    }
    


    function checkConditionRestOrWork(){
        cachedDataRestOrWork = localStorage.getItem('restOrWork')
        if(cachedDataRestOrWork == 'Work'){
            localStorage.setItem('restOrWork', 'Rest');
            return 'Rest';
        }else{
            localStorage.setItem('restOrWork', 'Work');
            return 'Work';
        }
    }

    function checkConditionRest(){
        conditionInCash = localStorage.getItem('condition');
        if(conditionInCash == 1){
            localStorage.setItem('condition', 2);
            return 2;
        } else if(conditionInCash == 2){
            localStorage.setItem('condition', 3);
            return 3;
        } else if(conditionInCash == 3){
            localStorage.setItem('condition', 4);
            return 4;
        } else if(conditionInCash == 4) {
            localStorage.setItem('condition', 1);
            return 1;
        }
    }

    function detectionCondition(){
        if(cachedDataRestOrWork == 'Rest'){
            transformationToRest()
        }
    }

    detectionCondition()

    function previewData() {

        conditionNumber.textContent = `${cachedData}/4`

        let minutes = Math.floor(remainingTime / 60);
        let seconds = remainingTime % 60;

        minutes = minutes < 10 ? '0' + minutes : minutes;
        seconds = seconds < 10 ? '0' + seconds : seconds;

        timerElement.textContent = `${minutes}:${seconds}`;
    }
    previewData();

    function toggleStartPause() {
        if (isRunning) {
            pause();
        } else {
            start();
        }
    }

    function transformationToRest(){
        isWork = false;
        conditionElement.src = relax_img;
        if(cachedData == 4){
            remainingTime = restLongInSeconds;
        }else {
            remainingTime = restInSeconds;
        }
    }


    function transformationToWork(){
        isWork = true;
        conditionElement.src = work_img;
        localStorage.setItem('condition', 1);
        cachedData = 1
        localStorage.setItem('restOrWork', 'Work');
        cachedDataRestOrWork = 'Work'
    }


    function start() {
        buttonElement.textContent = 'ПАУЗА';
        isRunning = true;
        clearInterval(timerInterval);
        updateTimer();
        timerInterval = setInterval(updateTimer, 1000);
    }

    function pause() {
        buttonElement.textContent = 'СТАРТ';
        isRunning = false;
        clearInterval(timerInterval);
    }

    function completed() {
        buttonElement.textContent = 'СТАРТ';
        isRunning = false;
        transformationToWork()
        clearInterval(timerInterval);
        remainingTime = isWork ? durationInSeconds : restInSeconds;
        updateTimer();
    }

    function stop() {
        buttonElement.textContent = 'СТАРТ';
        isRunning = false;
        clearInterval(timerInterval);
        console.log(cachedData)
        remainingTime = isWork ? durationInSeconds
                        : cachedData !== 4 ? restInSeconds
                        : restLongInSeconds;
        updateTimer();
    }

    function updateTimer() {
        previewData();
        remainingTime--;
        if (remainingTime < 0) {
            if (isWork && cachedDataRestOrWork == 'Work') {
                sendDataToServer(durationInSeconds, theme_id, '/dashboard/');
                conditionElement.src = relax_img;

                if(cachedData == 4){
                    remainingTime = restLongInSeconds;
                }else {
                    remainingTime = restInSeconds;
                };
                cachedDataRestOrWork = checkConditionRestOrWork();
                isWork = false;
                playNotificationSound(work_mp3);
                showNotification('Время отдыха!');

            } else {
                sendDataToServer(restInSeconds, theme_id, '/create_rest/')
                conditionElement.src = work_img;
                remainingTime = durationInSeconds;
                isWork = true;
                playNotificationSound(relax_mp3);
                showNotification('Время интенсивной работы!')
                cachedDataRestOrWork = checkConditionRestOrWork()
                cachedData = checkConditionRest()
                conditionNumber.textContent = `${cachedData}/4`
            }

            frame1.refresh(true);
            buttonElement.textContent = 'СТАРТ';
            clearInterval(timerInterval);
            previewData()
            pause()


        }
    }

    // Обработчики событий для кнопок
    document.getElementById('startButton').addEventListener('click', toggleStartPause);
    document.getElementById('stopButton').addEventListener('click', stop);
    document.getElementById('completed').addEventListener('click', completed);
}

