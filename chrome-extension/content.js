chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "GET_PAGE_TEXT") {
    sendResponse({ text: document.body.innerText });
  }
  return true;
});

