// Initialize the game board
const board = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
];

// Initialize the current player to "X"
let currentPlayer = "X";

// Function to print the game board to the console
function printBoard() {
    console.log(board[0][0] + " | " + board[0][1] + " | " + board[0][2]);
    console.log(board[1][0] + " | " + board[1][1] + " | " + board[1][2]);
    console.log(board[2][0] + " | " + board[2][1] + " | " + board[2][2]);
}

// Function to check if the game is over
function isGameOver() {
    // Check rows
    for (let i = 0; i < 3; i++) {
        if (board[i][0] !== "_" && board[i][0] === board[i][1] && board[i][1] === board[i][2]) {
            return true;
        }
    }

    // Check columns
    for (let j = 0; j < 3; j++) {
        if (board[0][j] !== "_" && board[0][j] === board[1][j] && board[1][j] === board[2][j]) {
            return true;
        }
    }

    // Check diagonals
    if (board[0][0] !== "_" && board[0][0] === board[1][1] && board[1][1] === board[2][2]) {
        return true;
    }
    if (board[0][2] !== "_" && board[0][2] === board[1][1] && board[1][1] === board[2][0]) {
        return true;
    }

    // Check if board is full
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            if (board[i][j] === "_") {
                return false;
            }
        }
    }
    return true;
}

// Function to prompt the current player to make a move
function promptMove() {
    console.log(currentPlayer + "'s turn to move.");
    let row = prompt("Enter row (0-2): ");
    let col = prompt("Enter column (0-2): ");
    if (board[row][col] === "_") {
        board[row][col] = currentPlayer;
    } else {
        console.log("Invalid move. Try again.");
        promptMove();
    }
}

// Game loop
while (!isGameOver()) {
    printBoard();
    promptMove();
    // Switch to the other player
    currentPlayer = currentPlayer === "X" ? "O" : "X";
}

// Print the final board and the winner
printBoard();
console.log("Game over. " + currentPlayer + " wins!");
