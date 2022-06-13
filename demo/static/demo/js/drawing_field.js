// Canvas init
let canvas = document.getElementById("myCanvas"),
    context = canvas.getContext("2d");

// Canvas settings
context.strokeStyle = "white";
context.lineWidth = 10;
context.lineCap = "round";
context.lineJoin = "round";
context.fillStyle = "black";

// Drawing init params
let mouse = {x: 0, y: 0};
let draw = false;

// Buttons
let clearButton = document.getElementById("clearButton");
let uploadButton = document.getElementById("uploadButton");

// canvas event listeners
canvas.addEventListener("mousedown", function (e) {
    mouse.x = e.pageX - this.offsetLeft;
    mouse.y = e.pageY - this.offsetTop;
    draw = true;
    context.beginPath();
    context.moveTo(mouse.x, mouse.y);
});

canvas.addEventListener("mousemove", function (e) {
    if (draw === true) {
        mouse.x = e.pageX - this.offsetLeft;
        mouse.y = e.pageY - this.offsetTop;
        context.lineTo(mouse.x, mouse.y);
        context.stroke();
    }
});

canvas.addEventListener("mouseup", function (e) {
    mouse.x = e.pageX - this.offsetLeft;
    mouse.y = e.pageY - this.offsetTop;
    context.lineTo(mouse.x, mouse.y);
    context.stroke();
    context.closePath();
    draw = false;
});

// Drawing panel button event listeners
clearButton.addEventListener("mouseup", function (e) {
    context.clearRect(0, 0, canvas.width, canvas.height);
});

// AJAX post logic
uploadButton.addEventListener("mouseup", function (e) {
    let tcan = resizeTo(canvas, 0.1);
    let image = tcan.toDataURL('image/jpeg');
    let postObj = {
        'image': image.replace("data:image/jpeg;base64,", "")
    };
    let json_image = JSON.stringify(postObj);

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

function resizeTo(canvas, pct) {
    let tempCanvas = document.createElement("canvas");
    let tctx = tempCanvas.getContext("2d");
    let cw = canvas.width;
    let ch = canvas.height;

    tempCanvas.width = cw;
    tempCanvas.height = ch;

    tctx.drawImage(canvas, 0, 0);
    tempCanvas.width *= pct;
    tempCanvas.height *= pct;

    let tcontext = tempCanvas.getContext('2d');
    tcontext.drawImage(canvas, 0, 0, cw, ch, 0, 0, cw * pct, ch * pct);
    return tempCanvas
}

function updatePredictionTable(json_data) {
    let predictionTable = document.getElementById('predictionTable');
    let predictions = json_data.data.prediction;
    let innerTBody = '';
    for (let key in predictions) {
        let thTag = '<th scope="row">' + key + '</th>';
        let tdTag = '<td>' + predictions[key].toFixed(3) + '</td>';
        if (key == json_data.data.predicted_num) {
            innerTBody += '<tr class="text-center text-primary fw-bold">' + thTag + tdTag + '</tr>';
        } else {
            innerTBody += '<tr class="text-center">' + thTag + tdTag + '</tr>';
        }
    }
    predictionTable.innerHTML = innerTBody;
}
