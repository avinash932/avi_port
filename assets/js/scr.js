// toggleicon navbar

let menuIcon = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

menuIcon.onclick = () => {
    menuIcon.classList.toggle('bx-x');
    navbar.classList.toggle('active');
};




let sections = document.querySelectorAll('section');
let navlinks = document.querySelectorAll('hearder nav a');

window.onscroll = () => {
    sections.forEach(sec => {
        let top = window.scrollY;
        let offset = sec.offsetTop - 150;
        let height = sec.getAttribute('id');

        if (top >= offset && top < offset + height) {
            navlinks.forEach(links => {
                links.classList.remove('active');
                document.querySelector('header nav a[href*=' + id + ']').classList.add('active');
            });

        };
    });

    // navbar stickey

    let header = document.querySelector('header');

    header.classList.toggle('sticky', window.scrollY > 100);

    // remove togle onclick link

    menuIcon.classList.remove('bx-x');
    navbar.classList.remove('active');

};

// screll reveal

ScrollReveal({
    reset: true,
    distance: '80px',
    duration: 3000,
    delay: 200


});

ScrollReveal().reveal('.home-content, .heading', { origin: 'left' });
ScrollReveal().reveal('.home-content h1 , h2',{ origin: 'top' });
ScrollReveal().reveal('.about-image', { origin: 'right' });
ScrollReveal().reveal('.home-image, .service-container', { origin: 'bottom' });
ScrollReveal().reveal('.contact, form', { origin: 'top' });


// typed js

const typed = new Typed('.multiple-text', {
    strings: ['Web Developer', 'BCA student'],
    typeSpeed: 200,
    backSpeed: 50,
    backDelay: 100,
    loop: true
});