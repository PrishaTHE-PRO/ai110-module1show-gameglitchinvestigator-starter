# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
1) The hints are not correct
2) When I click on New Game, the Secret changes but it doesn't let you continue playing and it says that you already won.
3) The Submit button doesn't work the first time I press it, it only works the 2nd time.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
1) I used Claude
2) I suggested I change the if/else logic for the hints, whcih was a correct identification of the error source.
3) It didn't suggest changing the "higher" and "lower" texts for the hints which was a large UI issue.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
1) I ran app.py again and checked if the feature I was focusing on worked as intended. Then I developed a test with the help of claude to test otehr cases.
2) One of the tests, tested the message generated for the hints against what the hint was supposed to be
3) Yes. AI helped me with examples test cases for tests.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?
1) Everytime I intereacted with the app, streamlit re-ran the entier app.py. So every re-run generated a new secret
2) If everytime you click any button on webpage, the entier page reloaded and forgot your inputs and progress. That's how streamlit works by default. A "rerun" is jsut Streamlit re-executing your whole python script.
3) I wrapped the secret number in an if check, so it would only generate a new secret if one doesn't already exist.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
1) I liked looking through app.py myslef first and identifing possible errors in the logic before prompting AI to fix the error.
2) I will work on each problem seperately now that I know its benefits of better clarity
3) I think that if AI is pormpted specifically and well that it is more likely to identify the source of a bug and fix it. Also, sometimes it doesn't fix the hwole issue so you will need to prompt it multiple times or look through it yourself and fix it.
