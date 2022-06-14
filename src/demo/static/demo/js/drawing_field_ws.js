// WebSocket
let url = 'ws://' + window.location.host + '/ws_draw/';
const appSocket = new WebSocket(url);

// WS post logic
canvas.addEventListener("mousemove", function (e) {
    if (draw === true) {
        let json_image = getJsonImage()

        appSocket.onmessage = function (e) {
            let response = JSON.parse(e.data);
            updatePredictionTable(response)
        }

        appSocket.send(json_image);
    }
});