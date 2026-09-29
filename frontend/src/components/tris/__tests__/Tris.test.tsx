import React from "react";
import { render, screen, fireEvent } from "@testing-library/react";
import Tris from "../Tris";

describe("Tris component", () => {
  beforeEach(() => {
    jest.clearAllMocks();
    render(<Tris />);
  });

  test("renders all cells as empty buttons", () => {
    const cells = screen.getAllByRole("button").filter(btn => btn.disabled === false);
    expect(cells.length).toBe(9);
    cells.forEach(cell => {
      expect(cell.textContent).toBe("");
    });
  });

  test("players alternate turns X and O on valid clicks", () => {
    const cells = screen.getAllByRole("button");
    fireEvent.click(cells[0]);
    expect(cells[0].textContent).toBe("X");
    fireEvent.click(cells[1]);
    expect(cells[1].textContent).toBe("O");
  });

  test("clicking a filled cell does nothing", () => {
    const cells = screen.getAllByRole("button");
    fireEvent.click(cells[0]);
    expect(cells[0].textContent).toBe("X");
    fireEvent.click(cells[0]);
    expect(cells[0].textContent).toBe("X"); // unchanged
  });

  test("detects a winner and disables further clicks", () => {
    const cells = screen.getAllByRole("button");
    fireEvent.click(cells[0]); // X
    fireEvent.click(cells[3]); // O
    fireEvent.click(cells[1]); // X
    fireEvent.click(cells[4]); // O
    fireEvent.click(cells[2]); // X wins

    expect(screen.getByText(/Vincitore: X/)).toBeInTheDocument();

    // Further clicks disabled
    fireEvent.click(cells[5]);
    expect(cells[5].textContent).toBe("");
  });

  test("detects tie game", () => {
    const cells = screen.getAllByRole("button");
    const moves = [0,1,2,4,3,5,7,6,8];
    moves.forEach(i => fireEvent.click(cells[i]));
    expect(screen.getByText(/Pareggio! Nessun vincitore./)).toBeInTheDocument();
  });

  test("reset button clears board and state", () => {
    const cells = screen.getAllByRole("button");
    fireEvent.click(cells[0]);
    expect(cells[0].textContent).toBe("X");
    const resetButton = screen.getByRole("button", { name: /reset partita/i });
    fireEvent.click(resetButton);
    cells.forEach(cell => expect(cell.textContent).toBe(""));
    expect(screen.queryByText(/Vincitore/i)).not.toBeInTheDocument();
  });

  test("populate example moves updates board accordingly", () => {
    const exampleButton = screen.getByRole("button", { name: /popola mosse di esempio/i });
    fireEvent.click(exampleButton);

    // Board must contain the example moves
    expect(screen.getByRole("button", { name: /Cell 1 filled by X/i }).textContent).toBe("X");
    expect(screen.getByRole("button", { name: /Cell 3 filled by O/i }).textContent).toBe("O");
    expect(screen.getByRole("button", { name: /Cell 5 filled by X/i }).textContent).toBe("X");
    expect(screen.getByRole("button", { name: /Cell 9 filled by X/i }).textContent).toBe("X");

    // Next player is "O"
    expect(screen.getByText(/Turno del giocatore: O/)).toBeInTheDocument();
  });

  test("toggle spectator mode disables clicks", () => {
    const spectatorButton = screen.getByRole("button", { name: /modalità spettatore/i });
    fireEvent.click(spectatorButton);
    expect(spectatorButton.textContent).toMatch(/disabilita modalita spettatore/i);

    const cells = screen.getAllByRole("button");
    fireEvent.click(cells[0]);
    expect(cells[0].textContent).toBe(""); // no move made

    // Disabling spectator mode re-enables clicks
    fireEvent.click(spectatorButton);
    fireEvent.click(cells[0]);
    expect(cells[0].textContent).toBe("X");
  });
});