// function toggleContentEditable(noteId) {
//     var titleTextElement = document.getElementById("title_text_" + noteId);

//     if (titleTextElement.contentEditable === "true") {
//         titleTextElement.contentEditable = "false";
//     } else {
//         titleTextElement.contentEditable = "true";
//     }
// }

// function toggleContentEditable(noteId) {
//     var titleTextElement = document.getElementById("title_text_" + noteId);
//     var editButton = document.getElementById("e_" + noteId).querySelector("img");

//     if (titleTextElement.contentEditable === "true") {
//         titleTextElement.contentEditable = "false";
//         // Змінити зображення, коли режим редагування вимкнено
//         editButton.src = "{% static 'textlist/images/save.svg' %}";
//     } else {
//         titleTextElement.contentEditable = "true";
//         // Змінити зображення, коли режим редагування увімкнено
//         editButton.src = "{% static 'textlist/images/editing.svg' %}";
//     }
// }


// function deleteNote(noteId) {
//     var elementToDelete = document.getElementById("d_" + noteId).closest('.vertical-block-todo');
    
//     $(elementToDelete).animate({ left: "-1000px", opacity: 0}, 600, function() {
//         elementToDelete.remove();
//     }); 
// }




