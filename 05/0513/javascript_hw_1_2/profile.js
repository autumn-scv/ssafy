const nameid = document.querySelector('#name')
const jobid = document.querySelector('#job')
const experienceid = document.querySelector('#experience')
const emailid = document.querySelector('#email')
const phoneid = document.querySelector('#phone')

nameid.textContent = '조가을'
jobid.textContent = '백엔드 개발자'
experienceid.textContent = '학습 중'
emailid.textContent = '@email.com'
phoneid.textContent = '010-0000-0000'

const profileImage = document.querySelector('img');
profileImage.src = 'profile.jpg'
profileImage.alt = '프로필 사진'