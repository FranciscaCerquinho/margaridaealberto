window.addEventListener("scroll", reveal);
window.addEventListener("load",updateAllProgressBars)

function reveal(){
    var reveals = document.querySelectorAll('.appearing')

    for (let reveal of reveals){
        let windowHeight = window.innerHeight;
        let revealTop = reveal.getBoundingClientRect().top;
        let revealPoint = 150;

        if (revealTop < windowHeight - revealPoint){
            reveal.classList.add('active');
        }else{
            reveal.classList.remove('active');
        }
    }
}

function changeNavbarDisplay(){
    let navbar = document.getElementById('collapsingNavbar');
    let body = document.getElementById('overlay');

    if (navbar.classList.contains("show")) {
        navbar.classList.remove("show");
        body.classList.remove("background_over")
    } else {
        navbar.classList.add("show");
        body.classList.add("background_over")
    }
}

function updateProgressBar(element){
    element.style.opacity = 1;
    element.style.width = element.getAttribute('data-done') + '%';
}

function updateAllProgressBars(){
    let progressBars = document.querySelectorAll('.progressBar-done');
    for (let element of progressBars){
        updateProgressBar(element)
    }
}

function redirectTo(ele){
    window.location.href = ele.dataset.url;
}
