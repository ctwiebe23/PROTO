const codeInput = document.getElementById("code-input");
const keywords = [
  ".component()",
  ".wait()",
  ".until()",
  ".action()",
  ".button()",
  ".pressed()",
  ".smallmotor()",
  ".largemotor()",
  ".spin()",
  ".stop()",
  ".drive()",
  ".drivetrain()",
  ".turn()",
  ".curve()",
];

let indentationLevel = 0;
let inIndentMode = false;

// Suggestion box element
const suggestionBox = document.getElementById("suggestion-box");

// Copy to Clipboard button
const copyButton = document.getElementById("copy-code-button");
copyButton.addEventListener("click", () => {
  const code = codeInput.innerText;
  navigator.clipboard.writeText(code).then(() => {
    alert("Code copied to clipboard!");
  });
});

// Save to File button
const saveButton = document.getElementById("save-code-button");
saveButton.addEventListener("click", () => {
  const code = codeInput.innerText;
  const blob = new Blob([code], { type: "text/plain" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = "main.py";
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
});

// Syncing the typed input with Prism.js highlighting and showing suggestions
codeInput.addEventListener("input", () => {
  const caretPosition = getCaretPosition(codeInput);
  const code = codeInput.innerText;
  const highlightedCode = Prism.highlight(
    code,
    Prism.languages.python,
    "python"
  );

  codeInput.innerHTML = highlightedCode;
  setCaretPosition(codeInput, caretPosition);

  const text = codeInput.innerText;
  const caretWordInfo = getWordAfterDotAtCaret(text, caretPosition);
  const { wordAfterDot, caretOffset } = caretWordInfo;

  const matchingKeywords = keywords.filter((keyword) =>
    keyword.startsWith(`.${wordAfterDot}`)
  );
  if (matchingKeywords.length > 0 && wordAfterDot.length > 0) {
    showSuggestions(matchingKeywords, caretOffset);
  } else {
    hideSuggestions();
  }
});

// Function to get the word after the dot for suggestions
function getWordAfterDotAtCaret(text, caretPosition) {
  const leftOfCaret = text.slice(0, caretPosition);
  const match = leftOfCaret.match(/\.([a-zA-Z_]*)$/);
  const wordAfterDot = match ? match[1] : "";
  return { wordAfterDot, caretOffset: leftOfCaret.length };
}

// Show suggestions in the suggestion box
function showSuggestions(matches, caretOffset) {
  suggestionBox.innerHTML = "";
  matches.forEach((match) => {
    const suggestion = document.createElement("div");
    suggestion.innerText = match;
    suggestionBox.appendChild(suggestion);
  });
  const rect = codeInput.getBoundingClientRect();
  suggestionBox.style.left = `${rect.left + window.scrollX}px`;
  suggestionBox.style.top = `${rect.bottom + window.scrollY}px`;
  suggestionBox.style.display = "block";
}

// Hide the suggestion box
function hideSuggestions() {
  suggestionBox.style.display = "none";
}

// Event listener for keydown to handle Tab and Enter
codeInput.addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    event.preventDefault();
    if (inIndentMode) {
      document.execCommand("insertLineBreak");
      for (let i = 0; i < indentationLevel; i++) {
        const indentSpan = document.createElement("span");
        indentSpan.className = "indent-space";
        indentSpan.innerHTML = "&nbsp;&nbsp;&nbsp;";
        const selection = window.getSelection();
        const range = selection.getRangeAt(0);
        range.insertNode(indentSpan);
        range.setStartAfter(indentSpan);
        selection.removeAllRanges();
        selection.addRange(range);
      }
    } else {
      document.execCommand("insertLineBreak");
    }
  }

  if (event.key === "Tab") {
    if (suggestionBox.style.display === "block") {
      event.preventDefault();
      const suggestion = suggestionBox.firstChild
        ? suggestionBox.firstChild.innerText
        : null;
      if (suggestion) {
        const caretPosition = getCaretPosition(codeInput);
        const text = codeInput.innerText;
        const caretWordInfo = getWordAfterDotAtCaret(text, caretPosition);
        const { wordAfterDot } = caretWordInfo;

        const beforeWord = text.slice(
          0,
          caretPosition - wordAfterDot.length - 1
        );
        const afterWord = text.slice(caretPosition);
        const updatedText = beforeWord + suggestion + afterWord;

        codeInput.innerText = updatedText;
        const highlightedCode = Prism.highlight(
          updatedText,
          Prism.languages.python,
          "python"
        );
        codeInput.innerHTML = highlightedCode;

        const newCaretPosition = beforeWord.length + suggestion.length;
        setCaretPosition(codeInput, newCaretPosition);
        hideSuggestions();
      }
    } else {
      event.preventDefault();
      inIndentMode = true;
      indentationLevel++;
      const indentSpan = document.createElement("span");
      indentSpan.className = "indent-space";
      indentSpan.innerHTML = "&nbsp;&nbsp;&nbsp;";
      const selection = window.getSelection();
      const range = selection.getRangeAt(0);
      range.insertNode(indentSpan);
      range.setStartAfter(indentSpan);
      selection.removeAllRanges();
      selection.addRange(range);
    }
  }

  if (event.key === "Backspace") {
    const selection = window.getSelection();
    if (selection.rangeCount > 0) {
      const range = selection.getRangeAt(0);
      if (
        range.startContainer.nodeType === Node.TEXT_NODE &&
        range.startOffset === 0
      ) {
        const previousNode = range.startContainer.previousSibling;
        if (
          previousNode &&
          previousNode.classList &&
          previousNode.classList.contains("indent-space")
        ) {
          event.preventDefault();
          previousNode.remove();
          indentationLevel--;
          if (indentationLevel === 0) inIndentMode = false;
        }
      } else if (range.startContainer.nodeType === Node.ELEMENT_NODE) {
        const previousNode =
          range.startContainer.childNodes[range.startOffset - 1];
        if (
          previousNode &&
          previousNode.classList &&
          previousNode.classList.contains("indent-space")
        ) {
          event.preventDefault();
          previousNode.remove();
          indentationLevel--;
          if (indentationLevel === 0) inIndentMode = false;
        }
      }
    }
  }
});

// Function to get the caret position within the contenteditable div
function getCaretPosition(element) {
  const selection = window.getSelection();
  let position = 0;

  if (selection.rangeCount !== 0) {
    const range = selection.getRangeAt(0);
    const preCaretRange = range.cloneRange();
    preCaretRange.selectNodeContents(element);
    preCaretRange.setEnd(range.endContainer, range.endOffset);
    position = preCaretRange.toString().length;
  }

  return position;
}

// Function to set the caret position within the contenteditable div
function setCaretPosition(element, position) {
  const range = document.createRange();
  const selection = window.getSelection();
  let currentNode = element;
  let currentOffset = 0;

  const nodeWalker = document.createTreeWalker(
    element,
    NodeFilter.SHOW_TEXT,
    null,
    false
  );
  while (nodeWalker.nextNode()) {
    const textNode = nodeWalker.currentNode;
    const nodeLength = textNode.length;

    if (position <= currentOffset + nodeLength) {
      range.setStart(textNode, position - currentOffset);
      range.collapse(true);
      break;
    }

    currentOffset += nodeLength;
  }

  selection.removeAllRanges();
  selection.addRange(range);
}
