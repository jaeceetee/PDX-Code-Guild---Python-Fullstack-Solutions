const inputText = document.querySelector("#input")
const addButton = document.querySelector("#add-button")
var listTodo = document.querySelector("#to-do")
var listCompleted = document.querySelector("#completed-list")
var headingTodo = document.querySelector("#to-do-heading")
var headingCompleted = document.querySelector("#completed-heading")



inputText.addEventListener("keyup", function (event) {
    //Check if key is ENTER. If ENTER, trigger the ADD button
    if (event.keyCode == 13) {
        addButton.click()
        inputText.value = null
    }
    if (inputText.value.length > 0) {
        addButton.disabled = false
    }
    else {
        addButton.disabled = true
    }
})

addButton.addEventListener("click", function() {
    
    let li = document.createElement('li')
    let btnComplete = document.createElement('button')
    let btnDelete = document.createElement('button')
    let btnGroup = document.createElement('div')
    btnGroup.className = 'btn-Group'
    btnComplete.className = 'btn btn-warning'
    btnDelete.className = 'btn btn-danger'
    li.innerText = inputText.value
    inputText.value = null;
    btnComplete.textContent = "Completed"
    btnComplete.addEventListener("click", function() {
        let liCompleted = document.createElement('li')
        while (li.lastChild.nodeName == "DIV"){
            li.lastChild.remove()
        }        
        liCompleted.innerText = li.innerText
        listCompleted.appendChild(liCompleted)
        li.remove()
        checkToDoList()
        checkCompletedList()
    })
    btnDelete.textContent = "Delete"
    btnDelete.addEventListener("click", function() {
        li.remove()
        checkToDoList()

    })
    listTodo.appendChild(li)
    li.appendChild(btnGroup)
    btnGroup.appendChild(btnComplete)
    btnGroup.appendChild(btnDelete)
    checkToDoList()
}) 

function checkToDoList() {
    if (listTodo.hasChildNodes){
        listTodo.hidden = false
        headingTodo.hidden = false
    }
    else {
        listTodo.hidden = true
        headingTodo.hidden = true
    }
}

function checkCompletedList() {
    if (listCompleted.hasChildNodes){
        listCompleted.hidden = false
        headingCompleted.hidden = false
    }
    else {
        listCompleted.hidden = true
        headingCompleted.hidden = true
    }
}