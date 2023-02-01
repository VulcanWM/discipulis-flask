function add_navbar(){
  var items = ['Home', "Nouns", "Verbs", "Convert Noun", "Convert Verb"]
  var urls = ['/', '/all_nouns', '/all_verbs', '/convert_noun', 'convert_verb']
  var navbar = document.getElementById("navbar")
  for (let i = 0; i < items.length; i++) {
    navbar.innerHTML += `<a href="${urls[i]}" class="navlink">${items[i]}</a>`
  }
}

function table_click(id, table){
    var cell_content = document.getElementById(id)
    var number = id.split(":")[0]
    var word_case = id.split(":")[1]
    if (cell_content.innerText == ""){
        cell_content.innerHTML = "<strong>" + table[number][word_case] + "</strong>"
    } else {
        cell_content.innerText = ""
        console.log(cell_content.innerHTML)
    }
}