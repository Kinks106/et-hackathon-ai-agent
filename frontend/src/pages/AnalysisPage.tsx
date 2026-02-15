import { useEffect, useState } from 'react';
import { useSearchParams, Link } from 'react-router-dom';
import axios from 'axios';
import { Loader2, AlertCircle, ArrowLeft, BarChart3, CheckCircle2 } from 'lucide-react';
import ReactMarkdown from 'react-markdown';
import { Layout } from '../components/Layout';
import { Navbar } from '../components/Navbar';
import { Footer } from '../components/Footer';

interface AnalysisResponse {
    result: string;
}

export function AnalysisPage() {
    const [searchParams] = useSearchParams();
    const ticker = searchParams.get('ticker');

    const [loading, setLoading] = useState(true);
    const [result, setResult] = useState<string | null>(null);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchAnalysis = async () => {
            if (!ticker) return;

            try {
                const response = await axios.post<AnalysisResponse>('http://localhost:8000/analyze', {
                    ticker: ticker
                });
                setResult(response.data.result);
            } catch (err: any) {
                console.error(err);
                setError(err.response?.data?.detail || 'Failed to fetch analysis. Ensure backend is running.');
            } finally {
                setLoading(false);
            }
        };

        fetchAnalysis();
    }, [ticker]);

    if (!ticker) {
        return (
            <Layout>
                <div className="flex-1 flex flex-col items-center justify-center">
                    <p className="text-red-400">No ticker provided.</p>
                    <Link to="/" className="text-blue-400 hover:underline mt-4">Go Home</Link>
                </div>
            </Layout>
        );
    }

    return (
        <Layout>
            <Navbar />
            <div className="flex-1 container mx-auto px-6 py-12 max-w-5xl">

                {/* Header */}
                <div className="mb-8 flex items-center justify-between">
                    <Link to="/" className="flex items-center gap-2 text-slate-400 hover:text-white transition-colors">
                        <ArrowLeft className="w-4 h-4" /> Back to Home
                    </Link>
                    <div className="flex items-center gap-2 px-3 py-1 rounded-full bg-blue-500/10 text-blue-400 text-sm font-medium border border-blue-500/20">
                        <BarChart3 className="w-4 h-4" />
                        Analysis for {ticker}
                    </div>
                </div>

                {/* Loading State */}
                {loading && (
                    <div className="flex flex-col items-center justify-center py-20 animate-in fade-in duration-700">
                        <div className="relative">
                            <div className="absolute inset-0 bg-blue-500/20 blur-xl rounded-full" />
                            <Loader2 className="relative w-16 h-16 text-blue-400 animate-spin" />
                        </div>
                        <h2 className="mt-8 text-2xl font-semibold text-white">Analyzing Market Data...</h2>
                        <p className="text-slate-400 mt-2 text-center max-w-md">
                            Our AI agents are currently researching news, financials, and technical indicators for {ticker}.
                            <br />
                            <span className="text-xs text-slate-500 mt-2 block">(This may take up to 60 seconds due to rate limits)</span>
                        </p>

                        {/* Progress Steps (Visual only) */}
                        <div className="mt-8 flex gap-3">
                            <div className="w-2 h-2 rounded-full bg-blue-400 animate-bounce" style={{ animationDelay: '0ms' }} />
                            <div className="w-2 h-2 rounded-full bg-blue-400 animate-bounce" style={{ animationDelay: '150ms' }} />
                            <div className="w-2 h-2 rounded-full bg-blue-400 animate-bounce" style={{ animationDelay: '300ms' }} />
                        </div>
                    </div>
                )}

                {/* Error State */}
                {error && (
                    <div className="bg-red-500/10 border border-red-500/20 rounded-2xl p-6 flex flex-col items-center text-center max-w-md mx-auto mt-12">
                        <AlertCircle className="w-12 h-12 text-red-400 mb-4" />
                        <h3 className="text-red-200 font-semibold mb-2 text-lg">Analysis Failed</h3>
                        <p className="text-red-300/80">{error}</p>
                        <Link
                            to="/"
                            className="mt-6 px-6 py-2 bg-red-500/20 hover:bg-red-500/30 text-red-200 rounded-lg transition-colors"
                        >
                            Try Again
                        </Link>
                    </div>
                )}

                {/* Result State */}
                {result && (
                    <div className="animate-in fade-in slide-in-from-bottom-8 duration-700">
                        <div className="bg-slate-900/60 backdrop-blur-md border border-white/10 rounded-3xl p-8 md:p-12 shadow-2xl ring-1 ring-white/5">

                            <div className="flex items-center gap-3 mb-8 pb-8 border-b border-white/5">
                                <CheckCircle2 className="w-6 h-6 text-emerald-400" />
                                <h1 className="text-2xl font-bold">Comprehensive Analysis Report</h1>
                            </div>

                            <div className="prose prose-invert prose-lg max-w-none prose-headings:text-blue-100 prose-a:text-blue-400 prose-strong:text-slate-200 prose-li:text-slate-300 text-slate-300">
                                <ReactMarkdown>{result}</ReactMarkdown>
                            </div>
                        </div>
                    </div>
                )}

            </div>
            <Footer />
        </Layout>
    );
}
