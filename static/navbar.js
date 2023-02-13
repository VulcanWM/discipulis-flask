const flip_elements = [];
let test_mode = false;
window.addEventListener("load", function () {
    // Dark Mode
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        document.body.classList.add("dark-mode")
    }

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

	// Flip animation
	const elements = Array.from(document.querySelectorAll(".flip[data-hidden]"));
	for (let i = 0; i < elements.length; i++) {
		const td = elements[i];

		const visibleContent = td.textContent;
		td.textContent = "";

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
		hidden.textContent = td.getAttribute("data-hidden");
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
	const hideButton = document.getElementById("hide");
	if (hideButton) {
		hideButton.addEventListener("click", function () {
			for (let i = 0; i < flip_elements.length; i++) {
				flip_elements[i].removeAttribute("hidden");
				if (flip_elements[i].nextElementSibling) {
					flip_elements[i].parentElement.removeChild(flip_elements[i].nextElementSibling);
				}
				flip_elements[i].classList.remove("flip");
			}
			test_mode = false;
		});
	}

	// Show all
	const showButton = document.getElementById("show");
	if (showButton) {
		showButton.addEventListener("click", function () {
			for (let i = 0; i < flip_elements.length; i++) {
				flip_elements[i].removeAttribute("hidden");
				if (flip_elements[i].nextElementSibling) {
					flip_elements[i].parentElement.removeChild(flip_elements[i].nextElementSibling);
				}
				if (!flip_elements[i].classList.contains("flip")) {
					flip_elements[i].classList.add("flip");
				}
			}
			test_mode = false;
		});
	}
	var url = document.URL
	if (url.includes("/verb/") && url.includes("number=")){
	    var info = url.split("?")[1]
	    if (info.includes("tense")){
	        var person = ""
            var number = ""
            var tense = ""
            for (element_index in info.split("&")){
                var element = info.split("&")[element_index]
                if (element.includes("tense=")){
                    document.getElementById(element.split("=")[1]).scrollIntoView();
                    tense = element.split("=")[1]
                }
                else if (element.includes("person=")){
                    person = element.split("=")[1]
                }
                else if (element.includes("number=")){
                    number = element.split("=")[1]
                }
            }
            const cell_id = tense + ":" + person + " " + number
            const inner = document.getElementById(cell_id).querySelectorAll(".inner")[0];
            inner.classList.add("flip");
	    }
	}
	if (url.includes("/noun/") && url.includes("number=")){
	    var info = url.split("?")[1]
	    console.log(info)
	    var number = ""
	    var cell_case = ""
	    for (element_index in info.split("&")){
	        var element = info.split("&")[element_index]
	        if (element.includes("number=")){
	            document.getElementById(element.split("=")[1]).scrollIntoView();
	            number = element.split("=")[1]
	        }
	        else if (element.includes("case=")){
	            cell_case = element.split("=")[1]
	        }
	    }
	    const cell_id = number + ":" + cell_case
	    const inner = document.getElementById(cell_id).querySelectorAll(".inner")[0];
        inner.classList.add("flip");

	}
});

// Test mode
function test_mode_on() {
	if (test_mode) {
		return;
	}
	for (let i = 0; i < flip_elements.length; i++) {
		const word = flip_elements[i].parentElement.getAttribute("data-hidden");
		console.log(word)
		flip_elements[i].setAttribute("hidden", true);
		const container = document.createElement("div");
		const input = document.createElement("input");
		input.setAttribute("id", "input+" + i);
		container.append(input);
		const button = document.createElement("button");
		button.textContent = "enter";
		button.setAttribute("id", "button+" + i);
		button.addEventListener("click", function () {
		    var button_id_string = button.id
		    var button_id = button_id_string.split("+")[1]
		    var answer = flip_elements[button_id].parentElement.getAttribute("data-hidden")
			if (input.value.toLowerCase() === answer) {
				container.innerHTML = "<strong>" + answer + "</strong>";
			} else {
				container.innerHTML = "<span class='red'>" + answer + "</strong>";
			}
		});
		container.append(button);
		flip_elements[i].parentElement.append(container);
	}
	test_mode = true;
}