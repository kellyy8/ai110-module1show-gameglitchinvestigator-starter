# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

| Bug | Expected Behavior |
|-----|-------------------|
| Instructions say: "Guess a number between 1 and 100," but I am able to enter numbers that are less than 1 or greater than 100. | The application should prevent me from entering numbers that are out of bounds. |
| Invalid inputs are counted as attempts. If I enter a number that is out of bounds or a non-numerical input, I get a hint that warns me but my attempt is also counted. | The application should show the warning, but not consider my input as an attempt. |
| If I repeatedly enter non-numerical inputs, I reach a negative number of attempts left. | The smallest number of attempts left should be 0. If we run out of attempts before guessing the number, the game should end. |
| If I submit `1000` twice, I get one hint that says to go LOWER and then another hint that says to go HIGHER. | Same inputs should receive same hints. Each input should only have one deterministic hint. |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - I used Copilot.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - AI suggested that to parse the guess, we need to check that the guess is non-empty, that the guess contains valid characters that can
    be converted into an integer, and that the integer was within the specified bounds.
    This is correct because a non-empty input means a guess does not exist. If the guess cannot be converted into an integer, then we cannot
    compare the guess against the bounds nor the secret (correct answer), which is an integer.
    I verified the result by manually playing the game and entering different inputs that would go through each of the control flows.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - AI suggested 2 pytest cases that tested for non-numerical inputs and an input that was greater than the upper bound.
  - While these pytest cases are good, AI did not account for other valid and invalid inputs.
    Another invalid input would be an input that is less than the lower bound.
    Valid inputs include inputs that are exactly at the lower and upper bounds and inputs that are within bounds.
    Without these additional exhaustive test cases, our code is not 100% resilient against all inputs.
    I verified that the test cases were missing and necessary by reviewing the changes to the test_game_logic.py file,
    prompting AI to add the missing test cases, running the test cases via my command line, and manually playing the game to ensure the game works.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - Ensuring that there was a test case for each scenario and that each test case tested for all the control flows in the fixed implementation.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
  - The test case `test_parse_guess_out_of_bounds_input_upper` that I ran using pytest showed that my code catches when the input is
    greater than the upper bound.
- Did AI help you design or understand any tests? How?
  - Yes. AI helped suggest test cases like `test_parse_guess_non_numeric_input` and `test_parse_guess_out_of_bounds_input_upper`. Based on
    these test cases I prompted AI to create more test cases to make the test set exhaustive. For instance, I asked AI to write a test case
    that would test if the input would be less than the lower bound, at the lower bound, at the upper bound, or within the bounds.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
