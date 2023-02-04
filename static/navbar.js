const flip_elements = [];
window.addEventListener("load", function() {
	// Google Analytics
	const Script1 = document.createElement("script");
	Script1.setAttribute("async", null);
	Script1.setAttribute("src", "https://www.googletagmanager.com/gtag/js?id=G-LKMN9BPTZC");
	document.head.append(Script1);

	const Script2 = document.createElement("script");
	Script2.innerText = "window.dataLayer = window.dataLayer || [];function gtag(){dataLayer.push(arguments);}gtag('js', new Date());gtag('config', 'G-LKMN9BPTZC');";
	document.head.append(Script2);
	
	// Adding navigation bar
	const items = ["Home", "Nouns", "Verbs", "Convert Noun", "Convert Verb"];
	const urls = ["/", "/all_nouns", "/all_verbs", "/convert_noun", "convert_verb"];
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
		td.addEventListener("click", function() {
			inner.classList.toggle("flip");
		});

		td.append(inner);
		flip_elements.push(inner);
	}
});

// table functions

test_mode = false;

function table_hide_all() {
	for (let i = 0; i < flip_elements.length; i++) {
		flip_elements[i].classList.remove("flip");
	}
}

function table_show_all(table) {
	for (let i = 0; i < flip_elements.length; i++) {
		if (!flip_elements[i].classList.contains("flip")) {
			flip_elements[i].classList.add("flip");
		}
	}
}

function test_mode_on(table) {
	const tds = document.getElementsByTagName("td");
	for (index in tds) {
		if (index.length < 4) {
			if (tds[index].id.includes(":")) {
			    console.log(tds[index].id)
				tds[index].innerHTML = "";
				let td_index_id = tds[index].id;
				const input = document.createElement("input");
				input.setAttribute("id", "input+" + td_index_id);
				tds[index].append(input);
				const button = document.createElement("BUTTON");
				const text = document.createTextNode("enter");
				button.append(text);
				button.setAttribute("id", "button+" + td_index_id);
				button.addEventListener("click", function() {
					submit_test(td_index_id, table);
				});
				tds[index].append(button);
			}
		}
	}
	test_mode = true;
}

function submit_test(id, table) {
	if (test_mode == true) {
		const guess = document.getElementById("input+" + id).value;
		const number = id.split(":")[0];
		const word_case = id.split(":")[1];
		const answer = table[number][word_case];
		const cell_element = document.getElementById("input+" + id);
		console.log(cell_element);
		if (guess.toLowerCase() == answer) {
			document.getElementById(id).innerHTML = "<strong>" + answer + "</strong>";
		} else {
			document.getElementById(id).innerHTML = "<span class='red'>" + answer + "</strong>";
		}
	}
}
