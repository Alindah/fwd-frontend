function test() {
	// https://javascript.info/fetch
	url = "http://127.0.0.1:5000/"
	let promise = await fetch(url)

	if (response.ok) {
		let text = await response.text();
	}
	else {
		alert("HTTP-Error: " + response.status);
	}
	console.log("retrieved " + text);
}