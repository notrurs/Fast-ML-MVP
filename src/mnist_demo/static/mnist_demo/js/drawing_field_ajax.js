let uploadButton = document.getElementById("uploadButton");

// AJAX post logic
uploadButton.addEventListener("mouseup", function (e) {
    let json_image = getJsonImage()

    fetch("/ajax_draw/", {
        method: 'post',
        body: json_image,
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': Cookies.get('csrftoken')
        }
    }).then((response) => {
        return response.json()
    }).then((res) => {
        updatePredictionTable(res)
    }).catch((error) => {
        console.log(error)
    })
});
