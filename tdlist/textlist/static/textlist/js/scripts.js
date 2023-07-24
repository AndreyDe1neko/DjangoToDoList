function toggleContentEditable(noteId) {
    var titleTextElement = document.getElementById("title_text_" + noteId);

    if (titleTextElement.contentEditable === "true") {
        titleTextElement.contentEditable = "false";
    } else {
        titleTextElement.contentEditable = "true";
    }
}


function deleteNote(noteId) {
    var elementToDelete = document.getElementById("d_" + noteId).closest('.vertical-block-todo');
    
    $(elementToDelete).animate({ left: "-1000px", opacity: 0}, 600, function() {
        elementToDelete.remove();
    }); 
}




