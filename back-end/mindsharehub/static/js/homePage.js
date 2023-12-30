function scrolling() {
    const posts = document.querySelector('.posts')
    const fiends = document.querySelector('.friends')

    posts.addEventListener('focusin',(e) => {
        e.preventDefault();
        e.target.focus({preventScroll: true});

    })
    fiends.addEventListener('focusin',(e) => {
        e.preventDefault();
        e.target.focus({preventScroll: true});
    })
}
scrolling();


function openNewPost() {
    const modal = document.querySelector(".modal")

    modal.innerHTML = `
        <p onclick="closePostModal()" class="close-link">X</p>
        <h1 class="modal-title">Post</h1>
        <textarea class="modal-textarea" placeholder="Enter post here"> </textarea>
        <button class="submit-post" onclick="posting();">Post</botton>
        `
    modal.style.display = 'block'   

    // modal.addEventListener("focusout", () => {
    //     modal.style.display = 'none'   
    // })



}

function posting() {
    const modal = document.querySelector(".modal")
    const form = document.querySelector(".post-form")
    const text = document.querySelector(".modal-textarea")
    const input = document.querySelector('.new-post')

    input.value = text.value

    modal.style.display = 'none'
    form.submit()
}

function closePostModal() {
    const modal = document.querySelector(".modal")
    modal.style.display = 'none'
    
}

function showComments(pk) {
    const comments = document.querySelector(`.comments-${pk}`)

    if (comments.style.display === "flex") {
        comments.style.display = "none"
    }
    else {
        comments.style.display = "flex"
    }

}