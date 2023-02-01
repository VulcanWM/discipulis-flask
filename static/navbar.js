// Google Analytics

var Script1 = document.createElement("script");
Script1.setAttribute("async", null);
Script1.src =
"https://www.googletagmanager.com/gtag/js?id=G-LKMN9BPTZC";
document.head.appendChild(Script1);

var Script2 = document.createElement("script");
Script2.innerText =
"window.dataLayer = window.dataLayer || [];function gtag(){dataLayer.push(arguments);}gtag('js', new Date());gtag('config', 'G-LKMN9BPTZC');";
document.head.appendChild(Script2);


// Adding navigation bar
function add_navbar(){
  var items = ['Home', "Nouns", "Verbs", "Convert Noun", "Convert Verb"]
  var urls = ['/', '/all_nouns', '/all_verbs', '/convert_noun', 'convert_verb']
  var navbar = document.getElementById("navbar")
  for (let i = 0; i < items.length; i++) {
    navbar.innerHTML += `<a href="${urls[i]}" class="navlink">${items[i]}</a>`
  }
}


// table functions
function table_click(id, table){
    var cell_content = document.getElementById(id)
    var number = id.split(":")[0]
    var word_case = id.split(":")[1]
    if (cell_content.innerText == ""){
        cell_content.innerHTML = "<strong>" + table[number][word_case] + "</strong>"
    } else {
        cell_content.innerText = ""
    }
}

function table_hide_all(){
    var tds = document.getElementsByTagName("td")
    for (index in tds){
        if (index.length < 4){
            if (tds[index].id.includes(":")){
                tds[index].innerText = ""
            }
        }
    }
}

function table_show_all(table){
    var tds = document.getElementsByTagName("td")
    for (index in tds){
        if (index.length < 4){
            if (tds[index].id.includes(":")){
                var cell_content = tds[index]
                var number = cell_content.id.split(":")[0]
                var word_case = cell_content.id.split(":")[1]
                cell_content.innerHTML = "<strong>" + table[number][word_case] + "</strong>"
            }
        }
    }
}