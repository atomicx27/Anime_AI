import React, { useState, useEffect, useRef } from 'react';
import './index.css';

function App() {
  const [agents, setAgents] = useState([]);
  const [selectedAgent, setSelectedAgent] = useState(null);
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  useEffect(() => {
    fetch('http://localhost:8000/api/agents')
      .then((res) => res.json())
      .then((data) => setAgents(data.agents))
      .catch((err) => console.error("Error fetching agents:", err));
  }, []);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, loading]);

  const selectAgent = (agent) => {
    setSelectedAgent(agent);
    setMessages([{ role: 'system', content: `Chat started with ${agent.name}` }]);
  };

  const sendMessage = async (e) => {
    e.preventDefault();
    if (!input.trim() || !selectedAgent) return;

    const userMessage = { role: 'user', content: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput('');
    setLoading(true);

    try {
      const response = await fetch('http://localhost:8000/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          agent_name: selectedAgent.name,
          message: input,
        }),
      });

      const data = await response.json();

      const agentMessage = {
        role: 'agent',
        content: data.final_answer,
        log: data.log,
        thought: data.thought
      };

      setMessages((prev) => [...prev, agentMessage]);
    } catch (err) {
      console.error("Error sending message:", err);
      setMessages((prev) => [...prev, { role: 'system', content: "Error communicating with agent." }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex h-screen bg-gray-900 text-white font-sans">
      {/* Sidebar */}
      <div className="w-64 bg-gray-800 border-r border-gray-700 flex flex-col">
        <div className="p-4 border-b border-gray-700">
          <h1 className="text-xl font-bold text-cyan-400">Anime Agents</h1>
        </div>
        <div className="flex-1 overflow-y-auto">
          {agents.map((agent) => (
            <div
              key={agent.name}
              onClick={() => selectAgent(agent)}
              className={`p-4 cursor-pointer hover:bg-gray-700 transition-colors border-b border-gray-700 ${
                selectedAgent?.name === agent.name ? 'bg-gray-700 border-l-4 border-cyan-400' : ''
              }`}
            >
              <h3 className="font-semibold">{agent.name}</h3>
              <p className="text-xs text-gray-400 truncate">{agent.core_emotion}</p>
            </div>
          ))}
        </div>
      </div>

      {/* Main Chat Area */}
      <div className="flex-1 flex flex-col relative">
        {selectedAgent ? (
          <>
            {/* Header */}
            <div className="p-4 bg-gray-800 border-b border-gray-700 shadow-sm flex items-center justify-between z-10">
              <div>
                <h2 className="text-lg font-bold text-cyan-400">{selectedAgent.name}</h2>
                <p className="text-xs text-gray-400">{selectedAgent.archetype}</p>
              </div>
            </div>

            {/* Chat History */}
            <div className="flex-1 overflow-y-auto p-4 space-y-6 bg-gray-900">
              {messages.map((msg, index) => (
                <div key={index} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                  {msg.role === 'system' ? (
                    <div className="mx-auto bg-gray-800 text-gray-400 text-xs py-1 px-3 rounded-full">
                      {msg.content}
                    </div>
                  ) : (
                    <div className={`max-w-[80%] ${msg.role === 'user' ? '' : 'w-full'}`}>
                      {/* Thought Process (only for agent) */}
                      {msg.role === 'agent' && msg.log && (
                        <div className="mb-2 bg-gray-800/50 rounded-lg p-3 text-xs border border-gray-700">
                          <details className="cursor-pointer outline-none">
                            <summary className="text-cyan-500 font-semibold mb-1 hover:text-cyan-400 transition-colors">
                              View Thought Process & Tool Usage
                            </summary>
                            <div className="mt-2 space-y-2 text-gray-300">
                              {msg.log.map((logItem, i) => (
                                <div key={i} className="pl-2 border-l-2 border-gray-600">
                                  {logItem.type === 'tool_execution' ? (
                                    <>
                                      <div className="text-purple-400 font-semibold mt-1">Tool: {logItem.tool}</div>
                                      <div className="text-gray-400 bg-black/30 p-1 rounded mt-1 overflow-x-auto">Input: {logItem.input}</div>
                                      <div className="text-green-400 bg-black/30 p-1 rounded mt-1 overflow-x-auto">Observation: {logItem.observation}</div>
                                    </>
                                  ) : (
                                    <div className="whitespace-pre-wrap">{logItem.content}</div>
                                  )}
                                </div>
                              ))}
                            </div>
                          </details>
                        </div>
                      )}

                      {/* The actual message bubble */}
                      <div className={`p-4 rounded-2xl shadow-sm ${
                        msg.role === 'user'
                          ? 'bg-cyan-600 text-white rounded-tr-none'
                          : 'bg-gray-800 text-gray-100 rounded-tl-none border-l-2 border-cyan-500'
                      }`}>
                        {msg.content}
                      </div>
                    </div>
                  )}
                </div>
              ))}
              {loading && (
                <div className="flex justify-start">
                  <div className="bg-gray-800 text-gray-400 p-3 rounded-2xl rounded-tl-none border-l-2 border-cyan-500 flex items-center space-x-2">
                    <div className="w-2 h-2 bg-cyan-500 rounded-full animate-pulse"></div>
                    <div className="w-2 h-2 bg-cyan-500 rounded-full animate-pulse delay-75"></div>
                    <div className="w-2 h-2 bg-cyan-500 rounded-full animate-pulse delay-150"></div>
                  </div>
                </div>
              )}
              <div ref={messagesEndRef} />
            </div>

            {/* Input Area */}
            <div className="p-4 bg-gray-800 border-t border-gray-700">
              <form onSubmit={sendMessage} className="flex space-x-2">
                <input
                  type="text"
                  value={input}
                  onChange={(e) => setInput(e.target.value)}
                  placeholder="Chat with your agent..."
                  className="flex-1 bg-gray-900 border border-gray-700 rounded-lg px-4 py-3 focus:outline-none focus:border-cyan-500 focus:ring-1 focus:ring-cyan-500 transition-colors"
                  disabled={loading}
                />
                <button
                  type="submit"
                  disabled={loading || !input.trim()}
                  className="bg-cyan-600 hover:bg-cyan-500 disabled:opacity-50 text-white px-6 py-3 rounded-lg font-semibold transition-colors"
                >
                  Send
                </button>
              </form>
            </div>
          </>
        ) : (
          <div className="flex-1 flex items-center justify-center bg-gray-900 text-gray-500">
            <div className="text-center">
              <div className="text-6xl mb-4">🤖</div>
              <h2 className="text-xl font-bold">Select an Agent</h2>
              <p className="mt-2 text-sm">Choose a character from the sidebar to begin chatting.</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
