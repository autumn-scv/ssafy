const bodyel = document.querySelector('body');
bodyel.classList.add('container');
const titlel = document.querySelector('h1')
titlel.classList.add('title')
const imgel = document.querySelector('img');
imgel.classList.add('img');

document.querySelector('#name').classList.add('highlight');
document.querySelector('#job').classList.add('highlight');
document.querySelector('#experience').classList.add('highlight');
document.querySelector('#email').classList.add('highlight');
document.querySelector('#phone').classList.add('highlight');

document.querySelector('#phone').parentElement.insertAdjacentHTML('afterend', '<p>SNS : <b id="sns" class="highlight">hgd@sns.com</b></p>');