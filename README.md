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

### 5. Anime Team Builder AI

The **Anime Team Builder AI** is a web-based, agentic application that acts as an intelligent squad commander. Users describe a complex mission, and the AI evaluates all characters from the table based on their Core Emotion, Personality Profile, and Unique Quality to assemble the optimal team for the job.

#### Folder Location
`anime_team_builder/`

#### Features
- **Intelligent Role Assignment**: The agent analyzes mission requirements (e.g., combat, stealth, diplomacy) and matches characters to roles like Combat Specialist, Diplomat, or Strategist based on their specific traits.
- **Dynamic Team Composition**: Automatically selects the top candidates and provides a detailed rationale for why they are the best fit for the mission.
- **Sleek UI/UX**: Features a modern, dark-themed interface built with Tailwind CSS, including an animated "Commander Terminal" that displays the agent's thought process in real-time.
- **Dynamic Character Loading**: Backend API automatically parses the root `README.md` to load character details.

#### How to Run
```bash
# Install dependencies
cd anime_team_builder/backend
pip install -r requirements.txt

# Run the server
python3 main.py

# Access the UI
# Open your browser and navigate to http://localhost:8004/
```

### 6. Anime Matchmaker AI

The **Anime Matchmaker AI** is a web-based, agentic application that acts as a personal matchmaker for the user. Users describe their own personality profile and relationship preferences (e.g., friendship, romance, rival), and the AI evaluates all characters from the table to find the best possible matches based on their Core Emotion and Personality Profile.

#### Folder Location
`anime_matchmaker/`

#### Features
- **Personality Matching Algorithm**: The Matchmaker Agent analyzes the user's input and scores compatibility based on shared values, complementary traits, or desired relationship dynamics.
- **Dynamic Relationship Types**: Users can seek different types of connections (Friendship, Romance, Rivalry, Mentor), which changes the agent's evaluation criteria.
- **Agent Output Terminal**: A live, animated terminal UI displays the agent's thought process as it evaluates each character.
- **Sleek UI/UX**: Built with Vanilla HTML, JS, and Tailwind CSS, featuring smooth animations and a modern dark theme.
### 6. Anime Debate Arena AI

The **Anime Debate Arena AI** is an intelligent web-based platform that dynamically selects two characters with contrasting philosophies to engage in a formal debate on any given topic.

#### Folder Location
`anime_debate_arena/`

#### Features
- **Dynamic Matchmaking**: An agent categorizes characters by their Core Emotion and pairs diametrically opposed perspectives for maximum conflict.
- **Agentic Simulation**: A backend `DebateAgent` generates in-character opening statements and rebuttals based directly on the characters' Unique Qualities.
- **Cinematic UI**: An animated Tailwind CSS frontend that simulates an AI thought terminal followed by a theatrical "VS" screen and typing-effect chat transcript.
### 6. Anime World Simulator AI

The **Anime World Simulator AI** is a web-based, multi-agent application that simulates how the characters in the database would react to a global event or crisis. It dynamically evaluates their "Core Emotion", "Personality Profile", and "Unique Quality & Philosophy" to determine an "Action State" (Aggressive, Defensive, Diplomatic, etc.) and generates a personalized reaction strategy.

#### Folder Location
`anime_world_simulator/`

#### Features
- **Dynamic Scenario Processing**: An agent reads a user-inputted scenario and generates unique reactions for every character simultaneously.
- **Action State Categorization**: Characters are assigned specific states (e.g., Strategic, Chaotic, Protective) based on their psychological profiles.
- **Sleek, Animated UI**: A modern, dark-themed interface built with Tailwind CSS featuring an animated terminal log and responsive, color-coded character cards.
- **Dynamic Character Loading**: Backend API automatically parses the root `README.md` to load character details.

#### How to Run
```bash
# Install dependencies
cd anime_matchmaker/backend
cd anime_debate_arena/backend
cd anime_world_simulator/backend
pip install -r requirements.txt

# Run the server
python3 main.py

# Access the UI
# Open your browser and navigate to http://localhost:8005/
```

### 7. Anime Affinity Matcher AI

The **Anime Affinity Matcher AI** is a web-based, agentic application that acts as a personalized matchmaking system. Users input a self-description encompassing their personality, goals, and values. The AI evaluates this input against all characters from the table based on their Core Emotion, Personality Profile, and Unique Quality to categorize them into affinities like "Soulmate/Best Friend", "Rival", "Mentor", or "Opposite/Enemy".

#### Folder Location
`anime_affinity_matcher/`

#### Features
- **Intelligent Affinity Categorization**: The agent analyzes the user's personality traits and calculates similarity/difference scores against the characters to dynamically match them into relationship archetypes.
- **Dynamic Reasoning**: The agent provides a detailed rationale explaining why a character matches the user's specific input.
- **Sleek UI/UX**: Features a modern, dark-themed interface built with Tailwind CSS, including an animated "Agent Thought Process" terminal and stylish character match cards.
- **Dynamic Character Loading**: Backend API automatically parses the root `README.md` to load character details.

#### How to Run
```bash
# Install dependencies
cd anime_affinity_matcher/backend
pip install -r requirements.txt

# Run the server
python3 main.py

# Access the UI
# Open your browser and navigate to the frontend index.html file, or use a local HTTP server in the frontend directory.
```
