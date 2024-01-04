function deleteNote(noteId){
    fetch('/delete-note',{
        method: 'POST',
        // turn the noteId into string
        body: JSON.stringify({noteId: noteId}),
    }).then((_res) => {
        // reload the window
        window.location.href = "/"
    });
}
