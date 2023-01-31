function add_navbar(){
  var items = ['Home', "Nouns", "Verbs", "Convert Noun", "Convert Verb"]
  var urls = ['/', '/all_nouns', '/all_verbs', '/convert_noun', 'convert_verb']
  var navbar = document.getElementById("navbar")
  for (let i = 0; i < items.length; i++) {
    navbar.innerHTML += `<a href="${urls[i]}" class="navlink">${items[i]}</a>`
  }
}