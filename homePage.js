function scrolling() {
    const posts = document.querySelector('.posts')
    const fiends = document.querySelector('.friends')

    posts.addEventListener('focusin',(e) => {
        console.log('posts');
        e.preventDefault();
        e.target.focus({preventScroll: true});

    })
    fiends.addEventListener('focusin',(e) => {
        console.log('fiends');
        e.preventDefault();
        e.target.focus({preventScroll: true});
    })
}
scrolling();
