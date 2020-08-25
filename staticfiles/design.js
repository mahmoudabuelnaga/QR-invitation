function loadPixi(openImageDialog,event_id,svgPath){
var loaded_state;

var pixie = new Pixie({
	  baseUrl: 'http://127.0.0.1:8000',
	  tools: {
        shapes: {
            replaceDefault: true,
            items: [
                {
                    name: ' QR Code',
                    type: 'Path',
                    options: {
	                    lockUniScaling: false,
	                    path: svgPath,
	                   // path: 'M 24 29 L 24 30 L 25 30 L 25 29 z M 20 13 L 20 14 L 21 14 L 21 13 z M 10 32 L 10 33 L 11 33 L 11 32 z M 23 8 L 23 9 L 24 9 L 24 8 z M 21 24 L 21 25 L 22 25 L 22 24 z M 24 11 L 24 12 L 25 12 L 25 11 z M 22 23 L 22 24 L 23 24 L 23 23 z M 27 30 L 27 31 L 28 31 L 28 30 z M 14 11 L 14 12 L 15 12 L 15 11 z M 4 21 L 4 22 L 5 22 L 5 21 z M 28 18 L 28 19 L 29 19 L 29 18 z M 5 32 L 5 33 L 6 33 L 6 32 z M 29 19 L 29 20 L 30 20 L 30 19 z M 17 24 L 17 25 L 18 25 L 18 24 z M 7 6 L 7 7 L 8 7 L 8 6 z M 20 4 L 20 5 L 21 5 L 21 4 z M 10 27 L 10 28 L 11 28 L 11 27 z M 24 18 L 24 19 L 25 19 L 25 18 z M 22 14 L 22 15 L 23 15 L 23 14 z M 27 23 L 27 24 L 28 24 L 28 23 z M 25 19 L 25 20 L 26 20 L 26 19 z M 26 16 L 26 17 L 27 17 L 27 16 z M 13 13 L 13 14 L 14 14 L 14 13 z M 27 13 L 27 14 L 28 14 L 28 13 z M 14 18 L 14 19 L 15 19 L 15 18 z M 15 19 L 15 20 L 16 20 L 16 19 z M 28 25 L 28 26 L 29 26 L 29 25 z M 19 17 L 19 18 L 20 18 L 20 17 z M 17 17 L 17 18 L 18 18 L 18 17 z M 4 18 L 4 19 L 5 19 L 5 18 z M 7 15 L 7 16 L 8 16 L 8 15 z M 31 10 L 31 11 L 32 11 L 32 10 z M 32 5 L 32 6 L 33 6 L 33 5 z M 10 18 L 10 19 L 11 19 L 11 18 z M 23 22 L 23 23 L 24 23 L 24 22 z M 11 19 L 11 20 L 12 20 L 12 19 z M 24 25 L 24 26 L 25 26 L 25 25 z M 25 12 L 25 13 L 26 13 L 26 12 z M 27 10 L 27 11 L 28 11 L 28 10 z M 14 13 L 14 14 L 15 14 L 15 13 z M 12 29 L 12 30 L 13 30 L 13 29 z M 18 23 L 18 24 L 19 24 L 19 23 z M 14 23 L 14 24 L 15 24 L 15 23 z M 29 29 L 29 30 L 30 30 L 30 29 z M 19 14 L 19 15 L 20 15 L 20 14 z M 15 30 L 15 31 L 16 31 L 16 30 z M 4 9 L 4 10 L 5 10 L 5 9 z M 28 6 L 28 7 L 29 7 L 29 6 z M 5 4 L 5 5 L 6 5 L 6 4 z M 29 7 L 29 8 L 30 8 L 30 7 z M 8 15 L 8 16 L 9 16 L 9 15 z M 32 28 L 32 29 L 33 29 L 33 28 z M 7 26 L 7 27 L 8 27 L 8 26 z M 10 5 L 10 6 L 11 6 L 11 5 z M 23 31 L 23 32 L 24 32 L 24 31 z M 24 32 L 24 33 L 25 33 L 25 32 z M 10 31 L 10 32 L 11 32 L 11 31 z M 25 21 L 25 22 L 26 22 L 26 21 z M 23 5 L 23 6 L 24 6 L 24 5 z M 21 21 L 21 22 L 22 22 L 22 21 z M 12 4 L 12 5 L 13 5 L 13 4 z M 18 30 L 18 31 L 19 31 L 19 30 z M 14 30 L 14 31 L 15 31 L 15 30 z M 30 29 L 30 30 L 31 30 L 31 29 z M 4 32 L 4 33 L 5 33 L 5 32 z M 28 13 L 28 14 L 29 14 L 29 13 z M 29 8 L 29 9 L 30 9 L 30 8 z M 32 27 L 32 28 L 33 28 L 33 27 z M 30 7 L 30 8 L 31 8 L 31 7 z M 31 14 L 31 15 L 32 15 L 32 14 z M 8 28 L 8 29 L 9 29 L 9 28 z M 32 17 L 32 18 L 33 18 L 33 17 z M 20 15 L 20 16 L 21 16 L 21 15 z M 10 22 L 10 23 L 11 23 L 11 22 z M 25 30 L 25 31 L 26 31 L 26 30 z M 21 14 L 21 15 L 22 15 L 22 14 z M 24 5 L 24 6 L 25 6 L 25 5 z M 27 24 L 27 25 L 28 25 L 28 24 z M 26 15 L 26 16 L 27 16 L 27 15 z M 19 28 L 19 29 L 20 29 L 20 28 z M 4 23 L 4 24 L 5 24 L 5 23 z M 16 23 L 16 24 L 17 24 L 17 23 z M 5 22 L 5 23 L 6 23 L 6 22 z M 29 17 L 29 18 L 30 18 L 30 17 z M 6 29 L 6 30 L 7 30 L 7 29 z M 30 14 L 30 15 L 31 15 L 31 14 z M 4 13 L 4 14 L 5 14 L 5 13 z M 7 8 L 7 9 L 8 9 L 8 8 z M 32 8 L 32 9 L 33 9 L 33 8 z M 9 10 L 9 11 L 10 11 L 10 10 z M 21 7 L 21 8 L 22 8 L 22 7 z M 24 12 L 24 13 L 25 13 L 25 12 z M 22 12 L 22 13 L 23 13 L 23 12 z M 26 6 L 26 7 L 27 7 L 27 6 z M 14 16 L 14 17 L 15 17 L 15 16 z M 12 24 L 12 25 L 13 25 L 13 24 z M 15 5 L 15 6 L 16 6 L 16 5 z M 13 21 L 13 22 L 14 22 L 14 21 z M 28 27 L 28 28 L 29 28 L 29 27 z M 17 15 L 17 16 L 18 16 L 18 15 z M 30 25 L 30 26 L 31 26 L 31 25 z M 4 4 L 4 5 L 5 5 L 5 4 z M 7 17 L 7 18 L 8 18 L 8 17 z M 8 18 L 8 19 L 9 19 L 9 18 z M 32 7 L 32 8 L 33 8 L 33 7 z M 6 14 L 6 15 L 7 15 L 7 14 z M 7 23 L 7 24 L 8 24 L 8 23 z M 10 16 L 10 17 L 11 17 L 11 16 z M 24 27 L 24 28 L 25 28 L 25 27 z M 22 7 L 22 8 L 23 8 L 23 7 z M 26 9 L 26 10 L 27 10 L 27 9 z M 27 4 L 27 5 L 28 5 L 28 4 z M 13 30 L 13 31 L 14 31 L 14 30 z M 18 21 L 18 22 L 19 22 L 19 21 z M 14 21 L 14 22 L 15 22 L 15 21 z M 19 24 L 19 25 L 20 25 L 20 24 z M 15 32 L 15 33 L 16 33 L 16 32 z M 28 8 L 28 9 L 29 9 L 29 8 z M 31 21 L 31 22 L 32 22 L 32 21 z M 5 10 L 5 11 L 6 11 L 6 10 z M 32 30 L 32 31 L 33 31 L 33 30 z M 30 10 L 30 11 L 31 11 L 31 10 z M 9 12 L 9 13 L 10 13 L 10 12 z M 7 28 L 7 29 L 8 29 L 8 28 z M 8 23 L 8 24 L 9 24 L 9 23 z M 9 22 L 9 23 L 10 23 L 10 22 z M 10 29 L 10 30 L 11 30 L 11 29 z M 21 27 L 21 28 L 22 28 L 22 27 z M 24 8 L 24 9 L 25 9 L 25 8 z M 22 24 L 22 25 L 23 25 L 23 24 z M 12 6 L 12 7 L 13 7 L 13 6 z M 13 7 L 13 8 L 14 8 L 14 7 z M 18 28 L 18 29 L 19 29 L 19 28 z M 14 28 L 14 29 L 15 29 L 15 28 z M 15 25 L 15 26 L 16 26 L 16 25 z M 28 15 L 28 16 L 29 16 L 29 15 z M 16 26 L 16 27 L 17 27 L 17 26 z M 6 32 L 6 33 L 7 33 L 7 32 z M 31 16 L 31 17 L 32 17 L 32 16 z M 8 30 L 8 31 L 9 31 L 9 30 z M 32 19 L 32 20 L 33 20 L 33 19 z M 20 17 L 20 18 L 21 18 L 21 17 z M 10 20 L 10 21 L 11 21 L 11 20 z M 25 28 L 25 29 L 26 29 L 26 28 z M 23 12 L 23 13 L 24 13 L 24 12 z M 21 12 L 21 13 L 22 13 L 22 12 z M 14 7 L 14 8 L 15 8 L 15 7 z M 19 30 L 19 31 L 20 31 L 20 30 z M 15 14 L 15 15 L 16 15 L 16 14 z M 16 17 L 16 18 L 17 18 L 17 17 z M 5 20 L 5 21 L 6 21 L 6 20 z M 29 23 L 29 24 L 30 24 L 30 23 z M 19 4 L 19 5 L 20 5 L 20 4 z M 30 12 L 30 13 L 31 13 L 31 12 z M 7 10 L 7 11 L 8 11 L 8 10 z M 5 14 L 5 15 L 6 15 L 6 14 z M 32 10 L 32 11 L 33 11 L 33 10 z M 23 21 L 23 22 L 24 22 L 24 21 z M 21 5 L 21 6 L 22 6 L 22 5 z M 22 10 L 22 11 L 23 11 L 23 10 z M 26 4 L 26 5 L 27 5 L 27 4 z M 13 17 L 13 18 L 14 18 L 14 17 z M 12 26 L 12 27 L 13 27 L 13 26 z M 14 24 L 14 25 L 15 25 L 15 24 z M 19 13 L 19 14 L 20 14 L 20 13 z M 17 13 L 17 14 L 18 14 L 18 13 z M 15 29 L 15 30 L 16 30 L 16 29 z M 30 23 L 30 24 L 31 24 L 31 23 z M 4 6 L 4 7 L 5 7 L 5 6 z M 7 19 L 7 20 L 8 20 L 8 19 z M 31 30 L 31 31 L 32 31 L 32 30 z M 8 12 L 8 13 L 9 13 L 9 12 z M 9 17 L 9 18 L 10 18 L 10 17 z M 10 6 L 10 7 L 11 7 L 11 6 z M 8 26 L 8 27 L 9 27 L 9 26 z M 23 26 L 23 27 L 24 27 L 24 26 z M 25 24 L 25 25 L 26 25 L 26 24 z M 26 31 L 26 32 L 27 32 L 27 31 z M 18 27 L 18 28 L 19 28 L 19 27 z M 19 26 L 19 27 L 20 27 L 20 26 z M 30 30 L 30 31 L 31 31 L 31 30 z M 4 29 L 4 30 L 5 30 L 5 29 z M 28 10 L 28 11 L 29 11 L 29 10 z M 16 29 L 16 30 L 17 30 L 17 29 z M 31 23 L 31 24 L 32 24 L 32 23 z M 32 24 L 32 25 L 33 25 L 33 24 z M 6 7 L 6 8 L 7 8 L 7 7 z M 30 8 L 30 9 L 31 9 L 31 8 z M 7 30 L 7 31 L 8 31 L 8 30 z M 31 13 L 31 14 L 32 14 L 32 13 z M 10 9 L 10 10 L 11 10 L 11 9 z M 9 20 L 9 21 L 10 21 L 10 20 z M 24 28 L 24 29 L 25 29 L 25 28 z M 26 22 L 26 23 L 27 23 L 27 22 z M 24 10 L 24 11 L 25 11 L 25 10 z M 22 22 L 22 23 L 23 23 L 23 22 z M 27 31 L 27 32 L 28 32 L 28 31 z M 12 8 L 12 9 L 13 9 L 13 8 z M 13 5 L 13 6 L 14 6 L 14 5 z M 14 10 L 14 11 L 15 11 L 15 10 z M 15 27 L 15 28 L 16 28 L 16 27 z M 4 20 L 4 21 L 5 21 L 5 20 z M 28 17 L 28 18 L 29 18 L 29 17 z M 18 4 L 18 5 L 19 5 L 19 4 z M 6 30 L 6 31 L 7 31 L 7 30 z M 30 19 L 30 20 L 31 20 L 31 19 z M 7 7 L 7 8 L 8 8 L 8 7 z M 8 8 L 8 9 L 9 9 L 9 8 z M 20 19 L 20 20 L 21 20 L 21 19 z M 10 26 L 10 27 L 11 27 L 11 26 z M 22 17 L 22 18 L 23 18 L 23 17 z M 26 19 L 26 20 L 27 20 L 27 19 z M 14 5 L 14 6 L 15 6 L 15 5 z M 12 21 L 12 22 L 13 22 L 13 21 z M 4 27 L 4 28 L 5 28 L 5 27 z M 28 24 L 28 25 L 29 25 L 29 24 z M 16 19 L 16 20 L 17 20 L 17 19 z M 5 26 L 5 27 L 6 27 L 6 26 z M 29 21 L 29 22 L 30 22 L 30 21 z M 17 18 L 17 19 L 18 19 L 18 18 z M 30 26 L 30 27 L 31 27 L 31 26 z M 4 17 L 4 18 L 5 18 L 5 17 z M 7 12 L 7 13 L 8 13 L 8 12 z M 8 7 L 8 8 L 9 8 L 9 7 z M 32 4 L 32 5 L 33 5 L 33 4 z M 6 19 L 6 20 L 7 20 L 7 19 z M 20 10 L 20 11 L 21 11 L 21 10 z M 23 23 L 23 24 L 24 24 L 24 23 z M 11 16 L 11 17 L 12 17 L 12 16 z M 24 24 L 24 25 L 25 25 L 25 24 z M 22 8 L 22 9 L 23 9 L 23 8 z M 20 32 L 20 33 L 21 33 L 21 32 z M 26 10 L 26 11 L 27 11 L 27 10 z M 12 28 L 12 29 L 13 29 L 13 28 z M 15 9 L 15 10 L 16 10 L 16 9 z M 13 25 L 13 26 L 14 26 L 14 25 z M 28 31 L 28 32 L 29 32 L 29 31 z M 16 10 L 16 11 L 17 11 L 17 10 z M 29 30 L 29 31 L 30 31 L 30 30 z M 19 15 L 19 16 L 20 16 L 20 15 z M 17 11 L 17 12 L 18 12 L 18 11 z M 15 31 L 15 32 L 16 32 L 16 31 z M 4 8 L 4 9 L 5 9 L 5 8 z M 16 32 L 16 33 L 17 33 L 17 32 z M 8 14 L 8 15 L 9 15 L 9 14 z M 6 10 L 6 11 L 7 11 L 7 10 z M 9 15 L 9 16 L 10 16 L 10 15 z M 10 4 L 10 5 L 11 5 L 11 4 z M 23 28 L 23 29 L 24 29 L 24 28 z M 24 23 L 24 24 L 25 24 L 25 23 z M 20 23 L 20 24 L 21 24 L 21 23 z M 10 30 L 10 31 L 11 31 L 11 30 z M 18 25 L 18 26 L 19 26 L 19 25 z M 19 20 L 19 21 L 20 21 L 20 20 z M 4 31 L 4 32 L 5 32 L 5 31 z M 28 12 L 28 13 L 29 13 L 29 12 z M 30 6 L 30 7 L 31 7 L 31 6 z M 7 32 L 7 33 L 8 33 L 8 32 z M 31 15 L 31 16 L 32 16 L 32 15 z M 32 16 L 32 17 L 33 17 L 33 16 z M 21 15 L 21 16 L 22 16 L 22 15 z M 24 4 L 24 5 L 25 5 L 25 4 z M 22 20 L 22 21 L 23 21 L 23 20 z M 12 10 L 12 11 L 13 11 L 13 10 z M 13 11 L 13 12 L 14 12 L 14 11 z M 18 32 L 18 33 L 19 33 L 19 32 z M 19 29 L 19 30 L 20 30 L 20 29 z M 4 22 L 4 23 L 5 23 L 5 22 z M 28 19 L 28 20 L 29 20 L 29 19 z M 18 10 L 18 11 L 19 11 L 19 10 z M 16 22 L 16 23 L 17 23 L 17 22 z M 5 23 L 5 24 L 6 24 L 6 23 z M 6 28 L 6 29 L 7 29 L 7 28 z M 4 12 L 4 13 L 5 13 L 5 12 z M 31 4 L 31 5 L 32 5 L 32 4 z M 8 10 L 8 11 L 9 11 L 9 10 z M 32 15 L 32 16 L 33 16 L 33 15 z M 20 5 L 20 6 L 21 6 L 21 5 z M 10 24 L 10 25 L 11 25 L 11 24 z M 23 16 L 23 17 L 24 17 L 24 16 z M 27 22 L 27 23 L 28 23 L 28 22 z M 12 17 L 12 18 L 13 18 L 13 17 z M 26 17 L 26 18 L 27 18 L 27 17 z M 12 23 L 12 24 L 13 24 L 13 23 z M 13 22 L 13 23 L 14 23 L 14 22 z M 28 26 L 28 27 L 29 27 L 29 26 z M 16 13 L 16 14 L 17 14 L 17 13 z M 5 24 L 5 25 L 6 25 L 6 24 z M 29 27 L 29 28 L 30 28 L 30 27 z M 19 16 L 19 17 L 20 17 L 20 16 z M 17 16 L 17 17 L 18 17 L 18 16 z M 6 23 L 6 24 L 7 24 L 7 23 z M 30 24 L 30 25 L 31 25 L 31 24 z M 5 18 L 5 19 L 6 19 L 6 18 z M 32 6 L 32 7 L 33 7 L 33 6 z M 6 17 L 6 18 L 7 18 L 7 17 z M 9 4 L 9 5 L 10 5 L 10 4 z M 7 20 L 7 21 L 8 21 L 8 20 z M 23 25 L 23 26 L 24 26 L 24 25 z M 21 9 L 21 10 L 22 10 L 22 9 z M 11 18 L 11 19 L 12 19 L 12 18 z M 24 26 L 24 27 L 25 27 L 25 26 z M 22 6 L 22 7 L 23 7 L 23 6 z M 26 8 L 26 9 L 27 9 L 27 8 z M 22 32 L 22 33 L 23 33 L 23 32 z M 15 11 L 15 12 L 16 12 L 16 11 z M 13 31 L 13 32 L 14 32 L 14 31 z M 18 20 L 18 21 L 19 21 L 19 20 z M 16 4 L 16 5 L 17 5 L 17 4 z M 29 28 L 29 29 L 30 29 L 30 28 z M 19 25 L 19 26 L 20 26 L 20 25 z M 4 10 L 4 11 L 5 11 L 5 10 z M 28 7 L 28 8 L 29 8 L 29 7 z M 29 6 L 29 7 L 30 7 L 30 6 z M 32 29 L 32 30 L 33 30 L 33 29 z M 6 8 L 6 9 L 7 9 L 7 8 z M 7 29 L 7 30 L 8 30 L 8 29 z M 10 10 L 10 11 L 11 11 L 11 10 z M 20 25 L 20 26 L 21 26 L 21 25 z M 10 28 L 10 29 L 11 29 L 11 28 z M 25 20 L 25 21 L 26 21 L 26 20 z M 22 27 L 22 28 L 23 28 L 23 27 z M 12 5 L 12 6 L 13 6 L 13 5 z M 19 22 L 19 23 L 20 23 L 20 22 z M 15 22 L 15 23 L 16 23 L 16 22 z M 17 28 L 17 29 L 18 29 L 18 28 z M 30 4 L 30 5 L 31 5 L 31 4 z M 8 29 L 8 30 L 9 30 L 9 29 z M 32 18 L 32 19 L 33 19 L 33 18 z M 9 32 L 9 33 L 10 33 L 10 32 z M 20 16 L 20 17 L 21 17 L 21 16 z M 25 29 L 25 30 L 26 30 L 26 29 z M 23 13 L 23 14 L 24 14 L 24 13 z M 26 26 L 26 27 L 27 27 L 27 26 z M 24 6 L 24 7 L 25 7 L 25 6 z M 12 12 L 12 13 L 13 13 L 13 12 z M 14 6 L 14 7 L 15 7 L 15 6 z M 4 24 L 4 25 L 5 25 L 5 24 z M 28 21 L 28 22 L 29 22 L 29 21 z M 18 8 L 18 9 L 19 9 L 19 8 z M 16 16 L 16 17 L 17 17 L 17 16 z M 5 21 L 5 22 L 6 22 L 6 21 z M 17 21 L 17 22 L 18 22 L 18 21 z M 6 26 L 6 27 L 7 27 L 7 26 z M 5 15 L 5 16 L 6 16 L 6 15 z M 8 4 L 8 5 L 9 5 L 9 4 z M 32 9 L 32 10 L 33 10 L 33 9 z M 10 14 L 10 15 L 11 15 L 11 14 z M 23 18 L 23 19 L 24 19 L 24 18 z M 11 23 L 11 24 L 12 24 L 12 23 z M 24 13 L 24 14 L 25 14 L 25 13 z M 25 16 L 25 17 L 26 17 L 26 16 z M 26 7 L 26 8 L 27 8 L 27 7 z M 13 18 L 13 19 L 14 19 L 14 18 z M 27 14 L 27 15 L 28 15 L 28 14 z M 12 25 L 12 26 L 13 26 L 13 25 z M 28 28 L 28 29 L 29 29 L 29 28 z M 14 27 L 14 28 L 15 28 L 15 27 z M 29 25 L 29 26 L 30 26 L 30 25 z M 19 18 L 19 19 L 20 19 L 20 18 z M 17 14 L 17 15 L 18 15 L 18 14 z M 6 21 L 6 22 L 7 22 L 7 21 z M 30 22 L 30 23 L 31 23 L 31 22 z M 4 5 L 4 6 L 5 6 L 5 5 z M 7 16 L 7 17 L 8 17 L 8 16 z M 5 16 L 5 17 L 6 17 L 6 16 z M 8 19 L 8 20 L 9 20 L 9 19 z M 6 15 L 6 16 L 7 16 L 7 15 z M 9 18 L 9 19 L 10 19 L 10 18 z M 7 22 L 7 23 L 8 23 L 8 22 z M 11 12 L 11 13 L 12 13 L 12 12 z M 24 20 L 24 21 L 25 21 L 25 20 z M 22 30 L 22 31 L 23 31 L 23 30 z M 12 32 L 12 33 L 13 33 L 13 32 z M 13 29 L 13 30 L 14 30 L 14 29 z M 18 26 L 18 27 L 19 27 L 19 26 z M 16 6 L 16 7 L 17 7 L 17 6 z M 19 27 L 19 28 L 20 28 L 20 27 z M 4 28 L 4 29 L 5 29 L 5 28 z M 16 28 L 16 29 L 17 29 L 17 28 z M 31 20 L 31 21 L 32 21 L 32 20 z M 29 4 L 29 5 L 30 5 L 30 4 z M 32 31 L 32 32 L 33 32 L 33 31 z M 6 6 L 6 7 L 7 7 L 7 6 z M 10 8 L 10 9 L 11 9 L 11 8 z M 8 32 L 8 33 L 9 33 L 9 32 z M 9 21 L 9 22 L 10 22 L 10 21 z M 24 9 L 24 10 L 25 10 L 25 9 z M 27 28 L 27 29 L 28 29 L 28 28 z M 13 6 L 13 7 L 14 7 L 14 6 z M 14 29 L 14 30 L 15 30 L 15 29 z M 15 24 L 15 25 L 16 25 L 16 24 z M 16 27 L 16 28 L 17 28 L 17 27 z M 32 22 L 32 23 L 33 23 L 33 22 z M 7 4 L 7 5 L 8 5 L 8 4 z M 31 19 L 31 20 L 32 20 L 32 19 z M 32 12 L 32 13 L 33 13 L 33 12 z M 26 24 L 26 25 L 27 25 L 27 24 z M 24 16 L 24 17 L 25 17 L 25 16 z M 27 21 L 27 22 L 28 22 L 28 21 z M 12 14 L 12 15 L 13 15 L 13 14 z M 14 4 L 14 5 L 15 5 L 15 4 z M 15 17 L 15 18 L 16 18 L 16 17 z M 4 26 L 4 27 L 5 27 L 5 26 z M 28 23 L 28 24 L 29 24 L 29 23 z M 6 24 L 6 25 L 7 25 L 7 24 z M 30 13 L 30 14 L 31 14 L 31 13 z M 4 16 L 4 17 L 5 17 L 5 16 z M 7 13 L 7 14 L 8 14 L 8 13 z M 8 6 L 8 7 L 9 7 L 9 6 z M 6 18 L 6 19 L 7 19 L 7 18 z M 20 9 L 20 10 L 21 10 L 21 9 z M 10 12 L 10 13 L 11 13 L 11 12 z M 23 20 L 23 21 L 24 21 L 24 20 z M 21 4 L 21 5 L 22 5 L 22 4 z M 11 17 L 11 18 L 12 18 L 12 17 z M 20 31 L 20 32 L 21 32 L 21 31 z M 21 30 L 21 31 L 22 31 L 22 30 z M 26 5 L 26 6 L 27 6 L 27 5 z M 12 27 L 12 28 L 13 28 L 13 27 z M 15 6 L 15 7 L 16 7 L 16 6 z M 13 26 L 13 27 L 14 27 L 14 26 z M 28 30 L 28 31 L 29 31 L 29 30 z M 18 17 L 18 18 L 19 18 L 19 17 z M 16 9 L 16 10 L 17 10 L 17 9 z M 19 12 L 19 13 L 20 13 L 20 12 z M 17 12 L 17 13 L 18 13 L 18 12 z M 4 7 L 4 8 L 5 8 L 5 7 z M 28 4 L 28 5 L 29 5 L 29 4 z M 7 24 L 7 25 L 8 25 L 8 24 z M 10 7 L 10 8 L 11 8 L 11 7 z M 9 26 L 9 27 L 10 27 L 10 26 z M 20 22 L 20 23 L 21 23 L 21 22 z M 26 28 L 26 29 L 27 29 L 27 28 z M 22 28 L 22 29 L 23 29 L 23 28 z M 18 24 L 18 25 L 19 25 L 19 24 z M 19 21 L 19 22 L 20 22 L 20 21 z M 30 31 L 30 32 L 31 32 L 31 31 z M 4 30 L 4 31 L 5 31 L 5 30 z M 16 30 L 16 31 L 17 31 L 17 30 z M 31 22 L 31 23 L 32 23 L 32 22 z M 29 10 L 29 11 L 30 11 L 30 10 z M 6 4 L 6 5 L 7 5 L 7 4 z M 31 12 L 31 13 L 32 13 L 32 12 z',
                    }
                },
                {
                name: 'circle',
                type:'Circle'
                }
            ]
        }
	  },
	  ui: {
  		openImageDialog: {
  			show: openImageDialog
  		},
  		 nav: {
            position: 'top',
            replaceDefault: true,
            items: [
                {name: 'QR Code', icon: 'qrcode', action: 'shapes'},
                {name: 'filter', icon: 'filter-custom', action: 'filter'},
                {type: 'separator'},
                {name: 'resize', icon: 'resize-custom', action: 'resize'},
                {name: 'crop', icon: 'crop-custom', action: 'crop'},
                {name: 'transform', icon: 'transform-custom', action: 'transform'},
                {type: 'separator'},

                {name: 'text', icon: 'text-box-custom', action: 'text'},
                {name: 'stickers', icon: 'sticker-custom', action: 'stickers'},
                {name: 'frame', icon: 'frame-custom', action: 'frame'},
                {type: 'separator'},
                {name: 'corners', icon: 'rounded-corner-custom', action: 'corners'},
                {name: 'background', icon: 'background-custom', action: 'background'},
            ],
        }
  	  },
	  objectDefaults: {
        global: {
            fill: 'rgb(0, 0, 0)',
        }
       },
      onLoad: function() {
      setTimeout(function() {
      $.ajax({
        url: '/get_image_state',
        data: {'event_id': event_id},
        dataType: 'json',
        success: function (data) {
          if (data.has_values) {
             loaded_state=data.state;
             pixie.loadState(data.state).then(function() {});
          }
		}
      });
	 });
		},
     onSave: function(data, name) {
            var state = pixie.getState();
            if(loaded_state==state){
            console.log('equal state');
            timeFunction(0);
            }
            else {
            console.log('also equal state');
            pixie.http().post('../save_image_state/' +event_id, {state: state}).subscribe(function(response) {});
            pixie.http().post('../convert_data_to_image/' + event_id, {name: name, data: data}).subscribe(function(response) {});
             $("#wait").css("display", "block");
             timeFunction(500);
            }

            },
            });
}
function timeFunction(ms) {
setTimeout(function(){
window.location.href='../events';
}, ms);
}

