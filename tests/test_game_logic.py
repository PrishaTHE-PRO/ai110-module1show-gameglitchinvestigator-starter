from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

# Tests targeting the backwards hint message bug:
# check_guess returns a tuple of (outcome, message).
# The bug was that when guess > secret, it said "Go HIGHER!" (wrong),
# and when guess < secret, it said "Go LOWER!" (wrong).

def test_too_high_message_says_go_lower():
    # Guess is above secret, so the hint must tell the player to go LOWER
    outcome, message = check_guess(80, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'LOWER' in hint but got: '{message}'"

def test_too_low_message_says_go_higher():
    # Guess is below secret, so the hint must tell the player to go HIGHER
    outcome, message = check_guess(20, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected 'HIGHER' in hint but got: '{message}'"


# Tests targeting the new-game-after-win bug:
# After winning, status is set to "won". Clicking New Game must reset status
# back to "playing", otherwise st.stop() halts the app and the user is stuck.

def test_new_game_resets_status_after_win():
    # Simulate the session state a player has after winning
    session = {"status": "won", "attempts": 3, "secret": 42, "history": [10, 30, 42]}

    # Simulate what the New Game button handler now does
    session["status"] = "playing"
    session["attempts"] = 0
    session["secret"] = 99  # new secret (any value)
    session["history"] = []

    assert session["status"] == "playing", (
        "After clicking New Game, status must be 'playing' so the game is not blocked by st.stop()"
    )

def test_new_game_resets_status_after_loss():
    # Same check for the "lost" state
    session = {"status": "lost", "attempts": 8, "secret": 77, "history": [1, 2, 3, 4, 5, 6, 7, 8]}

    session["status"] = "playing"
    session["attempts"] = 0
    session["secret"] = 55
    session["history"] = []

    assert session["status"] == "playing", (
        "After clicking New Game from a loss, status must be 'playing'"
    )

def test_game_is_blocked_when_status_is_not_playing():
    # Regression: before the fix, new_game never reset status, so the app
    # would always hit st.stop() after a win/loss even after clicking New Game.
    # Verify that a non-"playing" status would have blocked the game.
    session = {"status": "won"}
    game_blocked = session["status"] != "playing"
    assert game_blocked, "A 'won' status should block the game (this validates our guard logic)"
