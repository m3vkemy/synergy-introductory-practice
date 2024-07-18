const images = [
    'img/image1.jpeg',
    'img/image2.jpeg',
    'img/image3.jpeg',
    'img/image4.jpeg',
    'img/image5.jpeg'
];

let currentIndex = 0;

const sliderImage = document.getElementById('slider-image');
const imageCounter = document.getElementById('image-counter');
const prevBtn = document.getElementById('prev-btn');
const nextBtn = document.getElementById('next-btn');

function updateSlider() {
    console.log(`Updating slider to image index: ${currentIndex}`);
    sliderImage.src = images[currentIndex];
    sliderImage.onerror = function() {
        console.error('Error loading image:', sliderImage.src);
    };
    updateCounterText();
}

function updateCounterText() {
    imageCounter.textContent = `Изображение ${currentIndex + 1} из ${images.length}`;
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