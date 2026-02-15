import { BarChart3, Github } from 'lucide-react';

export function Navbar() {
    return (
        <nav className="sticky top-0 z-50 w-full border-b border-white/5 bg-slate-950/80 backdrop-blur-md supports-[backdrop-filter]:bg-slate-950/60">
            <div className="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
                <div className="flex items-center gap-2 font-bold text-xl tracking-tight text-white">
                    <div className="p-1.5 bg-blue-500/10 rounded-lg ring-1 ring-blue-500/20">
                        <BarChart3 className="w-5 h-5 text-blue-400" />
                    </div>
                    <span>Eternal<span className="text-blue-400">AI</span></span>
                </div>

                <div className="hidden md:flex items-center gap-8 text-sm font-medium text-slate-400">
                    <a href="#features" className="hover:text-white transition-colors">Features</a>
                    <a href="#how-it-works" className="hover:text-white transition-colors">How it Works</a>
                    <a href="https://github.com" target="_blank" rel="noopener noreferrer" className="hover:text-white transition-colors">
                        <Github className="w-5 h-5" />
                    </a>
                </div>
            </div>
        </nav>
    );
}
