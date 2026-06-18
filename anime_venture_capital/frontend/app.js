document.getElementById('pitch-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const pitch = document.getElementById('pitch-input').value;
    if (!pitch) return;

    const btn = document.getElementById('pitch-btn');
    const spinner = document.getElementById('loading-spinner');
    const terminal = document.getElementById('terminal-log');
    const resultsContainer = document.getElementById('results-container');
    const grid = document.getElementById('evaluations-grid');
    const verdictEl = document.getElementById('final-verdict');

    // Reset UI
    btn.disabled = true;
    spinner.classList.remove('hidden');
    resultsContainer.classList.add('hidden');
    grid.innerHTML = '';
    terminal.innerHTML = '> Transmitting pitch to the board...<br>';
    verdictEl.className = 'px-4 py-2 rounded-full font-bold text-sm bg-slate-800 border';
    verdictEl.innerHTML = '';

    try {
        const response = await fetch('http://localhost:8009/api/pitch', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ pitch })
        });

        const data = await response.json();

        // Simulate Terminal Logs typing effect
        for (let i = 0; i < data.logs.length; i++) {
            await new Promise(r => setTimeout(r, 600)); // Delay between logs
            terminal.innerHTML += `> ${data.logs[i]}<br>`;
            terminal.scrollTop = terminal.scrollHeight;
        }

        await new Promise(r => setTimeout(r, 1000));

        // Render Verdict
        verdictEl.innerText = data.final_verdict;
        if (data.final_verdict.includes("Funded")) {
            verdictEl.classList.add('text-green-400', 'border-green-400/50');
        } else if (data.final_verdict.includes("Rejected")) {
            verdictEl.classList.add('text-red-400', 'border-red-400/50');
        } else {
            verdictEl.classList.add('text-yellow-400', 'border-yellow-400/50');
        }

        // Render Role Cards
        data.evaluations.forEach((eval, index) => {
            const card = document.createElement('div');
            card.className = `glass-panel p-5 fade-in border-l-4 ${getBorderColor(eval.role)}`;
            card.style.animationDelay = `${index * 0.2}s`;

            let decisionBadge = '';
            if (eval.decision === 'Invest') {
                decisionBadge = '<span class="bg-green-900/50 text-green-400 text-xs px-2 py-1 rounded border border-green-500/30">INVEST</span>';
            } else if (eval.decision === 'Pass') {
                decisionBadge = '<span class="bg-red-900/50 text-red-400 text-xs px-2 py-1 rounded border border-red-500/30">PASS</span>';
            } else {
                decisionBadge = '<span class="bg-yellow-900/50 text-yellow-400 text-xs px-2 py-1 rounded border border-yellow-500/30">WAIT</span>';
            }

            card.innerHTML = `
                <div class="flex justify-between items-start mb-3">
                    <div>
                        <div class="text-xs font-bold text-slate-400 uppercase tracking-wider mb-1">${eval.role}</div>
                        <div class="font-bold text-lg text-slate-200">${eval.character}</div>
                    </div>
                    ${decisionBadge}
                </div>
                <div class="text-sm text-slate-300 italic border-t border-slate-700/50 pt-3">
                    "${eval.feedback}"
                </div>
            `;
            grid.appendChild(card);
        });

        resultsContainer.classList.remove('hidden');

    } catch (error) {
        terminal.innerHTML += `> <span class="text-red-500">ERROR: Connection to boardroom lost.</span><br>`;
    } finally {
        btn.disabled = false;
        spinner.classList.add('hidden');
    }
});

function getBorderColor(role) {
    switch(role) {
        case 'Pragmatist': return 'border-blue-500';
        case 'Visionary': return 'border-yellow-400';
        case 'Skeptic': return 'border-purple-500';
        case 'Wildcard': return 'border-red-500';
        default: return 'border-slate-500';
    }
}