// navbar
let subMenu = document.getElementById("subMenu");
function toggleMenu() {
	subMenu.classList.toggle("open-menu");
}



// gallery



// If you want to add a smooth scrolling effect to the text popup
// $('a[href^="#"]').on('click', function(event) {
//     var target = $(this.getAttribute('href'));
//     if( target.length ) {
//       event.preventDefault();
//       $('html, body').animate({
//         scrollTop: target.offset().top
//       }, 1000);
//     }
//   });

// slider 2
// $('#recipeCarousel').carousel({
//     interval: 10000
//   })

//   $('.carousel .carousel-item').each(function(){
//       var minPerSlide = 3;
//       var next = $(this).next();
//       if (!next.length) {
//       next = $(this).siblings(':first');
//       }
//       next.children(':first-child').clone().appendTo($(this));

//       for (var i=0;i<minPerSlide;i++) {
//           next=next.next();
//           if (!next.length) {
//               next = $(this).siblings(':first');
//             }

//           next.children(':first-child').clone().appendTo($(this));
//         }
//   });

// Get all the carousel items
// Get all the carousel items
// var carouselItems = document.querySelectorAll('.carousel .carousel-item');

// // Loop through each carousel item
// carouselItems.forEach(function(item) {
//   var next = item.nextElementSibling;
//   if (!next) {
//     next = item.parentNode.firstElementChild;
//   }
//   var clone = next.firstElementChild.cloneNode(true);
//   item.appendChild(clone);
//   for (var i = 0; i < 6; i++) {
//     next = next.nextElementSibling;
//     if (!next) {
//       next = this.parentNode.firstElementChild;
//     }
//     next.children[0].classList.add('cloneditem-' + (i+1));
//     this.appendChild(next.children[0].cloneNode(true));
//   }
// })

//   slider

// const slider = document.querySelector('.slider');
// const sliderWrapper = document.querySelector('.slider-wrapper');
// const prevButton = document.querySelector('.prev');
// const nextButton = document.querySelector('.next');

// let currentIndex = 0;

// function slideToIndex(index) {
//   const cardWidth = slider.querySelector('.slider-card').offsetWidth;
//   const offset = -1 * index * (cardWidth + 20);
//   slider.style.transform = `translateX(${offset}px)`;
//   currentIndex = index;
// }

// function slideLeft() {
//   if (currentIndex > 0) {
//     slideToIndex(currentIndex - 1);
//   } else {
//     slideToIndex(slider.children.length - 3);
//   }
// }

// function slideRight() {
//   if (currentIndex < slider.children.length - 3) {
//     slideToIndex(currentIndex + 1);
//   } else {
//     slideToIndex(0);
//   }
// }

// prevButton.addEventListener('click', slideLeft);
// nextButton.addEventListener('click', slideRight);

// let autoSlideInterval = setInterval(slideRight, 1000);

// sliderWrapper.addEventListener('mouseenter', () => {
//   clearInterval(autoSlideInterval);
// });

// sliderWrapper.addEventListener('mouseleave', () => {
//   autoSlideInterval = setInterval(slideRight, 5000);
// });

// image slider

var swiper = new Swiper(".slide-content", {
	slidesPerView: 3,
	spaceBetween: 25,
	loop: true,
	centerSlide: "true",
	fade: "true",
	grabCursor: "true",
	pagination: {
		el: ".swiper-pagination",
		clickable: true,
		dynamicBullets: true,
	},
	navigation: {
		nextEl: ".swiper-button-next",
		prevEl: ".swiper-button-prev",
	},

	breakpoints: {
		0: {
			slidesPerView: 1,
		},
		520: {
			slidesPerView: 2,
		},
		950: {
			slidesPerView: 3,
		},
	},
});




// home

// const changeBg = () =>{
//     const images =[
//         "url('../images/home1.jpg')",
//         "url('../images/home3.jpg')",
//     ]


// }

// $('#myCarousel').carousel({
//     interval: 3000,
//  })

// changeBg()
