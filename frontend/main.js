const form = document.querySelector('form')
const API_URL = 'http://localhost:8000'
// TODO: button to call newGame
async function newGame() {
    await fetch(`${API_URL}/new-game`)
}

async function submit(e) {
    e.preventDefault()

    // get info from form
    const form = document
    const playerGuess = Number(form.querySelector('input').value)

    // compare and show feedback
    const opts = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ guess: playerGuess })
    }
    const response = await fetch(`${API_URL}/check-player-guess`, opts)
    const { feedback } = await response.json()
    document.querySelector('.feedback').textContent = feedback
}

form.addEventListener('submit', submit)

newGame()