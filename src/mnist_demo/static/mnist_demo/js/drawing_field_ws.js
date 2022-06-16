// WebSocket init
let url = 'ws://' + window.location.host + '/ws_draw/';
const appSocket = new WebSocket(url);

// What to do when websocket gets message from server
appSocket.onmessage = function (e) {
    let response = JSON.parse(e.data);
    updatePredictionTable(response)
}

// Canvas mousemove listener
canvas.addEventListener("mousemove", function (e) {
    if (draw === true) {
        let json_image = getJsonImage()
        appSocket.send(json_image);
    }
});