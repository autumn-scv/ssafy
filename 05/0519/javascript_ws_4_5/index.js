
let count1 = 0;
let count2 = 0;


const choices = ['scissors', 'rock', 'paper'];


let intervalId = null;
let timeoutId = null;

const countAEl = document.querySelector('.countA');
const countBEl = document.querySelector('.countB');
const player1Img = document.getElementById('player1-img');
const player2Img = document.getElementById('player2-img');

const scissorsBtn = document.getElementById('scissors-button');
const rockBtn = document.getElementById('rock-button');
const paperBtn = document.getElementById('paper-button');


const buttons = [scissorsBtn, rockBtn, paperBtn];


function playGame(player1, player2) {

  if (player1 === 'scissors') {
    if (player2 === 'rock') {
      count2++;
      return 2;
    } else if (player2 === 'paper') {
      count1++;
      return 1;
    }
  }

  else if (player1 === 'rock') {
    if (player2 === 'scissors') {
      count1++;
      return 1; 
    } else if (player2 === 'paper') {
      count2++;
      return 2; 
    }
  }

  else if (player1 === 'paper') {
    if (player2 === 'rock') {
      count1++;
      return 1; 
    } else if (player2 === 'scissors') {
      count2++;
      return 2; 
    }
  }


  return 0; 
}

function buttonClickHandler(choice) {

  buttons.forEach(btn => btn.disabled = true);
  player1Img.src = `./img/${choice}.png`;


  intervalId = setInterval(() => {
    const randomIndex = Math.floor(Math.random() * choices.length);
    player2Img.src = `./img/${choices[randomIndex]}.png`;
  }, 100); 


  timeoutId = setTimeout(() => {
    clearInterval(intervalId);

    const finalRandomIndex = Math.floor(Math.random() * choices.length);
    const player2FinalChoice = choices[finalRandomIndex];


    player2Img.src = `./img/${player2FinalChoice}.png`;


    const result = playGame(choice, player2FinalChoice);


    countAEl.textContent = count1;
    countBEl.textContent = count2;


    const modal = document.querySelector('.modal');
    const modalContent = document.querySelector('.modal-content');
    
    if (result === 1) {
      modalContent.textContent = 'Player1 승리!';
    } else if (result === 2) {
      modalContent.textContent = 'Player2 승리!';
    } else {
      modalContent.textContent = '무승부!';
    }
    modal.style.display = 'flex';


    setTimeout(() => {
      modal.style.display = 'none';
      buttons.forEach(btn => btn.disabled = false);
    }, 1500);

  }, 3000);
}


scissorsBtn.addEventListener('click', () => buttonClickHandler('scissors'));
rockBtn.addEventListener('click', () => buttonClickHandler('rock'));
paperBtn.addEventListener('click', () => buttonClickHandler('paper'));