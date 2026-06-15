import React, { useState, useEffect, useRef } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Send, Bot, User, Sparkles } from 'lucide-react';
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
    <div className="flex h-screen bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900 animate-gradient-x text-white font-sans">
      {/* Sidebar */}
      <div className="w-72 bg-gray-900/50 backdrop-blur-md border-r border-gray-800 flex flex-col shadow-xl z-20">
        <div className="p-6 border-b border-gray-800 flex items-center gap-3">
          <div className="bg-cyan-500/20 p-2 rounded-xl shadow-[0_0_15px_rgba(34,211,238,0.3)]">
            <Sparkles className="w-6 h-6 text-cyan-400" />
          </div>
          <h1 className="text-xl font-extrabold bg-clip-text text-transparent bg-gradient-to-r from-cyan-400 to-blue-500 tracking-tight drop-shadow-[0_0_8px_rgba(34,211,238,0.4)]">Anime Agents</h1>
        </div>
        <div className="flex-1 overflow-y-auto py-2 custom-scrollbar">
          <AnimatePresence>
            {agents.map((agent, index) => (
              <motion.div
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                whileHover={{ scale: 1.02, x: 5 }}
                whileTap={{ scale: 0.98 }}
                transition={{ duration: 0.3, delay: index * 0.05 }}
                key={agent.name}
                onClick={() => selectAgent(agent)}
                className={`mx-3 my-1 p-3 rounded-xl cursor-pointer transition-all duration-300 border border-transparent flex items-center gap-3 group ${
                  selectedAgent?.name === agent.name
                    ? 'bg-gradient-to-r from-cyan-900/40 to-blue-900/40 border-cyan-500/50 shadow-[0_0_15px_rgba(6,182,212,0.3)]'
                    : 'hover:bg-gray-800/80 hover:border-gray-600 hover:shadow-[0_0_10px_rgba(255,255,255,0.05)]'
                }`}
              >
                <div className={`w-10 h-10 rounded-full flex items-center justify-center shrink-0 transition-colors ${
                  selectedAgent?.name === agent.name ? 'bg-cyan-500 text-white shadow-lg shadow-cyan-500/30' : 'bg-gray-800 text-gray-400'
                }`}>
                  <Bot size={20} />
                </div>
                <div className="min-w-0 flex-1">
                  <h3 className={`font-semibold truncate transition-colors ${selectedAgent?.name === agent.name ? 'text-cyan-400' : 'text-gray-200'}`}>{agent.name}</h3>
                  <p className="text-xs text-gray-500 truncate">{agent.core_emotion}</p>
                </div>
              </motion.div>
            ))}
          </AnimatePresence>
        </div>
      </div>

      {/* Main Chat Area */}
      <div className="flex-1 flex flex-col relative bg-[radial-gradient(ellipse_at_top_right,_var(--tw-gradient-stops))] from-gray-800/40 via-gray-900 to-black animate-gradient-xy">
        {selectedAgent ? (
          <>
            {/* Header */}
            <div className="p-5 bg-gray-900/80 backdrop-blur-md border-b border-gray-800 shadow-sm flex items-center gap-4 z-10">
              <div className="w-12 h-12 bg-cyan-500 rounded-full flex items-center justify-center text-white shadow-lg shadow-cyan-500/20 shrink-0">
                <Bot size={24} />
              </div>
              <div>
                <h2 className="text-lg font-bold text-white tracking-wide">{selectedAgent.name}</h2>
                <p className="text-sm text-cyan-400/80 font-medium">{selectedAgent.archetype}</p>
              </div>
            </div>

            {/* Chat History */}
            <div className="flex-1 overflow-y-auto p-6 space-y-6 custom-scrollbar">
              <AnimatePresence>
                {messages.map((msg, index) => (
                  <motion.div
                    initial={{ opacity: 0, y: 20, scale: 0.95 }}
                    animate={{ opacity: 1, y: 0, scale: 1 }}
                    transition={{ duration: 0.5, type: "spring", stiffness: 300, damping: 20, delay: index * 0.05 }}
                    key={index}
                    className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}
                  >
                    {msg.role === 'system' ? (
                      <div className="mx-auto bg-gray-800/60 backdrop-blur-sm border border-gray-700/50 text-gray-400 text-xs py-1.5 px-4 rounded-full shadow-sm">
                        {msg.content}
                      </div>
                    ) : (
                      <div className={`flex gap-3 max-w-[85%] ${msg.role === 'user' ? 'flex-row-reverse' : 'flex-row'}`}>
                        {/* Avatar */}
                        <div className={`w-8 h-8 rounded-full flex items-center justify-center shrink-0 mt-1 shadow-sm ${
                          msg.role === 'user' ? 'bg-blue-600' : 'bg-cyan-600'
                        }`}>
                          {msg.role === 'user' ? <User size={16} /> : <Bot size={16} />}
                        </div>

                        <div className={`flex flex-col ${msg.role === 'user' ? 'items-end' : 'items-start'}`}>
                          {/* Thought Process (only for agent) */}
                          {msg.role === 'agent' && msg.log && (
                            <div className="mb-2 bg-gray-900/60 backdrop-blur-sm rounded-xl p-3 text-xs border border-gray-800 shadow-inner w-full max-w-xl">
                              <details className="cursor-pointer outline-none group">
                                <summary className="text-cyan-400/80 font-medium hover:text-cyan-300 transition-colors flex items-center gap-2 list-none">
                                  <div className="w-4 h-4 flex items-center justify-center transition-transform group-open:rotate-90">
                                    ▶
                                  </div>
                                  View Thought Process & Tool Usage
                                </summary>
                                <div className="mt-3 space-y-3 text-gray-300 pt-2 border-t border-gray-800">
                                  {msg.log.map((logItem, i) => (
                                    <div key={i} className="pl-3 border-l-2 border-gray-700">
                                      {logItem.type === 'tool_execution' ? (
                                        <div className="space-y-1">
                                          <div className="text-fuchsia-400 font-semibold text-[11px] uppercase tracking-wider">🛠 Tool: {logItem.tool}</div>
                                          <div className="text-gray-300 bg-black/40 p-2 rounded-lg mt-1 overflow-x-auto font-mono text-[11px] border border-gray-800/50">Input: {logItem.input}</div>
                                          <div className="text-emerald-400 bg-black/40 p-2 rounded-lg mt-1 overflow-x-auto font-mono text-[11px] border border-gray-800/50">Observation: {logItem.observation}</div>
                                        </div>
                                      ) : (
                                        <div className="whitespace-pre-wrap leading-relaxed text-[13px]">{logItem.content}</div>
                                      )}
                                    </div>
                                  ))}
                                </div>
                              </details>
                            </div>
                          )}

                          {/* The actual message bubble */}
                          <div className={`p-4 rounded-2xl shadow-md text-[15px] leading-relaxed ${
                            msg.role === 'user'
                              ? 'bg-gradient-to-br from-blue-600 to-blue-700 text-white rounded-tr-sm shadow-blue-900/20'
                              : 'bg-gray-800/90 backdrop-blur-sm text-gray-100 rounded-tl-sm border border-gray-700 shadow-black/20'
                          }`}>
                            {msg.content}
                          </div>
                        </div>
                      </div>
                    )}
                  </motion.div>
                ))}
              </AnimatePresence>
              {loading && (
                <motion.div
                  initial={{ opacity: 0, y: 15, scale: 0.95 }}
                  animate={{ opacity: 1, y: 0, scale: 1 }}
                  transition={{ duration: 0.3, type: "spring" }}
                  className="flex justify-start gap-3 max-w-[85%]"
                >
                  <div className="w-8 h-8 rounded-full bg-cyan-600 flex items-center justify-center shrink-0 mt-1 shadow-sm">
                    <Bot size={16} />
                  </div>
                  <div className="bg-gray-800/90 backdrop-blur-sm p-4 rounded-2xl rounded-tl-sm border border-gray-700 shadow-md flex items-center gap-2 h-[52px]">
                    <motion.div
                      className="w-2 h-2 bg-cyan-400 rounded-full"
                      animate={{ y: [0, -5, 0], opacity: [0.5, 1, 0.5] }}
                      transition={{ duration: 0.6, repeat: Infinity, delay: 0 }}
                    />
                    <motion.div
                      className="w-2 h-2 bg-blue-400 rounded-full"
                      animate={{ y: [0, -5, 0], opacity: [0.5, 1, 0.5] }}
                      transition={{ duration: 0.6, repeat: Infinity, delay: 0.2 }}
                    />
                    <motion.div
                      className="w-2 h-2 bg-indigo-400 rounded-full"
                      animate={{ y: [0, -5, 0], opacity: [0.5, 1, 0.5] }}
                      transition={{ duration: 0.6, repeat: Infinity, delay: 0.4 }}
                    />
                  </div>
                </motion.div>
              )}
              <div ref={messagesEndRef} />
            </div>

            {/* Input Area */}
            <div className="p-5 bg-gray-900/80 backdrop-blur-md border-t border-gray-800 z-10">
              <form onSubmit={sendMessage} className="flex gap-3 max-w-4xl mx-auto">
                <div className="relative flex-1">
                  <input
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    placeholder="Type a message..."
                    className="w-full bg-gray-800/50 border border-gray-700 focus:border-cyan-500/50 focus:ring-2 focus:ring-cyan-500/30 rounded-2xl px-5 py-4 pl-5 pr-12 text-[15px] outline-none transition-all shadow-inner hover:bg-gray-800"
                    disabled={loading}
                  />
                </div>
                <motion.button
                  whileHover={{ scale: 1.05 }}
                  whileTap={{ scale: 0.95 }}
                  type="submit"
                  disabled={loading || !input.trim()}
                  className="bg-gradient-to-r from-cyan-600 to-blue-600 hover:from-cyan-500 hover:to-blue-500 disabled:opacity-50 disabled:cursor-not-allowed text-white px-6 py-4 rounded-2xl font-semibold transition-all shadow-lg shadow-cyan-900/40 flex items-center justify-center shrink-0"
                >
                  <Send size={20} className={input.trim() && !loading ? "translate-x-1 transition-transform duration-300" : ""} />
                </motion.button>
              </form>
            </div>
          </>
        ) : (
          <div className="flex-1 flex items-center justify-center relative overflow-hidden bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-gray-800 via-gray-900 to-black animate-gradient-y">
            {/* Decorative background elements */}
            <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-cyan-900/20 rounded-full blur-[100px] pointer-events-none" />
            <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-blue-900/20 rounded-full blur-[100px] pointer-events-none" />

            <motion.div
              initial={{ opacity: 0, y: 30 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, ease: "easeOut" }}
              className="text-center z-10 max-w-sm px-6"
            >
              <motion.div
                animate={{ y: [0, -10, 0] }}
                transition={{ duration: 4, repeat: Infinity, ease: "easeInOut" }}
                className="w-24 h-24 bg-gradient-to-tr from-cyan-500/20 to-blue-500/20 rounded-3xl mx-auto flex items-center justify-center mb-6 shadow-[0_0_30px_rgba(6,182,212,0.15)] border border-gray-700/50 backdrop-blur-xl rotate-3"
              >
                <Bot size={48} className="text-cyan-400 -rotate-3 drop-shadow-[0_0_15px_rgba(34,211,238,0.5)]" />
              </motion.div>
              <h2 className="text-2xl font-bold mb-3 text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-blue-400 drop-shadow-[0_0_8px_rgba(34,211,238,0.4)]">Welcome to Anime Agents</h2>
              <p className="text-gray-400 leading-relaxed text-[15px]">
                Select a character from the sidebar to begin your conversation. Each agent has unique personality traits and philosophies.
              </p>
            </motion.div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
