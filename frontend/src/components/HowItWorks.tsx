import { Search, BrainCircuit, FileText } from 'lucide-react';

const steps = [
    {
        id: 1,
        title: 'Input Ticker',
        description: 'Enter a stock symbol (e.g., AAPL). The system instantly spins up a dedicated crew of agents.',
        icon: Search,
    },
    {
        id: 2,
        title: 'Parallel Analysis',
        description: 'Agents simultaneously analyze news, financials, and health metrics in real-time.',
        icon: BrainCircuit,
    },
    {
        id: 3,
        title: 'Comprehensive Report',
        description: 'Receive a unified investment thesis with clear actionable insights.',
        icon: FileText,
    },
];

export function HowItWorks() {
    return (
        <div id="how-it-works" className="py-24 bg-slate-950 relative overflow-hidden">
            <div className="max-w-7xl mx-auto px-6 relative z-10">
                <div className="text-center mb-16">
                    <h2 className="text-3xl md:text-4xl font-bold mb-4">How It Works</h2>
                    <p className="text-slate-400 max-w-2xl mx-auto">
                        From input to insight in under 60 seconds.
                    </p>
                </div>

                <div className="relative grid grid-cols-1 md:grid-cols-3 gap-12">
                    {/* Connector Line (Desktop) */}
                    <div className="hidden md:block absolute top-12 left-[16%] right-[16%] h-0.5 bg-gradient-to-r from-blue-500/0 via-blue-500/30 to-blue-500/0" />

                    {steps.map((step) => (
                        <div key={step.id} className="relative flex flex-col items-center text-center">
                            <div className="w-24 h-24 rounded-2xl bg-slate-900 border border-slate-800 flex items-center justify-center mb-6 shadow-xl shadow-blue-500/5 z-10">
                                <step.icon className="w-10 h-10 text-blue-400" />
                            </div>
                            <h3 className="text-xl font-semibold mb-3">{step.title}</h3>
                            <p className="text-slate-400 leading-relaxed text-sm">
                                {step.description}
                            </p>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
}
