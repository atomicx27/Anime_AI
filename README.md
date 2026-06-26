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

### 7. Anime Debate Arena AI

The **Anime Debate Arena AI** is a web-based, multi-agent application where you can watch iconic anime characters clash in a battle of ideals. You enter a topic, and the system selects two characters with contrasting traits to debate, while a third character acts as the judge to deliver a final verdict based on their unique philosophies.

#### Folder Location
`anime_debate_arena/`

#### Features
- **Dynamic Debater Selection**: Randomly selects two debaters and one judge from the roster to provide unique perspectives on the topic.
- **Simulated Debate Generation**: Constructs an argument and rebuttal based on the characters' Core Emotion, Personality Profile, and Unique Quality.
- **Sleek, Animated UI**: Features a modern, glassmorphism interface built with Tailwind CSS, displaying live character cards and a smoothly typing chat transcript.
### Anime Power Scaler AI

The **Anime Power Scaler AI** is a web-based, multi-agent application that evaluates how anime characters from the database would scale against a user-provided opponent or threat. It dynamically evaluates their "Core Emotion", "Personality Profile", and "Unique Quality & Philosophy" to categorize them into power tiers like Overkill, Even Match, Underdog, or Support.
### 7. Anime Power Scaler AI

The **Anime Power Scaler AI** is a web-based, multi-agent application that pits a user's custom character or ability description against the entire anime roster. The AI acts as a combat analyst, simulating 1v1 matchups by evaluating core emotions and unique qualities to declare a Win, Loss, or Draw for each character.

#### Folder Location
`anime_power_scaler/`

#### Features
- **Dynamic Power Scaling**: An agent reads a user-inputted opponent and generates a battle strategy and tier ranking for every character.
- **Categorized Tier Outcomes**: Characters are assigned specific tiers (e.g., Overkill, Even Match) based on their psychological profiles and powers.
- **Sleek, Animated UI**: A modern, dark-themed interface built with Tailwind CSS featuring animated result cards and visually appealing tier indicators.
- **Dynamic Matchup Evaluation**: The agent analyzes custom user abilities and compares them against every character's traits in the database.
- **Visual Matchup Cards**: A sleek frontend UI using Tailwind CSS presents visually distinct results (Win/Loss/Draw) with detailed explanations.
- **Dynamic Character Loading**: Backend API automatically parses the root `README.md` to dynamically load character details for scaling.
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
cd anime_debate_arena/backend
cd anime_power_scaler/backend
cd anime_affinity_matcher/backend
pip install -r requirements.txt

# Run the server
python3 main.py

# Access the UI
# Open your browser and navigate to http://localhost:8006/
# Open your browser and navigate to the frontend/index.html file locally.
# Open your browser and navigate to http://localhost:8006/
# Open your browser and navigate to the frontend index.html file, or use a local HTTP server in the frontend directory.
```
### 8. Anime Detective Agency AI

The **Anime Detective Agency AI** is a web-based, multi-agent application that acts as an orchestration system for solving mysteries. Users submit a "case file" or mystery description, and the AI evaluates all characters from the database based on their Core Emotion, Personality Profile, and Unique Quality to assign them specialized roles within the detective agency (e.g., Lead Detective, Forensics, Interrogator, Enforcer).

### 8. Anime Detective Agency AI

The **Anime Detective Agency AI** is a web-based, multi-agent application where users provide a mystery or crime scene description. The AI acts as a Chief Inspector and assigns unique deductive roles to anime characters based on their core traits, providing diverse perspectives on the case.
The **Anime Detective Agency AI** is a web-based, multi-agent application that acts as an intelligent investigative task force. Users submit a mystery or case description, and the AI evaluates all characters from the table based on their Core Emotion, Personality Profile, and Unique Quality to assign them specialized roles within the detective agency (e.g., Lead Detective, Medical Examiner, Interrogator, Forensics).
The **Anime Detective Agency AI** is a web-based, multi-agent application that acts as a premier investigation team. Users submit a description of a crime or mystery, and the AI evaluates all characters from the table based on their Core Emotion, Personality Profile, and Unique Quality to assign them specialized investigation roles (e.g., Lead Investigator, Forensics Analyst, Interrogator, Profiler).
The **Anime Detective Agency AI** is a web-based, multi-agent application where characters form an investigation team to solve mysteries submitted by the user.

#### Folder Location
`anime_detective_agency/`

#### Features
- **Dynamic Role Assignment**: The agent analyzes the case description and character traits to logically assign roles that best fit their psychological profiles and abilities.
- **Investigative Insights**: Generates unique, character-specific strategies and insights on how they would approach solving the case.
- **Sleek UI/UX**: Features a modern, cyberpunk-inspired dark theme built with Tailwind CSS, including an animated "Director AI Terminal" and stylish glassmorphism role cards.
- **Dynamic Role Assignment**: The agent analyzes characters' psychological profiles to assign roles like "Forensic Analyst", "Psychological Profiler", or "Enforcer".
- **Unique Deductions**: Each character investigates the case and provides simulated insights colored by their core emotion and philosophy.
- **Sleek UI/UX**: Features a modern, dark-themed interface built with Tailwind CSS, including a typing-effect Chief Inspector terminal and visually appealing investigation cards.
- **Dynamic Role Assignment**: The agent analyzes the user's mystery input and assigns highly specific investigation roles to each character based on their unique traits and psychological profiles.
- **In-Character Insights**: Characters provide tailored insights or proposed actions for the investigation, reflecting their core philosophy (e.g., Naruto using "Talk no Jutsu" for interrogation).
- **Agent Terminal Log**: An animated "Agent Thoughts Terminal" displays the system's live evaluation and assignment process.
- **Sleek UI/UX**: Built with Vanilla HTML, JS, and Tailwind CSS, featuring a beautiful dark theme with glassmorphism, radial gradients, shadow glows, and smooth hover animations.
- **Dynamic Character Loading**: Backend API automatically parses the root `README.md` to load character details dynamically.
- **Dynamic Role Assignment**: The agent analyzes character traits and dynamically assigns them to specific investigative roles best suited to their personalities and skills.
- **Agentic Simulation**: A backend `DetectiveAgencyAgent` generates unique, character-specific investigation strategies and findings for each assigned role.
- **Modern UI/UX**: Features a highly polished interface built with Tailwind CSS, incorporating glassmorphism, radial gradients, shadow glows, and smooth hover animations.
- **Dynamic Character Loading**: Backend API automatically parses the root `README.md` to load character details dynamically.
- **Dynamic Role Assignment**: The DetectiveAgent automatically assigns roles like "Lead Detective", "Forensics/Analyst", and "Interrogator/Enforcer" based on the characters' Core Emotion, Personality Profile, and Unique Quality.
- **Agentic Investigation Log**: A generated log showing how the assigned team evaluates the user's mystery, highlighting each character's unique traits in their actions.
- **Sleek UI/UX**: Built with Vanilla HTML, JS, and Tailwind CSS, featuring glassmorphism panels, glowing shadow effects, and smooth rendering of the agent thought process.
- **Dynamic Character Loading**: Backend API automatically parses the root `README.md` to dynamically load character details for the agency.
### 8. Anime Courtroom AI

The **Anime Courtroom AI** is a web-based, multi-agent application that simulates a trial where anime characters take on the roles of Judge, Prosecutor, Defense Attorney, and Jury. It dynamically evaluates their "Core Emotion", "Personality Profile", and "Unique Quality & Philosophy" to determine the verdict of a user-submitted case.

### 8. Anime Courtroom AI

The **Anime Courtroom AI** is a web-based, multi-agent application that simulates a trial based on a user-provided case or moral dilemma. The AI automatically assigns characters from the database to roles such as Judge, Prosecutor, Defense, and Jury based on their "Core Emotion" and "Personality Profile."
### 8. Anime Courtroom AI

The **Anime Courtroom AI** is a web-based, multi-agent application that simulates a trial based on a user-submitted crime or action. The AI dynamically assigns the roles of Judge, Prosecutor, and Defense Attorney to anime characters based on their Core Emotion and Personality Profile, and generates a realistic mock trial transcript.

#### Folder Location
`anime_courtroom/`

#### Features
- **Dynamic Role Assignment**: Agents analyze character traits to assign suitable courtroom roles (e.g., logical characters as Judges, protective characters as Defense).
- **Agentic Trial Simulation**: Generates in-character opening statements, jury deliberation thoughts, and a final verdict based on the characters' worldviews.
- **Sleek, Animated UI**: A modern, dark-themed interface built with Tailwind CSS featuring an animated trial transcript and distinct role cards with glassmorphism effects.
- **Dynamic Role Assignment**: Characters are dynamically slotted into courtroom roles based on their traits (e.g., stoic/logical characters become Judges, empathetic characters become Defense).
- **Agentic Simulation**: Generates a simulated trial transcript where each character argues the case according to their "Unique Quality & Philosophy."
- **Cinematic UI/UX**: A modern, dark-themed interface built with Tailwind CSS featuring glassmorphism, radial gradients, shadow glows, smooth hover animations, and a real-time typing transcript.
- **Dynamic Character Loading**: Backend API automatically parses the root `README.md` to load character details for the simulation.
- **Dynamic Role Assignment**: Characters are categorized into Judicial, Prosecutorial, or Defense roles based on traits like logic, ambition, or empathy.
- **Agentic Simulation**: Generates in-character opening statements, rebuttals, and a final verdict directly influenced by the characters' Unique Qualities.
- **Sleek UI/UX**: A modern, dark-themed interface built with Tailwind CSS featuring glassmorphism, radial gradients, shadow glows, and smooth message animations.
- **Dynamic Character Loading**: Backend API automatically parses the root `README.md` to load character details.

#### How to Run
```bash
# Install dependencies
cd anime_detective_agency/backend
cd anime_courtroom/backend
pip install -r requirements.txt

# Run the server
python3 main.py

# Access the UI
# Open your browser and navigate to the frontend index.html file locally.
# Open your browser and navigate to http://localhost:8008/ using a local HTTP server in the frontend directory.
# Open your browser and navigate to http://localhost:8007/ if the frontend is served,
# or open the anime_detective_agency/frontend/index.html file locally.
# Open your browser and navigate to http://localhost:8007/
```

### 9. Anime Survival Game AI

The **Anime Survival Game AI** is a web-based, multi-agent application that simulates a catastrophic survival scenario. Users input a description of a crisis (e.g., zombie apocalypse, deserted island), and the AI evaluates all characters from the table based on their Core Emotion, Personality Profile, and Unique Quality to assign them survival roles and simulate who lives and who dies.

#### Folder Location
`anime_survival_game/`

#### Features
- **Dynamic Role Assignment**: The agent analyzes character traits and assigns them to roles like "Leader/Strategist", "Scavenger/Forager", "Defender/Vanguard", or "Medic/Support".
- **Agentic Survival Simulation**: Generates unique, character-specific survival strategies and determines their ultimate fate based on their assigned role and a probabilistic simulation.
- **Modern UI/UX**: Features a highly polished interface built with Tailwind CSS, incorporating glassmorphism, radial gradients, glowing elements, and an animated AI thought terminal.
- **Dynamic Character Loading**: Backend API automatically parses the root `README.md` to load character details dynamically.

#### How to Run
```bash
# Install dependencies
cd anime_survival_game/backend
pip install -r requirements.txt

# Run the server
python3 main.py

# Access the UI
# Open your browser and navigate to http://localhost:8008/
```
