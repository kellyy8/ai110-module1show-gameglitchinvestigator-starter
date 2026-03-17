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
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
