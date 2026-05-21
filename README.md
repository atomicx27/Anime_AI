# Anime_AI

# Comprehensive Character Data Table

| Character | Archetype & MBTI | Core Emotion | Personality Profile | Unique Quality & Philosophy |
|---|---|---|---|---|
| Naruto Uzumaki | Protagonist, ENFP | Desire for Acknowledgment & Empathy | Boisterous, exuberant, and deeply determined. Masks his childhood loneliness with loud antics but possesses an unbreakable will. | "Talk no Jutsu" — the ability to resonate with the trauma of his enemies, forcing them to reflect on their own pain. |
| Son Goku | Protagonist, ENFP | Excitement for Combat & Self-Improvement | Innocent, cheerful, and obsessively competitive regarding martial arts. Fights for the thrill of facing stronger opponents. | Limitless potential driven strictly by intrinsic motivation rather than external malice. Purity of heart allows emotional clarity. |
| Ichigo Kurosaki | Protagonist | Duty & The Desire to Protect | Stubborn, short-tempered, and fiercely loyal. Seeks only the power necessary to protect his immediate friends and family. | A reactive evolutionary curve merging spiritual races. Adapts and powers up directly in response to specific threats to loved ones. |
| Rimuru Tempest | Protagonist | Desire for Comfort & Peaceful Coexistence | Pragmatic, easygoing, and diplomatic. Avoids unnecessary conflict but becomes ruthlessly calculating if his subordinates are threatened. | Limitless adaptability combined with extreme political acumen. Solves problems through economic trade and diplomacy. |
| Asta | Protagonist, ESFP | Defiance & Unyielding Determination | Loud, hyperactive, and perpetually optimistic. Refuses to acknowledge societal limits and responds to despair with physical effort. | Wielding Anti-Magic. His sheer physical grit turns his greatest biological flaw into the ultimate counter-meta weapon. |
| Yuno | Rival, INTJ | Calm Ambition & Hidden Passion | Quiet, composed, and outwardly aloof. Rarely shows emotion but shares a deeply competitive bond with Asta. | Effortless talent masking extreme dedication. Respects hard work and uses Asta's effort as a benchmark for his own mastery. |
| Natsu Dragneel | Protagonist, Enneagram 7w6 | Fiery Passion & Familial Love | Reckless, destructive, but intensely loyal to his guild. Operates entirely on instinct and emotion. | Emotional resonance directly tied to physical magic power. Turns literal emotions into fuel, scaling proportionally to his desire to protect. |
| Itachi Uchiha | Antagonist, INFJ | Deep Love Masked by Cold Logic | Stoic, hyper-intelligent, and tragic. Operates with a utilitarian mindset, bearing the hatred of the world to prevent a greater war. | Mastery of genjutsu reflecting his life: a complex, painful illusion manipulating outcomes for the greater good at the cost of his own soul. |
| Obito Uchiha | Antagonist, ENFP | Grief, Despair & Nihilism | Once optimistic, trauma shattered his worldview, turning him manipulative and cynical. Views reality as "hell" and seeks to replace it entirely. | Kamui is the literal manifestation of his psychological state: the ability to slip through reality and escape to an isolated dimension. |
| Madara Uchiha | Antagonist, ENTJ | Arrogance & Absolute Control | Prideful, battle-hungry, and philosophically cynical. Believes true peace requires subjugation and a forced unified reality. | Overwhelming martial and strategic dominance. Possesses generational patience and sheer combat power to enforce his will. |
| Vegeta | Rival | Pride & Deep-Seated Inferiority | Arrogant, abrasive, yet constantly evolving. A lifelong struggle to reclaim his pride while slowly learning humility and familial love. | Profound character development. Transitions from a genocidal conqueror to a dedicated protector, using rivalry for endless self-betterment. |
| Jiraiya | Mentor, ENFP | Regret & Hope for the Future | Outwardly goofy and relaxed, but inwardly melancholic and deeply wise. Carries the weight of past failures. | The ultimate teacher. His unique contribution is his philosophy of enduring pain and refusing to give up, passed to the next generation. |
| Pain (Nagato) | Antagonist, INFP | Shared Trauma & Divine Justice | Cold, emotionless, and harboring a god complex. Desires world peace through collective, devastating trauma. | The philosophy of shared pain. Weaponizes trauma using the Rinnegan to force the world into a state of terrified pacifism. |
| Kakashi Hatake | Mentor, INTJ | Regret & Acceptance | Aloof, laid-back, and strictly punctual. Uses a detached exterior to mask severe PTSD, prioritizing teamwork above rigid rules. | Bridges the gap between raw talent and applied wisdom. Teaches his students to break the rules that led to his own psychological ruin. |

---

## Projects

### 1. Anime Agents CLI

The **Anime Agents CLI** is an interactive command-line application that acts as a wrapper around the characters defined in the table above. It parses this `README.md` to dynamically load each character's traits, and then sets up an AI Agent system prompt tailored to their Core Emotion, Personality Profile, and Unique Quality & Philosophy.

#### Folder Location
`anime_agents_cli/`

#### Features
- **Dynamic Markdown Parsing**: Automatically extracts character data from this README.
- **Agent Initialization**: Constructs a tailored LLM system prompt instructing the agent to adopt the specific character's persona and core emotions.
- **Interactive Chat Interface**: A simple command-line chat where users can select a character and engage in conversation (currently utilizing a mock fallback, extensible with OpenAI/Anthropic APIs).

#### How to Run
```bash
cd anime_agents_cli
python3 main.py
```

### 2. Anime Council AI

The **Anime Council AI** is a collaborative command-line agentic application where all characters from the table assemble as a "council". It dynamically loads character data and acts as an orchestrator (a Moderator Agent), prompting each character agent to give advice based on their core emotion, personality profile, and unique philosophy.

#### Folder Location
`anime_council/`

#### Features
- **Dynamic Markdown Parsing**: Extends the original parsing logic to assemble all characters.
- **Council Meeting Interface**: Users input a topic or problem, and each Character Agent provides templated insights rooted in their unique traits.
- **Moderator Synthesis**: The system collects all insights and synthesizes a final resolution representing the combined philosophical angles of the entire council.

#### How to Run
```bash
cd anime_council
python3 main.py
```

### 3. Anime Group Chat

The **Anime Group Chat** is a web-based, multi-agent application that simulates a Discord-like chat environment. Instead of talking to a single character, users interact with a simulated "server" where an Orchestrator AI dynamically selects multiple characters from the roster to respond to user messages, creating a cohesive, group-based conversational dynamic.

#### Folder Location
`anime_group_chat/`

#### Features
- **Group Conversation Dynamics**: An Orchestrator Agent reads the user's input and selects 2-4 distinct characters to provide sequential, context-aware responses.
- **Discord-like UI/UX**: A modern, sleek frontend built with Tailwind CSS mimicking a popular chat app interface, complete with online status, custom avatars, and message formatting.
- **Dynamic Character Loading**: Backend API automatically parses the root `README.md` to load character details and serve them to the UI.

#### How to Run
```bash
# Install dependencies
cd anime_group_chat/backend
pip install -r requirements.txt

# Run the server
python3 main.py

# Access the UI
# Open your browser and navigate to http://localhost:8001/
```

### 4. Anime Scenario Ranker AI

The **Anime Scenario Ranker AI** is a web-based, multi-agent application that evaluates a given hypothetical scenario and dynamically ranks the anime characters into a Tier List (S, A, B, C, D) based on their Core Emotion, Personality Profile, and Unique Quality.

#### Folder Location
`anime_scenario_ranker/`

#### Features
- **Dynamic Scenario Evaluation**: A Scenario Ranker Agent reads the user's scenario input and evaluates every character in the database against it.
- **Real-time Thought Terminal**: See the agent's thought process as it evaluates each character's traits and decides their rank.
- **Animated Tier List UI**: A sleek, responsive frontend built with Tailwind CSS that dynamically organizes characters into a visually appealing tier list, complete with tooltips explaining the reasoning for their rank.
- **Dynamic Character Loading**: Backend API automatically parses the root `README.md` to load character details and evaluate them.

#### How to Run
```bash
# Install dependencies
cd anime_scenario_ranker/backend
pip install -r requirements.txt

# Run the server
python3 main.py

# Access the UI
# Open your browser and navigate to http://localhost:8002/
```
