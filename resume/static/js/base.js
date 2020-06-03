
const [red, green, blue] = [251, 243, 251];

window.addEventListener('scroll', () => {
  let y = 1 + (window.scrollY || window.pageYOffset) / 50
  y = y < 1 ? 1 : y // ensure y is always >= 1 (due to Safari's elastic scroll)
  const [r, g, b] = [red-2*y, green-y, blue-y].map(Math.round)
  
  if(y==1){
    document.body.style.backgroundColor = `rgb(${red}, ${green}, ${blue}, ${0.85})`
  }
  else{
    document.body.style.backgroundColor = `rgb(${r}, ${g}, ${b}, ${0.85})`
  }
})

window.onscroll = function() {myFunction()};

// Get the navbar
var navbar = document.getElementById("navbar");

// Get the offset position of the navbar
var sticky = navbar.offsetTop;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}

const navSlide = () => {
  const burger = document.querySelector('.burger');
  const nav = document.querySelector('.nav__links');
  const navLinks = document.querySelectorAll('.nav__links li');

  burger.addEventListener('click', () => {
    nav.classList.toggle('nav-active');
    navLinks.forEach((link, index) => {
      if(link.style.animation) {
        link.style.animation = ``;
      }
      else {
        link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.6}s`;
      }
    });

    burger.classList.toggle('toggle');
  });

  
}

navSlide();