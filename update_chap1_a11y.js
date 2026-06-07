const fs = require('fs');

let content = fs.readFileSync('Term_chapitre1.html', 'utf8');

content = content.replace(
  '<button class="icon-btn" id="themeBtn" title="Thème">🌙</button>',
  '<button class="icon-btn" id="themeBtn" title="Thème" aria-label="Changer de thème">🌙</button>'
);

content = content.replace(
  '<button class="icon-btn" onclick="window.print()" title="Imprimer">⎙</button>',
  '<button class="icon-btn" onclick="window.print()" title="Imprimer" aria-label="Imprimer">⎙</button>'
);

content = content.replace(
  '<button class="icon-btn" onclick="copyCurrentPrompt()" title="Copier prompt IA">⌘</button>',
  '<button class="icon-btn" onclick="copyCurrentPrompt()" title="Copier prompt IA" aria-label="Copier prompt IA">⌘</button>'
);

fs.writeFileSync('Term_chapitre1.html', content);
console.log('Updated Term_chapitre1.html');
