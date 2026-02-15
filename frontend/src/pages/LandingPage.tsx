import { Layout } from '../components/Layout';
import { Navbar } from '../components/Navbar';
import { Hero } from '../components/Hero';
import { Features } from '../components/Features';
import { HowItWorks } from '../components/HowItWorks';
import { Footer } from '../components/Footer';

export function LandingPage() {
    return (
        <Layout>
            <Navbar />
            <Hero />
            <Features />
            <HowItWorks />
            <Footer />
        </Layout>
    );
}
