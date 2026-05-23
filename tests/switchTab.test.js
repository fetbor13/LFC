const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

describe('switchTab', () => {
  let dom;
  let document;
  let window;

  beforeEach(() => {
    const html = fs.readFileSync(path.resolve(__dirname, '../Term_chapitre5.html'), 'utf-8');

    // Create jsdom environment with url to simulate localStorage
    dom = new JSDOM(html, { runScripts: "dangerously", url: "http://localhost" });
    document = dom.window.document;
    window = dom.window;

    // Mock MathJax
    window.MathJax = {
      typesetPromise: jest.fn().mockResolvedValue()
    };

    // Mock specific window functions used by switchTab
    window.initFC = jest.fn();
    window.buildQuiz = jest.fn();
  });

  test('should initialize with cours tab active by default (if no local storage)', () => {
    const activePanel = document.querySelector('.tab-panel.active');
    expect(activePanel.id).toBe('panel-cours');
  });

  test('switchTab should change active tab panel and button', () => {
    // Call the function explicitly
    window.switchTab('exercices');

    const activePanel = document.querySelector('.tab-panel.active');
    expect(activePanel.id).toBe('panel-exercices');

    // Make sure other panels are NOT active
    const coursPanel = document.getElementById('panel-cours');
    expect(coursPanel.classList.contains('active')).toBe(false);

    // Check button
    const activeButtons = document.querySelectorAll('.tab-btn.active');
    expect(activeButtons.length).toBe(1);
    expect(activeButtons[0].textContent).toContain('Exercices');
  });

  test('switchTab should save selection to localStorage', () => {
    window.switchTab('mindmap');
    expect(window.localStorage.getItem('term5_tab')).toBe('mindmap');
  });

  test('switchTab should call initFC when flashcards tab is selected', () => {
    window.switchTab('flashcards');
    expect(window.initFC).toHaveBeenCalled();
  });

  test('switchTab should call buildQuiz when quiz tab is selected', () => {
    window.switchTab('quiz');
    expect(window.buildQuiz).toHaveBeenCalled();
  });

  test('switchTab should call MathJax.typesetPromise', () => {
    window.switchTab('exercices');
    expect(window.MathJax.typesetPromise).toHaveBeenCalled();
  });

  test('switchTab restores tab from localStorage on load', () => {
    // Modify html to clear out default
    window.localStorage.setItem('term5_tab', 'simulations');

    // Execute the immediate function again
    const script = `
      (()=>{const t=localStorage.getItem('term5_tab');if(t)switchTab(t);})();
    `;
    const scriptEl = document.createElement('script');
    scriptEl.textContent = script;
    document.body.appendChild(scriptEl);

    const activePanel = document.querySelector('.tab-panel.active');
    expect(activePanel.id).toBe('panel-simulations');
  });
});
