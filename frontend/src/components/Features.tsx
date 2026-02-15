import { Newspaper, TrendingUp, HeartPulse, Microscope } from 'lucide-react';

const features = [
    {
        name: 'News Analysis Agent',
        description: 'Scours global news sources to extract sentiment and market-moving events.',
        icon: Newspaper,
        color: 'text-blue-400',
        bg: 'bg-blue-500/10',
        border: 'border-blue-500/20',
    },
    {
        name: 'Financial Data Agent',
        description: 'Analyzes technical indicators, price action, and volatility patterns.',
        icon: TrendingUp,
        color: 'text-emerald-400',
        bg: 'bg-emerald-500/10',
        border: 'border-emerald-500/20',
    },
    {
        name: 'Health Check Agent',
        description: 'Deep dives into balance sheets and income statements to assess solvency.',
        icon: HeartPulse,
        color: 'text-rose-400',
        bg: 'bg-rose-500/10',
        border: 'border-rose-500/20',
    },
    {
        name: 'Outlook Agent',
        description: 'Synthesizes all data to provide tailored short, mid, and long-term forecasts.',
        icon: Microscope,
        color: 'text-indigo-400',
        bg: 'bg-indigo-500/10',
        border: 'border-indigo-500/20',
    },
];

export function Features() {
    return (
        <div id="features" className="py-24 bg-slate-900/50">
            <div className="max-w-7xl mx-auto px-6">
                <div className="text-center mb-16">
                    <h2 className="text-3xl md:text-4xl font-bold mb-4">Powered by Multi-Agent AI</h2>
                    <p className="text-slate-400 max-w-2xl mx-auto">
                        Our system orchestrates a team of specialized AI agents, each an expert in their field,
                        working together to deliver institution-grade analysis.
                    </p>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                    {features.map((feature) => (
                        <div
                            key={feature.name}
                            className={`p-6 rounded-2xl border ${feature.border} ${feature.bg} backdrop-blur-sm transition-transform hover:-translate-y-1`}
                        >
                            <div className={`w-12 h-12 rounded-xl ${feature.bg} flex items-center justify-center mb-4`}>
                                <feature.icon className={`w-6 h-6 ${feature.color}`} />
                            </div>
                            <h3 className="text-xl font-semibold mb-2">{feature.name}</h3>
                            <p className="text-slate-400 text-sm leading-relaxed">{feature.description}</p>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
}
