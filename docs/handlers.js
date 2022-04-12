/* Small script for handling events on the website.
   Copyright (c) 2022 mini-rose */

function get(query) {
	return document.querySelector(query)
}

function changeCSS(change_text, back, front, link) {
	let theme_change = get("#theme-change")
	let body = get("body")

	for (let a of document.querySelectorAll("a"))
		a.style.color = link

	theme_change.textContent = `(${change_text} theme)`
	theme_change.style.color = link
	body.style.background = back
	body.style.color = front
}

function changeTheme() {
	let theme
	if ((theme = localStorage.getItem("theme")) === null) {
		theme = "light"
		localStorage.setItem("theme", "light")
	}

	if (theme === "light")
		changeCSS("Dark", "white", "black", "blue")
	else
		changeCSS("Light", "#0f0f0f", "#dadada", "lightgreen")
}

document.querySelector("#theme-change").addEventListener("click", () => {
	localStorage.setItem(
		"theme",
		localStorage.getItem("theme") === "light" ? "dark" : "light"
	)
	changeTheme()
})
