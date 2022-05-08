console.log('Its working')

let theme = localStorage.getItem('theme')

if(theme == null){
	setTheme('light')
}else{
	setTheme(theme)
}

let themeDots = document.getElementsByClassName('theme-dot')


for (var i=0; themeDots.length > i; i++){
	themeDots[i].addEventListener('click', function(){
		let mode = this.dataset.mode
		console.log('Option clicked:', mode)
		setTheme(mode)
	})
}

function setTheme(mode){
	if(mode == 'light'){
		document.getElementById('theme-style').href = 'static/default.css'
		document.getElementById('a1').style = "color:black;text-align: center;line-height: 0;"
		document.getElementById('a2').style = "color:black;"
	}

	if(mode == 'blue'){
		document.getElementById('theme-style').href = 'static/blue.css'
		document.getElementById('a1').style = "color:white;text-align: center;line-height: 0;"
		document.getElementById('a2').style = "color:white;"
	}

	if(mode == 'green'){
		document.getElementById('theme-style').href = 'static/green.css'
		document.getElementById('a1').style = "color:white;text-align: center;line-height: 0;"
		document.getElementById('a2').style = "color:white;"
	}

	if(mode == 'purple'){
		document.getElementById('theme-style').href = 'static/purple.css'
		document.getElementById('a1').style = "color:white;text-align: center;line-height: 0;"
		document.getElementById('a2').style = "color:white;"
	}

	localStorage.setItem('theme', mode)
}