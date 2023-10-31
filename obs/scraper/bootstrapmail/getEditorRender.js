function selectTemplate(args){

    btnHtml = document.getElementById("viewCode")
    docCompiled = document.getElementById("compiledEditor")
    tmpl = document.getElementsByClassName('group text-white flex items-center space-x-2 hover:underline')
    
    for (let i = 0; i < tmpl.length; i++){
        if(tmpl[i].innerText == args){
            tmpl[i].click()
            btnHtml.click()
            
            return docCompiled.innerHTML
            
        }
    }

}


return selectTemplate(arguments[0])


