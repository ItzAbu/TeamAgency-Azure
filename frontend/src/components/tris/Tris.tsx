import React, { useState, useEffect } from "react";

type Player = "X" | "O";
type Cell = Player | null;

const WINNING_LINES = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8], // rows
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8], // cols
  [0, 4, 8],
  [2, 4, 6], // diagonals
];

// Accessible button styles + Tailwind utilities for grid cells
const cellStyles =
  "w-20 h-20 border border-gray-400 flex justify-center items-center text-4xl font-bold cursor-pointer select-none";

const buttonStyles = "mr-4 mb-2 px-4 py-2 rounded bg-blue-600 text-white hover:bg-blue-700 focus:outline focus:outline-2 focus:outline-blue-400";

const debugButtonStyles = "mr-2 mb-2 px-3 py-1 rounded bg-gray-300 dark:bg-gray-700 text-gray-900 dark:text-gray-100 hover:bg-gray-400 dark:hover:bg-gray-600 focus:outline focus:outline-2 focus:outline-offset-2 focus:outline-blue-500";

export default function Tris() {
  const [board, setBoard] = useState<Cell[]>(Array(9).fill(null));
  const [currentPlayer, setCurrentPlayer] = useState<Player>("X");
  const [winner, setWinner] = useState<Player | "Tie" | null>(null);
  const [isSpectator, setIsSpectator] = useState<boolean>(false);

  // Determine if there's a winner or tie
  function checkWinner(board: Cell[]): Player | "Tie" | null {
    for (const line of WINNING_LINES) {
      const [a, b, c] = line;
      if (
        board[a] &&
        board[a] === board[b] &&
        board[a] === board[c]
      ) {
        return board[a];
      }
    }
    if (board.every(cell => cell !== null)) {
      return "Tie";
    }
    return null;
  }

  // Handle clicking a cell on the board
  function handleCellClick(idx: number) {
    if (isSpectator) {
      console.debug("Spectator mode enabled: ignoring clicks.");
      return;
    }
    if (winner) {
      console.debug("Game finished: ignoring clicks.");
      return;
    }
    if (board[idx] !== null) {
      console.debug(`Cell ${idx} already filled.`);
      return;
    }
    const newBoard = [...board];
    newBoard[idx] = currentPlayer;
    console.info(`Player ${currentPlayer} moved on cell ${idx}`);
    setBoard(newBoard);
    const result = checkWinner(newBoard);
    if (result) {
      setWinner(result);
      console.info(`Game ended: Winner - ${result}`);
    } else {
      setCurrentPlayer(currentPlayer === "X" ? "O" : "X");
    }
  }

  // Reset game state + console log
  function resetGame() {
    setBoard(Array(9).fill(null));
    setCurrentPlayer("X");
    setWinner(null);
    console.info("Game reset");
  }

  // Populate example moves for debugging
  function populateExampleMoves() {
    // Example board state, no winner yet
    const exampleBoard: Cell[] = [
      "X", null, "O",
      "O", "X", null,
      null, null, "X",
    ];
    setBoard(exampleBoard);
    setCurrentPlayer("O"); // next move
    setWinner(null);
    console.info("Example moves populated");
  }

  // Toggle spectator mode (disable interaction)
  function toggleSpectatorMode() {
    setIsSpectator(!isSpectator);
    console.info(`Spectator mode ${!isSpectator ? "enabled" : "disabled"}`);
  }

  // Render cell content - accessible button with ARIA label
  function renderCell(idx: number) {
    return (
      <button
        aria-label={`Cell ${idx + 1} ${board[idx] ? `filled by ${board[idx]}` : "empty"}`}
        key={idx}
        className={cellStyles}
        onClick={() => handleCellClick(idx)}
        disabled={!!winner || isSpectator || board[idx] !== null}
        type="button"
      >
        {board[idx]}
      </button>
    );
  }

  return (
    <main className="max-w-md mx-auto p-6 text-gray-900 dark:text-gray-100 bg-white dark:bg-gray-900 min-h-screen flex flex-col">
      <h1 className="text-3xl font-extrabold mb-4 text-center">Tris - Tic Tac Toe</h1>
      <section
        role="grid"
        aria-label="Board"
        className="grid grid-cols-3 grid-rows-3 gap-1 mb-4 border-4 border-gray-600 dark:border-gray-400 rounded select-none"
      >
        {board.map((_, idx) => renderCell(idx))}
      </section>

      <p aria-live="polite" className="mb-4 min-h-[1.5rem] text-center text-lg font-semibold">
        {winner
          ? winner === "Tie"
            ? "Pareggio! Nessun vincitore."
            : `Vincitore: ${winner}`
          : `Turno del giocatore: ${currentPlayer}`}
      </p>

      <section className="flex flex-wrap justify-center mb-6" aria-label="Debug Controls">
        <button onClick={resetGame} className={debugButtonStyles} type="button" aria-pressed="false" title="Reset partita">
          Reset partita
        </button>
        <button onClick={populateExampleMoves} className={debugButtonStyles} type="button" aria-pressed="false" title="Popola mosse di esempio">
          Popola mosse di esempio
        </button>
        <button onClick={toggleSpectatorMode} className={debugButtonStyles} type="button" aria-pressed={isSpectator} title="Toggle modalità spettatore">
          {isSpectator ? "Disabilita modalita spettatore" : "Modalità spettatore"}
        </button>
      </section>

      <footer className="mt-auto text-center text-sm text-gray-500 dark:text-gray-400">
        <p>Tris creato con Next.js 13, React 18+, TypeScript e Tailwind CSS</p>
      </footer>
    </main>
  );
}