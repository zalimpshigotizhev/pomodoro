// Функция для выполнения асинхронного запроса с использованием Fetch API

const openClosedTabs = (container) => {
    if (container.style.display === 'block') {
      container.style.display = 'none';
    } else {
      listOpenWindow.forEach(tab => tab.style.display = 'none');
      container.style.display = 'block';
      listOpenWindow.push(container);
    }
  }

async function fetchData() {
    const iframe = document.getElementById('iframeContainer1');

    try {
      // Выполнение GET-запроса
      const response = await fetch('/stats/');
  
      // Проверка успешности запроса
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const responseData = await response.text();
      // Получение данных в формате JSON
  
      // Обновление содержимого фрейма
        iframe.contentDocument.body.innerHTML = responseData;
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  }



const graph_themes = (themes) => {
        const xArray = themes.map(theme => theme.name);
        const yArray = themes.map(theme => theme.count);

        const colors = ['rgba(255,99,132,1)', 'rgba(255,205,86,1)', 'rgba(75,192,192,1)', 'rgba(54,162,235,1)', 'rgba(153,102,255,1)'];

        const data = [{
            labels: xArray,
            values: yArray,
            type: "pie",
            marker: {
                colors: colors,
                showlegend: false,
                line: {
                    color: 'rgba(255,255,255,0.8)',
                    width: 2
                },
            },
        }];

        const layout = {height: 300, width: 450, paper_bgcolor: "rgba(0,0,0,0)"};

        Plotly.newPlot("myPlot", data, layout,  {displayModeBar: false});
    }


function selectImage(selectedImage, value) {
    // Убираем рамку у всех картинок
    var images = document.querySelectorAll('.image-container img');
    images.forEach(function(image) {
        image.classList.remove('selected');
    });

    // Добавляем рамку выбранной картинке
    selectedImage.classList.add('selected');

    // Устанавливаем значение в поле input
    document.getElementById('selectedImage').value = value;
}

function reloadPageAsync(serverUrl,  container,  color_navigation) {
    function loadContent() {
        fetch(serverUrl)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.text();
            })
            .then(data => {
                container.innerHTML = data;
                container.style.backgroundColor = color_navigation;
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
            });
    }

    document.addEventListener('DOMContentLoaded', loadContent);
    return {
        refresh: function (forceRefresh) {
            if (forceRefresh) {
                loadContent();
            }
        }
    };
}


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}



function playNotificationSound(song) {
    // Создаем аудио-элемент
    var audio = new Audio(song); // Укажите путь к звуковому файлу

    // Воспроизводим звук
    audio.play();
}


function showNotification(title, body) {
    var notificationContainer = document.getElementById('notification-container');
    var notificationTitle = document.getElementById('notification-title');
    var notificationBody = document.getElementById('notification-body');
  
    notificationTitle.innerText = title;
    notificationBody.innerText = body;
  
    notificationContainer.classList.remove('hidden');
    notificationContainer.classList.add('show');
  
    setTimeout(function () {
      notificationContainer.classList.remove('show');
      notificationContainer.classList.add('hidden');
    }, 5000); // Уведомление будет автоматически скрыто через 5 секунд
  }


function updateSelectionRelax(radio) {
    if (radio.checked) {
        selectedValueRelax = radio.value;
        console.log(selectedValueRelax)
        }
    }

function updateSelectionWork(radio) {
    if (radio.checked) {
        selectedValueWork = radio.value;
        console.log(selectedValueWork)
    }
}

function playSelectSoundRelax(condition){
    if(condition == 'relax'){
        playNotificationSound(selectedValueRelax)
    }else {
        playNotificationSound(selectedValueWork)
    }
}

// Загрузка фреймов 
function loadContentInFrame(url, container) {
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(data => {
            container.innerHTML = data;
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
}













const url_stats = '/stats/'
const frame1 = reloadPageAsync(serverUrl1, container1, color_navigation)
reloadPageAsync(serverUrl2, container2, color_navigation)
graph_themes(themes);
startTimer(
    durationInSeconds=durationInSeconds,
    restInSeconds=1,
    restLongInSeconds=2,
    theme_id=theme_id,
    relax_img=relax_img,
    work_img=work_img,
    relax_mp3=relax_mp3,
    work_mp3=work_mp3
  );


  
function sendDataToServer(InSeconds, theme_id, url) {
    // reloadPageAsync(serverUrl1, container)
    // Получение CSRF-токена из мета-тега в HTML
    const csrfToken = getCookie('csrftoken');


    // Отправка данных на сервер с использованием Fetch API и передачей CSRF-токена
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({ seconds: InSeconds, theme: theme_id}),
    })
    
}

function showContent1(id, button) {
    // Скрываем все контенты
    console.log(button.classList.value)
    var contents = document.querySelectorAll('.content');
    contents.forEach(function(content) {
      content.classList.remove('active');
    });

    // Показываем выбранный контент
    var selectedContent = document.getElementById(id);
    selectedContent.classList.add('active');

    var contents2 = document.querySelectorAll('.stats-nav2');
    contents2.forEach(function(content) {
        content.classList.remove('active-butt-stats');
      });
    button.classList.add('active-butt-stats')

  }

function showContent2(id, button) {
    // Скрываем все контенты
    var contents = document.querySelectorAll('.f-content');
    contents.forEach(function(content) {
      content.classList.remove('f-active');
    });

    // Показываем выбранный контент
    var selectedContent = document.getElementById(id);
    selectedContent.classList.add('f-active');

    
    var contents2 = document.querySelectorAll('.stats-nav');
    contents2.forEach(function(content) {
        content.classList.remove('active-butt');
      });
    button.classList.add('active-butt')
  } 

// Функция для отображения/скрытия текста
function toggleText() {
    var hiddenText = document.getElementById("hiddenText");
    // Переключение видимости текста
    hiddenText.style.display = (hiddenText.style.display === "none") ? "block" : "none";
}

// Добавление обработчика события на элемент
var toggleButton = document.getElementById("toggleButton");
toggleButton.addEventListener("click", toggleText);





document.getElementById('profileButton').addEventListener('click', function () {
  openClosedTabs(tabsContainerProfile)
});

document.getElementById('pomodorButton').addEventListener('click', function () {
  openClosedTabs(tabsContainerPomodoro)
});
  
  // Добавляем обработчики событий для каждой вкладки (можете добавить свою логику)
  document.getElementById('tab1').addEventListener('click', function () {
    alert('Вы находитесь на вкладке 1');
  });
  
  document.getElementById('tab2').addEventListener('click', function () {
    alert('Вы находитесь на вкладке 2');
  });
  
