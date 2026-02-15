import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Send } from 'lucide-react';

export function Hero() {
    const [ticker, setTicker] = useState('');
    const navigate = useNavigate();

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        if (!ticker.trim()) return;
        navigate(`/analyze?ticker=${ticker}`);
    };

    return (
        <div className="relative container mx-auto px-6 pt-20 pb-32 flex flex-col items-center">

            {/* Hero Content */}
            <div className="text-center max-w-3xl mx-auto space-y-8 mb-16">
                <h1 className="text-5xl md:text-7xl font-extrabold tracking-tight bg-clip-text text-transparent bg-gradient-to-b from-white via-white/90 to-white/50">
                    Financial Intelligence <br />
                    <span className="text-blue-400">Reimagined</span>
                </h1>
                <p className="text-xl text-slate-400 leading-relaxed">
                    Unlock institutional-grade market insights with our multi-agent AI.
                    Analyze any stock in seconds.
                </p>
            </div>

            {/* Input Form */}
            <div className="w-full max-w-2xl mx-auto mb-12">
                <div className="bg-slate-900/50 backdrop-blur-xl border border-white/10 rounded-2xl p-2 shadow-2xl shadow-blue-500/10 ring-1 ring-white/5 transition-all focus-within:ring-blue-500/50">
                    <form onSubmit={handleSubmit} className="relative flex items-center">
                        <input
                            type="text"
                            value={ticker}
                            onChange={(e) => setTicker(e.target.value.toUpperCase())}
                            placeholder="Enter Ticker (e.g., AAPL, TSLA)"
                            className="w-full bg-transparent px-6 py-4 text-lg font-medium placeholder-slate-500 text-white outline-none"
                        />
                        <button
                            type="submit"
                            disabled={!ticker}
                            className="p-3 bg-blue-600 hover:bg-blue-500 text-white rounded-xl transition-all disabled:opacity-50 disabled:cursor-not-allowed hover:shadow-lg hover:shadow-blue-500/25 active:scale-95 ml-2"
                        >
                            <Send className="w-5 h-5" />
                        </button>
                    </form>
                </div>
            </div>
        </div>
    );
}
