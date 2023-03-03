// Initialize the game board and current player
let board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
];
let currentPlayer = "X";

// Function to print the board to the console
function printBoard() {
    console.log(board[0][0] + " | " + board[0][1] + " | " + board[0][2]);
    console.log("---------");
    console.log(board[1][0] + " | " + board[1][1] + " | " + board[1][2]);
    console.log("---------");
    console.log(board[2][0] + " | " + board[2][1] + " | " + board[2][2]);
}

// Function to check if the game is over
function isGameOver() {
    // Check for a win
    for (let i = 0; i < 3; i++) {
        if (board[i][0] !== "" && board[i][0] === board[i][1] && board[i][1] === board[i][2]) {
            return true;
        }
        if (board[0][i] !== "" && board[0][i] === board[1][i] && board[1][i] === board[2][i]) {
            return true;
        }
    }
    if (board[0][0] !== "" && board[0][0] === board[1][1] && board[1][1] === board[2][2]) {
        return true;
    }
    if (board[0][2] !== "" && board[0][2] === board[1][1] && board[1][1] === board[2][0]) {
        return true;
    }

    // Check for a tie
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            if (board[i][j] === "") {
                return false;
            }
        }
    }
    return true;
}

// Function to update the player-turn element
function updatePlayerTurn() {
    let playerTurnElement = document.getElementById("player-turn");
    playerTurnElement.textContent = "Player " + currentPlayer + "'s turn";
}

// Function to handle a button click
function handleClick(row, col) {
    // Check if the button has already been clicked
    let button = document.getElementById(row + "_" + col);
    if (button.disabled) {
        return
    }

    // Update the button and board arrays
    button.textContent = currentPlayer;
    button.disabled = true;
    board[row][col] = currentPlayer;

    // Check if the game is over
    if (isGameOver()) {
        let playerTurnElement = document.getElementById("player-turn");
        playerTurnElement.textContent = "Game over!";
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++) {
                let button = document.getElementById(i + "_" + j);
                button.disabled = true;
            }
        }
    } else {
        // Switch to the other player
        currentPlayer = currentPlayer === "X" ? "O" : "X";
        updatePlayerTurn();
    }
}

// Function to reset the game
function resetGame() {
    // Reset the board and current player
    board = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ];
    currentPlayer = "X";

    // Reset the button text and enable all buttons
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            let button = document.getElementById(i + "_" + j);
            button.textContent = "";
            button.disabled = false;
        }
    }

    // Update the player-turn element
    updatePlayerTurn();
}

// Add event listeners to the buttons and restart button
for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
        let button = document.getElementById(i + "_" + j);
        button.addEventListener("click", function () {
            handleClick(i, j);
        });
    }
}
let restartButton = document.getElementById("restart-button");
restartButton.addEventListener("click", resetGame);

// Update the player-turn element
updatePlayerTurn();

