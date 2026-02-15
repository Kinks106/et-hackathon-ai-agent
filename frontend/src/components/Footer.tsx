export function Footer() {
    return (
        <footer className="border-t border-white/5 bg-slate-950 py-12">
            <div className="max-w-7xl mx-auto px-6 flex flex-col md:flex-row justify-between items-center gap-6">
                <p className="text-slate-500 text-sm">
                    © {new Date().getFullYear()} Eternal AI Agent. Built for the ET Hackathon.
                </p>
                <div className="flex gap-6 text-slate-500 text-sm">
                    <a href="#" className="hover:text-white transition-colors">Privacy Policy</a>
                    <a href="#" className="hover:text-white transition-colors">Terms of Service</a>
                </div>
            </div>
        </footer>
    );
}
