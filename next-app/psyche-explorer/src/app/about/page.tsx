import Image from "next/image";
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";

export default function About() {
    return (
        <main className="flex flex-col justify-between min-h-screen bg-[#0f041E] text-white">
            <Navbar />
            <section className="flex flex-col align-center text-center">
                <h1 className="text-6xl p-10">About Psyche Explorer</h1>
            </section>
            <Footer />
        </main>
    );
}