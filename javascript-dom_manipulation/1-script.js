const color_changer = document.querySelector('#red_header');
const header = document.querySelector('header');
color_changer.addEventListener('click', function () {
  header.style.color = '#FF0000';
});
