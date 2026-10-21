document.addEventListener('DOMContentLoaded', () => {
    const submitBtn = document.getElementById('submit-case-btn');
    const caseInput = document.getElementById('case-input');
    const spinner = document.getElementById('loading-spinner');
    const courtroomContainer = document.getElementById('courtroom-container');
    const transcriptLog = document.getElementById('transcript-log');

    // UI Elements for Roles
    const judgeName = document.getElementById('judge-name');
    const judgeTrait = document.getElementById('judge-trait');
    const prosName = document.getElementById('pros-name');
    const prosTrait = document.getElementById('pros-trait');
    const defName = document.getElementById('def-name');
    const defTrait = document.getElementById('def-trait');
    const juryContainer = document.getElementById('jury-container');
    const caseTitle = document.getElementById('case-title');

    // Utility: Apply typing effect to text
    async function typeText(element, text, speed = 20) {
        element.textContent = '';
        for (let i = 0; i < text.length; i++) {
            element.textContent += text.charAt(i);
            await new Promise(r => setTimeout(r, speed));
        }
    }

    submitBtn.addEventListener('click', async () => {
        const caseDescription = caseInput.value.trim();

        if (!caseDescription) {
            alert('Please describe a case first!');
            return;
        }

        // UI Reset
        submitBtn.disabled = true;
        spinner.classList.remove('hidden');
        courtroomContainer.classList.add('hidden');
        transcriptLog.innerHTML = '';
        juryContainer.innerHTML = '';

        try {
            const response = await fetch('/api/simulate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ case_description: caseDescription })
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();

            // Populate Roles
            const roles = data.roles;

            judgeName.textContent = roles.Judge.name;
            judgeTrait.textContent = roles.Judge.core_emotion;

            prosName.textContent = roles.Prosecutor.name;
            prosTrait.textContent = roles.Prosecutor.core_emotion;

            defName.textContent = roles.Defense.name;
            defTrait.textContent = roles.Defense.core_emotion;

            // Populate Jury
            roles.Jury.forEach(juror => {
                const badge = document.createElement('div');
                badge.className = 'px-3 py-1 bg-gray-800/80 border border-gray-600 rounded-full text-xs text-gray-300 shadow-sm';
                badge.textContent = juror.name;
                juryContainer.appendChild(badge);
            });

            caseTitle.textContent = `Case: "${data.case.substring(0, 40)}${data.case.length > 40 ? '...' : ''}"`;

            // Reveal Courtroom
            spinner.classList.add('hidden');
            courtroomContainer.classList.remove('hidden');

            // Simulate Trial Transcript Animation
            for (let i = 0; i < data.trial_log.length; i++) {
                const log = data.trial_log[i];
                await simulateStatement(log, i * 200); // Stagger animations slightly
            }

        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while simulating the trial.');
            spinner.classList.add('hidden');
        } finally {
            submitBtn.disabled = false;
        }
    });

    async function simulateStatement(log, delay) {
        return new Promise(resolve => {
            setTimeout(async () => {
                const statementDiv = document.createElement('div');
                statementDiv.className = `statement-card statement-${log.role} p-4 rounded-r-xl slide-up`;

                let roleColor = 'text-gray-400';
                if (log.role === 'Judge') roleColor = 'text-accentGold';
                if (log.role === 'Prosecutor') roleColor = 'text-accentRed';
                if (log.role === 'Defense') roleColor = 'text-accentBlue';

                statementDiv.innerHTML = `
                    <div class="flex items-baseline gap-2 mb-1">
                        <span class="font-bold text-white text-lg">${log.character.name}</span>
                        <span class="text-xs font-semibold ${roleColor} uppercase tracking-wider">[${log.role} - ${log.phase}]</span>
                    </div>
                    <div class="text-gray-300 italic statement-text pl-2 border-l-2 border-gray-600/50"></div>
                `;

                transcriptLog.appendChild(statementDiv);

                // Auto-scroll
                transcriptLog.scrollTop = transcriptLog.scrollHeight;

                const textContainer = statementDiv.querySelector('.statement-text');
                await typeText(textContainer, `"${log.statement}"`, 15);

                resolve();
            }, delay);
        });
    }
});