const flip_elements = [];
window.addEventListener("load", function () {
	// Google Analytics
	const Script1 = document.createElement("script");
	Script1.setAttribute("async", null);
	Script1.setAttribute("src", "https://www.googletagmanager.com/gtag/js?id=G-LKMN9BPTZC");
	document.head.append(Script1);

	const Script2 = document.createElement("script");
	Script2.innerText = "window.dataLayer = window.dataLayer || [];function gtag(){dataLayer.push(arguments);}gtag('js', new Date());gtag('config', 'G-LKMN9BPTZC');";
	document.head.append(Script2);

	// Adding navigation bar
	const items = ["Home", "Nouns", "Verbs", "Convert Noun", "Convert Verb", "Browse Sets"];
	const urls = ["/", "/all_nouns", "/all_verbs", "/convert_noun", "convert_verb", "/browse_sets"];
	const navbar = document.createElement("nav");
	navbar.classList.add("mobile-nav");
	navbar.setAttribute("id", "navbar");
	for (let i = 0; i < items.length; i++) {
		navbar.innerHTML += `<a href="${urls[i]}" class="navlink">${items[i]}</a>`;
	}
	document.body.prepend(navbar);
	// Flip Animation
	const elements = Array.from(document.querySelectorAll(".flip[data-hidden]"));
	for (let i = 0; i < elements.length; i++) {
		const td = elements[i];

		const visibleContent = td.textContent;
		td.textContent = "";

		const hiddenContent = td.getAttribute("data-hidden");
		td.removeAttribute("data-hidden");

		const inner = document.createElement("div");
		inner.classList.add("inner");

		const front = document.createElement("div");
		front.classList.add("front");

		const visible = document.createElement("p");
		visible.textContent = visibleContent;
		front.append(visible);

		const back = document.createElement("div");
		back.classList.add("back");

		const hidden = document.createElement("p");
		hidden.textContent = hiddenContent;
		back.append(hidden);

		inner.append(front);
		inner.append(back);
		td.addEventListener("click", function () {
			inner.classList.toggle("flip");
		});

		td.append(inner);
		flip_elements.push(inner);
	}

	// Hide all
	document.getElementById("hide").addEventListener("click", function () {
		for (let i = 0; i < flip_elements.length; i++) {
			flip_elements[i].classList.remove("flip");
		}
	});
	// Show all
	document.getElementById("show").addEventListener("click", function () {
		for (let i = 0; i < flip_elements.length; i++) {
			if (!flip_elements[i].classList.contains("flip")) {
				flip_elements[i].classList.add("flip");
			}
		}
	});
});

// Test mode
let test_mode = false;
function test_mode_on(table) {
	const tds = Array.from(document.getElementsByTagName("td"));
	for (let i = 0; i < tds.length; i++) {
		const word = tds[i].getAttribute("data-hidden");
		if (word) {
			const inner = tds[i].innerHTML;
			tds[i].innerHTML = "";
			const td_index_id = i;
			const input = document.createElement("input");
			input.setAttribute("id", "input+" + td_index_id);
			tds[i].append(input);
			const button = document.createElement("button");
			const text = document.createTextNode("enter");
			button.append(text);
			button.setAttribute("id", "button+" + td_index_id);
			button.addEventListener("click", function () {
				if (input.value.toLowerCase() === tds[td_index_id].getAttribute("data-hidden")) {
					tds[td_index_id].innerHTML = "<strong>" + tds[td_index_id].getAttribute("data-hidden") + "</strong>";
				} else {
					tds[td_index_id].innerHTML = "<span class='red'>" + tds[td_index_id].getAttribute("data-hidden") + "</strong>";
				}
			});
			tds[i].append(button);
		}
	}
	test_mode = true;
}