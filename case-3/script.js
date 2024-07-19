const images = [
    'img/image1.jpeg',
    'img/image2.jpeg',
    'img/image3.jpeg',
    'img/image4.jpeg',
    'img/image5.jpeg',
    'img/image6.jpeg'
];

let currentIndex = 0;

const sliderImage = document.getElementById('slider-image');
const imageCounter = document.getElementById('image-counter');
const prevBtn = document.getElementById('prev-btn');
const nextBtn = document.getElementById('next-btn');
const indicatorsContainer = document.querySelector('.indicators');

function updateSlider() {
    sliderImage.src = images[currentIndex];
    sliderImage.onerror = function() {
        console.error('Error loading image:', sliderImage.src);
        sliderImage.src = 'img/placeholder.jpeg'; // Placeholder image
    };
    updateCounterText();
    updateIndicators();
}

function updateCounterText() {
    imageCounter.textContent = `Изображение ${currentIndex + 1} из ${images.length}`;
}

function updateIndicators() {
    indicatorsContainer.innerHTML = '';
    for (let i = 0; i < images.length; i++) {
        const indicator = document.createElement('span');
        indicator.classList.add('indicator');
        if (i === currentIndex) {
            indicator.classList.add('active');
        }
        indicatorsContainer.appendChild(indicator);
    }
}

function showNextImage() {
    currentIndex = (currentIndex + 1) % images.length;
    updateSlider();
}

function showPrevImage() {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    updateSlider();
}

prevBtn.addEventListener('click', showPrevImage);
nextBtn.addEventListener('click', showNextImage);

updateSlider();
