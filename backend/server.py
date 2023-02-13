import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


def get_random_guess():
    return random.randrange(1, 100)


def set_random_guess():
    global computer_guess
    computer_guess = get_random_guess()


@app.get("/")
async def root():
    return {"message": "Hello World"}


computer_guess = get_random_guess()


@app.get("/new-game")
async def create_computer_guess():
    set_random_guess()
    return {"status": "ok"}


class Guess(BaseModel):
    guess: int


@app.post("/check-player-guess/")
async def check_player_guess(guess: Guess):
    player_guess = guess.guess
    if player_guess < computer_guess:
        feedback = "too low"
    elif player_guess > computer_guess:
        feedback = "too high"
    else:
        feedback = "You Won!"

    print(computer_guess)

    return {"feedback": feedback}
