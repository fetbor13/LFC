const fs = require('fs');

let content = fs.readFileSync('index_sim.html', 'utf8');

let badStart = content.indexOf('        window.MathJax = {\n            tex: { inlineMath: [[\'</head>');
let endTarget = "</html>'], ['\\\\(', '\\\\)']] },";
let badEnd = content.indexOf(endTarget, badStart);

if (badStart !== -1 && badEnd !== -1) {
    let actualEnd = badEnd + endTarget.length;
    let correctConfig = `        window.MathJax = {
            tex: { inlineMath: [['$', '$'], ['\\\\(', '\\\\)']] },`;

    content = content.substring(0, badStart) + correctConfig + content.substring(actualEnd);
    fs.writeFileSync('index_sim.html', content);
    console.log("Removed hallucination");
} else {
    console.log("Could not find boundaries.");
}
