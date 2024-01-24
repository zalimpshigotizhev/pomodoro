document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('tasksButton').addEventListener('click', function () {
        loadContentInFrame('{% url "tasks" %}', 'iframeContainer2');
    });
});

function loadContentInFrame(url, containerId) {
    var container = document.getElementById(containerId);

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