const scanBtn = document.getElementById("scanBtn");
const askBtn = document.getElementById("askBtn");
const questionInput = document.getElementById("question");
const answerBox = document.getElementById("answer");

const BACKEND_URL = "http://127.0.0.1:8001";

scanBtn.addEventListener("click", () => {
  answerBox.innerText = "Scanning page...";

  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    if (!tabs || !tabs[0]) {
      answerBox.innerText = "No active tab.";
      return;
    }

    const tabId = tabs[0].id;

    chrome.scripting.executeScript(
      {
        target: { tabId },
        func: () => document.body.innerText
      },
      async (results) => {
        if (!results || !results[0] || !results[0].result) {
          answerBox.innerText = "Failed to extract page content.";
          return;
        }

        const pageText = results[0].result;

        try {
          const res = await fetch(`${BACKEND_URL}/scan`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: pageText }),
          });

          const data = await res.json();
          answerBox.innerText = "Page scanned successfully ✅";
        } catch (err) {
          console.error(err);
          answerBox.innerText = "Backend error.";
        }
      }
    );
  });
});

askBtn.addEventListener("click", async () => {
  const question = questionInput.value.trim();
  if (!question) {
    answerBox.innerText = "Enter a question.";
    return;
  }

  answerBox.innerText = "Thinking...";

  try {
    const res = await fetch(`${BACKEND_URL}/ask`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question }),
    });

    const data = await res.json();
    answerBox.innerText = data.answer;
  } catch (err) {
    console.error(err);
    answerBox.innerText = "Failed to get answer.";
  }
});

